# Contents and reading paths

The library is arranged by mathematical branch. Each category and each individual topic folder has a short introduction, so browsing from the folder tree works as well as following the links below.

## 1. Linear algebra and analysis

[Category introduction](01-linear-algebra-and-analysis/README.md)

### [Vectors, operators, and function spaces](01-linear-algebra-and-analysis/vectors-operators-and-function-spaces/README.md)

The long-form backbone of the collection. It begins with geometric vectors and the dot product, then places finite-dimensional vectors, sequences, and functions side by side. Later chapters develop operators, adjoints, spectra, Fourier coordinates, heat flow, and the infinite square well.

Best for: understanding why a function can be treated as a vector and why a differential operator plays the role of a matrix.

## 2. Vector calculus and coordinate systems

[Category introduction](02-vector-calculus-and-coordinate-systems/README.md)

### [Integral theorems](02-vector-calculus-and-coordinate-systems/integral-theorems/README.md)

A geometric guide to the gradient theorem, Green’s theorem, the divergence theorem, and Stokes’ theorem. The emphasis is on dot products, orientation, flux, circulation, and why boundary and interior descriptions agree.

### [Polar-coordinate vectors](02-vector-calculus-and-coordinate-systems/polar-coordinate-vectors/README.md)

A slow derivation of the rotating basis, velocity, acceleration, kinetic energy, and circular-orbit scaling, with TikZ diagrams.

### [Spherical Laplacian](02-vector-calculus-and-coordinate-systems/spherical-laplacian/README.md)

A separate derivation of the scalar Laplacian in spherical coordinates, including scale factors, divergence, geometric checks, and common errors.

## 3. Variational and classical mechanics

[Category introduction and sequence](03-variational-and-classical-mechanics/README.md)

### [Action and the calculus of variations](03-variational-and-classical-mechanics/action-and-calculus-of-variations/README.md)

Builds from ordinary derivatives to variations of an entire path, derives the Euler–Lagrange equation, and explains endpoint conditions, total derivatives, and the second variation.

### [Lagrangian mechanics](03-variational-and-classical-mechanics/lagrangian-mechanics/README.md)

Shows how constraints and coordinates lead naturally to (L=T-V), then develops cyclic coordinates, energy, polar motion, and small oscillations through worked examples.

### [Hamiltonian mechanics](03-variational-and-classical-mechanics/hamiltonian-mechanics/README.md)

Starts from the practical question: if position and momentum are known now, how do they change next? Hamilton’s equations are recognised for a familiar particle before the Legendre-transform derivation.

## 4. Quantum mechanics

[Category introduction](04-quantum-mechanics/README.md)

### [Solving the Schrödinger equation: thirteen worked demonstrations](04-quantum-mechanics/schrodinger-equation-worked-models/README.md)

An 89-page, discussion-first worked volume built around thirteen recurring solution patterns: the one-dimensional infinite well; steps above and below threshold; barriers below and above threshold; a semi-infinite finite well; the harmonic oscillator by series and ladder operators; the three-dimensional box and oscillator; central-potential separation; the spherical well; and the hydrogen-like atom. Coordinate-system derivations, separation-of-variables guidance, and master tables support the worked examples.

### [Schrödinger equation as operator evolution](04-quantum-mechanics/schrodinger-operator-bridge/README.md)

A focused companion linking state vectors, self-adjoint operators, the Hamiltonian, unitary time evolution, Fourier modes, and the infinite square well.

## 5. Workbooks

[Category introduction](05-workbooks/README.md)

### [Euler–Lagrange illustrated problem workbook](05-workbooks/euler-lagrange-workbook/README.md)

Fifteen progressive problems with generous working space, diagrams, and complete solutions. Topics include oscillators, pendulums, polar coordinates, constraints, central forces, coupled systems, moving supports, rotating frames, and the double pendulum.

## 6. Probability and partial differential equations

[Category introduction](06-probability-and-partial-differential-equations/README.md)

### [From a random walk to the heat equation](06-probability-and-partial-differential-equations/random-walk-to-heat-equation/README.md)

A patient illustrated derivation of the one-dimensional heat equation from an unbiased nearest-neighbour walk. It separates the exact discrete probability update from the smooth-profile assumption, builds the centred second difference geometrically, explains the scaling \(h^2/(2\tau)\to D\), and discusses parity, probability density, mean-square displacement, drift, and the limits of the argument.

## Suggested routes

### Mechanics route

Action and variations → Lagrangian mechanics → polar-coordinate vectors → Hamiltonian mechanics → workbook.

### Mathematics-and-physics route

Vectors and operators → integral theorems → spherical Laplacian → Schrödinger/operator bridge → worked Schrödinger models.

### Quantum bridge

Dot products and projections → function spaces → self-adjoint operators → Fourier coordinates → Schrödinger/operator bridge → worked Schrödinger models.

### Probability-to-PDE route

Discrete paths and probabilities → lattice evolution rule → centred second difference → diffusive scaling → heat equation.
