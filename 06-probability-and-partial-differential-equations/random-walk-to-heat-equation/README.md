# From a random walk to the heat equation

These notes derive the one-dimensional heat—or diffusion—equation from a particle that jumps one step left or right with equal probability.

The route is deliberately slow. It begins with two-step paths and the exact lattice update

\[
p_j^{n+1}=\tfrac12p_{j-1}^n+\tfrac12p_{j+1}^n,
\]

then introduces physical step length \(h\), time step \(\tau\), a smooth macroscopic profile, the centred second difference, and the diffusive scaling \(h^2/(2\tau)\to D\). This produces

\[
u_t=D u_{xx}.
\]

The appendices discuss the parity alternation in the exact walk, probability-density scaling, mean-square displacement, biased walks and drift, and the distinction between a guided derivation and a proof of convergence.

## Available editions

- [Typeset PDF](random-walk-to-heat-equation.pdf) — 13 illustrated pages.
- [LaTeX source](random-walk-to-heat-equation.tex) — complete editable source with TikZ diagrams.
- [Readable Markdown](random-walk-to-heat-equation.md) — GitHub-friendly reading edition with diagram pointers.

These are discussion-first notes. The continuum passage is explained carefully but is not presented as a rigorous limit theorem.

[Back to probability and PDEs](../README.md) · [Library home](../../README.md)
