# Integral Theorems

> Markdown reading edition. TikZ diagrams and print-layout elements are preserved in the PDF and LaTeX editions.

*Why boundaries know about interiors*

Dot products, circulation, flux, divergence, and curl

## One pattern behind several theorems

The fundamental theorem of calculus says

$$

\int_a^b f'(x)\,\,\mathrm d x=f(b)-f(a).

$$

An accumulated derivative in the interior equals a net change on the boundary. Green's theorem, the divergence theorem, and Stokes' theorem repeat this pattern in higher dimensions.

**The shared architecture**

$$

\boxed{\int_{\text{interior}}(\text{derivative})
=\int_{\text{boundary}}(\text{original quantity}).}

$$

The derivative and the kind of boundary integral change with dimension, but the logic remains the same.

## The dot product selects a component

If $\mathbf{a}$ and $\mathbf{b}$ make an angle $\theta$, then

$$

\mathbf{a}\cdot\mathbf{b}=|\mathbf{a}|\,|\mathbf{b}|\cos\theta.

$$

When $\mathbf{u}$ is a unit vector,

$$

\mathbf{F}\cdot\mathbf{u}

$$

is the signed component of $\mathbf{F}$ along $\mathbf{u}$.

This single idea explains the two most common vector integrals:

- $\mathbf{F}\cdot\mathbf{t}$ measures the component tangent to a curve;
- $\mathbf{F}\cdot\mathbf{n}$ measures the component normal to a surface.

> Diagram: see the PDF or LaTeX edition.

## Line integrals: adding along a curve

Let a curve be parametrised by $\mathbf{r}(s)$. The vector line element is

$$

\,\mathrm d\mathbf{r}=\td{\mathbf{r}}{s}\,\mathrm d s.

$$

For a vector field $\mathbf{F}$,

$$

\int_C\mathbf{F}\cdot\,\mathrm d\mathbf{r}
=\int_{s_0}^{s_1}\mathbf{F}(\mathbf{r}(s))\cdot\td{\mathbf{r}}{s}\,\,\mathrm d s.

$$

The dot product keeps only the tangential component. Physically this may represent work; geometrically it measures circulation along the curve.

Reversing the orientation changes the sign:

$$

\int_{-C}\mathbf{F}\cdot\,\mathrm d\mathbf{r}=-\int_C\mathbf{F}\cdot\,\mathrm d\mathbf{r}.

$$

## Surface integrals: adding through a surface

For an oriented surface with unit normal $\mathbf{n}$,

$$

\boxed{\iint_S\mathbf{F}\cdot\mathbf{n}\,\,\mathrm d S}

$$

measures flux through $S$. Positive contributions point with the chosen normal; negative contributions point against it.

If $S$ is parametrised by $\mathbf{r}(u,v)$, then

$$

\mathbf{n}\,\,\mathrm d S
=\left(\pd{\mathbf{r}}{u}\times\pd{\mathbf{r}}{v}\right)\,\mathrm d u\,\,\mathrm d v.

$$

The order of the parameters fixes the orientation. Swapping $u$ and $v$ reverses the normal and the flux sign.

## The gradient theorem

For a scalar field $\phi$ and a curve from $A$ to $B$,

$$

\boxed{\int_C\boldsymbol\nabla\phi\cdot\,\mathrm d\mathbf{r}=\phi(B)-\phi(A).}

$$

To see why, parametrise the curve by $\mathbf{r}(s)$. The chain rule gives

$$

\frac{\mathrm d }{\mathrm d s}\phi(\mathbf{r}(s))
=\boldsymbol\nabla\phi\cdot\td{\mathbf{r}}{s}.

$$

Integrating with respect to $s$ gives the theorem directly.

Consequences:

- The integral depends only on the endpoints, not the path.
- Around a closed curve, $\oint_C\boldsymbol\nabla\phi\cdot\,\mathrm d\mathbf{r}=0$.
- A field of the form $\mathbf{F}=\boldsymbol\nabla\phi$ is conservative on a suitable domain.

**Domain matters**

A curl-free field need not possess a single-valued potential on a domain with a hole. Local derivative tests and global topology are separate pieces of information.

## Green's theorem in the plane

Let $C$ be the positively oriented boundary of a planar region $D$, and let

$$

\mathbf{F}=(P,Q).

$$

The circulation form is

$$

\boxed{
\oint_C P\,\,\mathrm d x+Q\,\,\mathrm d y
=\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\,\mathrm d A.}

$$

The quantity

$$

\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}

$$

measures local planar rotation. Green's theorem says that total microscopic rotation inside equals macroscopic circulation around the edge.

The flux form is

$$

\boxed{
\oint_C\mathbf{F}\cdot\mathbf{n}\,\,\mathrm d s
=\iint_D\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}\right)\,\mathrm d A.}

$$

Here the interior derivative is the two-dimensional divergence.

**Why internal edges cancel**

Split $D$ into tiny cells. Each internal edge belongs to two cells with opposite orientations, so its two boundary integrals cancel. Only the outer boundary survives. The small-cell circulation is approximated by curl times area; summing produces Green's theorem.

## Divergence: local source strength

For

$$

\mathbf{F}=(F_x,F_y,F_z),

$$

the divergence is

$$

\boxed{\boldsymbol\nabla\cdot\mathbf{F}
=\frac{\partial F_x}{\partial x}+\frac{\partial F_y}{\partial y}+\frac{\partial F_z}{\partial z}.}

$$

It measures the net outward flux per unit volume in the limit of a small volume:

$$

\boldsymbol\nabla\cdot\mathbf{F}
=\lim_{V\to0}\frac{1}{\operatorname{vol}(V)}
\iint_{\partial V}\mathbf{F}\cdot\mathbf{n}\,\,\mathrm d S.

$$

Positive divergence indicates local source-like behaviour; negative divergence indicates sink-like behaviour.

## The divergence theorem

For a volume $V$ with outward-oriented boundary $\partial V$,

$$

\boxed{
\iiint_V\boldsymbol\nabla\cdot\mathbf{F}\,\,\mathrm d V
=\iint_{\partial V}\mathbf{F}\cdot\mathbf{n}\,\,\mathrm d S.}

$$

The left side adds local source strength throughout the volume. The right side measures the total amount leaving through the boundary.

### Example: a radial linear field

Let

$$

\mathbf{F}=(x,y,z).

$$

Then

$$

\boldsymbol\nabla\cdot\mathbf{F}=3.

$$

For a ball of radius $R$,

$$

\iiint_V3\,\,\mathrm d V=3\left(\frac43\pi R^3\right)=4\pi R^3.

$$

On the sphere, $\mathbf{F}=R\mathbf{n}$, so

$$

\iint_{\partial V}\mathbf{F}\cdot\mathbf{n}\,\,\mathrm d S
=R(4\pi R^2)=4\pi R^3.

$$

The two descriptions agree.

## Curl: local circulation density

The curl is

$$

\boxed{
\boldsymbol\nabla\times\mathbf{F}
=\begin{vmatrix}
\mathbf{e_x}&\mathbf{e_y}&\mathbf{e_z}\\
\partial_x&\partial_y&\partial_z\\
F_x&F_y&F_z
\end{vmatrix}.}

$$

Its component along a unit normal $\mathbf{n}$ is the limiting circulation per unit area in the plane perpendicular to $\mathbf{n}$:

$$

(\boldsymbol\nabla\times\mathbf{F})\cdot\mathbf{n}
=\lim_{A\to0}\frac{1}{A}\oint_{\partial A}\mathbf{F}\cdot\,\mathrm d\mathbf{r}.

$$

The right-hand rule links the positive orientation of the boundary to the chosen normal.

## Stokes' theorem

For an oriented surface $S$ with boundary $\partial S$,

$$

\boxed{
\iint_S(\boldsymbol\nabla\times\mathbf{F})\cdot\mathbf{n}\,\,\mathrm d S
=\oint_{\partial S}\mathbf{F}\cdot\,\mathrm d\mathbf{r}.}

$$

The left side adds local circulation density across the surface. The right side measures circulation around the rim.

> Diagram: see the PDF or LaTeX edition.

Stokes' theorem is independent of which spanning surface is chosen, provided the field is smooth on the region between the surfaces and the orientations agree.

## Differential identities from boundary cancellation

Because the boundary of a boundary is empty, applying these theorems twice suggests two identities:

$$

\boxed{\boldsymbol\nabla\times(\boldsymbol\nabla\phi)=\vect0,}
\qquad
\boxed{\boldsymbol\nabla\cdot(\boldsymbol\nabla\times\mathbf{F})=0.}

$$

For example, Stokes' theorem applied to $\boldsymbol\nabla\phi$ gives zero circulation around every sufficiently small closed curve, forcing its curl to vanish.

## Choosing the correct theorem

p{.29\textwidth}p{.36\textwidth}}
**Boundary integral** & **Interior derivative** & **Theorem**
$$
1mm]
$\phi(B)-\phi(A)$ & $\boldsymbol\nabla\phi$ along a curve & Gradient theorem\\
circulation around a plane curve & scalar planar curl & Green, circulation form\\
flux across a closed curve & planar divergence & Green, flux form\\
flux across a closed surface & divergence in a volume & Divergence theorem\\
circulation around a space curve & normal curl across a surface & Stokes\\

## Orientation checklist

1. For a closed volume, use the outward normal.
1. For a surface with boundary, choose the normal first.
1. Curl the fingers of the right hand in the positive boundary direction; the thumb gives the compatible normal.
1. Reversing either the normal or the boundary orientation changes the sign.
1. State the orientation in the solution instead of leaving it implicit.

## Common mistakes

- Using $\mathbf{F}\cdot\mathbf{n}$ when the theorem requires the tangential component $\mathbf{F}\cdot\,\mathrm d\mathbf{r}$.
- Applying the divergence theorem to an open surface without adding the missing cap.
- Forgetting that Stokes requires a boundary orientation compatible with the normal.
- Assuming curl-free automatically means globally conservative without checking the domain.
- Expanding a difficult surface integral when the corresponding volume integral is easy, or vice versa.

**The unifying mental picture**

Tile the interior into tiny pieces. Boundary contributions on internal interfaces cancel in pairs. What remains is the outer boundary, while the sum of local derivative information becomes the interior integral.
