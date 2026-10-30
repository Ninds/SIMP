# From a moving pattern to the transport equation

These notes derive the one-dimensional transport—or advection—equation from a painted pattern moving rigidly along a belt.

The route begins with the exact one-neighbour update

\[
U_j^{n+1}=U_{j-1}^{n},
\]

introduces physical site spacing \(h\), tick duration \(\tau\), and a smooth intensity profile \(u(x,t)\), and then keeps the physical speed \(h/\tau\to c>0\) fixed as the grid is refined. This produces

\[
u_t+c u_x=0.
\]

The notes interpret the sign at a fixed camera, check the travelling profile \(u(x,t)=f(x-ct)\), distinguish exact discrete statements from continuum assumptions, and compare one-neighbour transport with the two-neighbour random walk that produces diffusion. Appendices cover deterministic particles, probability density, left-moving patterns, biased random jumps, nonsmooth profiles, and initial data.

## Available editions

- [Typeset PDF](transport-equation.pdf) — 17 illustrated pages.
- [LaTeX source](transport-equation.tex) — complete editable source with TikZ diagrams.
- [Readable Markdown](transport-equation.md) — GitHub-friendly reading edition with diagram pointers.

These are discussion-first notes. The small-step argument motivates the classical equation but is not presented as a general convergence theorem or a treatment of weak solutions.

Read the [random-walk to heat-equation derivation](../random-walk-to-heat-equation/README.md) alongside this note to compare translation with spreading and first with second spatial derivatives.

[Back to probability and PDEs](../README.md) · [Library home](../../README.md)
