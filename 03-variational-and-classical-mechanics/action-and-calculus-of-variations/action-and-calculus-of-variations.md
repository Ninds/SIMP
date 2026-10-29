# From Calculus to the Calculus of Variations

*A patient route to the Euler-Lagrange equation*

> Markdown reading edition prepared from the recovered ten-page companion PDF. The exact typesetting is preserved in the PDF. No original LaTeX source was recovered.

Ordinary calculus asks what happens when we change a number slightly. The calculus of variations asks what happens when we change an entire function slightly.

These notes follow [Why \(T-V\)?](../lagrangian-mechanics/README.md), which motivates the action and the Lagrangian. The aim here is to make stationary action mathematically precise.

## 1. A function takes a number to a number

For

\[
f(x)=x^2,
\]

changing \(x\) to \(x+\delta x\) gives

\[
f(x+\delta x)-f(x)
=2x\,\delta x+(\delta x)^2.
\]

For small \(\delta x\), the leading change is

\[
\delta f\approx2x\,\delta x.
\]

The derivative \(f'(x)=2x\) measures the sensitivity of the output to a small change in the numerical input.

## 2. A functional takes a function to a number

Now let the input be a whole function \(q\). For bounded real-valued functions on \([0,1]\), define

\[
\lVert q\rVert_\infty
=\sup_{0\le t\le1}|q(t)|.
\]

This supremum norm returns one number: the largest magnitude of the function, or its least upper bound when the largest value is not attained.

The map

\[
q\longmapsto\lVert q\rVert_\infty
\]

is a functional. A function such as \(f(x)=x^2\) accepts a number; a functional such as \(J[q]\) accepts an entire function. Square brackets help remind us of this distinction.

## 3. Other functionals: the whole curve matters

Two integral functionals are

\[
J_1[q]=\int_0^1q(t)\,dt,
\qquad
J_2[q]=\int_0^1q(t)^2\,dt.
\]

The first records signed area; the second records accumulated squared magnitude. For \(q(t)=t\),

\[
J_1[q]=\frac12,
\qquad
J_2[q]=\frac13.
\]

The action is another functional:

\[
S[q]=\int_{t_0}^{t_1}L(q(t),\dot q(t),t)\,dt.
\]

It takes a possible trajectory and assigns it one number.

## 4. What does it mean to perturb a function?

Ordinary calculus replaces \(x\) by \(x+\delta x\). Variational calculus replaces a function by a nearby function:

\[
q(t)\longmapsto q(t)+\delta q(t).
\]

Write this as

\[
q_\varepsilon(t)=q(t)+\varepsilon\eta(t),
\]

where \(q\) is the original curve, \(\eta\) is the shape of the perturbation, and \(\varepsilon\) controls its size.

For example, if

\[
q(t)=t,
\qquad
\eta(t)=t(1-t),
\]

then

\[
q_\varepsilon(t)=t+\varepsilon t(1-t).
\]

The curve bows away from the straight line while its endpoints remain fixed because \(\eta(0)=\eta(1)=0\).

Ordinary differentiation nudges a point on a number line. Variational differentiation nudges an entire graph.

## 5. A side-by-side comparison

| Ordinary calculus | Calculus of variations |
| --- | --- |
| Input: a number \(x\) | Input: a function \(q(t)\) |
| Output: \(f(x)\) | Output: \(J[q]\) |
| Perturb \(x\mapsto x+\varepsilon h\) | Perturb \(q\mapsto q+\varepsilon\eta\) |
| Examine \(f(x+\varepsilon h)\) | Examine \(J[q+\varepsilon\eta]\) |
| Differentiate with respect to \(\varepsilon\) at zero | Differentiate with respect to \(\varepsilon\) at zero |
| Stationary point: \(f'(x)=0\) | Stationary function: first variation zero for every allowed \(\eta\) |

Although \(J\) accepts a function, \(J[q+\varepsilon\eta]\) is an ordinary function of the single number \(\varepsilon\).

## 6. Differentiating a functional

Consider the smooth functional

\[
J[q]=\frac12\int_0^1q(t)^2\,dt.
\]

After the perturbation \(q\mapsto q+\varepsilon\eta\),

\[
\begin{aligned}
J[q+\varepsilon\eta]
&=\frac12\int_0^1(q+\varepsilon\eta)^2\,dt\\
&=\frac12\int_0^1q^2\,dt
+\varepsilon\int_0^1q\eta\,dt
+\frac{\varepsilon^2}{2}\int_0^1\eta^2\,dt.
\end{aligned}
\]

The coefficient of the term linear in \(\varepsilon\) gives the first-order response:

\[
\boxed{
\delta J[q;\eta]
=\left.\frac{d}{d\varepsilon}J[q+\varepsilon\eta]\right|_{\varepsilon=0}
=\int_0^1q(t)\eta(t)\,dt.}
\]

This is the first variation. It depends on both the original function \(q\) and the perturbation direction \(\eta\). We differentiate with respect to the perturbation size \(\varepsilon\), not with respect to time.

### Why not differentiate the supremum norm first?

The supremum norm is a useful example of a functional, but it is not generally differentiable. Its difficulties resemble the corner of the one-variable function \(|x|\) at zero. That is why the first derivative example uses a smooth integral functional.

## 7. What is a stationary function?

In ordinary calculus, \(x_*\) is stationary for \(f\) if

\[
f'(x_*)=0.
\]

In variational calculus, \(q_*\) is stationary for \(J\) if

\[
\boxed{\delta J[q_*;\eta]=0\quad\text{for every allowed }\eta.}
\]

The phrase “every perturbation” matters. A curve can be altered near the beginning, near the middle, over a broad interval, or in a narrow bump. Insensitivity to one selected perturbation is not stationarity.

As in ordinary calculus, stationary does not necessarily mean minimum.

## 8. From a functional to a trajectory

Let \(q(t)\) describe a particle's position, with velocity \(\dot q(t)\). Compare trajectories with fixed endpoints:

\[
q(t_0)=q_0,
\qquad
q(t_1)=q_1.
\]

For \(q_\varepsilon=q+\varepsilon\eta\), fixed endpoints require

\[
\eta(t_0)=\eta(t_1)=0.
\]

Between the endpoints, \(\eta\) can be any sufficiently smooth shape.

The action is

\[
S[q]=\int_{t_0}^{t_1}L(q,\dot q,t)\,dt.
\]

The preceding notes motivated the mechanical choice

\[
L=T+W=T-V,
\]

where \(W\) is the work done by a conservative force from a reference position and \(V\) is the potential energy. The question now is: given an action, how does stationarity produce an equation of motion?

## 9. Changing position also changes velocity

If

\[
q_\varepsilon(t)=q(t)+\varepsilon\eta(t),
\]

then

\[
\dot q_\varepsilon(t)=\dot q(t)+\varepsilon\dot\eta(t).
\]

Thus a trajectory perturbation changes both position and velocity. Differentiating

\[
S[q+\varepsilon\eta]
=\int_{t_0}^{t_1}L(q+\varepsilon\eta,\dot q+\varepsilon\dot\eta,t)\,dt
\]

with respect to \(\varepsilon\) gives

\[
\boxed{
\delta S[q;\eta]
=\int_{t_0}^{t_1}
\left(
\frac{\partial L}{\partial q}\eta
+\frac{\partial L}{\partial\dot q}\dot\eta
\right)dt.}
\]

The first term comes from changing position; the second comes from changing velocity.

## 10. The crucial step: integration by parts

We want the first variation entirely in terms of \(\eta\), not a mixture of \(\eta\) and \(\dot\eta\). Integration by parts gives

\[
\int_{t_0}^{t_1}\frac{\partial L}{\partial\dot q}\dot\eta\,dt
=\left[\frac{\partial L}{\partial\dot q}\eta\right]_{t_0}^{t_1}
-\int_{t_0}^{t_1}\frac{d}{dt}
\left(\frac{\partial L}{\partial\dot q}\right)\eta\,dt.
\]

The boundary term vanishes because \(\eta(t_0)=\eta(t_1)=0\). Hence

\[
\delta S[q;\eta]
=\int_{t_0}^{t_1}
\left[
\frac{\partial L}{\partial q}
-\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q}\right)
\right]\eta(t)\,dt.
\]

The bracket is fixed by the proposed trajectory, while \(\eta\) can be any sufficiently smooth bump. If the integral vanishes for every bump, the bracket must vanish throughout the interval. This is the fundamental lemma of the calculus of variations.

Therefore

\[
\boxed{
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q}\right)
-\frac{\partial L}{\partial q}=0.}
\]

This is the Euler-Lagrange equation. A global condition on an entire curve becomes a local differential equation because the perturbation can be concentrated near any chosen time.

## 11. Return to a familiar particle

For one-dimensional conservative motion,

\[
L(q,\dot q)=\frac12m\dot q^2-V(q).
\]

Then

\[
\frac{\partial L}{\partial\dot q}=m\dot q,
\qquad
\frac{\partial L}{\partial q}=-V'(q).
\]

The Euler-Lagrange equation becomes

\[
\frac{d}{dt}(m\dot q)+V'(q)=0.
\]

For constant mass,

\[
\boxed{m\ddot q=-V'(q)=F(q).}
\]

Thus stationary action reproduces Newton's second law for this system.

## 12. Why this is a satisfying connection

Ordinary calculus perturbs a number. If the first-order output change vanishes for every small change, the number is stationary.

Variational calculus perturbs a whole function. If the first-order output change vanishes for every allowed perturbation, the function is stationary.

The bridge is

\[
f'(x_*)=0
\quad\longleftrightarrow\quad
\delta S[q_*;\eta]=0\quad\text{for all }\eta.
\]

The action is a functional because it assigns one number to an entire possible history. The Euler-Lagrange equation is the differential equation hidden inside the stationarity condition on that history.

The earlier description of stationary action as a balance between the kinetic and work contributions is motivation, not a claim that either contribution is minimized separately or that their values are equal. What balances is their first-order response to a change of trajectory.
