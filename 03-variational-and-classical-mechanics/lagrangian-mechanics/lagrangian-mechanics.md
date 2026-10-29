# Lagrangian Mechanics

> Markdown reading edition. TikZ diagrams and print-layout elements are preserved in the PDF and LaTeX editions.

*Coordinates, constraints, and motion*

Why one scalar function can replace a collection of force components

## Why change the language of mechanics?

Newton's law

$$

\mathbf{F}=m\mathbf{a}

$$

is direct when Cartesian force components are easy to write. It becomes awkward when a particle is tied to a curve, several rods impose constraints, or the natural coordinates rotate with the system.

Lagrangian mechanics begins with a different question:

**The organising question**

What are the smallest number of coordinates needed to describe every allowed configuration? Once those coordinates are chosen, can the dynamics be written without solving explicitly for every constraint force?

The answer is yes. Choose generalised coordinates $q_1,\ldots,q_n$, write the kinetic and potential energies in those coordinates, and form

$$

\boxed{L(q_i,\dot q_i,t)=T-V.}

$$

The equations of motion are

$$

\boxed{\frac{\mathrm d }{\mathrm d t}\left(\frac{\partial L}{\partial \dot q_i}\right)-\frac{\partial L}{\partial q_i}=0.}

$$

## Generalised coordinates are labels, not directions

A coordinate $q_i$ may be a distance, angle, extension, or any other parameter that labels a configuration. It does not need to be a Cartesian component.

If a bead is constrained to a circular hoop of radius $a$, the Cartesian coordinates satisfy

$$

x^2+y^2=a^2.

$$

Using $x$ and $y$ introduces two coordinates plus a constraint. Using one angle,

$$

x=a\sin\theta,
\qquad
y=-a\cos\theta,

$$

builds the constraint into the description. The angle $\theta$ is the single degree of freedom.

> Diagram: see the PDF or LaTeX edition.

## Why $L=T-V$?

For a Cartesian particle in a potential $V(q)$,

$$

T=\frac12m\dot q^2,
\qquad
L=\frac12m\dot q^2-V(q).

$$

Then

$$

\frac{\partial L}{\partial \dot q}=m\dot q,
\qquad
\frac{\mathrm d }{\mathrm d t}\left(\frac{\partial L}{\partial \dot q}\right)=m\ddot q,
\qquad
\frac{\partial L}{\partial q}=-\frac{\mathrm d V}{\mathrm d q}.

$$

The Euler--Lagrange equation becomes

$$

m\ddot q=-\frac{\mathrm d V}{\mathrm d q}=F.

$$

Thus $L=T-V$ reproduces Newton's equation for conservative forces. Its real advantage is that the same construction continues to work in non-Cartesian coordinates and constrained systems.

## A dependable construction recipe

1. Draw the system and declare the positive directions.
1. Choose independent coordinates $q_i$.
1. Write the position of every mass in terms of $q_i$.
1. Differentiate those positions to obtain velocities.
1. Form $T=\sum_a \tfrac12m_a v_a^2$.
1. Choose a zero of potential and form $V$.
1. Compute $L=T-V$.
1. Apply one Euler--Lagrange equation for each coordinate.
1. Simplify only after all derivatives are visible.
1. Check units, signs, and a limiting case.

## Worked example: a simple pendulum

Take $\theta=0$ at the downward vertical. The bob position is

$$

x=\ell\sin\theta,
\qquad
y=-\ell\cos\theta.

$$

Differentiate:

$$

\dot x=\ell\cos\theta\,\dot\theta,
\qquad
\dot y=\ell\sin\theta\,\dot\theta.

$$

Therefore

$$

v^2=\dot x^2+\dot y^2
=\ell^2\dot\theta^2(\cos^2\theta+\sin^2\theta)
=\ell^2\dot\theta^2.

$$

Choose $V=0$ at the lowest point:

$$

T=\frac12m\ell^2\dot\theta^2,
\qquad
V=mg\ell(1-\cos\theta).

$$

Dropping the irrelevant additive constant $-mg\ell$ gives the convenient Lagrangian

$$

L=\frac12m\ell^2\dot\theta^2+mg\ell\cos\theta.

$$

Now

$$

\frac{\partial L}{\partial \dot\theta}=m\ell^2\dot\theta,
\qquad
\frac{\partial L}{\partial \theta}=-mg\ell\sin\theta.

$$

Hence

$$

\boxed{\ddot\theta+\frac g\ell\sin\theta=0.}

$$

**Small-angle check**

If $|\theta|\ll1$, then $\sin\theta\approx\theta$, so

$$

\ddot\theta+\frac g\ell\theta=0,

$$

with angular frequency $\omega=\sqrt{g/\ell}$. The dimensions are correct because $g/\ell$ has units of time$^{-2}$.

## Polar coordinates and the hidden geometry in $T$

For planar motion,

$$

\mathbf{r}=r\mathbf{e_r},
\qquad
\mathbf{v}=\dot r\mathbf{e_r}+r\dot\theta\mathbf{e}_\theta.

$$

Because the unit vectors are orthonormal,

$$

v^2=\dot r^2+r^2\dot\theta^2.

$$

Thus for a central potential $V(r)$,

$$

\boxed{L=\frac12m\left(\dot r^2+r^2\dot\theta^2\right)-V(r).}

$$

The angular coordinate does not appear explicitly. Its Euler--Lagrange equation is

$$

\frac{\mathrm d }{\mathrm d t}\left(mr^2\dot\theta\right)=0,

$$

so

$$

\boxed{mr^2\dot\theta=\ell_z=\text{constant}.}

$$

Angular momentum conservation is therefore visible before solving the orbit.

The radial equation is

$$

m\ddot r-mr\dot\theta^2+\frac{\mathrm d V}{\mathrm d r}=0.

$$

The term $-mr\dot\theta^2$ arises from the coordinate geometry encoded in the kinetic energy.

## Generalised momentum

For each coordinate define

$$

\boxed{p_i=\frac{\partial L}{\partial \dot q_i}.}

$$

This is the momentum conjugate to $q_i$. It agrees with familiar momentum components in simple Cartesian systems, but it should not be assumed to equal $m\dot q_i$ in general.

For the polar angle,

$$

p_\theta=\frac{\partial L}{\partial \dot\theta}=mr^2\dot\theta,

$$

which is angular momentum, not ``mass times angular speed''.

## Cyclic coordinates and conservation

If $L$ does not depend explicitly on $q_j$, then

$$

\frac{\partial L}{\partial q_j}=0.

$$

The Euler--Lagrange equation gives

$$

\frac{\mathrm d p_j}{\mathrm d t}=0.

$$

**Cyclic-coordinate rule**

If a coordinate is absent from the Lagrangian, its conjugate momentum is conserved. This is the simplest working form of the connection between symmetry and conservation.

Examples include translational symmetry giving linear momentum and rotational symmetry giving angular momentum.

## Energy from the Lagrangian

Define

$$

E_L=\sum_i\dot q_i\frac{\partial L}{\partial \dot q_i}-L.

$$

Differentiate and use the Euler--Lagrange equations:

$$
\begin{aligned}
\frac{\mathrm d E_L}{\mathrm d t}
&=\sum_i\left(
\ddot q_i\frac{\partial L}{\partial \dot q_i}
+\dot q_i\frac{\mathrm d }{\mathrm d t}\frac{\partial L}{\partial \dot q_i}
\right)-\frac{\mathrm d L}{\mathrm d t}\\
&=-\frac{\partial L}{\partial t}.
\end{aligned}
$$

Therefore, if $L$ has no explicit time dependence,

$$

\boxed{E_L=\text{constant}.}

$$

For ordinary systems with kinetic energy quadratic in velocities and a velocity-independent potential, $E_L=T+V$.

## Constraints and Lagrange multipliers

Sometimes it is inconvenient to eliminate a constraint $f(q_1,\ldots,q_n,t)=0$. Introduce a multiplier $\lambda(t)$ and use

$$

L'=L+\lambda f.

$$

Variation with respect to $\lambda$ recovers the constraint. Variation with respect to $q_i$ gives

$$

\frac{\mathrm d }{\mathrm d t}\frac{\partial L}{\partial \dot q_i}-\frac{\partial L}{\partial q_i}=\lambda\frac{\partial f}{\partial q_i}.

$$

The multiplier packages the constraint force. Its sign depends on whether $+\lambda f$ or $-\lambda f$ was chosen.

## Small oscillations

Near a stable equilibrium $q=q_0$, write $q=q_0+\xi$. Since $V'(q_0)=0$,

$$

V(q_0+\xi)\approx V(q_0)+\frac12V''(q_0)\xi^2.

$$

If $T\approx\tfrac12M\dot\xi^2$, then

$$

L\approx\frac12M\dot\xi^2-\frac12K\xi^2,
\qquad K=V''(q_0).

$$

Thus

$$

M\ddot\xi+K\xi=0,
\qquad
\omega^2=K/M.

$$

Many complicated systems look like coupled harmonic oscillators when viewed close enough to a stable equilibrium.

## Non-uniqueness and useful freedoms

The equations of motion are unchanged if a constant is added to $L$. More generally,

$$

L\mapsto L+\frac{\mathrm d }{\mathrm d t}F(q,t)

$$

changes the action only by endpoint terms when the endpoints are fixed. The Lagrangian is therefore a generator of equations, not a uniquely measurable energy.

## Common errors

- Forgetting that basis vectors may depend on time in curvilinear coordinates.
- Choosing dependent coordinates and then applying unconstrained equations.
- Writing $V=mgy$ without declaring which direction is positive.
- Treating $p_i$ as automatically equal to $m\dot q_i$.
- Missing the total time derivative in $\frac{\mathrm d }{\mathrm d t}(\partial L/\partial\dot q_i)$.
- Solving the differential equation before checking the model and signs.

**The central habit**

Do not begin with the Euler--Lagrange formula. Begin with the configuration, the independent coordinates, and the position of each mass. A correct $T$ and $V$ make the remaining calculation systematic.
