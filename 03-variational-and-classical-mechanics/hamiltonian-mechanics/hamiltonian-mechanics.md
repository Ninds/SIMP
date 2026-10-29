# Why Hamiltonian Mechanics?

> Markdown reading edition. TikZ diagrams and print-layout elements are preserved in the PDF and LaTeX editions.

*Predicting the next instant from position and momentum*

Discovering Hamilton's equations before deriving them

## The question that motivates the formalism

Lagrangian mechanics describes a configuration using $q$ and a velocity $\dot q$. It also introduces the conjugate momentum

$$

p=\frac{\partial L}{\partial \dot q}.

$$

For an ordinary particle, $p=m\dot q$, so position and momentum contain the same instantaneous information as position and velocity.

This suggests a practical question:

**What we actually need**

If the particle is currently at $(q,p)$, how do we find its position and momentum a moment later?

For a short interval $\Delta t$,

$$

q(t+\Delta t)\approx q(t)+\dot q\,\Delta t,
\qquad
p(t+\Delta t)\approx p(t)+\dot p\,\Delta t.

$$

We therefore need two rates:

$$

\dot q=f(q,p,t),
\qquad
\dot p=g(q,p,t).

$$

No partial derivatives of the Hamiltonian have been assumed. We have merely identified the information required to evolve the state.

## Discovering the equations for a familiar particle

For a particle in a potential $V(q)$, define

$$

H(q,p)=\frac{p^2}{2m}+V(q).

$$

We already know

$$

\dot q=\frac pm,
\qquad
\dot p=F=-\frac{\mathrm d V}{\mathrm d q}.

$$

Now differentiate $H$:

$$

\frac{\partial H}{\partial p}=\frac pm=\dot q,
\qquad
\frac{\partial H}{\partial q}=\frac{\mathrm d V}{\mathrm d q}=-\dot p.

$$

**Hamilton's equations, discovered**

$$

\boxed{
\dot q=\frac{\partial H}{\partial p},
\qquad
\dot p=-\frac{\partial H}{\partial q}.}

$$

The two rates needed to predict the next instant are already contained in the two partial derivatives of a single function.

## Why this is significant

Newton's equation is usually second order:

$$

m\ddot q=F(q).

$$

Hamilton's formulation replaces it with two coupled first-order equations for the state $(q,p)$. This is not less information: specifying $q$ and $p$ is equivalent to specifying $q$ and $\dot q$ for a regular mechanical system.

The pair $(q,p)$ is a point in *phase space*. As time changes, the state traces a curve there.

> Diagram: see the PDF or LaTeX edition.

At every point, Hamilton's equations assign the tangent vector

$$

(\dot q,\dot p)=\left(\frac{\partial H}{\partial p},-\frac{\partial H}{\partial q}\right).

$$

The Hamiltonian is therefore a rule for the flow through phase space.

## Why change variables from velocity to momentum?

The Lagrangian is naturally a function of $(q,\dot q,t)$. We want a new function of $(q,p,t)$. Merely replacing symbols is not enough because $p$ is defined by a derivative of $L$.

The required change is the Legendre transform:

$$

\boxed{H(q,p,t)=p\dot q-L(q,\dot q,t),}

$$

where $\dot q$ is re-expressed in terms of $(q,p,t)$ using

$$

p=\frac{\partial L}{\partial \dot q}.

$$

**What the Legendre transform does**

It replaces the slope-like variable $\dot q$ by the conjugate slope $p$. The correction term $p\dot q$ preserves the information while changing which variable is independent.

For

$$

L=\frac12m\dot q^2-V(q),
\qquad p=m\dot q,

$$

we have $\dot q=p/m$ and

$$
\begin{aligned}
H&=p\frac pm-\left[\frac12m\left(\frac pm\right)^2-V(q)\right]\\
&=\frac{p^2}{2m}+V(q)=T+V.
\end{aligned}
$$

This familiar equality relies on ordinary quadratic kinetic energy and a velocity-independent potential; $H$ is not automatically ``the energy'' in every model.

## General derivation of Hamilton's equations

Begin with

$$

H=p\dot q-L.

$$

Take a total differential:

$$

\,\mathrm d H=\dot q\,\,\mathrm d p+p\,\,\mathrm d\dot q-\,\mathrm d L.

$$

Since

$$

\,\mathrm d L=\frac{\partial L}{\partial q}\,\mathrm d q+\frac{\partial L}{\partial \dot q}\,\mathrm d\dot q+\frac{\partial L}{\partial t}\,\mathrm d t

$$

and $p=\partial L/\partial\dot q$, the two terms containing $\,\mathrm d\dot q$ cancel:

$$

\,\mathrm d H=\dot q\,\,\mathrm d p-\frac{\partial L}{\partial q}\,\mathrm d q-\frac{\partial L}{\partial t}\,\mathrm d t.

$$

The Euler--Lagrange equation gives

$$

\frac{\partial L}{\partial q}=\dot p.

$$

Therefore

$$

\,\mathrm d H=\dot q\,\,\mathrm d p-\dot p\,\,\mathrm d q-\frac{\partial L}{\partial t}\,\mathrm d t.

$$

But $H=H(q,p,t)$ also implies

$$

\,\mathrm d H=\frac{\partial H}{\partial q}\,\mathrm d q+\frac{\partial H}{\partial p}\,\mathrm d p+\frac{\partial H}{\partial t}\,\mathrm d t.

$$

Comparing independent coefficients yields

$$

\boxed{
\dot q=\frac{\partial H}{\partial p},
\qquad
\dot p=-\frac{\partial H}{\partial q},
\qquad
\frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t}.}

$$

## Many degrees of freedom

For coordinates $q_i$ and momenta

$$

p_i=\frac{\partial L}{\partial \dot q_i},

$$

define

$$

H(\mathbf{q},\mathbf{p},t)=\sum_i p_i\dot q_i-L.

$$

Then

$$

\boxed{
\dot q_i=\frac{\partial H}{\partial p_i},
\qquad
\dot p_i=-\frac{\partial H}{\partial q_i}.}

$$

The phase space has dimension $2n$: one coordinate and one conjugate momentum for each degree of freedom.

## Worked example: harmonic oscillator

For

$$

H(q,p)=\frac{p^2}{2m}+\frac12kq^2,

$$

Hamilton's equations give

$$

\dot q=\frac pm,
\qquad
\dot p=-kq.

$$

Differentiate the first equation and insert the second:

$$

\ddot q=\frac{\dot p}{m}=-\frac kmq.

$$

Thus

$$

\ddot q+\omega^2q=0,
\qquad \omega=\sqrt{k/m}.

$$

The constant-energy curves satisfy

$$

\frac{p^2}{2m}+\frac12kq^2=E,

$$

which are ellipses in the $(q,p)$ plane. The oscillator moves around one ellipse without crossing to another energy.

## Conservation of the Hamiltonian

Along a trajectory,

$$
\begin{aligned}
\frac{\mathrm d H}{\mathrm d t}
&=\frac{\partial H}{\partial q}\dot q+\frac{\partial H}{\partial p}\dot p+\frac{\partial H}{\partial t}\\
&=(-\dot p)\dot q+(\dot q)\dot p+\frac{\partial H}{\partial t}\\
&=\frac{\partial H}{\partial t}.
\end{aligned}
$$

Therefore, if $H$ has no explicit time dependence,

$$

\boxed{H=\text{constant along the motion}.}

$$

## Poisson brackets

For functions $A(q,p,t)$ and $B(q,p,t)$ define

$$

\{A,B\}=\frac{\partial A}{\partial q}\frac{\partial B}{\partial p}-\frac{\partial A}{\partial p}\frac{\partial B}{\partial q}.

$$

Hamilton's equations can be written

$$

\dot q=\{q,H\},
\qquad
\dot p=\{p,H\}.

$$

More generally,

$$

\boxed{\frac{\mathrm d A}{\mathrm d t}=\{A,H\}+\frac{\partial A}{\partial t}.}

$$

If $A$ has no explicit time dependence and $\{A,H\}=0$, then $A$ is conserved.

The basic bracket is

$$

\{q,p\}=1.

$$

This compact algebra becomes the classical precursor of commutators in quantum mechanics.

## Phase-space geometry

In two-dimensional phase space the velocity field is

$$

\mathbf{v}_{\rm ph}=\left(\frac{\partial H}{\partial p},-\frac{\partial H}{\partial q}\right).

$$

Its divergence is

$$

\frac{\partial }{\partial q}\left(\frac{\partial H}{\partial p}\right)
+\frac{\partial }{\partial p}\left(-\frac{\partial H}{\partial q}\right)=0

$$

when mixed derivatives commute. Small phase-space areas are neither compressed nor expanded by Hamiltonian flow. This is the local heart of Liouville's theorem.

## When the Legendre transform can fail

To solve $p=\partial L/\partial\dot q$ for $\dot q$, the velocity Hessian must be invertible. In one dimension this means

$$

\frac{\partial^2L}{\partial\dot q^2}\neq0.

$$

If it is singular, the system contains constraints and needs a more careful Hamiltonian treatment. The standard equations remain correct for regular Lagrangians.

## A numerical viewpoint

Hamilton's equations are an initial-value system. Given $(q_0,p_0)$, a simple first step is

$$

q_{n+1}=q_n+\Delta t\,\frac{\partial H}{\partial p}(q_n,p_n),
\qquad
p_{n+1}=p_n-\Delta t\,\frac{\partial H}{\partial q}(q_n,p_n).

$$

This explicit Euler rule is easy but does not preserve Hamiltonian geometry well over long times. Symplectic methods alter the update order to respect phase-space structure more faithfully.

## What to remember

1. Position and momentum specify the instantaneous state.
1. Predicting the next instant requires $\dot q$ and $\dot p$.
1. For a familiar particle, these rates are the two partial derivatives of $H$ with opposite signs.
1. The Legendre transform proves that the same structure follows generally from a regular Lagrangian.
1. The Hamiltonian generates a flow through phase space.

**The central insight**

Hamilton's equations are not arbitrary formulas involving partial derivatives. They say that a single scalar function contains the two local rates needed to move the complete state $(q,p)$ forward in time.
