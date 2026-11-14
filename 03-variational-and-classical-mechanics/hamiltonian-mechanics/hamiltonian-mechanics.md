# Hamiltonian Mechanics: An Intuition-First Tutorial

> Markdown reading edition. TikZ diagrams and print-layout elements are preserved in the PDF and LaTeX editions.

## Before we begin

You have already met the action, the calculus of variations, and the Euler--Lagrange equation. You know that a Lagrangian can be written as $L=T-V$ for an ordinary conservative mechanical system, or as $T+W$ when $W=-V$ is the appropriate *work potential* (up to an irrelevant constant).

This tutorial takes that understanding as its starting point. Its goal is not to make you fluent in advanced calculations. It is to make Hamiltonian mechanics feel *inevitable* rather than an arbitrary change of symbols.

The whole journey fits into one chain of thoughts:

$$

\boxed{\text{action}\ \longrightarrow\ L(q,\dot q)\ \longrightarrow\ p=\frac{\partial L}{\partial \dot q}\ \longrightarrow\ H(q,p)\ \longrightarrow\ (\dot q,\dot p).}

$$

We shall spend most of our time on the *why* behind the middle arrows.

**A word about notation.** We first study one coordinate $q(t)$, with velocity $\dot q=\mathrm dq/\mathrm dt$. Later, $q$ may mean an angle or any other *generalised coordinate*: it need not be a distance. The symbol $p$ will always mean the momentum *conjugate to that coordinate*.

## Why invent another way to describe motion?

### A familiar question, asked in a different form

Imagine a particle travelling along a line in a potential $V(q)$. Newton's law says

$$

m\ddot q=-V'(q).

$$

This is a *second-order* equation for position. To predict the future, we must know both the present position and velocity.

But we can rewrite exactly the same motion as a pair of *first-order* equations. Define the familiar momentum $p=m\dot q$. Then

$$

\boxed{\dot q=\frac{p}{m},\qquad \dot p=-V'(q).}

$$

The first equation answers: *how does position change?* The second answers: *how does momentum change?*

Nothing new has happened to the physics. We have merely described a moving state by a *pair* $(q,p)$ instead of by a second-order equation for $q$ alone.

### The quantity that gives both answers

For this particular system, its energy is

$$

E=T+V=\tfrac12m\dot q^2+V(q)
=\frac{p^2}{2m}+V(q).

$$

For a moment, call this expression $H(q,p)$. Do two simple differentiations:

$$

\frac{\partial H}{\partial p}=\frac{p}{m},\qquad \frac{\partial H}{\partial q}=V'(q).

$$

Compare these with the two equations in the displayed equation. We have *discovered*, before introducing any new formalism, that

$$

\boxed{\dot q=\frac{\partial H}{\partial p},\qquad
\dot p=-\frac{\partial H}{\partial q}.}

$$

These derivatives are not initially mysterious. In the simplest example, one derivative gives the velocity; the other gives minus the force.

This is the seed of Hamiltonian mechanics. A single function $H(q,p)$ supplies *both* directions of change.

Why not write $E(q,\dot q)=\tfrac12m\dot q^2+V(q)$ and differentiate with respect to velocity? Because $\partial E/\partial\dot q=m\dot q=p$, *not* $\dot q$. If we want the derivative of our new function to give velocity, $p$ is the more natural input variable.

### A state is now a point in a plane

Every pair $(q,p)$ is one possible instantaneous state, represented by a point in *phase space*. As the system evolves, the point traces a curve. Position and momentum are treated as independent coordinates for the purpose of describing the *current state*; the equations then tell us how that point moves.

This language becomes especially powerful when there are several coordinates, constraints, or interactions. We will return to phase-space pictures after deriving the general equations.

## Why momentum rather than velocity?

### What the action was already trying to tell us

Recall the action for one coordinate:

$$

S[q]=\int_{t_0}^{t_1}L(q,\dot q,t)\,\mathrm d t.

$$

Perturb the path slightly: $q(t)\mapsto q(t)+\varepsilon\eta(t)$, so that $\dot q\mapsto\dot q+\varepsilon\dot\eta$.

To first order, the change in the action is

$$

\delta S=\int_{t_0}^{t_1}
\left(\frac{\partial L}{\partial q}\,\eta+\frac{\partial L}{\partial \dot q}\,\dot\eta\right)\,\mathrm d t.

$$

Notice the factor multiplying the change in *velocity*:

$$

\boxed{\frac{\partial L}{\partial \dot q}.}

$$

It appears naturally, without us having chosen any new definition. The action itself is inviting us to give this quantity a name.

**Definition (canonical or conjugate momentum).** For a coordinate $q$ with Lagrangian $L(q,\dot q,t)$, define

$$

\boxed{p:=\frac{\partial L}{\partial \dot q}.}

$$

For a conventional particle with $L=\tfrac12m\dot q^2-V(q)$, this reduces to $p=m\dot q$.

### Momentum is the sensitivity of the Lagrangian to velocity

Hold position and time fixed, and make a tiny change in velocity. Then

$$

\Delta L\approx\frac{\partial L}{\partial \dot q}\,\Delta\dot q=p\,\Delta\dot q.

$$

So $p$ measures how strongly the Lagrangian responds to a small change in velocity. This is a subtler idea than simply memorising $p=m\dot q$.

It is also why $p$ can be meaningful even when $q$ is not a distance and $\dot q$ is not an ordinary linear velocity.

### The Euler--Lagrange equation is already an equation for momentum

The integration-by-parts step you know from the calculus of variations gives

$$

\delta S=
\left[\frac{\partial L}{\partial \dot q}\,\eta\right]_{t_0}^{t_1}
+\int_{t_0}^{t_1}
\left(\frac{\partial L}{\partial q}-\frac{\mathrm d }{\mathrm d t}\left(\frac{\partial L}{\partial \dot q}\right)\right)\eta\,\mathrm d t.

$$

For fixed endpoints the boundary term vanishes. Requiring $\delta S=0$ leads to

$$

\frac{\mathrm d }{\mathrm d t}\left(\frac{\partial L}{\partial \dot q}\right)=\frac{\partial L}{\partial q}.

$$

Now use the natural name $p=\partial L/\partial\dot q$:

$$

\boxed{\dot p=\frac{\partial L}{\partial q}.}

$$

The move from velocity to momentum is *not* something Hamilton invented out of nowhere. The Euler--Lagrange equation is already telling us what changes in time: it is $\partial L/\partial\dot q$. Hamiltonian mechanics takes that quantity seriously as a variable in its own right.

### A striking example: moving around a circle

Suppose a particle of mass $m$ is constrained to move on a circle of radius $R$, described by its angle $\theta$. Its speed is $R\dot\theta$, and

$$

L(\theta,\dot\theta)=\tfrac12mR^2\dot\theta^2-V(\theta).

$$

The momentum conjugate to $\theta$ is

$$

\boxed{p_\theta=\frac{\partial L}{\partial \dot\theta}=mR^2\dot\theta=I\dot\theta,\qquad I=mR^2.}

$$

This is *angular momentum*, not $m\dot\theta$. That is exactly as it should be: $\theta$ is an angle, so its conjugate momentum is the momentum associated with rotation.

More generally, different coordinates can lead to different kinds of conjugate momentum. The universal definition $p=\partial L/\partial\dot q$ adapts automatically.

What is the conjugate momentum for $L=\tfrac12a(q)\dot q^2-V(q)$, where $a(q)>0$? It is $p=a(q)\dot q$, not necessarily a constant multiple of velocity. We will use this example later.

### There is also a boundary interpretation

If we do *not* hold the endpoints of the varied path fixed, the first-order variation along a true physical path reduces to

$$

\delta S_{\mathrm{on\ shell}}=[p\,\delta q]_{t_0}^{t_1}.

$$

With the initial endpoint fixed, a tiny displacement of the final endpoint changes the physical action by approximately $p(t_1)\,\delta q(t_1)$. Momentum tells us how sensitive the action is to a displacement of the endpoint.

This observation is not needed to solve equations, but it gives the word *conjugate* a deeper meaning: $p$ is naturally paired with changes in $q$.

## The next puzzle: how to build a function of $(q,p)$

### We want to exchange velocity for momentum

In Lagrangian mechanics we feed $L$ a position and a velocity: $L(q,\dot q,t)$. We now want a function that takes position and momentum: $H(q,p,t)$.

The first requirement is that we can recover the velocity from $p=\partial L/\partial\dot q$. For a standard mass, $p=m\dot q$ gives $\dot q=p/m$.

When the Lagrangian has a sufficiently non-degenerate dependence on velocity, this inversion works locally. For several coordinates the relevant condition is that the velocity Hessian matrix $\bigl(\partial^2 L/\partial\dot q_i\partial\dot q_j\bigr)$ be invertible. Some constrained systems require extra machinery; we leave those aside.

### Why not just substitute $\dot q(p)$ into $L$?

For our ordinary particle,

$$

L=\frac12m\dot q^2-V(q),\qquad
L\bigl(q,\dot q(p)\bigr)=\frac{p^2}{2m}-V(q).

$$

Differentiate this substituted expression with respect to $p$. It gives $p/m=\dot q$: promising! But its derivative with respect to $q$ is $-V'(q)$, while the desired momentum equation $\dot p=-V'(q)$ would require the *negative* derivative of the new function to equal the force. We need a function whose $q$-derivative has the opposite sign from the $q$-derivative of $L$.

Indeed, simply replacing $\dot q$ by $p/m$ in $L$ does not produce the correct second equation. We need an adjustment, not a mere relabelling.

### Invent the adjustment from what we want its derivative to do

For the moment, keep $q,t$ fixed and imagine $L$ as a curve against velocity $v=\dot q$. We know

$$

p=\frac{\partial L}{\partial v}.

$$

The tangent line at the chosen velocity $v$ has slope $p$ and equation

$$

\text{tangent}(u)=L(v)+p(u-v)=p\,u-\bigl(pv-L(v)\bigr).

$$

The *negative of its vertical intercept* is $pv-L(v)$. This suggests a new quantity

$$

\boxed{H(q,p,t)=p\dot q-L(q,\dot q,t),\quad
\dot q=\dot q(q,p,t).}

$$

This procedure is called a *Legendre transform*. You do not need the name to understand its role: it swaps the variable $\dot q$ for the slope $p$ of the $L$-versus-velocity curve.

> Diagram: see the PDF or LaTeX edition.

{\smallThe geometry is shown for $L(v)=\tfrac12v^2$ with $q,t$ fixed. For a nonzero potential, the curve shifts vertically, but the tangent-slope construction is unchanged.}

The Legendre transform is not an arbitrary trick for changing a minus sign. It is the natural way to exchange a variable (velocity) for the slope associated with that variable (momentum), while retaining enough information to recover the original motion.

### See $T-V$ turn into $T+V$

For $L=\frac12m\dot q^2-V(q)$ and $p=m\dot q$,

$$
\begin{aligned}
H&=p\dot q-L\\
&=m\dot q^2-\left(\frac12m\dot q^2-V\right)\\
&=\frac12m\dot q^2+V\\
&=\boxed{\frac{p^2}{2m}+V(q)}.
\end{aligned}
$$

The change $T-V\to T+V$ is not inserted as a new axiom. It emerges from the Legendre transform. In this familiar class of systems, $H$ equals the total mechanical energy.

The Hamiltonian is not *defined* as $T+V$. It is defined as $p\dot q-L$, with velocity eliminated in favour of $p$. It happens to equal $T+V$ in many ordinary systems. Keeping this distinction will prevent confusion later.

## Why exactly are Hamilton's equations these two equations?

### Start by asking what we need to predict next

At any instant a state is $(q,p)$. To predict what happens an instant later, we need two rates of change:

$$

(q,p)\ \longrightarrow\ \bigl(q+\dot q\,\Delta t,\ p+\dot p\,\Delta t\bigr).

$$

So Hamiltonian mechanics must provide $\dot q$ *and* $\dot p$ from the current $(q,p)$. We have already seen, in the elementary particle example, that $H_p$ gives velocity and $-H_q$ gives force.

The question is: does this happen for *any regular Lagrangian*, or was it a coincidence of $p=m\dot q$?

### Follow the small changes in $H$

Write $v=\dot q$ temporarily to make the chain rule clearer. We have

$$

H(q,p,t)=p\,v(q,p,t)-L\bigl(q,v(q,p,t),t\bigr).

$$

Consider a tiny change in $q$, $p$, and $t$. By the product rule and chain rule,

$$
\begin{aligned}
\,\mathrm d H
&=v\,\mathrm d p+p\,\mathrm d v
-\frac{\partial L}{\partial q}\,\mathrm d q-\frac{\partial L}{\partial v}\,\mathrm d v-\frac{\partial L}{\partial t}\,\mathrm d t\\
&=v\,\mathrm d p+\underbrace{\left(p-\frac{\partial L}{\partial v}\right)}_{=\,0}\,\mathrm d v
-\frac{\partial L}{\partial q}\,\mathrm d q-\frac{\partial L}{\partial t}\,\mathrm d t.
\end{aligned}
$$

The terms involving $\,\mathrm d v$ *cancel exactly* because we defined $p=\partial L/\partial v$. This cancellation is the decisive reason for the Legendre-transform construction.

What remains is strikingly simple:

$$

\boxed{\,\mathrm d H=v\,\mathrm d p-\frac{\partial L}{\partial q}\,\mathrm d q-\frac{\partial L}{\partial t}\,\mathrm d t.}

$$

But because $H$ is now a function of $(q,p,t)$, its ordinary total differential is also

$$

\,\mathrm d H=\frac{\partial H}{\partial q}\,\mathrm d q+\frac{\partial H}{\partial p}\,\mathrm d p+\frac{\partial H}{\partial t}\,\mathrm d t.

$$

Comparing coefficients gives

$$

\frac{\partial H}{\partial p}=v=\dot q,\qquad
\frac{\partial H}{\partial q}=-\frac{\partial L}{\partial q},\qquad
\frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t}.

$$

Finally the Euler--Lagrange equation told us $\dot p=\partial L/\partial q$. Therefore

$$

\boxed{\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}.}

$$

**Hamilton's equations are not a guess.** They are the Euler--Lagrange equation rewritten using the natural slope $p=\partial L/\partial\dot q$ and the natural transformed function $H=p\dot q-L$.

### A physical reading of each derivative

- $\dot q=H_p$: how sensitively the Hamiltonian changes when you vary momentum at fixed position tells you how quickly position moves.
- $\dot p=-H_q$: how sensitively the Hamiltonian changes when you vary position at fixed momentum tells you how quickly the conjugate momentum changes, with a minus sign.

For $H=p^2/(2m)+V(q)$, the second relation becomes $\dot p=-V'(q)$, which is exactly the familiar force law. The negative sign reflects the way a conservative force points toward decreasing potential energy.

The equations are *crossed*: differentiate with respect to momentum to find the rate of change of position; differentiate with respect to position to find the rate of change of momentum. Their opposite signs make a remarkably symmetric pair. A displacement in either state variable drives change in the other.

### The many-coordinate version

If there are generalised coordinates $q_1,\ldots,q_n$, define

$$

p_i=\frac{\partial L}{\partial \dot q_i},\qquad
H=\sum_{i=1}^{n}p_i\dot q_i-L.

$$

Provided we can express all $\dot q_i$ in terms of $(q,p,t)$, the same cancellation works component by component:

$$

\boxed{\dot q_i=\frac{\partial H}{\partial p_i},\qquad
\dot p_i=-\frac{\partial H}{\partial q_i},\qquad i=1,\ldots,n.}

$$

A system with $n$ coordinates now has $2n$ first-order equations. The physics is unchanged, but its mathematical organisation has changed dramatically.

## The variational principle survives the change

### A new-looking action, with the same physics

Starting from $H=p\dot q-L$, rearrange:

$$

L=p\dot q-H.

$$

The original action can therefore be written, along a path where $p=\partial L/\partial\dot q$, as

$$

S=\int_{t_0}^{t_1}[p\dot q-H(q,p,t)]\,\mathrm d t.

$$

Now comes the interesting idea: regard $q(t)$ and $p(t)$ as *independent functions to vary*. Define the *phase-space action*

$$

\boxed{S_H[q,p]=\int_{t_0}^{t_1}\bigl[p\dot q-H(q,p,t)\bigr]\,\mathrm d t.}

$$

Why is $p$ allowed to vary independently? Because the equation obtained by varying $p$ will itself enforce the correct velocity--momentum relationship.

### Vary momentum first

Let $p\mapsto p+\varepsilon\xi$, with $q$ held fixed. To first order,

$$

\delta_p S_H=\int_{t_0}^{t_1}\left(\dot q-\frac{\partial H}{\partial p}\right)\xi\,\mathrm d t.

$$

If the action is stationary for arbitrary small $\xi(t)$, then

$$

\boxed{\dot q=H_p.}

$$

This is one of Hamilton's equations, coming directly from the variation of momentum.

### Now vary position

Let $q\mapsto q+\varepsilon\eta$, with $p$ fixed and $\eta(t_0)=\eta(t_1)=0$. Then

$$

\delta_q S_H=\int_{t_0}^{t_1}
\left(p\dot\eta-H_q\eta\right)\,\mathrm d t.

$$

Integrate the first term by parts:

$$

\delta_q S_H=[p\eta]_{t_0}^{t_1}
-\int_{t_0}^{t_1}\left(\dot p+H_q\right)\eta\,\mathrm d t.

$$

The endpoint term vanishes, and hence

$$

\boxed{\dot p=-H_q.}

$$

This gives a second, especially beautiful answer to *why those equations?* The phase-space action contains $p\dot q-H$. Vary $p$ and you get the velocity equation. Vary $q$ and, after integration by parts, you get the momentum equation and its minus sign. The whole pair still comes from stationary action.

## Is the Hamiltonian always the total energy?

### Usually, in the examples you first meet

For the common Lagrangian

$$

L(q,\dot q)=\tfrac12m\dot q^2-V(q),

$$

we have shown $H=T+V$. For many particles with ordinary kinetic energy, the conclusion is similar. Energy conservation can then be understood through the Hamiltonian.

Differentiate $H(q(t),p(t),t)$ along a physical trajectory:

$$
\begin{aligned}
\frac{\mathrm d H}{\mathrm d t}
&=H_q\dot q+H_p\dot p+H_t\\
&=H_q H_p+H_p(-H_q)+H_t\\
&=\boxed{H_t}.
\end{aligned}
$$

Thus, if $H$ has no explicit time dependence, it is conserved.

### Two distinctions that matter

**First: conserved does not automatically mean ``mechanical energy''.** The Hamiltonian is defined by the Legendre transform, not by the phrase $T+V$. In standard time-independent natural coordinates the two often coincide, but in more general formulations the identification needs checking.

**Second: being an energy does not automatically mean being conserved.** Take

$$

L=\tfrac12m\dot q^2-V(q,t),\quad
H=\frac{p^2}{2m}+V(q,t).

$$

This $H$ is still kinetic plus potential energy, yet it can change because $V$ changes explicitly with time:

$$

\dt H=\frac{\partial V}{\partial t}.

$$

A time-dependent environment can supply or remove energy.

If $H(q,p)$ is constant along a trajectory, why does that not imply $q$ and $p$ are each constant? Because a point can move *along a level curve* of a function while the value of that function stays unchanged. A swinging pendulum and a mass on a spring do exactly this.

## Worked example I: the free particle

This is the place to feel how little machinery is actually needed.

**1. Write the Lagrangian.**  For a particle on a frictionless line, choose the zero of potential energy so that

$$

L=\tfrac12m\dot q^2.

$$

**2. Identify conjugate momentum.**

$$

p=\frac{\partial L}{\partial \dot q}=m\dot q,\qquad\dot q=\frac{p}{m}.

$$

**3. Legendre transform.**

$$

H=p\dot q-L=\frac{p^2}{2m}.

$$

**4. Apply the two equations.**

$$

\dot q=\frac{\partial H}{\partial p}=\frac{p}{m},\qquad
\dot p=-\frac{\partial H}{\partial q}=0.

$$

**5. Interpret.**  $p$ stays fixed because $H$ has no $q$-dependence. With $p(t)=p_0$,

$$

\boxed{q(t)=q_0+\frac{p_0}{m}\,t.}

$$

An unchanged momentum gives a constant velocity. This is Newton's first law in Hamiltonian language.

Here a single glance at the shape of $H$ already reveals the motion. No $q$ in $H$ means no change in $p$. A quadratic dependence on $p$ means velocity is proportional to momentum.

## Worked example II: a mass on a spring

A mass $m$ is attached to an ideal spring of stiffness $k$, with displacement $q$ measured from equilibrium.

### Construct the Hamiltonian

The potential is $V(q)=\tfrac12kq^2$, so

$$

L=\frac12m\dot q^2-\frac12kq^2,\qquad
p=m\dot q.

$$

The Hamiltonian is

$$

\boxed{H(q,p)=\frac{p^2}{2m}+\frac12kq^2.}

$$

Hamilton's equations are

$$

\boxed{\dot q=\frac{p}{m},\qquad\dot p=-kq.}

$$

### See the motion without solving anything

Suppose the mass is displaced to the right ($q>0$) and released ($p=0$). Then $\dot q=0$ at that instant, but $\dot p=-kq<0$: its momentum immediately begins becoming negative. It starts moving left.

At equilibrium ($q=0$), we have $\dot p=0$, yet momentum need not vanish. In fact, speed is greatest there. On the left ($q<0$), $\dot p>0$, and momentum eventually turns positive.

This describes oscillation in two lines. Position tells you how momentum is being changed by the spring; momentum tells you how position is changing.

### Connect to the familiar second-order equation

Differentiate $\dot q=p/m$ with respect to time and insert $\dot p=-kq$:

$$

\ddot q=\frac{\dot p}{m}=-\frac{k}{m}q,
\qquad\text{so}\qquad m\ddot q+kq=0.

$$

We have exactly the standard harmonic oscillator. Nothing was replaced physically: one second-order equation became two first-order equations.

With $\omega=\sqrt{k/m}$ and initial data $(q_0,p_0)$, its motion is

$$
\begin{aligned}
q(t)&=q_0\cos(\omega t)+\frac{p_0}{m\omega}\sin(\omega t),\\
p(t)&=p_0\cos(\omega t)-m\omega q_0\sin(\omega t).
\end{aligned}
$$

You do not need to memorise these expressions for the conceptual journey.

### Look at the motion in phase space

Because $H$ is conserved, a physical state stays on

$$

\frac{p^2}{2m}+\frac{kq^2}{2}=E.

$$

For fixed $E>0$, this is an *ellipse* in the $(q,p)$ plane. The particle does not move along a line in this plane: as $q$ and $p$ change, the point runs around the ellipse.

> Diagram: see the PDF or LaTeX edition.

Here the arrows point clockwise: at $q>0,p=0$, $\dot p=-kq<0$, so the phase point initially moves downward. The particular ellipse depends on the mass, spring constant, and energy.

The energy equation gives the *shape of the allowed path*. Hamilton's equations give its *direction and speed of traversal*. The Hamiltonian is therefore more than a conserved number: through its derivatives it organises the entire motion.

## Worked example III: gravity along a vertical line

Choose $q$ as height, positive upwards. In a uniform gravitational field,

$$

V(q)=mgq,\qquad L=\tfrac12m\dot q^2-mgq.

$$

As usual, $p=m\dot q$, and

$$

H(q,p)=\frac{p^2}{2m}+mgq.

$$

The two equations are

$$

\dot q=\frac{p}{m},\qquad\dot p=-mg.

$$

The second says the momentum decreases by $mg$ every second: gravity exerts a constant downward force. Therefore,

$$

p(t)=p_0-mgt,
\qquad
q(t)=q_0+\frac{p_0}{m}t-\frac12gt^2.

$$

This is precisely the familiar constant-acceleration motion.

There is an instructive contrast: for the free particle, $H$ had no $q$ term and momentum stayed fixed; adding the term $mgq$ creates a constant $q$-slope, so $p$ changes at a constant rate.

## Worked example IV: the pendulum and angular momentum

A pendulum consists of a mass $m$ suspended from a light rod of length $\ell$. Let $\theta=0$ at the lowest point, and take the potential to vanish there.

$$

T=\tfrac12m\ell^2\dot\theta^2,
\qquad V=mg\ell(1-\cos\theta).

$$

Define $I=m\ell^2$. The Lagrangian and conjugate momentum are

$$

L=\tfrac12I\dot\theta^2-mg\ell(1-\cos\theta),
\qquad p_\theta=I\dot\theta.

$$

The Hamiltonian is

$$

\boxed{H(\theta,p_\theta)=\frac{p_\theta^2}{2I}+mg\ell(1-\cos\theta).}

$$

Its equations become

$$

\boxed{\dot\theta=\frac{p_\theta}{I},\qquad
\dot p_\theta=-mg\ell\sin\theta.}

$$

### Why this example matters

The natural position variable is an *angle*, and its natural momentum is *angular momentum*. Nevertheless, Hamilton's equations have exactly the same form as for an ordinary particle on a line.

Use $p_\theta=I\dot\theta$ in $\dot p_\theta=-mg\ell\sin\theta$ to recover

$$

I\ddot\theta=-mg\ell\sin\theta.

$$

For small angles, $\sin\theta\approx\theta$ and the pendulum behaves approximately like a harmonic oscillator. For larger angles the nonlinearity matters; Hamilton's equations themselves need no approximation.

At the turning point of a swinging pendulum, $\dot\theta=0$ so $p_\theta=0$. Does that mean the system is momentarily at equilibrium? No: unless $\sin\theta=0$, the angular momentum is *changing* and the pendulum immediately reverses direction.

## The deeper reason: generalised momentum is not always $m\dot q$

### A coordinate-dependent kinetic coefficient

Take a one-dimensional Lagrangian of the form

$$

L(q,\dot q)=\frac12a(q)\dot q^2-V(q),\qquad a(q)>0.

$$

You might encounter this because of a complicated coordinate system or a mechanical constraint. The key point is that the coefficient of $\dot q^2$ changes with position.

Directly from the definition,

$$

p=\frac{\partial L}{\partial \dot q}=a(q)\dot q,
\qquad\dot q=\frac{p}{a(q)}.

$$

The Legendre transform is

$$

\boxed{H(q,p)=\frac{p^2}{2a(q)}+V(q).}

$$

And Hamilton's equations are

$$

\boxed{\dot q=\frac{p}{a(q)},\qquad
\dot p=\frac{a'(q)p^2}{2a(q)^2}-V'(q).}

$$

The momentum rate now has a term involving $a'(q)$. This is not an extra physical force magically introduced by the formalism. It accounts for the way the chosen coordinate measures motion differently at different positions.

### Check that it is exactly Euler--Lagrange

Euler--Lagrange, applied directly to the displayed equation, says

$$

\frac{\mathrm d }{\mathrm d t}\bigl(a(q)\dot q\bigr)=\tfrac12a'(q)\dot q^2-V'(q).

$$

Expand the derivative and rearrange:

$$

a(q)\ddot q+\tfrac12a'(q)\dot q^2+V'(q)=0.

$$

Now take the Hamiltonian result, use $p=a(q)\dot q$, and compare:

$$

\dot p=a(q)\ddot q+a'(q)\dot q^2
=\tfrac12a'(q)\dot q^2-V'(q).

$$

They are identical.

**This is the strongest reason not to define momentum by $m\dot q$ in advance.** In generalised coordinates the correct momentum is whatever the Lagrangian tells us via $p=\partial L/\partial\dot q$. Hamiltonian mechanics works with that quantity directly, preserving the same simple pair of equations in very different settings.

### A useful extension: motion in polar coordinates

For a mass $m$ moving in a plane under a central potential $V(r)$,

$$

L=\tfrac12m\left(\dot r^2+r^2\dot\theta^2\right)-V(r).

$$

There are *two* conjugate momenta:

$$

p_r=m\dot r,\qquad p_\theta=mr^2\dot\theta.

$$

The Hamiltonian is

$$

\boxed{H=\frac{p_r^2}{2m}+\frac{p_\theta^2}{2mr^2}+V(r).}

$$

From its derivatives, all four equations follow:

$$
\begin{aligned}
\dot r&=\frac{p_r}{m},
&\dot\theta&=\frac{p_\theta}{mr^2},\\
\dot p_r&=\frac{p_\theta^2}{mr^3}-V'(r),
&\dot p_\theta&=0.
\end{aligned}
$$

The last equation is particularly satisfying: $H$ is independent of $\theta$, so $p_\theta$ is conserved. This is conservation of angular momentum emerging directly from the form of the Hamiltonian. The positive $p_\theta^2/(mr^3)$ term in the radial equation reflects radial motion in polar coordinates, not a newly added fundamental force.

## Phase space is more than a diagram

### Energy contours and the direction of motion

For a time-independent Hamiltonian $H(q,p)$, motion lies on a contour $H=E$. A tiny displacement $(\,\mathrm d q,\,\mathrm d p)$ tangent to such a contour obeys

$$

H_q\,\mathrm d q+H_p\,\mathrm d p=0.

$$

Hamilton's equations prescribe

$$

\begin{pmatrix}\dot q\\\dot p\end{pmatrix}
=\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\begin{pmatrix}H_q\\H_p\end{pmatrix}.

$$

In words, the velocity of the *phase-space point* is obtained by turning the gradient of $H$ through a right angle, with a particular orientation. Thus the motion is automatically tangent to the level curves, rather than crossing them.

> Diagram: see the PDF or LaTeX edition.

This picture is schematic: it communicates the geometry, not a particular mass or spring constant.

### Equilibrium is a stationary point of the Hamiltonian

An equilibrium phase-space state satisfies $\dot q=\dot p=0$, so for a smooth one-coordinate Hamiltonian

$$

H_p=0,\qquad H_q=0.

$$

For the spring $H=p^2/(2m)+kq^2/2$, the only equilibrium is $(q,p)=(0,0)$. The surrounding energy contours are closed, so small displacements cause oscillation rather than escape.

For the pendulum there are also upright equilibria at $\theta=\pi$ (modulo $2\pi$), which are unstable. The shape of the Hamiltonian, and not merely the individual differential equations, helps us understand these qualitative differences.

## A glimpse ahead: momentum can differ from mechanical momentum

We have seen angular momentum and coordinate-dependent momentum. There is one further distinction worth knowing now, even if you postpone the algebra.

For a charged particle of charge $e$ in electromagnetic potentials $\boldsymbol A(q,t)$ and $\phi(q,t)$, a standard Lagrangian is

$$

L=\frac12m\lVert\dot{\boldsymbol q}\rVert^2
+e\boldsymbol A\cdot\dot{\boldsymbol q}-e\phi.

$$

Its canonical momentum is

$$

\boxed{\boldsymbol p=m\dot{\boldsymbol q}+e\boldsymbol A.}

$$

The mechanical momentum is $m\dot{\boldsymbol q}$; the canonical momentum is $\boldsymbol p$. They need not be the same. The Hamiltonian is

$$

H=\frac{\lVert\boldsymbol p-e\boldsymbol A\rVert^2}{2m}+e\phi.

$$

And still $\dot{\boldsymbol q}=\partial H/\partial\boldsymbol p$.

This is precisely why the *definition* $p=\partial L/\partial\dot q$ is more general than the school-level formula $p=mv$. Hamiltonian mechanics is built around the momentum *conjugate to the coordinate*, not a preconceived notion of linear momentum.

## A short preview: Poisson brackets

You do not need this for the basics, but it reveals how tightly the structure fits together. For any smooth quantity $F(q,p,t)$, the chain rule and Hamilton's equations give

$$
\begin{aligned}
\dt F
&=F_q\dot q+F_p\dot p+F_t\\
&=F_qH_p-F_pH_q+F_t.
\end{aligned}
$$

Define the *Poisson bracket* of two functions by

$$

\{F,G\}:=F_qG_p-F_pG_q.

$$

Then the entire time evolution of any observable can be written as

$$

\boxed{\dt F=\{F,H\}+\frac{\partial F}{\partial t}.}

$$

For $F=q$ it gives $\dot q=H_p$; for $F=p$ it gives $\dot p=-H_q$. So the two Hamilton equations are special cases of a single rule describing how every physical quantity evolves.

## Guided practice: think before calculating

Try each question first without manipulating equations. Then use the short solutions that follow.

1. **Recognising what changes.** A Hamiltonian is $H(q,p)=p^2/(2m)+U_0$, where $U_0$ is constant. What happens to momentum? What does the particle do?
2. **Finding the force.** A particle has $H(q,p)=p^2/(2m)+\tfrac12kq^2+F_0q$. Write Hamilton's equations. What is the equilibrium position?
3. **Momentum is not always $m\dot q$.** A coordinate $x$ has $L=\tfrac12(1+x^2)\dot x^2-\tfrac12x^2$. Find $p$, eliminate $\dot x$, and construct $H(x,p)$.
4. **Conserved coordinate momentum.** If $H(q_1,q_2,p_1,p_2)$ does not depend on $q_2$, which momentum is conserved? Which Hamilton equation tells you this?
5. **Energy versus conservation.** For $H(q,p,t)=p^2/(2m)+\tfrac12k(t)q^2$, is $H$ necessarily constant? What is $\,\mathrm d H/\,\mathrm d t$ along the motion?
6. **Qualitative pendulum.** At a pendulum's lowest point with $\theta=0$ and $p_\theta>0$, which way does its angle initially change? What is $\dot p_\theta$ at that precise instant?

### Answers and the reason behind them

**1.** $\dot p=-H_q=0$, and $\dot q=p/m$ is constant. The additive constant $U_0$ does not affect the motion.

**2.** $\dot q=p/m$ and $\dot p=-kq-F_0$. Equilibrium requires $p=0$ and $-kq-F_0=0$, hence $q_{\rm eq}=-F_0/k$. Adding a linear potential term changes the force by a constant.

**3.** $p=(1+x^2)\dot x$, so $\dot x=p/(1+x^2)$ and

$$

H(x,p)=\frac{p^2}{2(1+x^2)}+\frac12x^2.

$$

The coordinate-dependent kinetic coefficient has been transferred to the denominator of the momentum term.

**4.** $\dot p_2=-\partial H/\partial q_2=0$, so $p_2$ is conserved. This is the simplest form of the connection between an absent coordinate (a *cyclic coordinate*) and a conserved conjugate momentum.

**5.** Not necessarily: $\,\mathrm d H/\,\mathrm d t=\partial H/\partial t=\tfrac12k'(t)q^2$. Changing the spring stiffness externally can do work on the system.

**6.** $\dot\theta=p_\theta/I>0$, so the angle is increasing. At $\theta=0$, $\dot p_\theta=-mg\ell\sin0=0$. A zero *instantaneous rate of change of momentum* does not imply zero momentum.

## One-page mental map

**The input from Lagrangian mechanics**

$$

S[q]=\int L(q,\dot q,t)\,\mathrm d t,
\qquad \frac{\mathrm d }{\mathrm d t}\left(\frac{\partial L}{\partial \dot q}\right)=\frac{\partial L}{\partial q}.

$$

**What the action tells us to call momentum**

$$

\boxed{p=\frac{\partial L}{\partial \dot q}.}

$$

**What we want to achieve**

Use $(q,p)$ to describe the current state and obtain its two rates of change directly.

**How we change variables**

$$

\boxed{H(q,p,t)=p\dot q-L(q,\dot q,t),\quad
\dot q=\dot q(q,p,t).}

$$

**What follows (not what we must guess)**

$$

\boxed{\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}.}

$$

**Why it works**

The unwanted $\,\mathrm d\dot q$ terms cancel in $\,\mathrm d H$ because $p=\partial L/\partial\dot q$; the remaining $q$ derivative agrees with Euler--Lagrange. Alternatively, both equations come from stationarity of $\int(p\dot q-H)\,\mathrm d t$.

**How to read it**

Momentum determines how position changes. Position determines how momentum changes. Taken together, these rates move the state through phase space.

### Five ideas to retain

1. Hamiltonian mechanics describes the *same physical motion* as Newtonian and Lagrangian mechanics.
2. The key variable is *conjugate* momentum, $p=L_{\dot q}$, not always $m\dot q$.
3. The Legendre transform exchanges velocity for momentum by using the slope of $L$ as the new variable.
4. Hamilton's crossed, opposite-sign equations are forced by that transform and the variational principle.
5. The Hamiltonian often equals total energy, but its *definition* is $\sum p_i\dot q_i-L$, and its chief job is to generate motion.

## Final perspective

Lagrangian mechanics asks which entire path makes the action stationary. Hamiltonian mechanics asks how the present state $(q,p)$ flows into the next state. It has not abandoned the action principle: it has reorganised it, exposing a paired structure that was present all along.

The most important step is the least arbitrary one. Because the action already gives $\partial L/\partial\dot q$ a special role, we call it momentum. Because we want a function of this momentum, we perform a Legendre transform. And because of how that transform works, Hamilton's equations follow.

**title={\strut The thought worth taking away}**

*Velocity tells us how position is changing. Conjugate momentum tells us which velocity-related quantity the action singles out. Hamiltonian mechanics uses that natural momentum so that one function can describe both the evolution of position and the evolution of momentum.*

{End of tutorial \quad\textbullet\quad Suggested next topic: symmetries, cyclic coordinates, and Poisson brackets.}
