# Building the LaTeX editions

## Requirements

- A modern TeX distribution
- `latexmk`
- PDFLaTeX

The documents use common packages including `amsmath`, `mathtools`, `tikz`, `tcolorbox`, `hyperref`, and `microtype`.

## Build one document

Run `latexmk` from the document's folder:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error document-name.tex
```

For documents that use the shared style, keep the repository layout intact so that `../../../intuitmath.sty` remains available from each document folder.

## Build every document

From the repository root:

```sh
python scripts/build_all.py
```

The script invokes `latexmk` in each source directory and leaves the resulting PDF beside its `.tex` source.

## Cleaning temporary files

```sh
python scripts/build_all.py --clean
```

The checked-in PDFs are reading copies. Build logs and auxiliary files are ignored by Git.

## PDF-only recovered mechanics volumes

The Lagrangian intuition volume and its calculus-of-variations companion were recovered as finished PDFs without their original LaTeX sources. Their checked-in PDFs are therefore canonical reading copies and are intentionally skipped by `scripts/build_all.py`. The accompanying Markdown files are reading editions, not claimed source originals.

## HTML-based recovered volume

The worked Schrödinger-equation volume was recovered as HTML rather than LaTeX. Its checked-in PDF is the prepared reading copy and its `.html` file is the editable layout source. It is intentionally not processed by `scripts/build_all.py`; opening the HTML in a modern browser provides the interactive reading edition, and browser print can be used to make a personal PDF copy.
