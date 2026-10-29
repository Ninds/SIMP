# Vectors in Polar Coordinates

> Markdown reading edition. TikZ diagrams and print-layout elements are preserved in the PDF and LaTeX editions.

## What polar coordinates describe

In a plane, a point can be located by either Cartesian coordinates $(x,y)$ or polar coordinates $(r,\theta)$. The two descriptions refer to the same point:

$$

x=r\cos\theta,
\qquad
y=r\sin\theta.

$$

Here $r\ge 0$ is the distance from the origin and $\theta$ is an angle measured counterclockwise from the positive $x$-axis. In mechanics, both may depend on time:

$$

r=r(t),
\qquad
\theta=\theta(t).

$$

### The two polar unit vectors

At the particle we attach two perpendicular unit vectors:

- $\mathbf e_r$ points directly away from the origin;
- $\mathbf e_\theta$ points in the direction of increasing $\theta$, tangent to the circle $r=\text{constant}$.

### Deriving the unit vectors from little triangles

The component formulas do not need to be memorised. Draw a short displacement, complete a right triangle, and read off its horizontal and vertical sides.

> Diagram: see the PDF or LaTeX edition.

{\bfseries The radial triangle.}
Take a tiny outward step of length $\,\mathrm d r$ at angle $\theta$. Its horizontal side is $\,\mathrm d r\cos\theta$ and its vertical side is $\,\mathrm d r\sin\theta$. Hence

$$
\begin{aligned}
\,\mathrm d\mathbf r_{\text{radial}}
&=\,\mathrm d r\cos\theta\,\mathbf i+\,\mathrm d r\sin\theta\,\mathbf j\\
&=\,\mathrm d r\left(\cos\theta\,\mathbf i+\sin\theta\,\mathbf j\right).
\end{aligned}
$$

Dividing by the step length $\,\mathrm d r$ leaves the radial unit direction:

$$

\mathbf e_r=\cos\theta\,\mathbf i+\sin\theta\,\mathbf j.

$$

{\bfseries The tangential triangle.}
Now increase the angle while keeping $r$ fixed. The tiny arc has length $r\,\,\mathrm d\theta$ and points $90^\circ$ counterclockwise from $\mathbf e_r$. In the first quadrant it points left and up: its horizontal component is negative, with magnitude $r\,\,\mathrm d\theta\sin\theta$, while its vertical component is positive, with magnitude $r\,\,\mathrm d\theta\cos\theta$. Therefore

$$
\begin{aligned}
\,\mathrm d\mathbf r_{\text{angular}}
&=-r\,\,\mathrm d\theta\sin\theta\,\mathbf i
+r\,\,\mathrm d\theta\cos\theta\,\mathbf j\\
&=r\,\,\mathrm d\theta
\left(-\sin\theta\,\mathbf i+\cos\theta\,\mathbf j\right).
\end{aligned}
$$

Dividing by the tangential step length $r\,\,\mathrm d\theta$ gives the positive angular unit direction:

$$

\mathbf e_\theta=-\sin\theta\,\mathbf i+\cos\theta\,\mathbf j.

$$

**Where the minus sign comes from**

For $0<\theta<\pi/2$, the positive tangential direction goes left and up. Left means a negative $\mathbf i$ component; up means a positive $\mathbf j$ component. The same formula continues to work in every quadrant.

Collecting the two results,

**Polar basis written in the Cartesian basis**

$$

\boxed{\mathbf e_r=\cos\theta\,\mathbf i+\sin\theta\,\mathbf j},
\qquad
\boxed{\mathbf e_\theta=-\sin\theta\,\mathbf i+\cos\theta\,\mathbf j}.

$$

These are unit vectors and they are perpendicular:

$$

\mathbf e_r\cdot\mathbf e_r=1,
\qquad
\mathbf e_\theta\cdot\mathbf e_\theta=1,
\qquad
\mathbf e_r\cdot\mathbf e_\theta=0.

$$

> Diagram: see the PDF or LaTeX edition.

**A useful warning**

The symbols $\mathbf e_r$ and $\mathbf e_\theta$ do *not* name two globally fixed directions. Their orientation depends on $\theta$. If the particle moves around the origin, the basis itself turns.

## Tiny displacements: one radial, one angular

Suppose the particle starts at $(r,\theta)$. We first change one coordinate at a time. This separates the geometry before we combine it.

### Step 1: change $r$, but hold $\theta$ fixed

Move from $(r,\theta)$ to $(r+\,\mathrm d r,\theta)$. The motion is along the radial line, so

$$

\,\mathrm d\mathbf r_{\text{radial}}=\,\mathrm d r\,\mathbf e_r.

$$

The scalar $\,\mathrm d r$ is a signed length. If $\,\mathrm d r>0$, the displacement is outward; if $\,\mathrm d r<0$, it is inward.

### Step 2: change $\theta$, but hold $r$ fixed

Now move from $(r,\theta)$ to $(r,\theta+\,\mathrm d\theta)$. The particle follows a tiny circular arc. Its length is

$$

\text{arc length}=r\,\,\mathrm d\theta,

$$

provided $\,\mathrm d\theta$ is measured in radians. The tangent direction is $\mathbf e_\theta$, so

$$

\,\mathrm d\mathbf r_{\text{angular}}=r\,\,\mathrm d\theta\,\mathbf e_\theta.

$$

> Diagram: see the PDF or LaTeX edition.

### Step 3: add the two independent changes

To first order, a general tiny displacement is the sum:

**Differential displacement in polar coordinates**

$$

\boxed{\,\mathrm d\mathbf r=\,\mathrm d r\,\mathbf e_r+r\,\,\mathrm d\theta\,\mathbf e_\theta.}

$$

The two coefficients have units of length: $\,\mathrm d r$ is a length, while $r\,\mathrm d\theta$ is also a length because an angle in radians is dimensionless.

**Why a tiny change matters**

For a finite angular change, the straight chord and the circular arc are not identical. Their difference enters beyond first order. Differential calculus keeps the terms linear in $\,\mathrm d r$ and $\,\mathrm d\theta$, which is exactly what is needed for velocity.

## Velocity

Divide the differential displacement by the elapsed time $\,\mathrm d t$:

$$
\begin{aligned}
\mathbf v
=\frac{\,\mathrm d\mathbf r}{\,\mathrm d t}
&=\frac{\,\mathrm d r}{\,\mathrm d t}\,\mathbf e_r
+r\frac{\,\mathrm d\theta}{\,\mathrm d t}\,\mathbf e_\theta \\
&=\dot r\,\mathbf e_r+r\dot\theta\,\mathbf e_\theta.
\end{aligned}
$$

**Polar velocity**

$$

\boxed{\mathbf v=\dot r\,\mathbf e_r+r\dot\theta\,\mathbf e_\theta.}

$$

The two pieces have immediate meanings:

- $\dot r\,\mathbf e_r$ is the radial velocity;
- $r\dot\theta\,\mathbf e_\theta$ is the tangential velocity.

### A Cartesian cross-check

Start from

$$

\mathbf r=x\mathbf i+y\mathbf j,
\qquad
x=r\cos\theta,
\qquad
y=r\sin\theta.

$$

Differentiate the scalar coordinates:

$$
\begin{aligned}
\dot x&=\dot r\cos\theta-r\dot\theta\sin\theta,\\
\dot y&=\dot r\sin\theta+r\dot\theta\cos\theta.
\end{aligned}
$$

Therefore

$$
\begin{aligned}
\mathbf v
&=\dot x\mathbf i+\dot y\mathbf j\\
&=\dot r(\cos\theta\,\mathbf i+\sin\theta\,\mathbf j)
+r\dot\theta(-\sin\theta\,\mathbf i+\cos\theta\,\mathbf j)\\
&=\dot r\,\mathbf e_r+r\dot\theta\,\mathbf e_\theta.
\end{aligned}
$$

The Cartesian calculation agrees with the geometric one. This is a useful check, but the polar form makes the physical directions much easier to see.

**Pause and picture it**

If $\dot r=0$, the particle has no inward or outward motion, but it can still be moving: $r\dot\theta$ is its speed around the circle. If $\dot\theta=0$, the direction from the origin is fixed, but the particle may still move radially.

## The basis vectors rotate

It is tempting to differentiate the velocity as if $\mathbf e_r$ and $\mathbf e_\theta$ were constants. They are not. We now calculate their derivatives explicitly.

### Differentiate with respect to the angle

Using their Cartesian expressions,

$$
\begin{aligned}
\frac{\,\mathrm d\mathbf e_r}{\,\mathrm d\theta}
&=\frac{\,\mathrm d}{\,\mathrm d\theta}
(\cos\theta\,\mathbf i+\sin\theta\,\mathbf j)\\
&=-\sin\theta\,\mathbf i+\cos\theta\,\mathbf j\\
&=\mathbf e_\theta,
\end{aligned}
$$

and

$$
\begin{aligned}
\frac{\,\mathrm d\mathbf e_\theta}{\,\mathrm d\theta}
&=\frac{\,\mathrm d}{\,\mathrm d\theta}
(-\sin\theta\,\mathbf i+\cos\theta\,\mathbf j)\\
&=-\cos\theta\,\mathbf i-\sin\theta\,\mathbf j\\
&=-\mathbf e_r.
\end{aligned}
$$

**How the polar basis turns**

$$

\boxed{\frac{\,\mathrm d\mathbf e_r}{\,\mathrm d\theta}=\mathbf e_\theta},
\qquad
\boxed{\frac{\,\mathrm d\mathbf e_\theta}{\,\mathrm d\theta}=-\mathbf e_r}.

$$

The first formula says that a small increase in angle tips $\mathbf e_r$ toward $\mathbf e_\theta$. The second says that the tangent direction bends inward, toward $-\mathbf e_r$.

### Convert angle derivatives to time derivatives

Apply the chain rule:

$$

\frac{\,\mathrm d\mathbf e_r}{\,\mathrm d t}
=\frac{\,\mathrm d\mathbf e_r}{\,\mathrm d\theta}\frac{\,\mathrm d\theta}{\,\mathrm d t}
=\dot\theta\,\mathbf e_\theta,

$$

and similarly

$$

\frac{\,\mathrm d\mathbf e_\theta}{\,\mathrm d t}
=\frac{\,\mathrm d\mathbf e_\theta}{\,\mathrm d\theta}\frac{\,\mathrm d\theta}{\,\mathrm d t}
=-\dot\theta\,\mathbf e_r.

$$

**Time derivatives of the rotating basis**

$$

\boxed{\dot{\mathbf e_r}=\dot\theta\,\mathbf e_\theta},
\qquad
\boxed{\dot{\mathbf e_\theta}=-\dot\theta\,\mathbf e_r}.

$$

## Acceleration, one product rule at a time

Begin with the velocity:

$$

\mathbf v=\dot r\,\mathbf e_r+r\dot\theta\,\mathbf e_\theta.

$$

Differentiate each vector term separately.

### Step 1: differentiate the radial velocity term

Use the product rule and $\dot{\mathbf e_r}=\dot\theta\mathbf e_\theta$:

$$
\begin{aligned}
\frac{\,\mathrm d}{\,\mathrm d t}(\dot r\,\mathbf e_r)
&=\ddot r\,\mathbf e_r+\dot r\,\dot{\mathbf e_r}\\
&=\ddot r\,\mathbf e_r+\dot r\dot\theta\,\mathbf e_\theta.
\end{aligned}
$$

### Step 2: differentiate the tangential velocity term

The scalar coefficient $r\dot\theta$ and the vector $\mathbf e_\theta$ both vary:

$$
\begin{aligned}
\frac{\,\mathrm d}{\,\mathrm d t}(r\dot\theta\,\mathbf e_\theta)
&=\frac{\,\mathrm d}{\,\mathrm d t}(r\dot\theta)\,\mathbf e_\theta
+r\dot\theta\,\dot{\mathbf e_\theta}\\
&=(\dot r\dot\theta+r\ddot\theta)\mathbf e_\theta
+r\dot\theta(-\dot\theta\mathbf e_r)\\
&=(\dot r\dot\theta+r\ddot\theta)\mathbf e_\theta
-r\dot\theta^{\,2}\mathbf e_r.
\end{aligned}
$$

### Step 3: collect like directions

Add the two results. The $\mathbf e_r$ terms go together and the $\mathbf e_\theta$ terms go together:

$$
\begin{aligned}
\mathbf a
&=\left(\ddot r-r\dot\theta^{\,2}\right)\mathbf e_r
+\left(\dot r\dot\theta+\dot r\dot\theta+r\ddot\theta\right)\mathbf e_\theta\\
&=\left(\ddot r-r\dot\theta^{\,2}\right)\mathbf e_r
+\left(2\dot r\dot\theta+r\ddot\theta\right)\mathbf e_\theta.
\end{aligned}
$$

**Polar acceleration**

$$

\boxed{
\mathbf a=\left(\ddot r-r\dot\theta^{\,2}\right)\mathbf e_r
+\left(2\dot r\dot\theta+r\ddot\theta\right)\mathbf e_\theta.}

$$

**The common mistake**

Writing only $\ddot r\mathbf e_r+r\ddot\theta\mathbf e_\theta$ misses the derivatives of the basis vectors. The missing terms, $-r\dot\theta^2\mathbf e_r$ and $2\dot r\dot\theta\mathbf e_\theta$, are not optional corrections; they are required by the geometry.

## What the four acceleration terms mean

The formula is easier to remember when each term has a job:

{>{\raggedright\arraybackslash}p{31mm} >{\raggedright\arraybackslash}p{31mm} X}
\toprule
**Term** & **Direction** & **Interpretation**\\
\midrule
$\ddot r$ & radial & Change in the radial speed. Positive is outward.\\
$-r\dot\theta^2$ & radial & Inward curvature term. It remains even when the speed around a circle is constant.\\
$r\ddot\theta$ & transverse & Tangential acceleration caused by changing angular speed.\\
$2\dot r\dot\theta$ & transverse & Coupling between radial motion and rotation of the basis, often called the Coriolis term in this coordinate description.\\
\bottomrule

### A quick dimensional check

Angles in radians are dimensionless. Therefore

$$

[\dot r]=LT^{-1},
\qquad
[\ddot r]=LT^{-2},
\qquad
[\dot\theta]=T^{-1},
\qquad
[\ddot\theta]=T^{-2}.

$$

Every coefficient in the acceleration formula has units $LT^{-2}$:

$$

[r\dot\theta^2]=L(T^{-1})^2=LT^{-2},

$$

$$

[\dot r\dot\theta]=(LT^{-1})(T^{-1})=LT^{-2},
\qquad
[r\ddot\theta]=L(T^{-2})=LT^{-2}.

$$

**Why the inward term appears at constant speed**

A velocity vector can change even if its magnitude does not. During circular motion the velocity continually turns, so its derivative points toward the centre. The term $-r\dot\theta^2\mathbf e_r$ measures exactly that inward turning.

### Three useful special cases

1. **Pure radial motion:** if $\dot\theta=0$, then $\mathbf a=\ddot r\mathbf e_r$.
1. **Motion at fixed radius:** if $r=R$, then

$$

\mathbf a=-R\dot\theta^2\mathbf e_r+R\ddot\theta\mathbf e_\theta.

$$

1. **Uniform circular motion:** if $r=R$ and $\dot\theta=\omega$ is constant, then

$$

\mathbf a=-R\omega^2\mathbf e_r.

$$

## Speed squared and kinetic energy

Start again from

$$

\mathbf v=\dot r\mathbf e_r+r\dot\theta\mathbf e_\theta.

$$

The square of the speed means the dot product $v^2=\mathbf v\cdot\mathbf v$:

$$
\begin{aligned}
v^2
&=(\dot r\mathbf e_r+r\dot\theta\mathbf e_\theta)
\cdot(\dot r\mathbf e_r+r\dot\theta\mathbf e_\theta)\\
&=\dot r^{\,2}(\mathbf e_r\cdot\mathbf e_r)
+2r\dot r\dot\theta(\mathbf e_r\cdot\mathbf e_\theta)
+r^2\dot\theta^{\,2}(\mathbf e_\theta\cdot\mathbf e_\theta).
\end{aligned}
$$

Now use orthonormality:

$$

\mathbf e_r\cdot\mathbf e_r=1,
\qquad
\mathbf e_r\cdot\mathbf e_\theta=0,
\qquad
\mathbf e_\theta\cdot\mathbf e_\theta=1.

$$

The cross term vanishes, leaving

**Speed in polar coordinates**

$$

\boxed{v^2=\dot r^{\,2}+r^2\dot\theta^{\,2}.}

$$

For a particle of mass $m$, the kinetic energy is

**Kinetic energy in polar coordinates**

$$

\boxed{K=\frac12m\left(\dot r^{\,2}+r^2\dot\theta^{\,2}\right).}

$$

For circular motion $r=R$ is constant, so $\dot r=0$. If $\dot\theta=\omega$, then

$$

v=R\omega,
\qquad
K=\frac12mR^2\omega^2.

$$

**Dimensions of the energy**

Both $\dot r^2$ and $r^2\dot\theta^2$ have units $L^2T^{-2}$. Multiplication by mass gives $ML^2T^{-2}$, the dimensions of energy.

## Uniform circular motion and centripetal force

The phrase *uniform circular motion* contains several assumptions. We state them before using the shortened formulas.

- The radius is constant: $r(t)=R$. Hence $\dot r=0$ and $\ddot r=0$.
- The angular speed is constant: $\dot\theta=\omega$. Hence $\ddot\theta=0$.
- The only acceleration is radial and inward.

Substitute these conditions into the general velocity and acceleration:

$$

\mathbf v=R\omega\mathbf e_\theta,
\qquad
\mathbf a=-R\omega^2\mathbf e_r.

$$

Newton's second law gives

**Force required for uniform circular motion**

$$

\boxed{\mathbf F=m\mathbf a=-mR\omega^2\mathbf e_r.}

$$

The minus sign says that the force points opposite to $\mathbf e_r$, toward the centre. Its magnitude is

$$

F_{\text{in}}=mR\omega^2=\frac{mv^2}{R}.

$$

> Diagram: see the PDF or LaTeX edition.

**Circular motion is a special solution**

A central force does not automatically make every orbit circular. A circular orbit requires the correct initial tangential speed and no initial radial speed. Other initial conditions can produce non-circular bound or unbound orbits.

## Inverse-square attraction and the orbital period

We now apply the circular-motion result to an attractive inverse-square field. It is safest to distinguish an *acceleration law* from a *force law*.

### Form A: inverse-square acceleration

For gravity around a fixed central mass $M$, define

$$

\mu=GM.

$$

The gravitational acceleration is

$$

\mathbf a_{\text{grav}}=-\frac{\mu}{r^2}\mathbf e_r.

$$

For a circular orbit of radius $R$, the required acceleration is $-R\omega^2\mathbf e_r$. Equate their magnitudes:

$$
\begin{aligned}
\frac{\mu}{R^2}&=R\omega^2,\\
\omega^2&=\frac{\mu}{R^3},\\
\omega&=\sqrt{\frac{\mu}{R^3}}.
\end{aligned}
$$

One revolution is $2\pi$ radians, so the period is

$$

P=\frac{2\pi}{\omega}.

$$

Substitution gives

**Period of a circular inverse-square orbit**

$$

\boxed{P=2\pi\sqrt{\frac{R^3}{\mu}}},
\qquad
\boxed{P^2=\frac{4\pi^2}{\mu}R^3}.

$$

Therefore, with the same central body fixed,

$$

\boxed{P\propto R^{3/2}.}

$$

### Dimensional check

The gravitational parameter has dimensions

$$

[\mu]=[GM]=L^3T^{-2}.

$$

Therefore

$$

\left[\frac{R^3}{\mu}\right]
=\frac{L^3}{L^3T^{-2}}=T^2,

$$

and its square root has units of time, as a period must.

### Form B: inverse-square force

Suppose instead that the force itself is written

$$

\mathbf F=-\frac{\kappa}{r^2}\mathbf e_r.

$$

Then $\kappa$ must have dimensions $ML^3T^{-2}$. On a circular orbit,

$$
\begin{aligned}
\frac{\kappa}{R^2}&=mR\omega^2,\\
\omega^2&=\frac{\kappa}{mR^3},\\
P&=2\pi\sqrt{\frac{mR^3}{\kappa}}.
\end{aligned}
$$

For gravity, $\kappa=GMm=\mu m$, so the orbiting mass cancels:

$$

P=2\pi\sqrt{\frac{mR^3}{GMm}}
=2\pi\sqrt{\frac{R^3}{GM}}.

$$

**How this matches shorthand notation**

If a handwritten derivation writes $k/R^2=R\omega^2$, then $k$ is being used as an acceleration parameter with dimensions $L^3T^{-2}$, like $\mu=GM$. If it writes a force $k/R^2$, an additional factor of $m$ belongs in Newton's second law unless $m$ has already been absorbed into $k$.

### What has, and has not, been shown

The calculation above establishes the $R^{3/2}$ scaling for circular orbits in an inverse-square field. Kepler's third law also holds for elliptical two-body orbits when $R$ is replaced by the semi-major axis $a$:

$$

P^2=\frac{4\pi^2}{\mu}a^3

$$

in the fixed-central-mass approximation. For the full two-body problem, $\mu=G(M+m)$. Those broader results require additional orbital mechanics; the circular derivation here captures the scaling in its simplest setting.

## The entire derivation on one page

1. Define the rotating polar basis:

$$

\mathbf e_r=\cos\theta\mathbf i+\sin\theta\mathbf j,
\qquad
\mathbf e_\theta=-\sin\theta\mathbf i+\cos\theta\mathbf j.

$$

1. Resolve a tiny displacement into radial and angular pieces:

$$

\,\mathrm d\mathbf r=\,\mathrm d r\mathbf e_r+r\,\mathrm d\theta\mathbf e_\theta.

$$

1. Divide by time:

$$

\mathbf v=\dot r\mathbf e_r+r\dot\theta\mathbf e_\theta.

$$

1. Account for the rotating basis:

$$

\dot{\mathbf e_r}=\dot\theta\mathbf e_\theta,
\qquad
\dot{\mathbf e_\theta}=-\dot\theta\mathbf e_r.

$$

1. Differentiate the velocity:

$$

\mathbf a=(\ddot r-r\dot\theta^2)\mathbf e_r
+(2\dot r\dot\theta+r\ddot\theta)\mathbf e_\theta.

$$

1. Use orthonormality to find speed and kinetic energy:

$$

v^2=\dot r^2+r^2\dot\theta^2,
\qquad
K=\frac12m(\dot r^2+r^2\dot\theta^2).

$$

1. For uniform circular motion, set $r=R$ and $\dot\theta=\omega$ constant:

$$

\mathbf a=-R\omega^2\mathbf e_r,
\qquad
\mathbf F=-mR\omega^2\mathbf e_r.

$$

1. Match this to inverse-square gravitational acceleration:

$$

\frac{\mu}{R^2}=R\omega^2
\quad\Longrightarrow\quad
P=2\pi\sqrt{\frac{R^3}{\mu}}
\quad\Longrightarrow\quad
P\propto R^{3/2}.

$$

**The conceptual thread**

The polar formulas are not mysterious new laws. They are ordinary vector differentiation expressed in a basis that turns with $\theta$. Once the basis derivatives are included, velocity, acceleration, energy, and circular-orbit dynamics follow in a continuous chain.

{}
$$
2mm]
{\smallEnd of tutorial}
