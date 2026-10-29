# Action and the Calculus of Variations

> Markdown reading edition. TikZ diagrams and print-layout elements are preserved in the PDF and LaTeX editions.

*Why mechanics compares whole paths*

From a small change of a curve to the Euler--Lagrange equation

## The new kind of question

Ordinary calculus asks how a number changes when we change another number. If

$$

f(x)=x^2,

$$

then $f'(x)$ measures the response to a small change $x\mapsto x+\varepsilon$.

The calculus of variations asks a similar question about an entire function. A path

$$

q:[t_0,t_1]\longrightarrow\mathbb R

$$

is the object being changed. A *functional* assigns one number to the whole path. The central example in mechanics is the action

$$

\boxed{S[q]=\int_{t_0}^{t_1}L(q,\dot q,t)\,\,\mathrm d t.}

$$

The square brackets are a useful reminder: $S$ consumes a function $q(t)$, not merely its value at one instant.

**A landscape whose points are curves**

Imagine that every admissible path is one point in a vast ``space of paths''. The action gives a height to each point. A physical path is stationary when every allowed infinitesimal direction through this space produces no first-order change in height.

## Why an integral over time?

The Lagrangian $L(q,\dot q,t)$ measures something locally, at one instant. The action adds that local contribution along the entire history. For an ordinary conservative particle,

$$

L=T-V.

$$

The action therefore balances motion and potential along a path rather than choosing the smallest energy at every instant.

**Stationary does not always mean smallest**

The physical path makes the first variation vanish. It may give a local minimum, a local maximum, or a saddle value of the action. ``Principle of stationary action'' is more accurate than ``principle of least action''.

## How to vary a path

Choose a reference path $q(t)$ and a smooth shape $\eta(t)$. Define a one-parameter family

$$

q_\varepsilon(t)=q(t)+\varepsilon\eta(t).

$$

The small number $\varepsilon$ controls the size of the change; $\eta$ controls its shape.

If the endpoints are fixed, every neighbouring path must begin and end at the same places, so

$$

\boxed{\eta(t_0)=\eta(t_1)=0.}

$$

> Diagram: see the PDF or LaTeX edition.

Because differentiation is linear,

$$

\dot q_\varepsilon=\dot q+\varepsilon\dot\eta.

$$

Changing the path therefore changes both the position argument and the velocity argument of $L$.

## The first variation

Insert the varied path into the action:

$$

S[q_\varepsilon]
=\int_{t_0}^{t_1}L(q+\varepsilon\eta,\dot q+\varepsilon\dot\eta,t)\,\,\mathrm d t.

$$

Now $S[q_\varepsilon]$ is an ordinary function of the number $\varepsilon$. A stationary path satisfies

$$

\left.\frac{\mathrm d }{\mathrm d \varepsilon}S[q_\varepsilon]\right|_{\varepsilon=0}=0.

$$

Using the chain rule,

$$
\begin{aligned}
\left.\frac{\mathrm d }{\mathrm d \varepsilon}S[q_\varepsilon]\right|_{\varepsilon=0}
&=\int_{t_0}^{t_1}
\left(
\frac{\partial L}{\partial q}\eta+\frac{\partial L}{\partial \dot q}\dot\eta
\right)\,\mathrm d t.
\end{aligned}
$$

This expression is called the *first variation* and is written $\delta S$.

## The decisive integration by parts

The second term contains $\dot\eta$, but we want the arbitrary function itself. Integrate by parts:

$$
\begin{aligned}
\int_{t_0}^{t_1}\frac{\partial L}{\partial \dot q}\dot\eta\,\,\mathrm d t
&=\left[\frac{\partial L}{\partial \dot q}\eta\right]_{t_0}^{t_1}
-\int_{t_0}^{t_1}\frac{\mathrm d }{\mathrm d t}\left(\frac{\partial L}{\partial \dot q}\right)\eta\,\,\mathrm d t.
\end{aligned}
$$

The boundary term vanishes because $\eta(t_0)=\eta(t_1)=0$. Hence

$$

\delta S=\int_{t_0}^{t_1}
\left[
\frac{\partial L}{\partial q}-\frac{\mathrm d }{\mathrm d t}\left(\frac{\partial L}{\partial \dot q}\right)
\right]\eta(t)\,\,\mathrm d t.

$$

The function $\eta$ may be chosen freely in the interior. The only way this integral can vanish for every such choice is for its coefficient to vanish point by point.

**Euler--Lagrange equation**

$$

\boxed{\frac{\mathrm d }{\mathrm d t}\left(\frac{\partial L}{\partial \dot q}\right)-\frac{\partial L}{\partial q}=0.}

$$

One integration by parts converts a statement about every nearby path into a differential equation for the stationary path.

## Example: the free particle

Let

$$

L=\frac12m\dot q^2.

$$

Then

$$

\frac{\partial L}{\partial \dot q}=m\dot q,
\qquad
\frac{\partial L}{\partial q}=0.

$$

The Euler--Lagrange equation gives

$$

m\ddot q=0.

$$

Thus the stationary path has constant velocity:

$$

q(t)=At+B.

$$

**Why a straight world-line?**

With no potential, unnecessary changes of velocity only increase the kinetic contribution. Between fixed endpoints and fixed times, the stationary path is the line of uniform motion.

## Example: the harmonic oscillator

For a mass on a spring,

$$

L=\frac12m\dot q^2-\frac12kq^2.

$$

The two required derivatives are

$$

\frac{\partial L}{\partial \dot q}=m\dot q,
\qquad
\frac{\partial L}{\partial q}=-kq.

$$

Therefore

$$

\boxed{m\ddot q+kq=0.}

$$

The familiar restoring-force equation has emerged from stationarity of a whole-path quantity.

## Many coordinates

If the configuration is described by $q_1,\ldots,q_n$, vary each independently:

$$

q_i\mapsto q_i+\varepsilon\eta_i.

$$

The result is one equation per coordinate:

$$

\boxed{\frac{\mathrm d }{\mathrm d t}\left(\frac{\partial L}{\partial \dot q_i}\right)-\frac{\partial L}{\partial q_i}=0,
\qquad i=1,\ldots,n.}

$$

This is why a single scalar function $L$ can encode the dynamics of a many-coordinate system.

## What if the endpoint is free?

When an endpoint value is not fixed, the corresponding value of $\eta$ need not vanish. The boundary term

$$

\left[\frac{\partial L}{\partial \dot q}\eta\right]_{t_0}^{t_1}

$$

must then be handled explicitly. For example, if $q(t_1)$ is free while $t_1$ is fixed, stationarity requires

$$

\left.\frac{\partial L}{\partial \dot q}\right|_{t_1}=0.

$$

Such conditions are called *natural boundary conditions*. They are not extra guesses; they are the part of the variational calculation that fixed endpoints previously hid.

## Adding a total derivative

Suppose

$$

\widetilde L=L+\frac{\mathrm d }{\mathrm d t}F(q,t).

$$

Then

$$

\widetilde S=S+F(q(t_1),t_1)-F(q(t_0),t_0).

$$

For fixed endpoints the added quantity is fixed, so it does not change the stationary paths. Different-looking Lagrangians can therefore encode the same equations of motion.

## From particles to fields

For a field $\phi(x,t)$, the action becomes an integral over space and time:

$$

S[\phi]=\int \mathcal L(\phi,\partial_\mu\phi,x)\,\,\mathrm d^{d+1}x.

$$

Varying the field and integrating by parts in every coordinate gives

$$

\boxed{
\frac{\partial \mathcal L}{\partial \phi}
-\partial_\mu\left(\frac{\partial \mathcal L}{\partial (\partial_\mu\phi)}\right)=0.
}

$$

The logical structure is unchanged: vary the whole object, move derivatives off the arbitrary variation, and require the remaining coefficient to vanish.

## First variation versus second variation

The condition $\delta S=0$ identifies a stationary path. To classify it, examine the quadratic term in

$$

S[q+\varepsilon\eta]
=S[q]+\varepsilon\,\delta S
+\frac12\varepsilon^2\,\delta^2S+\cdots.

$$

A positive second variation for every nonzero admissible $\eta$ indicates a local minimum. An indefinite second variation indicates a saddle. Mechanics usually begins with the first variation because it already supplies the equations of motion.

## A reliable derivation checklist

1. State the functional and the allowed class of paths.
1. Write $q_\varepsilon=q+\varepsilon\eta$.
1. Translate endpoint restrictions into conditions on $\eta$.
1. Differentiate with respect to $\varepsilon$ at $\varepsilon=0$.
1. Integrate by parts until derivatives no longer act on $\eta$.
1. Keep or justify every boundary term.
1. Use the arbitrariness of the interior variation.
1. Check the resulting equation against a familiar special case.

**One-sentence summary**

The Euler--Lagrange equation is the pointwise condition forced on a path when the first-order change of an integral functional vanishes for every allowed infinitesimal deformation of that path.
