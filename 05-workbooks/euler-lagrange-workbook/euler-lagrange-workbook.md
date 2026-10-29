# Euler-Lagrange Equations: Illustrated Problem Workbook

> Markdown reading edition. TikZ diagrams and print-layout elements are preserved in the PDF and LaTeX editions.

## Quick reference

For coordinates $q_i$,

$$

\boxed{\frac{\mathrm d }{\mathrm d t}\left(\frac{\partial L}{\partial \dot q_i}\right)-\frac{\partial L}{\partial q_i}=0.}

$$

For ordinary conservative systems,

$$

L=T-V,
\qquad
p_i=\frac{\partial L}{\partial \dot q_i}.

$$

If $q_j$ is absent from $L$, then $p_j$ is conserved. If $L$ has no explicit time dependence and the kinetic energy is quadratic in velocities, then $T+V$ is conserved.

**Before differentiating**

State the coordinate direction, the zero of potential, and every geometric relation. Most sign errors occur before the Euler--Lagrange equation is used.

### Progression

1. Problems 1--5: one coordinate and careful energy construction.
1. Problems 6--10: constraints, moving supports, cyclic coordinates, and effective potentials.
1. Problems 11--15: curved constraints, coupled systems, velocity-dependent terms, and normal modes.

## Problem 1: Harmonic oscillator

**Focus:** Applying the equation to a given Lagrangian

A particle has Lagrangian

$$

L(x,\dot x)=\frac12m\dot x^2-\frac12kx^2.

$$

1. Calculate $\partial L/\partial\dot x$ and $\partial L/\partial x$.
1. Derive the equation of motion.
1. Show that $E=\tfrac12m\dot x^2+\tfrac12kx^2$ is constant along a solution.
1. State the angular frequency.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 2: Simple pendulum

**Focus:** Building $T$ and $V$ from geometry

A bob of mass $m$ is attached to a massless rod of length $\ell$. Let $\theta$ be measured from the downward vertical.

1. Write the Cartesian position of the bob.
1. Show that $v^2=\ell^2\dot\theta^2$.
1. Choose the lowest point as $V=0$ and construct $L$.
1. Derive the exact equation of motion and its small-angle approximation.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 3: Bead on a rotating rod with a spring

**Focus:** Time-dependent geometry with one coordinate

A bead of mass $m$ slides without friction along a horizontal rod rotating at constant angular speed $\Omega$. A spring of stiffness $k$ connects the bead to the rotation axis. Let $r$ be the spring extension and take the natural length to be zero.

1. Show that $v^2=\dot r^2+\Omega^2r^2$.
1. Construct the Lagrangian.
1. Derive the radial equation.
1. For what relation between $k$, $m$, and $\Omega$ is $r=0$ stable?

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 4: Particle in a central potential

**Focus:** Polar kinetic energy and a cyclic coordinate

A particle of mass $m$ moves in a plane under a potential $V(r)$.

1. Use polar coordinates to write $T$ and $L$.
1. Derive the $r$ and $\theta$ equations.
1. Identify the conserved angular momentum $J$.
1. Eliminate $\dot\theta$ from the radial equation using $J$.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 5: Spring on an inclined plane

**Focus:** Potential-energy signs and equilibrium

A block of mass $m$ slides without friction down a plane inclined at angle $\alpha$. A spring of stiffness $k$ lies along the plane and has extension $s$, measured positively down the slope from its natural length.

1. Write $T$ and the gravitational and spring potentials.
1. Derive the equation for $s(t)$.
1. Find the equilibrium extension.
1. Find the small-oscillation frequency about equilibrium.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 6: Atwood machine

**Focus:** Using a string constraint to remove a coordinate

Two masses $m_1>m_2$ are joined by a light inextensible string over a frictionless pulley. Let $x$ be the downward displacement of $m_1$; the upward displacement of $m_2$ is then also $x$.

1. Express the total kinetic and potential energies in terms of $x$.
1. Derive the acceleration.
1. Explain why the string tension does not appear in the reduced Lagrangian.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 7: Pendulum with a moving support

**Focus:** An explicitly time-dependent Lagrangian

The support of a pendulum moves horizontally according to a prescribed function $X(t)$. The bob has mass $m$, the rod has length $\ell$, and $\theta$ is measured from the downward vertical.

1. Write the bob coordinates $x$ and $y$.
1. Construct $T$, $V$, and $L$.
1. Show that

$$

\ell\ddot\theta+g\sin\theta+\ddot X\cos\theta=0.

$$

1. State the equation when $X(t)=A\cos\Omega t$.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 8: Bead on a rotating vertical hoop

**Focus:** Equilibria in a rotating constraint

A bead of mass $m$ moves on a vertical circular hoop of radius $a$. The hoop rotates at constant angular speed $\Omega$ about its vertical diameter. Let $\theta$ be measured from the lowest point.

1. Show that

$$

v^2=a^2\dot\theta^2+\Omega^2a^2\sin^2\theta.

$$

1. Construct $L$ and derive the equation of motion.
1. Find all equilibrium angles.
1. When do off-axis equilibria exist?

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 9: Two coupled oscillators

**Focus:** Coupled Euler--Lagrange equations and normal modes

Two equal masses $m$ lie on a frictionless line. Three identical springs of stiffness $k$ connect wall--mass--mass--wall. Let $x_1,x_2$ be displacements from equilibrium.

1. Construct $T$, $V$, and $L$.
1. Derive the two coupled equations.
1. Try $x_i=A_i\cos\omega t$ and find the two normal frequencies.
1. Describe the relative motion in each mode.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 10: Kepler potential and effective energy

**Focus:** Cyclic coordinates and stability of circular motion

A particle moves in

$$

V(r)=-\frac{\mu}{r},\qquad \mu>0.

$$

1. Use the conserved angular momentum $J=mr^2\dot\theta$ to define

$$

U_{\rm eff}(r)=\frac{J^2}{2mr^2}-\frac{\mu}{r}.

$$

1. Find the circular-orbit radius $r_0$.
1. Show that the circular orbit is stable by evaluating $U_{\rm eff}''(r_0)$.
1. Find the angular frequency of the circular orbit.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 11: Bead constrained to a parabola

**Focus:** Kinetic energy on a curved track

A bead of mass $m$ slides without friction on the vertical curve

$$

y=ax^2,qquad a>0.

$$

Use $x$ as the coordinate and take gravity downward.

1. Show that

$$

v^2=(1+4a^2x^2)\dot x^2.

$$

1. Construct the Lagrangian.
1. Derive the exact equation of motion.
1. Linearise near $x=0$ and find the small-oscillation frequency.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 12: Bead on a cone

**Focus:** Two coordinates and an effective radial potential

A bead moves without friction on the cone $z=cr$, where $(r,\phi,z)$ are cylindrical coordinates and $c>0$. Gravity acts downward.

1. Show that

$$

T=\frac12m\left[(1+c^2)\dot r^2+r^2\dot\phi^2\right].

$$

1. Construct $L$ and identify the conserved momentum.
1. Derive the radial equation.
1. Write the effective potential after eliminating $\dot\phi$.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 13: Equal double pendulum

**Focus:** A genuinely coupled nonlinear system

Two equal masses $m$ are joined by two massless rods of equal length $\ell$. Angles $\theta_1,\theta_2$ are measured from the downward vertical.

1. Write both mass positions.
1. Show that, with $\Delta=\theta_1-\theta_2$,

$$

T=\frac12m\ell^2\left(2\dot\theta_1^2+\dot\theta_2^2+2\dot\theta_1\dot\theta_2\cos\Delta\right).

$$

1. Construct $V$ and $L$.
1. Derive the two coupled Euler--Lagrange equations.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 14: Charged particle in a magnetic field

**Focus:** A velocity-dependent Lagrangian

A particle of charge $q$ and mass $m$ moves in the $xy$-plane in a uniform magnetic field $B\mathbf{e_z}$. Consider

$$

L=\frac12m(\dot x^2+\dot y^2)+\frac{qB}{2}(x\dot y-y\dot x).

$$

1. Derive the equations for $x$ and $y$.
1. Show that the speed is constant.
1. Show that the motion is circular and find its angular frequency magnitude.
1. Explain why $T-V$ is too narrow a template for this example even though the Euler--Lagrange equations still apply.

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

## Problem 15: Coupled pendulums: small oscillations

**Focus:** Normal modes from a quadratic Lagrangian

Two equal pendulums of mass $m$ and length $\ell$ are coupled by a weak horizontal spring of stiffness $k$ joining the bobs. For small angles, the spring extension is approximately $\ell(\theta_2-\theta_1)$.

1. Write the quadratic small-angle Lagrangian.
1. Derive the linear equations.
1. Find the in-phase and anti-phase normal frequencies.
1. Which mode stretches the coupling spring?

> Diagram: see the PDF or LaTeX edition.

> Ruled working space is provided in the PDF edition.

# Worked solutions

## Solution 1: Harmonic oscillator

$$

\frac{\partial L}{\partial \dot x}=m\dot x,
\qquad
\frac{\partial L}{\partial x}=-kx.

$$

Therefore

$$

\boxed{m\ddot x+kx=0.}

$$

Multiply by $\dot x$:

$$

m\ddot x\dot x+kx\dot x=0
=\frac{\mathrm d }{\mathrm d t}\left(\frac12m\dot x^2+\frac12kx^2\right).

$$

Hence $E$ is constant. Comparing with $\ddot x+\omega^2x=0$ gives

$$

\boxed{\omega=\sqrt{k/m}.}

$$

## Solution 2: Simple pendulum

The bob position is

$$

x=\ell\sin\theta,
\qquad y=-\ell\cos\theta.

$$

Thus

$$

\dot x=\ell\cos\theta\dot\theta,
\qquad
\dot y=\ell\sin\theta\dot\theta,

$$

and $v^2=\ell^2\dot\theta^2$. With $V=mg\ell(1-\cos\theta)$,

$$

L=\frac12m\ell^2\dot\theta^2-mg\ell(1-\cos\theta).

$$

The equation is

$$

\boxed{\ddot\theta+\frac g\ell\sin\theta=0.}

$$

For small angles, $\sin\theta\approx\theta$:

$$

\ddot\theta+\frac g\ell\theta=0.

$$

## Solution 3: Bead on a rotating rod with a spring

In polar coordinates with prescribed $\theta=\Omega t$,

$$

v^2=\dot r^2+r^2\Omega^2.

$$

Therefore

$$

L=\frac12m(\dot r^2+\Omega^2r^2)-\frac12kr^2.

$$

Now

$$

\frac{\partial L}{\partial \dot r}=m\dot r,
\qquad
\frac{\partial L}{\partial r}=(m\Omega^2-k)r.

$$

Hence

$$

\boxed{m\ddot r+(k-m\Omega^2)r=0.}

$$

The origin is stable when

$$

\boxed{k>m\Omega^2.}

$$

At equality the quadratic restoring term vanishes.

## Solution 4: Particle in a central potential

The polar speed is

$$

v^2=\dot r^2+r^2\dot\theta^2,

$$

so

$$

L=\frac12m(\dot r^2+r^2\dot\theta^2)-V(r).

$$

For $r$,

$$

\boxed{m\ddot r-mr\dot\theta^2+V'(r)=0.}

$$

For $\theta$,

$$

\frac{\mathrm d }{\mathrm d t}(mr^2\dot\theta)=0,
\qquad
\boxed{J=mr^2\dot\theta.}

$$

Substitution gives

$$

\boxed{m\ddot r-\frac{J^2}{mr^3}+V'(r)=0.}

$$

## Solution 5: Spring on an inclined plane

With $s$ positive down the slope,

$$

T=\frac12m\dot s^2,
\qquad
V=\frac12ks^2-mgs\sin\alpha.

$$

Thus

$$

L=\frac12m\dot s^2-\frac12ks^2+mgs\sin\alpha.

$$

The equation is

$$

\boxed{m\ddot s+ks-mg\sin\alpha=0.}

$$

At equilibrium,

$$

\boxed{s_{\rm eq}=\frac{mg\sin\alpha}{k}.}

$$

Writing $s=s_{\rm eq}+\xi$ gives $m\ddot\xi+k\xi=0$, so $\omega=\sqrt{k/m}$.

## Solution 6: Atwood machine

The string constraint gives both masses the same speed magnitude:

$$

T=\frac12(m_1+m_2)\dot x^2.

$$

As $m_1$ moves down by $x$, its potential decreases by $m_1gx$; as $m_2$ moves up, its potential increases by $m_2gx$:

$$

V=(m_2-m_1)gx.

$$

Therefore

$$

L=\frac12(m_1+m_2)\dot x^2+(m_1-m_2)gx.

$$

The equation is

$$

(m_1+m_2)\ddot x=(m_1-m_2)g,

$$

so

$$

\boxed{\ddot x=\frac{m_1-m_2}{m_1+m_2}g.}

$$

The internal tension is absent because the constraint has already reduced the system to its allowed motion.

## Solution 7: Pendulum with a moving support

The bob position is

$$

x=X(t)+\ell\sin\theta,
\qquad y=-\ell\cos\theta.

$$

Hence

$$

T=\frac12m\left(\dot X^2+2\ell\dot X\cos\theta\dot\theta+\ell^2\dot\theta^2\right),
\qquad
V=-mg\ell\cos\theta.

$$

After differentiating, the terms proportional to $\dot X\dot\theta\sin\theta$ cancel, leaving

$$

\boxed{\ell\ddot\theta+g\sin\theta+\ddot X\cos\theta=0.}

$$

For $X=A\cos\Omega t$,

$$

\ell\ddot\theta+g\sin\theta-A\Omega^2\cos\Omega t\cos\theta=0.

$$

## Solution 8: Bead on a rotating vertical hoop

The distance from the rotation axis is $a\sin\theta$, while motion along the hoop contributes $a\dot\theta$. Thus

$$

T=\frac12ma^2\left(\dot\theta^2+\Omega^2\sin^2\theta\right),
\qquad
V=-mga\cos\theta.

$$

Therefore

$$

L=\frac12ma^2(\dot\theta^2+\Omega^2\sin^2\theta)+mga\cos\theta.

$$

The equation is

$$

\boxed{\ddot\theta=\Omega^2\sin\theta\cos\theta-\frac ga\sin\theta.}

$$

Equilibria satisfy

$$

\sin\theta\left(\Omega^2\cos\theta-\frac ga\right)=0.

$$

Thus $\theta=0,\pi$, and off-axis equilibria obey

$$

\boxed{\cos\theta=\frac{g}{a\Omega^2}.}

$$

They exist when $\Omega^2\ge g/a$.

## Solution 9: Two coupled oscillators

The energies are

$$

T=\frac12m(\dot x_1^2+\dot x_2^2),

$$

$$

V=\frac12k x_1^2+\frac12k(x_2-x_1)^2+\frac12k x_2^2.

$$

The equations are

$$

\boxed{m\ddot x_1+2kx_1-kx_2=0,}
\qquad
\boxed{m\ddot x_2+2kx_2-kx_1=0.}

$$

For $(A_1,A_2)=(1,1)$,

$$

\omega_+^2=\frac{k}{m};

$$

the middle spring is unstretched. For $(1,-1)$,

$$

\omega_-^2=\frac{3k}{m};

$$

the masses move oppositely and the middle spring stretches most strongly.

## Solution 10: Kepler potential and effective energy

The radial energy is

$$

E=\frac12m\dot r^2+U_{\rm eff}(r),
\qquad
U_{\rm eff}=\frac{J^2}{2mr^2}-\frac\mu r.

$$

A circular orbit is a stationary point:

$$

U_{\rm eff}'=-\frac{J^2}{mr^3}+\frac\mu{r^2}=0.

$$

Hence

$$

\boxed{r_0=\frac{J^2}{m\mu}.}

$$

Also

$$

U_{\rm eff}''(r_0)=\frac{3J^2}{mr_0^4}-\frac{2\mu}{r_0^3}
=\frac{\mu}{r_0^3}>0,

$$

so the orbit is stable. Using $mr_0\omega^2=\mu/r_0^2$,

$$

\boxed{\omega^2=\frac{\mu}{mr_0^3}.}

$$

## Solution 11: Bead constrained to a parabola

Since $y=ax^2$,

$$

\dot y=2ax\dot x,
\qquad
v^2=\dot x^2+\dot y^2=(1+4a^2x^2)\dot x^2.

$$

Thus

$$

L=\frac12m(1+4a^2x^2)\dot x^2-mgax^2.

$$

The exact equation is

$$

\boxed{(1+4a^2x^2)\ddot x+4a^2x\dot x^2+2gax=0.}

$$

Near $x=0$, nonlinear terms are negligible:

$$

\ddot x+2ga\,x=0,
\qquad
\boxed{\omega=\sqrt{2ga}.}

$$

## Solution 12: Bead on a cone

With $z=cr$, $\dot z=c\dot r$, so

$$

T=\frac12m[(1+c^2)\dot r^2+r^2\dot\phi^2],
\qquad V=mgcr.

$$

The angle is cyclic:

$$

\boxed{J=mr^2\dot\phi.}

$$

The radial equation is

$$

\boxed{m(1+c^2)\ddot r-mr\dot\phi^2+mgc=0.}

$$

Eliminating $\dot\phi$ gives

$$

\frac12m(1+c^2)\dot r^2+U_{\rm eff}(r)=E,

$$

with

$$

\boxed{U_{\rm eff}(r)=\frac{J^2}{2mr^2}+mgcr.}

$$

## Solution 13: Equal double pendulum

The positions are

$$

x_1=\ell\sin\theta_1,
\quad y_1=-\ell\cos\theta_1,

$$

$$

x_2=x_1+\ell\sin\theta_2,
\quad y_2=y_1-\ell\cos\theta_2.

$$

This yields

$$

T=\frac12m\ell^2(2\dot\theta_1^2+\dot\theta_2^2+2\dot\theta_1\dot\theta_2\cos\Delta),

$$

$$

V=-mg\ell(2\cos\theta_1+\cos\theta_2).

$$

The equations are

$$

\boxed{
2\ddot\theta_1+\ddot\theta_2\cos\Delta
+\dot\theta_2^2\sin\Delta
+2\frac g\ell\sin\theta_1=0,}

$$

$$

\boxed{
\ddot\theta_2+\ddot\theta_1\cos\Delta
-\dot\theta_1^2\sin\Delta
+\frac g\ell\sin\theta_2=0.}

$$

## Solution 14: Charged particle in a magnetic field

For $x$,

$$

\frac{\partial L}{\partial \dot x}=m\dot x-\frac{qB}{2}y,
\qquad
\frac{\partial L}{\partial x}=\frac{qB}{2}\dot y.

$$

For $y$ the analogous calculation gives

$$

\boxed{m\ddot x=qB\dot y,}
\qquad
\boxed{m\ddot y=-qB\dot x.}

$$

Then

$$

\frac{\mathrm d }{\mathrm d t}(\dot x^2+\dot y^2)
=2\dot x\ddot x+2\dot y\ddot y=0,

$$

so the speed is constant. The acceleration is always perpendicular to velocity, producing circular motion with

$$

\boxed{|\omega_c|=\frac{|qB|}{m}.}

$$

The term linear in velocity represents magnetic coupling through a vector potential; the Euler--Lagrange formalism is broader than the simple template $T-V$.

## Solution 15: Coupled pendulums: small oscillations

To quadratic order,

$$

T=\frac12m\ell^2(\dot\theta_1^2+\dot\theta_2^2),

$$

$$

V=\frac12mg\ell(\theta_1^2+\theta_2^2)
+\frac12k\ell^2(\theta_2-\theta_1)^2.

$$

The equations are

$$

m\ell^2\ddot\theta_1+mg\ell\theta_1+k\ell^2(\theta_1-\theta_2)=0,

$$

$$

m\ell^2\ddot\theta_2+mg\ell\theta_2+k\ell^2(\theta_2-\theta_1)=0.

$$

For the in-phase mode $(1,1)$, the spring does not stretch:

$$

\boxed{\omega_{\rm in}^2=\frac g\ell.}

$$

For the anti-phase mode $(1,-1)$,

$$

\boxed{\omega_{\rm anti}^2=\frac g\ell+\frac{2k}{m}.}

$$

Only the anti-phase mode stretches the coupling spring to first order.

## Final checklist

Before accepting an equation of motion, ask:

- Are the coordinates independent?
- Does every term in $T$ have units of energy?
- Is the zero and sign of $V$ declared?
- Does a cyclic coordinate give the expected conserved quantity?
- Does the equation reduce correctly when a coupling, rotation, or angle is set to zero?
- Is the small-angle or small-displacement approximation stated only after the exact equation?

**What fluency looks like**

The goal is not to memorise fifteen answers. It is to make the sequence

$$

\text{geometry}\to\text{coordinates}\to T,V\to L\to\text{equations}

$$

feel routine enough that attention can move to interpretation.
