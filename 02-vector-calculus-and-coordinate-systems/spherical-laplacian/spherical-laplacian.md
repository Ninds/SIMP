# The Laplacian in Spherical Coordinates

> Markdown reading edition. TikZ diagrams and print-layout elements are preserved in the PDF and LaTeX editions.

## What we are trying to derive

Let \(f=f(r,\theta,\phi)\) be a smooth scalar field. It might be temperature, pressure, concentration, or potential. Our target is the spherical-coordinate form of

$$

\nabla^2f=\nabla\cdot(\nabla f).

$$

The final expression contains several factors of \(r\) and \(\sin\theta\). Instead of memorising them, we will account for each one geometrically.

**Physical meaning**

The gradient tells us how \(f\) rises with physical distance. The divergence of that gradient measures the net outward gradient flux per unit volume. Thus the Laplacian compares a value with the values around it.

The derivation has four stages:

1. find the lengths corresponding to \(\,\mathrm d r\), \(\,\mathrm d\theta\), and \(\,\mathrm d\phi\);
1. derive \(\nabla f\) from \(\,\mathrm d f=\nabla f\cdot\,\mathrm d\mathbf{\ell}\);
1. derive \(\nabla\cdot\mathbf{A}\) from flux divided by volume;
1. substitute \(\mathbf{A}=\nabla f\).

### Fix the convention before doing algebra

We use the convention common in physics:

- \(r\geq0\) is distance from the origin;
- \(0\leq\theta\leq\pi\) is measured down from \(+z\);
- \(0\leq\phi<2\pi\) is measured around the \(z\)-axis from \(+x\).

Therefore

$$
\begin{aligned}
x&=r\sin\theta\cos\phi,\\
y&=r\sin\theta\sin\phi,\\
z&=r\cos\theta.
\end{aligned}
$$

At every ordinary point we attach three mutually perpendicular unit vectors:

$$

\mathbf e_r,\qquad\mathbf e_\theta,\qquad\mathbf e_\phi.

$$

They point in the directions of increasing \(r\), increasing \(\theta\), and increasing \(\phi\).

**Notation warning**

Some books exchange the names \(\theta\) and \(\phi\). Always check which angle is measured from the \(z\)-axis. A swapped convention gives a formula that looks different even though the geometry is the same.

## Three coordinate changes, three physical lengths

The symbols \(\,\mathrm d r\), \(\,\mathrm d\theta\), and \(\,\mathrm d\phi\) are coordinate changes. Only \(\,\mathrm d r\) is already a physical length. An angle change must be multiplied by the radius of the circle along which the point moves.

### Radial step: change \(r\), hold both angles fixed

The point moves straight outward. A small increase \(\,\mathrm d r\) gives

$$

\,\mathrm d\mathbf{\ell_r}=\,\mathrm d r\,\mathbf e_r.

$$

Its physical length is simply

$$

\boxed{\,\mathrm d\ell_r=\,\mathrm d r}.

$$

The scale factor is the physical length per unit coordinate change:

$$

h_r=\frac{\,\mathrm d\ell_r}{\,\mathrm d r}=1.

$$

### Polar step: change \(\theta\), hold \(r\) and \(\phi\) fixed

The point moves along a meridian. This is a circle of radius \(r\), centred at the origin.

For an angle measured in radians,

$$

\text{arc length}
=(\text{circle radius})(\text{angle change}).

$$

Therefore

$$

\,\mathrm d\mathbf{\ell}_\theta=r\,\,\mathrm d\theta\,\mathbf e_\theta,
\qquad
\boxed{\,\mathrm d\ell_\theta=r\,\,\mathrm d\theta}.

$$

The scale factor is

$$

h_\theta=\frac{\,\mathrm d\ell_\theta}{\,\mathrm d\theta}=r.

$$

### Azimuthal step: change \(\phi\), hold \(r\) and \(\theta\) fixed

The point moves around the \(z\)-axis on a circle of latitude. We must first find the radius of that circle.

In a meridional right triangle, the hypotenuse is \(r\) and the side perpendicular to the \(z\)-axis is

$$

\rho=r\sin\theta.

$$

Thus the azimuthal circle has radius \(r\sin\theta\), not \(r\). The arc length is

$$

\,\mathrm d\mathbf{\ell}_\phi
=r\sin\theta\,\,\mathrm d\phi\,\mathbf e_\phi,
\qquad
\boxed{\,\mathrm d\ell_\phi=r\sin\theta\,\,\mathrm d\phi}.

$$

The scale factor is

$$

h_\phi=\frac{\,\mathrm d\ell_\phi}{\,\mathrm d\phi}=r\sin\theta.

$$

> Diagram: see the PDF or LaTeX edition.

## Collect the geometry

The three independent steps combine to give the tiny displacement

**Spherical line element**

$$

\boxed{
\,\mathrm d\mathbf{\ell}
=\,\mathrm d r\,\mathbf e_r
+r\,\,\mathrm d\theta\,\mathbf e_\theta
+r\sin\theta\,\,\mathrm d\phi\,\mathbf e_\phi.}

$$

Because the three directions are perpendicular,

$$

\boxed{
\,\mathrm d\ell^2
=\,\mathrm d r^2+r^2\,\mathrm d\theta^2
+r^2\sin^2\theta\,\,\mathrm d\phi^2.}

$$

The scale factors are therefore

$$

\boxed{h_r=1,\qquad h_\theta=r,\qquad h_\phi=r\sin\theta.}

$$

{>{\bfseries}c X c c}
\toprule
Change & Curve followed & Physical length & Scale factor\\
\midrule
$\,\mathrm d r$ & straight radial line & $\,\mathrm d r$ & $h_r=1$\\
$\,\mathrm d\theta$ & meridian circle of radius $r$ & $r\,\,\mathrm d\theta$ & $h_\theta=r$\\
$\,\mathrm d\phi$ & latitude circle of radius $r\sin\theta$ & $r\sin\theta\,\,\mathrm d\phi$ & $h_\phi=r\sin\theta$\\
\bottomrule

**A pole check**

Near either pole, \(\sin\theta\) is small. Turning through a fixed \(\,\mathrm d\phi\) moves the point only a small distance. At a pole, \(\sin\theta=0\), so changing \(\phi\) does not move the point at all. At the equator, \(\sin\theta=1\), so the azimuthal circle has radius \(r\).

### The tiny volume

A sufficiently small spherical coordinate cell looks locally like a rectangular box. Its perpendicular edge lengths are

$$

\,\mathrm d r,\qquad r\,\,\mathrm d\theta,\qquad r\sin\theta\,\,\mathrm d\phi.

$$

Multiply them:

**Tiny spherical volume**

$$

\boxed{
\,\mathrm d V
=(\,\mathrm d r)(r\,\,\mathrm d\theta)(r\sin\theta\,\,\mathrm d\phi)
=r^2\sin\theta\,\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi.}

$$

This volume will be the denominator in the divergence calculation.

## Derive the gradient

Let \(f=f(r,\theta,\phi)\). Its ordinary total differential is

$$

\,\mathrm d f
=\frac{\partial f}{\partial r}\,\mathrm d r
+\frac{\partial f}{\partial\theta}\,\mathrm d\theta
+\frac{\partial f}{\partial\phi}\,\mathrm d\phi.

$$

This describes change per coordinate increment. The gradient must describe change per physical distance.

### Use the defining property

The gradient is defined by

$$

\,\mathrm d f=\nabla f\cdot\,\mathrm d\mathbf{\ell}.

$$

Write its unknown components as

$$

\nabla f=G_r\mathbf e_r+G_\theta\mathbf e_\theta+G_\phi\mathbf e_\phi.

$$

Now insert the line element:

$$
\begin{aligned}
\,\mathrm d f
&=(G_r\mathbf e_r+G_\theta\mathbf e_\theta+G_\phi\mathbf e_\phi)\cdot\\
&\quad(\,\mathrm d r\,\mathbf e_r+r\,\,\mathrm d\theta\,\mathbf e_\theta
+r\sin\theta\,\,\mathrm d\phi\,\mathbf e_\phi).
\end{aligned}
$$

Because the basis is orthonormal, equal directions have dot product \(1\) and different directions have dot product \(0\). Thus

$$

\,\mathrm d f
=G_r\,\mathrm d r+G_\theta r\,\,\mathrm d\theta
+G_\phi r\sin\theta\,\,\mathrm d\phi.

$$

The coordinate changes are independent. Their coefficients must match those in the ordinary total differential.

#### Match the coefficient of \(\,\mathrm d r\)

$$

G_r=\frac{\partial f}{\partial r}.

$$

#### Match the coefficient of \(\,\mathrm d\theta\)

$$

rG_\theta=\frac{\partial f}{\partial\theta}
\quad\Longrightarrow\quad
G_\theta=\frac{1}{r}\frac{\partial f}{\partial\theta}.

$$

#### Match the coefficient of \(\,\mathrm d\phi\)

$$

r\sin\theta\,G_\phi=\frac{\partial f}{\partial\phi}
\quad\Longrightarrow\quad
G_\phi=\frac{1}{r\sin\theta}\frac{\partial f}{\partial\phi}.

$$

Therefore

**Gradient in spherical coordinates**

$$

\boxed{
\nabla f
=\frac{\partial f}{\partial r}\mathbf e_r
+\frac{1}{r}\frac{\partial f}{\partial\theta}\mathbf e_\theta
+\frac{1}{r\sin\theta}\frac{\partial f}{\partial\phi}\mathbf e_\phi.}

$$

**The reciprocal factors are physical**

\(\partial f/\partial\theta\) is change per radian. One radian in the \(\theta\) direction spans physical distance \(r\), so change per unit length is \((1/r)\partial f/\partial\theta\). Similarly, one radian in the \(\phi\) direction spans \(r\sin\theta\).

If \(f\) has units \([f]\), every gradient component has units \([f]/L\).

## Prepare the six flux faces

Let

$$

\mathbf{A}=A_r\mathbf e_r+A_\theta\mathbf e_\theta+A_\phi\mathbf e_\phi

$$

be a vector field. Divergence is net outward flux per unit volume:

$$

\nabla\cdot\mathbf{A}
=\lim_{\Delta V\to0}
\frac{\text{outward flux through the boundary}}{\Delta V}.

$$

We use a tiny cell with coordinate widths \(\,\mathrm d r,\,\mathrm d\theta,\,\mathrm d\phi\).

> Diagram: see the PDF or LaTeX edition.

### Face areas from edge lengths

A face normal to \(\mathbf e_r\) uses the other two edge lengths:

$$

\boxed{\,\mathrm d S_r
=(r\,\,\mathrm d\theta)(r\sin\theta\,\,\mathrm d\phi)
=r^2\sin\theta\,\,\mathrm d\theta\,\,\mathrm d\phi.}

$$

A face normal to \(\mathbf e_\theta\) uses the radial and azimuthal edges:

$$

\boxed{\,\mathrm d S_\theta
=(\,\mathrm d r)(r\sin\theta\,\,\mathrm d\phi)
=r\sin\theta\,\,\mathrm d r\,\,\mathrm d\phi.}

$$

A face normal to \(\mathbf e_\phi\) uses the radial and polar edges:

$$

\boxed{\,\mathrm d S_\phi
=(\,\mathrm d r)(r\,\,\mathrm d\theta)
=r\,\,\mathrm d r\,\,\mathrm d\theta.}

$$

The field component normal to a face is the only component that crosses that face.

## Radial flux pair

The inner radial face is at \(r\). Its outward normal is \(-\mathbf e_r\), so its flux enters with a minus sign:

$$

-A_r(r,\theta,\phi)\,
r^2\sin\theta\,\,\mathrm d\theta\,\,\mathrm d\phi.

$$

The outer radial face is at \(r+\,\mathrm d r\). Its outward normal is \(+\mathbf e_r\). Both the field and the area are evaluated at the larger radius:

$$

A_r(r+\,\mathrm d r,\theta,\phi)\,
(r+\,\mathrm d r)^2\sin\theta\,\,\mathrm d\theta\,\,\mathrm d\phi.

$$

Subtract inner from outer:

$$
\begin{aligned}
\,\mathrm d\Phi_r
={}&\Big[(r+\,\mathrm d r)^2A_r(r+\,\mathrm d r,\theta,\phi)
-r^2A_r(r,\theta,\phi)\Big]\\
&\times\sin\theta\,\,\mathrm d\theta\,\,\mathrm d\phi.
\end{aligned}
$$

The bracket is a small change in the single quantity \(r^2A_r\). By the definition of a derivative,

$$

(r+\,\mathrm d r)^2A_r(r+\,\mathrm d r)-r^2A_r(r)
=\frac{\partial}{\partial r}(r^2A_r)\,\mathrm d r

$$

to first order. Therefore

**Net radial flux**

$$

\boxed{
\,\mathrm d\Phi_r
=\frac{\partial}{\partial r}(r^2A_r)
\sin\theta\,\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi.}

$$

**Why \(r^2\) remains inside the derivative**

The outer radial face is larger than the inner face. Even if \(A_r\) is unchanged, more flux can cross the larger face. Differentiating \(r^2A_r\) includes both the change in field strength and the change in area.

Divide this flux by the tiny volume:

$$
\begin{aligned}
\frac{\,\mathrm d\Phi_r}{\,\mathrm d V}
&=
\frac{
\frac{\partial}{\partial r}(r^2A_r)
\sin\theta\,\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi
}{
r^2\sin\theta\,\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi
}\\
&=\boxed{
\frac{1}{r^2}\frac{\partial}{\partial r}(r^2A_r)}.
\end{aligned}
$$

## Polar-angle flux pair

The lower polar face is at \(\theta\). Its outward normal is \(-\mathbf e_\theta\). Its flux contribution is

$$

-A_\theta(r,\theta,\phi)\,
r\sin\theta\,\,\mathrm d r\,\,\mathrm d\phi.

$$

The upper face is at \(\theta+\,\mathrm d\theta\), with outward normal \(+\mathbf e_\theta\):

$$

A_\theta(r,\theta+\,\mathrm d\theta,\phi)\,
r\sin(\theta+\,\mathrm d\theta)\,\,\mathrm d r\,\,\mathrm d\phi.

$$

Subtract lower from upper:

$$
\begin{aligned}
\,\mathrm d\Phi_\theta
={}&r\Big[
\sin(\theta+\,\mathrm d\theta)A_\theta(r,\theta+\,\mathrm d\theta,\phi)\\
&\qquad-\sin\theta A_\theta(r,\theta,\phi)
\Big]\,\mathrm d r\,\,\mathrm d\phi.
\end{aligned}
$$

The bracket is a small change in \(\sin\theta A_\theta\):

$$

\sin(\theta+\,\mathrm d\theta)A_\theta(\theta+\,\mathrm d\theta)
-\sin\theta A_\theta(\theta)
=
\frac{\partial}{\partial\theta}
(\sin\theta A_\theta)\,\mathrm d\theta.

$$

Thus

**Net polar-angle flux**

$$

\boxed{
\,\mathrm d\Phi_\theta
=r\frac{\partial}{\partial\theta}
(\sin\theta A_\theta)
\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi.}

$$

Divide by the tiny volume:

$$
\begin{aligned}
\frac{\,\mathrm d\Phi_\theta}{\,\mathrm d V}
&=
\frac{
r\frac{\partial}{\partial\theta}(\sin\theta A_\theta)
\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi
}{
r^2\sin\theta\,\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi
}\\
&=\boxed{
\frac{1}{r\sin\theta}
\frac{\partial}{\partial\theta}(\sin\theta A_\theta)}.
\end{aligned}
$$

**The geometric change here**

Latitude circles change size as \(\theta\) changes. That is why \(\sin\theta\) must be included inside the derivative, just as \(r^2\) was included for the radial faces.

## Azimuthal flux pair

The lower azimuthal face is at \(\phi\), with outward normal \(-\mathbf e_\phi\):

$$

-A_\phi(r,\theta,\phi)\,
r\,\,\mathrm d r\,\,\mathrm d\theta.

$$

The upper face is at \(\phi+\,\mathrm d\phi\), with outward normal \(+\mathbf e_\phi\):

$$

A_\phi(r,\theta,\phi+\,\mathrm d\phi)\,
r\,\,\mathrm d r\,\,\mathrm d\theta.

$$

At fixed \(r\) and \(\theta\), the face area \(r\,\,\mathrm d r\,\,\mathrm d\theta\) does not depend on \(\phi\). The difference is

$$
\begin{aligned}
\,\mathrm d\Phi_\phi
&=r\Big[
A_\phi(r,\theta,\phi+\,\mathrm d\phi)
-A_\phi(r,\theta,\phi)
\Big]\,\mathrm d r\,\,\mathrm d\theta\\
&=r\frac{\partial A_\phi}{\partial\phi}
\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi.
\end{aligned}
$$

Therefore

**Net azimuthal flux**

$$

\boxed{
\,\mathrm d\Phi_\phi
=r\frac{\partial A_\phi}{\partial\phi}
\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi.}

$$

Divide by the tiny volume:

$$
\begin{aligned}
\frac{\,\mathrm d\Phi_\phi}{\,\mathrm d V}
&=
\frac{
r\frac{\partial A_\phi}{\partial\phi}
\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi
}{
r^2\sin\theta\,\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi
}\\
&=\boxed{
\frac{1}{r\sin\theta}
\frac{\partial A_\phi}{\partial\phi}}.
\end{aligned}
$$

### Add the three flux densities

Adding the radial, polar, and azimuthal contributions gives

**Divergence in spherical coordinates**

$$

\boxed{
\nabla\cdot\mathbf{A}
=\frac{1}{r^2}\frac{\partial}{\partial r}(r^2A_r)
+\frac{1}{r\sin\theta}\frac{\partial}{\partial\theta}
(\sin\theta A_\theta)
+\frac{1}{r\sin\theta}\frac{\partial A_\phi}{\partial\phi}.}

$$

This formula was obtained only from physical face areas, signs of outward normals, and flux per volume.

## Substitute the gradient into the divergence

The Laplacian is

$$

\nabla^2f=\nabla\cdot(\nabla f).

$$

Give the three gradient components short names:

$$
\begin{aligned}
A_r&=\frac{\partial f}{\partial r},\\
A_\theta&=\frac{1}{r}\frac{\partial f}{\partial\theta},\\
A_\phi&=\frac{1}{r\sin\theta}\frac{\partial f}{\partial\phi}.
\end{aligned}
$$

We now substitute one component at a time.

### Radial contribution

Start from the radial divergence term:

$$

\frac{1}{r^2}\frac{\partial}{\partial r}(r^2A_r).

$$

Insert \(A_r=\partial f/\partial r\):

$$

\boxed{
\frac{1}{r^2}\frac{\partial}{\partial r}
\left(r^2\frac{\partial f}{\partial r}\right)}.

$$

### Polar-angle contribution

Start from

$$

\frac{1}{r\sin\theta}
\frac{\partial}{\partial\theta}(\sin\theta A_\theta).

$$

Insert \(A_\theta=(1/r)\partial f/\partial\theta\):

$$

\frac{1}{r\sin\theta}
\frac{\partial}{\partial\theta}
\left(\sin\theta\frac{1}{r}
\frac{\partial f}{\partial\theta}\right).

$$

While differentiating with respect to \(\theta\), \(r\) is fixed. Move \(1/r\) outside:

$$

\boxed{
\frac{1}{r^2\sin\theta}
\frac{\partial}{\partial\theta}
\left(\sin\theta\frac{\partial f}{\partial\theta}\right)}.

$$

### Azimuthal contribution

Start from

$$

\frac{1}{r\sin\theta}\frac{\partial A_\phi}{\partial\phi}.

$$

Insert \(A_\phi=(1/(r\sin\theta))\partial f/\partial\phi\):

$$

\frac{1}{r\sin\theta}
\frac{\partial}{\partial\phi}
\left(\frac{1}{r\sin\theta}
\frac{\partial f}{\partial\phi}\right).

$$

While differentiating with respect to \(\phi\), both \(r\) and \(\theta\) are fixed. Move the second factor outside:

$$

\boxed{
\frac{1}{r^2\sin^2\theta}
\frac{\partial^2 f}{\partial\phi^2}}.

$$

## The spherical Laplacian

Add the three contributions:

**Conservative form**

$$

\boxed{
\nabla^2 f
=\frac{1}{r^2}\frac{\partial}{\partial r}
\left(r^2\frac{\partial f}{\partial r}\right)
+\frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}
\left(\sin\theta\frac{\partial f}{\partial\theta}\right)
+\frac{1}{r^2\sin^2\theta}
\frac{\partial^2 f}{\partial\phi^2}.}

$$

This is usually the safest form to use. The area factors remain visible inside the derivatives, so the geometry is harder to lose.

### Expand the radial term

Use the product rule:

$$
\begin{aligned}
\frac{1}{r^2}\frac{\partial}{\partial r}
\left(r^2\frac{\partial f}{\partial r}\right)
&=
\frac{1}{r^2}
\left(
2r\frac{\partial f}{\partial r}
+r^2\frac{\partial^2 f}{\partial r^2}
\right)\\
&=
\frac{2}{r}\frac{\partial f}{\partial r}
+\frac{\partial^2 f}{\partial r^2}.
\end{aligned}
$$

### Expand the polar-angle term

Again use the product rule:

$$
\begin{aligned}
&\frac{1}{r^2\sin\theta}
\frac{\partial}{\partial\theta}
\left(\sin\theta\frac{\partial f}{\partial\theta}\right)\\
&\quad=
\frac{1}{r^2\sin\theta}
\left(
\cos\theta\frac{\partial f}{\partial\theta}
+\sin\theta\frac{\partial^2f}{\partial\theta^2}
\right)\\
&\quad=
\frac{\cot\theta}{r^2}\frac{\partial f}{\partial\theta}
+\frac{1}{r^2}\frac{\partial^2f}{\partial\theta^2}.
\end{aligned}
$$

The azimuthal term is already expanded. Therefore

**Expanded form**

$$

\boxed{
\nabla^2f
=\frac{\partial^2f}{\partial r^2}
+\frac{2}{r}\frac{\partial f}{\partial r}
+\frac{1}{r^2}\frac{\partial^2f}{\partial\theta^2}
+\frac{\cot\theta}{r^2}\frac{\partial f}{\partial\theta}
+\frac{1}{r^2\sin^2\theta}
\frac{\partial^2f}{\partial\phi^2}.}

$$

**Why first-derivative terms appear**

Cartesian coordinate boxes keep the same size everywhere. Spherical coordinate cells spread out as \(r\) grows, and latitude circles change size with \(\theta\). The terms \((2/r)f_r\) and \((\cot\theta/r^2)f_\theta\) record this changing geometry.

## Dimensional and structural checks

Angles in radians are dimensionless. If \(f\) has units \([f]\), every Laplacian term must have units \([f]/L^2\).

For example,

$$

\left[\frac{\partial^2f}{\partial r^2}\right]
=\frac{[f]}{L^2},

$$

and

$$

\left[
\frac{1}{r^2}
\frac{\partial^2f}{\partial\theta^2}
\right]
=\frac{[f]}{L^2}.

$$

The same is true for the \(\phi\) term because \(r^2\) supplies the two powers of length and \(\sin\theta\) is dimensionless.

### Check with \(f=r^2\)

Since \(r^2=x^2+y^2+z^2\), Cartesian coordinates give

$$

\nabla^2r^2=2+2+2=6.

$$

The spherical result agrees:

$$
\begin{aligned}
\nabla^2r^2
&=\frac{1}{r^2}\frac{\,\mathrm d}{\,\mathrm d r}
\left(r^2\frac{\,\mathrm d}{\,\mathrm d r}r^2\right)\\
&=\frac{1}{r^2}\frac{\,\mathrm d}{\,\mathrm d r}(2r^3)\\
&=\frac{6r^2}{r^2}=6.
\end{aligned}
$$

### Spherically symmetric fields

If \(f=f(r)\), all angular derivatives vanish:

**Radial-only formula**

$$

\boxed{
\nabla^2f(r)
=\frac{1}{r^2}\frac{\,\mathrm d}{\,\mathrm d r}
\left(r^2\frac{\,\mathrm d f}{\,\mathrm d r}\right)
=f''(r)+\frac{2}{r}f'(r).}

$$

### Check with \(f=1/r\), away from the origin

For \(r>0\),

$$
\begin{aligned}
\nabla^2\left(\frac1r\right)
&=
\frac{1}{r^2}\frac{\,\mathrm d}{\,\mathrm d r}
\left[r^2\frac{\,\mathrm d}{\,\mathrm d r}\left(\frac1r\right)\right]\\
&=
\frac{1}{r^2}\frac{\,\mathrm d}{\,\mathrm d r}
\left[r^2\left(-\frac1{r^2}\right)\right]\\
&=\frac{1}{r^2}\frac{\,\mathrm d}{\,\mathrm d r}(-1)=0.
\end{aligned}
$$

**Do not include the origin in that calculation**

The function \(1/r\) is singular at \(r=0\). Distributionally,

$$

\nabla^2\left(\frac1r\right)
=-4\pi\delta^{(3)}(\mathbf{r}).

$$

It is harmonic away from the origin but represents a point source at the origin.

## Symmetry reductions and coordinate singularities

### Axisymmetry

If \(f\) is independent of \(\phi\), then \(\partial f/\partial\phi=0\). The last term disappears:

$$

\boxed{
\nabla^2f
=
\frac{1}{r^2}\frac{\partial}{\partial r}
\left(r^2\frac{\partial f}{\partial r}\right)
+
\frac{1}{r^2\sin\theta}
\frac{\partial}{\partial\theta}
\left(\sin\theta\frac{\partial f}{\partial\theta}\right).}

$$

If the field is also independent of \(\theta\), only the radial term remains.

### Why the formula looks singular at poles

The factors \(1/r\) and \(1/\sin\theta\) signal places where the coordinates degenerate:

- at \(r=0\), every pair of angles labels the same point;
- at \(\theta=0\) or \(\pi\), every value of \(\phi\) labels the same point.

A smooth physical field need not be singular there. Its angular dependence must combine so that the full scalar result remains finite. A coordinate singularity is not automatically a physical singularity.

**Trace every factor back to geometry**

$$

r^2
\quad\hbox{comes from the area of a spherical shell,}

$$

$$

\sin\theta
\quad\hbox{comes from the radius of a latitude circle,}

$$

and

$$

r^2\sin\theta
\quad\hbox{comes from the tiny spherical volume.}

$$

These are the only geometric ingredients needed.

## The entire derivation on one page

1. The three tiny physical lengths are

$$

\,\mathrm d\ell_r=\,\mathrm d r,\qquad
\,\mathrm d\ell_\theta=r\,\,\mathrm d\theta,\qquad
\,\mathrm d\ell_\phi=r\sin\theta\,\,\mathrm d\phi.

$$

1. Hence

$$

\,\mathrm d\mathbf{\ell}
=\,\mathrm d r\,\mathbf e_r+r\,\,\mathrm d\theta\,\mathbf e_\theta
+r\sin\theta\,\,\mathrm d\phi\,\mathbf e_\phi.

$$

1. Match \(\,\mathrm d f=\nabla f\cdot\,\mathrm d\mathbf{\ell}\):

$$

\nabla f
=f_r\mathbf e_r+\frac1r f_\theta\mathbf e_\theta
+\frac{1}{r\sin\theta}f_\phi\mathbf e_\phi.

$$

1. The tiny volume is

$$

\,\mathrm d V=r^2\sin\theta\,
\,\mathrm d r\,\,\mathrm d\theta\,\,\mathrm d\phi.

$$

1. Flux through each opposite face pair gives

$$

\nabla\cdot\mathbf{A}
=\frac1{r^2}\partial_r(r^2A_r)
+\frac1{r\sin\theta}\partial_\theta(\sin\theta A_\theta)
+\frac1{r\sin\theta}\partial_\phi A_\phi.

$$

1. Set \(\mathbf{A}=\nabla f\):

$$

\boxed{
\nabla^2 f
=\frac{1}{r^2}\partial_r(r^2f_r)
+\frac{1}{r^2\sin\theta}\partial_\theta(\sin\theta f_\theta)
+\frac{1}{r^2\sin^2\theta}f_{\phi\phi}.}

$$

**The conceptual chain**

Tiny arcs determine scale factors. Scale factors determine physical derivatives, areas, and volume. Physical derivatives give the gradient. Face fluxes give the divergence. Taking the divergence of the gradient gives the spherical Laplacian. Every factor of \(r\) and \(\sin\theta\) has a geometric origin.

{}
$$
2mm]
{\smallEnd of tutorial}
