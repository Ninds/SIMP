# Why \(T-V\)?

*A gentle route to the action and Lagrangian mechanics*

> Markdown reading edition prepared from the recovered nine-page PDF. The diagrams and exact typesetting are preserved in the PDF. No original LaTeX source was recovered.

This is a conceptual explanation, not a problem-solving manual. It distinguishes what the intuition suggests from what the principle of stationary action actually states.

## 1. Begin with a free particle

Imagine a particle travelling from \(A\) to \(B\) in a fixed time \(\tau\), with no force acting. Many possible journeys share those endpoints and that duration, but the steady journey has a special property.

Suppose a particle travels 10 m in 2 s:

| Journey | First second | Second second | Average \(v^2\) |
| --- | ---: | ---: | ---: |
| Steady | 5 | 5 | 25 |
| Uneven | 3 | 7 | 29 |

Both journeys cover the same distance, but the uneven one has the larger average of \(v^2\). Since

\[
T=\frac12mv^2,
\]

velocity fluctuations increase the accumulated kinetic energy.

Write any velocity profile as

\[
v(t)=\bar v+u(t),
\qquad
\int_0^\tau u(t)\,dt=0.
\]

Then

\[
\int_0^\tau T\,dt
=\frac{m\tau}{2}\bar v^2
+\frac m2\int_0^\tau u(t)^2\,dt.
\]

The second term cannot be negative and vanishes only when \(u(t)=0\). Thus the constant-velocity path minimizes accumulated kinetic energy among paths with the same endpoints and duration.

This does not mean that the particle is trying to save fuel. It identifies a mathematical property of inertial motion.

## 2. What does unnecessary variation mean?

The fixed-displacement condition makes the average velocity fixed. Any departure \(u(t)\) from that average has zero time integral, while its square contributes positively. The square is why a period of extra speed is not cancelled by an equally long period of reduced speed.

## 3. Change the question: where can a particle rest?

Now place the particle in a force field and ask where it could remain at rest.

At an equilibrium point \(x_0\),

\[
F(x_0)=0.
\]

For a small displacement \(\delta x\), the work done by the force is approximately

\[
\delta W=F(x_0)\,\delta x.
\]

At equilibrium there is no first-order work. This condition alone identifies equilibrium, not stability: both the bottom of a bowl and the top of a hill can be equilibrium points.

## 4. Exactly what is \(W\)?

For a conservative force, choose a reference position \(x_r\) and define

\[
W(x)=\int_{x_r}^{x}F(s)\,ds.
\]

This is the work done by the force in moving from the reference position to \(x\). It is a function of position, not extra work performed during every later second of the motion.

For a constant force \(F\), with \(x_r=0\),

\[
W(x)=Fx,
\qquad
\delta W\simeq F\,\delta x.
\]

## 5. Work done by the force versus potential energy

Potential energy uses the opposite sign:

\[
F(x)=-\frac{dV}{dx},
\qquad
F(x)=\frac{dW}{dx}.
\]

Therefore

\[
W(x)=-V(x)+C.
\]

With matching reference constants, \(W=-V\).

| | \(W(x)\) | \(V(x)\) |
| --- | --- | --- |
| Meaning | Work done by the force from a reference point | Potential energy at the position |
| Moving with the force | Increases | Decreases |
| Moving against the force | Decreases | Increases |
| Stable equilibrium | Local maximum | Local minimum |

Near Earth's surface, with upward coordinate \(y\),

\[
V(y)=mgy,
\qquad
W(y)=-mgy.
\]

Raising the particle requires positive work against gravity. Gravity itself does negative work, so \(W\) decreases as \(V\) increases.

## 6. Now let the particle move

Return to a journey from \(A\) to \(B\) in time \(\tau\), now in the presence of a force. A small alteration of the proposed position-time curve changes both the positions visited and the velocities around the altered section.

The free-particle observation still matters: making the velocity profile more uneven tends to increase \(\int T\,dt\). But the force contribution must also enter.

## 7. Two effects of one small perturbation

A small path perturbation has two consequences:

1. It changes the velocities, and hence the accumulated kinetic energy \(\int T\,dt\).
2. It changes the positions visited in the force field. Since \(\delta W=F(x)\delta x\), it changes \(\int W(x(t))\,dt\).

These first-order changes can have opposite signs. This motivates assigning the whole journey the quantity

\[
S[x]=\int_0^\tau \bigl(T+W(x)\bigr)\,dt,
\]

called the action.

The intuitive proposal is that, for the physical journey, the first-order changes of the kinetic and work contributions balance when the path is altered slightly.

## 8. What exactly is being balanced?

It is not the values of \(T\) and \(W\) themselves. They need not be equal or individually small. What balances is their response to a small alteration of the path:

\[
\delta\int_0^\tau T\,dt
+\delta\int_0^\tau W\,dt=0.
\]

The endpoints and elapsed time remain fixed, and the condition must hold for every sufficiently small permitted perturbation.

## 9. From small time steps to the full action

Divide the journey into short intervals \(\Delta t\). The contribution from one interval is approximately

\[
\Delta S\approx (T+W)\Delta t.
\]

Adding the contributions and refining the partition gives

\[
S=\lim_{\Delta t\to0}\sum_i(T_i+W_i)\Delta t
=\int_0^\tau(T+W)\,dt.
\]

Action has units of energy multiplied by time. It is neither the particle's total energy nor the total work done along the actual path.

A local subtlety matters: displacing the path at one time changes velocities just before and after that time. We therefore require the integrated first-order change to vanish, not \(\delta T+\delta W=0\) separately at each isolated instant.

## 10. Why the familiar minus sign appears

For a conservative force, \(W=-V\). Hence

\[
S[x]=\int_0^\tau(T-V)\,dt.
\]

The integrand is the Lagrangian:

\[
\boxed{L=T-V.}
\]

The minus sign does not mean that nature prefers high potential energy. It appears because potential energy is the negative of the work done by a conservative force.

The physical path is stationary:

\[
\boxed{\delta S=0.}
\]

For a free particle the stationary value is a minimum, but in general stationary does not always mean smallest. This is why the principle is called stationary action rather than universally least action.

The free-particle and equilibrium examples motivate the form \(T+W\), but they do not logically force it. Stationary action is a physical principle whose consequences must agree with observed motion.

## 11. Does the balance give the right motion?

For a constant force \(F\), take \(W(x)=Fx\). Then

\[
S=\int_0^\tau\left(\frac12m\dot x^2+Fx\right)dt.
\]

Alter the path by \(\delta x(t)\), with \(\delta x=0\) at the endpoints. The work contribution changes by

\[
\delta\int_0^\tau W\,dt
=\int_0^\tau F\,\delta x\,dt.
\]

The kinetic contribution changes by

\[
\delta\int_0^\tau T\,dt
=\int_0^\tau m\dot x\,\delta\dot x\,dt
=-\int_0^\tau m\ddot x\,\delta x\,dt,
\]

where integration by parts and the fixed endpoints were used. Therefore

\[
\delta S=\int_0^\tau(F-m\ddot x)\delta x\,dt.
\]

If this vanishes for every permitted \(\delta x(t)\), then

\[
\boxed{m\ddot x=F.}
\]

Thus the kinetic response produces the acceleration term, the work response produces the force term, and stationarity balances them.

## 12. Why call this a new formalism?

Newton's description begins with a force and asks for the resulting acceleration. Lagrange's description begins with a scalar \(L\), assigns an action to every possible history, and identifies the actual history through stationarity.

For a simple particle the descriptions give the same motion. The Lagrangian viewpoint becomes especially useful when coordinates, constraints and systems become more complicated.

## 13. The whole intuition in one place

1. **Start with inertia.** For fixed endpoints and elapsed time, uniform free motion minimizes accumulated kinetic energy; velocity fluctuations add a positive contribution.
2. **Consider equilibrium.** A particle can remain where a small displacement produces no first-order work. Stability requires a restoring response.
3. **Combine the ideas.** In a conservative force field, altering a trajectory changes both the accumulated kinetic energy and the position-dependent work contribution. The physical trajectory is stationary when their first-order changes balance:

\[
\delta\int_0^\tau(T+W)\,dt=0,
\]

and because \(W=-V\),

\[
\boxed{\delta\int_0^\tau(T-V)\,dt=0.}
\]

The action is not an ordinary cost that nature must always minimize. Its stationarity expresses a balance between the inertial and force-related effects of perturbing a possible history.
