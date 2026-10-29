# The Schrödinger Equation as Operator Evolution

> Markdown reading edition. TikZ diagrams and print-layout elements are preserved in the PDF and LaTeX editions.

*A bridge from vectors and matrices to wavefunctions*

Why quantum mechanics looks like linear algebra in an infinite-dimensional space

## From coordinate lists to functions

A finite vector may be written

$$

\mathbf{v}=(v_1,v_2,\ldots,v_N).

$$

The index $i$ tells us which coordinate we are reading. A function $\psi(x)$ can be viewed similarly: the continuous label $x$ replaces the discrete label $i$.

The finite inner product

$$

\langle\mathbf{u},\mathbf{v}\rangle=\sum_i u_i^*v_i

$$

becomes

$$

\boxed{\langle\phi,\psi\rangle
=\int_{-\infty}^{\infty}\phi^*(x)\psi(x)\,\,\mathrm d x.}

$$

The norm is

$$

\|\psi\|^2=\langle\psi,\psi\rangle
=\int|\psi(x)|^2\,\,\mathrm d x.

$$

**The bridge**

A wavefunction is not merely a graph in physical space. It is one vector in a function space. Its value at $x$ is analogous to a coordinate of that vector in the position-labelled description.

## Normalisation and probability

Quantum states are normalised so that

$$

\boxed{\int_{-\infty}^{\infty}|\psi(x,t)|^2\,\,\mathrm d x=1.}

$$

For an interval $[a,b]$,

$$

\Pr(a\le x\le b)=\int_a^b|\psi(x,t)|^2\,\,\mathrm d x.

$$

Multiplying $\psi$ by a global phase $\mathrm e^{i\alpha}$ does not change $|\psi|^2$, so state vectors that differ only by a global phase represent the same physical ray.

## Operators are the infinite-dimensional analogue of matrices

A matrix maps vectors to vectors. A linear operator maps functions to functions:

$$

\widehat A(\alpha\psi+\beta\phi)
=\alpha\widehat A\psi+\beta\widehat A\phi.

$$

Important examples in one dimension are

$$

\widehat x\psi=x\psi,
\qquad
\widehat p\psi=-i\hbar\frac{\partial \psi}{\partial x}.

$$

The Hamiltonian for a particle in a potential is

$$

\boxed{
\widehat H=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x).}

$$

The kinetic energy is a differential operator; the potential energy is a multiplication operator.

## Self-adjointness and real measurements

An operator is self-adjoint when

$$

\langle\phi,\widehat A\psi\rangle
=\langle\widehat A\phi,\psi\rangle

$$

for all functions in an appropriate domain.

If

$$

\widehat A\psi=a\psi,

$$

then, for a normalised eigenfunction,

$$
\begin{aligned}
a&=\langle\psi,a\psi\rangle
=\langle\psi,\widehat A\psi\rangle\\
&=\langle\widehat A\psi,\psi\rangle
=a^*.
\end{aligned}
$$

Hence $a$ is real.

**Domains are part of the operator**

A differential expression alone is not a complete operator. Boundary conditions and regularity determine the domain, and the domain determines whether integration by parts produces unwanted boundary terms.

## The time-dependent Schrödinger equation

The evolution law is

$$

\boxed{i\hbar\frac{\partial \psi}{\partial t}=\widehat H\psi.}

$$

In vector notation,

$$

i\hbar\frac{\mathrm d }{\mathrm d t}\operatorname{ket}{\psi(t)}=\widehat H\operatorname{ket}{\psi(t)}.

$$

This is a first-order differential equation in time for a vector in a function space. Compare it with a finite linear system

$$

\td{\mathbf{v}}{t}=A\mathbf{v}.

$$

The Hamiltonian is the generator of quantum time evolution.

If $\widehat H$ is time independent, the formal solution is

$$

\boxed{
\operatorname{ket}{\psi(t)}=exp\left(-\frac{i}{\hbar}\widehat Ht\right)\operatorname{ket}{\psi(0)}.}

$$

## Why the norm is preserved

Let $\widehat H$ be self-adjoint. Then

$$
\begin{aligned}
\frac{\mathrm d }{\mathrm d t}\langle\psi,\psi\rangle
&=\left\langle\frac{\partial \psi}{\partial t},\psi\right\rangle
+\left\langle\psi,\frac{\partial \psi}{\partial t}\right\rangle\\
&=\frac{i}{\hbar}\langle\widehat H\psi,\psi\rangle
-\frac{i}{\hbar}\langle\psi,\widehat H\psi\rangle=0.
\end{aligned}
$$

Thus a normalised state stays normalised. The evolution operator is unitary.

## Energy eigenfunctions separate the time dependence

Suppose

$$

\widehat H\phi_n=E_n\phi_n.

$$

Then

$$

\psi_n(x,t)=\phi_n(x)\mathrm e^{-iE_nt/\hbar}

$$

solves the time-dependent equation. Its probability density is stationary:

$$

|\psi_n(x,t)|^2=|\phi_n(x)|^2.

$$

For a superposition,

$$

\psi(x,0)=\sum_n c_n\phi_n(x),

$$

linearity gives

$$

\boxed{
\psi(x,t)=\sum_n c_n\mathrm e^{-iE_nt/\hbar}\phi_n(x).}

$$

Time evolution rotates each energy coordinate by its own phase.

## The infinite square well

Let

$$

V(x)=0\quad(0<x<L),
\qquad
V=\infty\quad\text{outside}.

$$

The boundary conditions are

$$

\phi(0)=\phi(L)=0.

$$

Inside the well,

$$

-\frac{\hbar^2}{2m}\phi''=E\phi.

$$

Write

$$

k^2=\frac{2mE}{\hbar^2}.

$$

Then

$$

\phi(x)=A\sin(kx)+B\cos(kx).

$$

The condition at $x=0$ gives $B=0$. The condition at $x=L$ gives

$$

\sin(kL)=0
\quad\Longrightarrow\quad
kL=n\pi.

$$

Therefore

$$

\boxed{
\phi_n(x)=\sqrt{\frac2L}\sin\frac{n\pi x}{L},
\qquad
E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}.}

$$

> Diagram: see the PDF or LaTeX edition.

Quantisation is a boundary-condition effect: only certain standing-wave shapes fit the interval.

## Fourier coordinates diagonalise free evolution

For a free particle,

$$

\widehat H=-\frac{\hbar^2}{2m}\partial_x^2.

$$

The plane wave $\mathrm e^{ikx}$ is an eigenfunction because

$$

\partial_x^2\mathrm e^{ikx}=-k^2\mathrm e^{ikx}.

$$

Thus

$$

\widehat H\mathrm e^{ikx}=\frac{\hbar^2k^2}{2m}\mathrm e^{ikx}.

$$

In Fourier coordinates, the differential operator becomes multiplication by $\hbar^2k^2/(2m)$. Each Fourier component evolves independently:

$$

\widetilde\psi(k,t)
=\mathrm e^{-i\hbar k^2t/(2m)}\widetilde\psi(k,0).

$$

## Heat flow and quantum evolution

The heat equation

$$

\frac{\partial u}{\partial t}=D\partial_x^2u

$$

and the free Schrödinger equation

$$

\frac{\partial \psi}{\partial t}=\frac{i\hbar}{2m}\partial_x^2\psi

$$

use the same spatial operator but different time generators.

For a Fourier mode $\mathrm e^{ikx}$:

$$

\widetilde u(k,t)=\mathrm e^{-Dk^2t}\widetilde u(k,0),

$$

so high-frequency heat modes decay. Quantum modes acquire phases:

$$

\widetilde\psi(k,t)=\mathrm e^{-i\hbar k^2t/(2m)}\widetilde\psi(k,0),

$$

so their magnitudes do not decay.

**Same basis, different geometry**

Heat flow contracts vectors toward smoother states. Quantum evolution rotates state-space coordinates without changing the norm.

## Commutators and incompatible operations

The commutator is

$$

[\widehat A,\widehat B]=\widehat A\widehat B-\widehat B\widehat A.

$$

For position and momentum,

$$
\begin{aligned}
[\widehat x,\widehat p]\psi
&=x(-i\hbar\psi')+i\hbar(x\psi)'\\
&=i\hbar\psi.
\end{aligned}
$$

Hence

$$

\boxed{[\widehat x,\widehat p]=i\hbar\widehat I.}

$$

Noncommutation is the operator statement behind the position--momentum uncertainty relation.

## Expectation values

For a normalised state,

$$

\boxed{\langle A\rangle
=\langle\psi,\widehat A\psi\rangle
=\int\psi^*(x)(\widehat A\psi)(x)\,\,\mathrm d x.}

$$

The spread is

$$

(\Delta A)^2=\langle(\widehat A-\langle A\rangle)^2\rangle.

$$

The expectation is a weighted average over possible measurement outcomes, not generally an eigenvalue attached to the current state.

## What to remember

1. A wavefunction is a vector in a function space.
1. Integrals replace finite coordinate sums in inner products.
1. Differential operators play the role of matrices.
1. Self-adjointness supplies real eigenvalues and unitary evolution.
1. The Hamiltonian generates time evolution.
1. Choosing an eigenbasis can turn an operator equation into independent scalar equations for coordinates.

**The infinite-dimensional bridge**

The conceptual jump from linear algebra to quantum mechanics is smaller than it first appears: replace finite coordinate lists by functions, sums by integrals, matrices by operators, and matrix exponentials by operator exponentials.
