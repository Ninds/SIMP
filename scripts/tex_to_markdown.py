from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TITLES = {
    "vectors-operators-and-function-spaces": "Vectors, Operators, and Function Spaces",
    "integral-theorems": "Integral Theorems: Boundary and Interior",
    "schrodinger-operator-bridge": "The Schrödinger Equation as Operator Evolution",
    "action-and-calculus-of-variations": "Action and the Calculus of Variations",
    "lagrangian-mechanics": "Lagrangian Mechanics",
    "hamiltonian-mechanics": "Why Hamiltonian Mechanics?",
    "polar-coordinate-vectors": "Vectors in Polar Coordinates",
    "spherical-laplacian": "The Laplacian in Spherical Coordinates",
    "euler-lagrange-workbook": "Euler-Lagrange Equations: Illustrated Problem Workbook",
    "random-walk-to-heat-equation": "From a Random Walk to the Heat Equation",
    "transport-equation": "From a Moving Pattern to the Transport Equation",
}


def braced(text: str, command: str, replacement) -> str:
    pattern = re.compile(r"\\" + command + r"\{([^{}]*)\}")
    while pattern.search(text):
        text = pattern.sub(replacement, text)
    return text


def balanced_command(text: str, command: str, replacement) -> str:
    """Replace commands whose arguments contain nested TeX groups."""
    needle = "\\" + command + "{"
    start = text.find(needle)
    while start >= 0:
        content_start = start + len(needle)
        depth = 1
        cursor = content_start
        while cursor < len(text) and depth:
            if text[cursor] == "{" and (cursor == 0 or text[cursor - 1] != "\\"):
                depth += 1
            elif text[cursor] == "}" and (cursor == 0 or text[cursor - 1] != "\\"):
                depth -= 1
            cursor += 1
        if depth:
            break
        content = text[content_start : cursor - 1]
        text = text[:start] + replacement(content) + text[cursor:]
        start = text.find(needle, start)
    return text


def convert_simple_tabular(match: re.Match[str]) -> str:
    body = match.group(1)
    body = re.sub(r"\\(?:toprule|midrule|bottomrule)", "", body)
    rows: list[list[str]] = []
    for raw_row in re.split(r"\\\\(?:\[[^\]]*\])?", body):
        raw_row = raw_row.strip()
        if not raw_row or "&" not in raw_row:
            continue
        rows.append([re.sub(r"\s+", " ", cell.strip()) for cell in raw_row.split("&")])
    if not rows:
        return "> Table preserved in the PDF and LaTeX editions."
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    lines = [
        "| " + " | ".join(rows[0]) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in rows[1:])
    return "\n" + "\n".join(lines) + "\n"


def convert_enumerate(match: re.Match[str]) -> str:
    items = [item.strip() for item in match.group(1).split("\\item") if item.strip()]
    return "\n" + "\n".join(f"{number}. {item}" for number, item in enumerate(items, start=1)) + "\n"


def convert_dictionary_table(text: str) -> str:
    """Convert the one long comparison table to portable Markdown."""
    start = text.find("\\begin{longtable}")
    end_marker = "\\end{longtable}"
    end = text.find(end_marker, start)
    if start < 0 or end < 0:
        return text

    block = text[start : end + len(end_marker)]
    body_start = block.find("\\endlastfoot")
    if body_start < 0:
        replacement = "> The comparison table is preserved in the PDF and LaTeX editions."
    else:
        data = block[body_start + len("\\endlastfoot") :]
        data = data.rsplit(end_marker, 1)[0]
        rows = []
        pending = []
        for raw_line in data.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            pending.append(line)
            if re.search(r"\\\\\*?$", line):
                row = " ".join(pending)
                row = re.sub(r"\\\\\*?$", "", row).strip()
                cells = [re.sub(r"\s+", " ", cell.strip()) for cell in row.split("&")]
                if len(cells) == 4:
                    rows.append(cells)
                pending = []

        header = ["Concept", "Finite vectors: $\\mathbb R^N$", "Sequences: $\\ell^2$", "Functions: $L^2(I)$"]
        lines = [
            "| " + " | ".join(header) + " |",
            "| --- | --- | --- | --- |",
        ]
        lines.extend("| " + " | ".join(row) + " |" for row in rows)
        replacement = "\n".join(lines)

    return text[:start] + replacement + text[end + len(end_marker) :]


def convert(source: Path) -> str:
    key = source.stem
    text = source.read_text(encoding="utf-8")
    if "\\begin{document}" in text:
        text = text.split("\\begin{document}", 1)[1]
    text = text.rsplit("\\end{document}", 1)[0]

    if key in {"random-walk-to-heat-equation", "transport-equation"}:
        opening_box = "takeaway" if key == "random-walk-to-heat-equation" else "pointbox"
        first_box = text.find(f"\\begin{{{opening_box}}}")
        if first_box >= 0:
            text = text[first_box:]

    text = re.sub(r"\\begin\{titlepage\}.*?\\end\{titlepage\}", "", text, flags=re.S)
    text = re.sub(
        r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",
        "\n\n> Diagram: see the PDF or LaTeX edition.\n\n",
        text,
        flags=re.S,
    )
    text = convert_dictionary_table(text)
    text = re.sub(r"(?m)^\s*%.*$", "", text)
    text = text.replace('Schr\\"odinger', "Schrödinger")

    text = re.sub(
        r"\\tutorialtitle\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}",
        lambda m: f"# {m.group(1)}\n\n*{m.group(2)}*\n\n{m.group(3)}",
        text,
    )
    text = re.sub(
        r"\\problemstart\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}",
        lambda m: f"\n## Problem {m.group(1)}: {m.group(2)}\n\n**Focus:** {m.group(3)}\n",
        text,
    )
    text = re.sub(
        r"\\solutionstart\{([^{}]*)\}\{([^{}]*)\}",
        lambda m: f"\n## Solution {m.group(1)}: {m.group(2)}\n",
        text,
    )
    text = text.replace("\\workingspace", "\n> Ruled working space is provided in the PDF edition.\n")

    if key == "transport-equation":
        section_number = 0

        def transport_heading(value: str) -> str:
            nonlocal section_number
            section_number += 1
            return f"\n## {section_number}. {value}\n"

        text = balanced_command(text, "secstart", transport_heading)
    else:
        text = balanced_command(text, "secstart", lambda value: f"\n## {value}\n")
    text = balanced_command(text, "substart", lambda value: f"\n### {value}\n")

    for command, marks in [
        ("part", ("#",)),
        ("chapter", ("##",)),
        ("section", ("##",)),
        ("subsection", ("###",)),
        ("subsubsection", ("####",)),
    ]:
        text = re.sub(
            rf"\\{command}\*?\{{([^{{}}]*)\}}",
            lambda m, mark=marks[0]: f"\n{mark} {m.group(1)}\n",
            text,
        )

    text = re.sub(r"\\begin\{enumerate\}(?:\[[^\]]*\])?(.*?)\\end\{enumerate\}", convert_enumerate, text, flags=re.S)
    text = re.sub(r"\\begin\{itemize\}(?:\[[^\]]*\])?(.*?)\\end\{itemize\}", lambda m: m.group(1).replace("\\item", "-"), text, flags=re.S)
    text = text.replace("\\item", "-")

    text = re.sub(
        r"\\begin\{tabular\}\{[^\n]*\}\s*(.*?)\\end\{tabular\}",
        convert_simple_tabular,
        text,
        flags=re.S,
    )

    text = re.sub(r"\\begin\{think\}(?:\[[^\]]*\])?", "\n**Stop and think**\n\n", text)
    text = text.replace("\\end{think}", "\n")
    text = re.sub(r"\\begin\{takeaway\}(?:\[[^\]]*\])?", "\n**Key takeaway**\n\n", text)
    text = text.replace("\\end{takeaway}", "\n")
    text = balanced_command(text, "ans", lambda value: f"\n\n**Answer.** {value}")
    text = balanced_command(text, "aside", lambda value: f"\n\n> {value}\n")
    text = re.sub(r"\\begin\{thinkbox\}(?:\[[^\]]*\])?", "\n**Stop and think**\n\n", text)
    text = text.replace("\\end{thinkbox}", "\n")
    text = re.sub(r"\\begin\{pointbox\}(?:\[[^\]]*\])?", "\n**Key point**\n\n", text)
    text = text.replace("\\end{pointbox}", "\n")
    text = re.sub(r"\\answer(?![A-Za-z])", "\n\n**Answer.** ", text)
    text = balanced_command(text, "captionline", lambda value: f"\n*{value}*\n")
    text = balanced_command(text, "highlight", lambda value: f"**{value}**")
    text = text.replace("\\smalldiv", "")

    box_names = [
        "intuition", "resultbox", "checkBox", "warningbox",
        "bridge", "caution", "summarybox", "idea", "notecheck", "result",
    ]
    for name in box_names:
        text = re.sub(
            rf"\\begin\{{{name}\}}(?:\[([^\]]*)\])?",
            lambda m: (f"\n**{m.group(1)}**\n\n" if m.group(1) else "\n"),
            text,
        )
        text = text.replace(f"\\end{{{name}}}", "\n")

    theorem_names = ["definition", "theorem", "proposition", "lemma", "corollary", "example", "remark", "proof"]
    for name in theorem_names:
        label = name.replace("example", "worked example").title()
        text = re.sub(
            rf"\\begin\{{{name}\}}(?:\[([^\]]*)\])?",
            lambda m, label=label: f"\n**{label}" + (f": {m.group(1)}" if m.group(1) else "") + "**\n\n",
            text,
        )
        text = text.replace(f"\\end{{{name}}}", "\n")

    protected_breaks: dict[str, str] = {}
    def protect_break(match: re.Match[str]) -> str:
        token = f"@@TEX-LINEBREAK-{len(protected_breaks)}@@"
        protected_breaks[token] = match.group(0)
        return token
    text = re.sub(r"\\\\\[[^\]]+\]", protect_break, text)
    text = text.replace("\\[", "\n$$\n").replace("\\]", "\n$$\n")
    for token, linebreak in protected_breaks.items():
        text = text.replace(token, linebreak)
    text = re.sub(r"\\begin\{align\*?\}", lambda _: "\n$$\n\\begin{aligned}", text)
    text = re.sub(r"\\end\{align\*?\}", lambda _: "\\end{aligned}\n$$\n", text)
    text = re.sub(r"\\begin\{equation\*?\}", "\n$$\n", text)
    text = re.sub(r"\\end\{equation\*?\}", "\n$$\n", text)
    text = re.sub(r"\\begin\{gather\*?\}", lambda _: "\n$$\n\\begin{gathered}", text)
    text = re.sub(r"\\end\{gather\*?\}", lambda _: "\\end{gathered}\n$$\n", text)

    text = re.sub(r"\\href\{([^{}]*)\}\{([^{}]*)\}", r"[\2](\1)", text)
    text = braced(text, "textbf", lambda m: f"**{m.group(1)}**")
    text = braced(text, "emph", lambda m: f"*{m.group(1)}*")
    text = braced(text, "texttt", lambda m: f"`{m.group(1)}`")
    text = braced(text, "vect", lambda m: rf"\mathbf{{{m.group(1)}}}")
    text = braced(text, "bm", lambda m: rf"\mathbf{{{m.group(1)}}}")
    text = re.sub(r"\\vect\s*([A-Za-z](?:_[A-Za-z0-9]+)?)", r"\\mathbf{\1}", text)
    text = re.sub(
        r"\\bm\s*(\\[A-Za-z]+(?:_[A-Za-z0-9]+)?|[A-Za-z](?:_[A-Za-z0-9]+)?)",
        lambda m: rf"\mathbf{{{m.group(1)}}}",
        text,
    )
    text = re.sub(
        r"\\ip\{([^{}]*)\}\{([^{}]*)\}",
        r"\\left\\langle \1,\2\\right\\rangle",
        text,
    )
    text = braced(text, "norm", lambda m: rf"\left\lVert {m.group(1)}\right\rVert")

    text = re.sub(r"\\pd\{([^{}]*)\}\{([^{}]*)\}", r"\\frac{\\partial \1}{\\partial \2}", text)
    text = re.sub(r"\\td\{([^{}]*)\}\{([^{}]*)\}", r"\\frac{\\mathrm d \1}{\\mathrm d \2}", text)
    text = re.sub(r"\\ut(?![A-Za-z])", r"\\frac{\\partial u}{\\partial t}", text)
    text = re.sub(r"\\ux(?![A-Za-z])", r"\\frac{\\partial u}{\\partial x}", text)
    text = re.sub(r"\\dd(?![A-Za-z])", r"\\,\\mathrm d", text)
    text = re.sub(r"\\grad(?![A-Za-z])", r"\\boldsymbol\\nabla", text)
    text = re.sub(r"\\R(?![A-Za-z])", r"\\mathbb R", text)
    text = re.sub(r"\\C(?![A-Za-z])", r"\\mathbb C", text)
    text = re.sub(r"\\Z(?![A-Za-z])", r"\\mathbb Z", text)
    text = re.sub(r"\\N(?![A-Za-z])", r"\\mathbb N", text)
    text = re.sub(r"\\Span(?![A-Za-z])", r"\\operatorname{span}", text)
    text = re.sub(r"\\ran(?![A-Za-z])", r"\\operatorname{ran}", text)
    text = re.sub(r"\\Ker(?![A-Za-z])", r"\\operatorname{ker}", text)
    text = re.sub(r"\\Id(?![A-Za-z])", r"\\mathrm I", text)
    text = re.sub(r"\\e(?![A-Za-z])", r"\\mathrm e", text)
    text = re.sub(r"\\one(?![A-Za-z])", r"\\mathbf 1", text)
    for macro, replacement in {
        "er": r"\\mathbf e_r",
        "etheta": r"\\mathbf e_\\theta",
        "ephi": r"\\mathbf e_\\phi",
        "ii": r"\\mathbf i",
        "jj": r"\\mathbf j",
        "rr": r"\\mathbf r",
        "vv": r"\\mathbf v",
        "acc": r"\\mathbf a",
        "FF": r"\\mathbf F",
    }.items():
        text = re.sub(rf"\\{macro}(?![A-Za-z])", replacement, text)
    text = text.replace(
        "\\PartMap",
        r"\mathbb R^N\;\longrightarrow\;\ell^2\;\longrightarrow\;L^2",
    )
    text = re.sub(r"\\ket(?![A-Za-z])", r"\\operatorname{ket}", text)
    text = re.sub(r"\\bra(?![A-Za-z])", r"\\operatorname{bra}", text)

    remove_lines = [
        r"\\tableofcontents", r"\\clearpage", r"\\newpage", r"\\appendix", r"\\thispagestyle\{[^{}]*\}",
        r"\\pagenumbering\{[^{}]*\}", r"\\setcounter\{[^{}]*\}\{[^{}]*\}",
        r"\\phantomsection", r"\\markboth\{[^{}]*\}\{[^{}]*\}",
        r"\\addcontentsline\{[^{}]*\}\{[^{}]*\}\{[^{}]*\}",
        r"\\vfill", r"\\noindent", r"\\smallskip", r"\\medskip", r"\\bigskip",
    ]
    for pattern in remove_lines:
        text = re.sub(pattern, "", text)

    for env in ["center", "flushleft", "flushright", "tabular", "tabularx", "minipage", "landscape"]:
        text = re.sub(rf"\\begin\{{{env}\}}(?:\[[^\]]*\])?(?:\{{[^}}]*\}})?", "", text)
        text = re.sub(rf"\\end\{{{env}\}}", "", text)

    text = re.sub(r"\\(?:vspace|hspace)\*?\{[^{}]*\}", "", text)
    text = re.sub(r"\\(?:newgeometry|geometry)\{[^{}]*\}", "", text)
    text = text.replace("\\restoregeometry", "")
    text = re.sub(r"(?m)^\s*\\small\s*$", "", text)
    text = re.sub(r"(?m)^\s*\\renewcommand\{\\arraystretch\}\{[^{}]*\}\s*$", "", text)
    text = re.sub(r"(?m)^\s*\\setlength\{\\tabcolsep\}\{[^{}]*\}\s*$", "", text)
    text = re.sub(r"(?<!\\)\\[ \t]*\n", "\n", text)
    text = re.sub(r"\\(?:color|textcolor)\{[^{}]*\}", "", text)
    text = re.sub(r"\\rule\{[^{}]*\}\{[^{}]*\}", "", text)
    text = re.sub(r"\\\\\[[^\]]*\]\s*\\small\s+", "\n", text)
    text = re.sub(r"\\small\s+", "", text)
    text = re.sub(r"\\par(?![A-Za-z])", "\n", text)
    text = re.sub(r"\\label\{[^{}]*\}", "", text)
    text = re.sub(r"\\ref\{([^{}]*)\}", r"Section \1", text)

    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"(\*\*)\\quad\s+", r"\1 ", text)
    text = re.sub(r"(\*\*)\\\\\s*\n", r"\1\n\n", text)
    text = re.sub(r"(\*\*)\\\\\s*(?=\*\*)", r"\1\n\n", text)
    text = text.replace("\\\\\n**Answer:**", "\n\n**Answer:**")
    text = re.sub(r"(\*\*Answer\.\*\*)\s{2,}", r"\1 ", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    title = TITLES.get(key, key.replace("-", " ").title())
    if not text.startswith("# "):
        text = f"# {title}\n\n{text}"
    note = (
        "> Markdown reading edition. TikZ diagrams and print-layout elements are preserved "
        "in the PDF and LaTeX editions.\n\n"
    )
    first_break = text.find("\n\n")
    return text[: first_break + 2] + note + text[first_break + 2 :] + "\n"


def main() -> None:
    sources = [Path(argument).resolve() for argument in sys.argv[1:]]
    if not sources:
        sources = sorted(ROOT.glob("[0-9][0-9]-*/*/*.tex"))
    for source in sources:
        target = source.with_suffix(".md")
        target.write_text(convert(source), encoding="utf-8", newline="\n")
        print(target.relative_to(ROOT))


if __name__ == "__main__":
    main()
