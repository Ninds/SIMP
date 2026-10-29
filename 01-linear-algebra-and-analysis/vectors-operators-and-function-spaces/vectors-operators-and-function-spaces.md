# Vectors, Operators, and Function Spaces

> Markdown reading edition. TikZ diagrams and print-layout elements are preserved in the PDF and LaTeX editions.

## How to use these notes

Part 0 recalls geometric vectors in $\mathbb R^3$.  It also establishes the norm,
Cauchy--Schwarz and projection results used later.

The main ideas are then developed in three parallel settings:

$$

\boxed{\mathbb R^N\;\longrightarrow\;\ell^2\;\longrightarrow\;L^2}.

$$

Part I uses finitely many components $v_i$.  Part II uses $a_n$, indexed by
$n\in\mathbb N$.  Part III begins with $f_x$, indexed by $x\in\mathbb R$, before returning
to $f(x)$.

Matching section numbers treat matching ideas.  For example, Sections 1.10,
2.10 and 3.10 treat projections; Sections 1.11, 2.11 and 3.11 compare
$p$-norms.  The final table collects the full dictionary.

Infinite-dimensional results are preparatory.  Convergence, domains and
spectral subtleties are stated without measure-theoretic detail.

Part IV applies the same coordinate picture to Fourier series, Fourier
transforms, the heat equation and the infinite square well.

# Part 0: Geometric Vectors in $\mathbb R^3$

## Geometric Vectors in $\mathbb R^3$

**Part 0.**  A geometric warm-up using the familiar unit vectors
$\mathbf i$, $\mathbf j$ and $\mathbf k$.

## Coordinates and unit vectors

**Definition: Coordinate vector**

Every vector in $\mathbb R^3$ has the form

$$

\boxed{\mathbf v=v_1\mathbf i+v_2\mathbf j+v_3\mathbf k}.

$$

Its coordinate triple is $(v_1,v_2,v_3)$.

The unit vectors are

$$

\mathbf i=(1,0,0),\qquad
\mathbf j=(0,1,0),\qquad
\mathbf k=(0,0,1).

$$

**Worked Example: Displacement**

The displacement

$$

\mathbf d=3\mathbf i-2\mathbf j+\mathbf k

$$

has coordinate triple $(3,-2,1)$.

## Length and norms

**Definition: Euclidean norm**

The length of $\mathbf v=(v_1,v_2,v_3)$ is

$$

\boxed{\left\lVert \mathbf v\right\rVert_2=\sqrt{v_1^2+v_2^2+v_3^2}}.

$$

**Definition: Norm**

A norm assigns a length $\norm v$ to every vector $v$.

For all vectors $u,v$ and scalars $\alpha$:
[label=(\roman*),leftmargin=2.7em]
1. $\norm v\ge0$, with equality only for $v=0$;
1. $\left\lVert \alpha v\right\rVert=|\alpha|\norm v$;
1. $\left\lVert u+v\right\rVert\le\norm u+\norm v$.

**Worked Example: Length and normalisation**

Let $\mathbf v=2\mathbf i-\mathbf j+2\mathbf k$.  Then

$$

\left\lVert \mathbf v\right\rVert_2=3,
\qquad
\widehat{\mathbf v}=\frac13(2,-1,2).

$$

The vector $\widehat{\mathbf v}$ has length one.

## Dot product and Cauchy--Schwarz

**Definition: Dot product**

For $\mathbf u,\mathbf v\in\mathbb R^3$,

$$

\boxed{\mathbf u\cdot\mathbf v
=u_1v_1+u_2v_2+u_3v_3}.

$$

Moreover,

$$

\left\lVert \mathbf v\right\rVert_2^2
=\mathbf v\cdot\mathbf v.

$$

**Theorem: Cauchy--Schwarz inequality**

For all $\mathbf u,\mathbf v\in\mathbb R^3$,

$$

\boxed{|\mathbf u\cdot\mathbf v|
\le \left\lVert \mathbf u\right\rVert_2\left\lVert \mathbf v\right\rVert_2}.

$$

**Proof**

The result is immediate if $\mathbf v=0$.

For $\mathbf v\ne0$, a squared length cannot be negative:

$$

0\le
\norm{\mathbf u-
\frac{\mathbf u\cdot\mathbf v}
{\left\lVert \mathbf v\right\rVert_2^2}\mathbf v}_2^2.

$$

Expanding gives

$$

0\le \left\lVert \mathbf u\right\rVert_2^2
-\frac{(\mathbf u\cdot\mathbf v)^2}
{\left\lVert \mathbf v\right\rVert_2^2}.

$$

Rearranging proves the inequality.

**Corollary: Triangle inequality**

For $\mathbf u,\mathbf v\in\mathbb R^3$,

$$

\left\lVert \mathbf u+\mathbf v\right\rVert_2
\le \left\lVert \mathbf u\right\rVert_2+\left\lVert \mathbf v\right\rVert_2.

$$

**Proof**

By Cauchy--Schwarz,

$$

\left\lVert \mathbf u+\mathbf v\right\rVert_2^2
\le \bigl(\left\lVert \mathbf u\right\rVert_2+\left\lVert \mathbf v\right\rVert_2\bigr)^2.

$$

Take the non-negative square root.

## Shadows and projections

**Definition: Projection onto a direction**

Let $\mathbf e$ be a unit vector.

The scalar shadow of $\mathbf v$ on $\mathbf e$ is

$$

\mathbf e\cdot\mathbf v.

$$

The vector shadow, or projection, is

$$

\boxed{P_{\mathbf e}\mathbf v
=(\mathbf e\cdot\mathbf v)\mathbf e}.

$$

**Worked Example: A shadow on a line**

Let

$$

\mathbf e=\frac1{\sqrt2}(\mathbf i+\mathbf j),
\qquad
\mathbf v=3\mathbf i+\mathbf j+2\mathbf k.

$$

Then

$$

\mathbf e\cdot\mathbf v=2\sqrt2,
\qquad
P_{\mathbf e}\mathbf v=2\mathbf i+2\mathbf j.

$$

The remainder $\mathbf v-P_{\mathbf e}\mathbf v$ is perpendicular to
$\mathbf e$.

The familiar formula

$$

(\mathbf e\cdot\mathbf v)\mathbf e

$$

becomes $\ip e v e$ in an abstract inner-product space.  It is the same
``shadow'' in every part of these notes.

# Finite-Dimensional Vectors over the Real Field

## Finite-Dimensional Vectors: $\mathbb R^N$

**Part I.**  The finite-dimensional model: finite sums, matrices and no
convergence questions.

## Vectors and vector spaces

**Definition: Real vector space**

A real vector space is a set $V$ with addition and scalar multiplication by
$\mathbb R$, satisfying the vector-space axioms.

The model example is

$$

\mathbb R^N=\{(v_1,\ldots,v_N):v_i\in\mathbb R\}.

$$

Here $v_i$ is the $i$th component.  Vectors may represent arrows,
coefficients, data or discretised fields.

**Worked Example: A force and a coefficient vector**

$F=(3,-4,0)\in\mathbb R^3$ may be a force.  The vector
$c=(1,-2,5,7)\in\mathbb R^4$ may store the coefficients of a cubic polynomial.

The index set is presently finite:

$$

v=(v_1,\ldots,v_N),\qquad i\in\{1,\ldots,N\}.

$$

Parts II and III change only the index set.

## Linear combinations, span and linear independence

**Definition**

A *linear combination* of $v_1,\ldots,v_k\in V$ has the form
$\sum_{j=1}^k\alpha_jv_j$.  Their span is the set of these combinations.  They
are linearly independent if

$$

\alpha_1v_1+\cdots+\alpha_kv_k=0
\quad\Longrightarrow\quad
\alpha_1=\cdots=\alpha_k=0.

$$

Span records what the vectors generate; independence removes redundancy.

**Worked Example: Testing span and independence**

Let $u=(1,1,0)$ and $v=(1,-1,0)$.  If $\alpha u+\beta v=0$, then
$(\alpha+\beta,\alpha-\beta,0)=0$, so $\alpha=\beta=0$.  Thus $u,v$ are
independent.  Their span is the plane $\{(x,y,0):x,y\in\mathbb R\}$, since

$$

(x,y,0)=\frac{x+y}{2}u+\frac{x-y}{2}v.

$$

## Bases and coordinates

**Definition**

A basis of $V$ is a linearly independent set that spans $V$.  The standard
basis of $\mathbb R^N$ is $e_1,\ldots,e_N$, where $(e_i)_j=\delta_{ij}$ and

$$

\delta_{ij}=\begin{cases}1,&i=j,\\0,&i\ne j.\end{cases}

$$

A basis supplies coordinates.  The vector is fixed; its coordinates depend on
the chosen basis.

**Worked Example: The same vector in two bases**

In $\mathbb R^2$ let $b_1=(1,1)$ and $b_2=(1,-1)$.  Since

$$

(3,1)=2b_1+b_2,

$$

the standard coordinates of the vector are $(3,1)$, whereas its coordinates
in the ordered basis $(b_1,b_2)$ are $(2,1)$.

## Decomposition in a basis

**Proposition: Unique decomposition**

If $(b_1,\ldots,b_N)$ is a basis of $V$, then every $v\in V$ has a unique
representation

$$

\boxed{v=\sum_{i=1}^{N}v_i b_i}.

$$

**Proof**

Existence follows because the basis spans $V$.

For uniqueness, suppose

$$

v=\sum_{i=1}^{N}v_i b_i
\qquad\text{and}\qquad
v=\sum_{i=1}^{N}w_i b_i.

$$

Subtracting gives

$$

\sum_{i=1}^{N}(v_i-w_i)b_i=0.

$$

Linear independence gives

$$

v_i=w_i\qquad(i=1,\ldots,N).

$$

**Worked Example: A polynomial as a coordinate vector**

In the vector space of polynomials of degree at most two, take the basis
$(1,x,x^2)$.  Then

$$

p(x)=2-3x+5x^2

$$

has coordinate vector $(2,-3,5)$.  With the alternative basis
$(1,x,1+x^2)$ it becomes $p(x)=-3+(-3)x+5(1+x^2)$, so its coordinate vector
is $(-3,-3,5)$.

## Linear operators

**Definition**

A map $A:V\to W$ is linear if

$$

A(\alpha u+\beta v)=\alpha Au+\beta Av

$$

for all $u,v\in V$ and $\alpha,\beta\in\mathbb R$.

Linearity is the superposition principle.

**Worked Example: Rotation through a right angle**

The operator $R:\mathbb R^2\to\mathbb R^2$ defined by $R(x,y)=(-y,x)$ is linear.  It is
represented in the standard basis by

$$

R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.

$$

By contrast, $T(x,y)=(x+1,y)$ is not linear because $T(0,0)\ne(0,0)$.

## Matrix elements and operator action

Let

$$

A:V\longrightarrow W

$$

be a linear operator.  It takes an input vector $v\in V$ to an output vector
$Av\in W$.

Choose a basis $(b_j)$ for the input space $V$ and a basis $(c_i)$ for the
output space $W$.

The numbers $A_{ij}$ are defined by

$$

\boxed{Ab_j=\sum_i A_{ij}c_i}.

$$

Thus the $j$th column records the coordinates of $Ab_j$.

Now let

$$

v=\sum_jv_jb_j.

$$

Linearity gives

$$

Av=A\left(\sum_jv_jb_j\right)
=\sum_jv_jAb_j.

$$

Substitute the basis expansion of $Ab_j$:

$$

Av=\sum_i\left(\sum_j A_{ij}v_j\right)c_i.

$$

Therefore the $i$th output component is

$$

\boxed{(Av)_i=\sum_{j=1}^{N}A_{ij}v_j}.

$$

The row label $i$ selects an output component.  The column label $j$ runs over
the input components.

**Worked Example: Reading rows as output components**

For

$$

A=\begin{pmatrix}2&-1\\3&4\end{pmatrix},
\qquad v=\begin{pmatrix}5\\2\end{pmatrix},

$$

one obtains $(Av)_1=2(5)-1(2)=8$ and
$(Av)_2=3(5)+4(2)=23$.  Thus $Av=(8,23)^T$.

Keep the component formula visible.  It will become

$$

\begin{gathered}
(Av)_i=\sum_jA_{ij}v_j
\quad\longrightarrow\quad
(Aa)_n=\sum_mA_{nm}a_m,
$$
2mm]
(Af)_x=\sum_y(A_{xy}f_y)
\quad\rightsquigarrow\quad \int A(x,y)f(y)\,\mathrm d y.
\end{gathered}

$$

## Inner products

**Definition**

An inner product is a bilinear, symmetric, positive-definite map
$V\times V\to\mathbb R$.  On $\mathbb R^N$ the standard choice is

$$

\boxed{\left\langle u,v\right\rangle=\sum_{i=1}^{N}u_iv_i=u^Tv}.

$$

The proof in Section 0.3 uses only the inner-product rules.  It therefore gives
Cauchy--Schwarz in $\mathbb R^N$:

$$

|\left\langle u,v\right\rangle|\le\left\lVert u\right\rVert_2\left\lVert v\right\rVert_2.

$$

For non-zero vectors,
$\cos\theta=\left\langle u,v\right\rangle/(\left\lVert u\right\rVert_2\left\lVert v\right\rVert_2)$.

**Worked Example: Angle from an inner product**

For $u=(1,1,0)$ and $v=(1,0,1)$,

$$

\left\langle u,v\right\rangle=1,
\qquad \left\lVert u\right\rVert_2=\left\lVert v\right\rVert_2=\sqrt2,
\qquad \cos\theta=\frac12.

$$

Hence $\theta=\pi/3$.

## Norms and $p$-norms

The abstract definition of a norm was given in Section 0.2.

**Definition: $p$-norms on $\mathbb R^N$**

For $1\le p<\infty$,

$$

\left\lVert v\right\rVert_p=\left(\sum_{i=1}^{N}|v_i|^p\right)^{1/p},
\qquad
\left\lVert v\right\rVert_{\infty}=\max_{1\le i\le N}|v_i|.

$$

The inner-product norm is $\left\lVert v\right\rVert_2=\sqrt{\left\langle v,v\right\rangle}$.

**Worked Example: Different measurements of the same vector**

For $v=(3,-4)$,

$$

\left\lVert v\right\rVert_1=7,\qquad \left\lVert v\right\rVert_2=5,
\qquad \left\lVert v\right\rVert_{\infty}=4.

$$

The values differ; the induced notions of convergence do not.

## Normalisation and orthogonality

**Definition**

A non-zero vector $v$ is normalised by setting

$$

\widehat v=\frac{v}{\left\lVert v\right\rVert_2}.

$$

Vectors $u$ and $v$ are orthogonal if $\left\langle u,v\right\rangle=0$.

**Worked Example: Normalising an orthogonal pair**

The vectors $u=(1,1)$ and $v=(1,-1)$ are orthogonal.  Their normalised forms
are

$$

\widehat u=\frac1{\sqrt2}(1,1),
\qquad
\widehat v=\frac1{\sqrt2}(1,-1).

$$

The Pythagorean identity follows immediately:
$\left\lVert \alpha\widehat u+\beta\widehat v\right\rVert_2^2=\alpha^2+\beta^2$.

## Orthonormal bases and projections

**Definition**

A basis $(e_1,\ldots,e_N)$ is orthonormal if
$\left\langle e_i,e_j\right\rangle=\delta_{ij}$.  The orthogonal projection onto the line
$\operatorname{span}\{e_i\}$ is

$$

\boxed{P_i v=\left\langle e_i,v\right\ranglee_i}.

$$

More generally, if $U=\operatorname{span}\{e_1,\ldots,e_k\}$, then
$P_Uv=\sum_{i=1}^k\left\langle e_i,v\right\ranglee_i$.

Geometrically, $P_Uv$ is the shadow of $v$ on $U$.

The remainder $v-P_Uv$ points away from the subspace and satisfies

$$

v-P_Uv\perp U.

$$

Also $P_U^2=P_U$: projecting a shadow again does not change it.

**Worked Example: Nearest point on a line**

Let $e=\frac1{\sqrt2}(1,1)$ and $v=(3,1)$.  Then

$$

P_ev=\left\langle e,v\right\ranglee=\frac4{\sqrt2}\frac1{\sqrt2}(1,1)=(2,2).

$$

The error $(1,-1)$ is orthogonal to the line.  Thus $(2,2)$ is also the point
on the line nearest to $(3,1)$.

## Equivalence of norms in finite dimensions

**Theorem: $p$-norm equivalence on $\mathbb R^N$**

Let $1\le p,q\le\infty$.

There is a constant $C\ge1$, independent of $v$, such that

$$

\boxed{C^{-1}\left\lVert v\right\rVert_p\le\left\lVert v\right\rVert_q\le C\left\lVert v\right\rVert_p}

$$

for every $v\in\mathbb R^N$.

Hence all $p$-norms on a fixed $\mathbb R^N$ are equivalent.

A proof is given in Appendix Section appendix:norm-equivalence.

**Worked Example: Why the constant depends on dimension**

For $\mathbf1_N=(1,\ldots,1)$,
$\left\lVert \mathbf1_N\right\rVert_p=N^{1/p}$ and
$\left\lVert \mathbf1_N\right\rVert_q=N^{1/q}$.  The ratio therefore changes with $N$.

This causes no problem while $N$ is fixed.  It becomes decisive in Part II.

**Corollary**

A sequence of vectors in $\mathbb R^N$ converges in one $p$-norm if and only if it
converges in every other $p$-norm.

## Resolution of the identity and Parseval's identity

**Proposition: Basis expansion**

Let $(e_i)_{i=1}^N$ be an orthonormal basis.

Every vector satisfies

$$

v=\sum_{i=1}^{N}\left\langle e_i,v\right\ranglee_i.

$$

Equivalently,

$$

\boxed{\mathrm I=\sum_{i=1}^{N}P_i}.

$$

This is the *resolution of the identity*.

**Proposition: Parseval's identity**

For every $v\in\mathbb R^N$,

$$

\boxed{\left\lVert v\right\rVert_2^2=\sum_{i=1}^{N}|\left\langle e_i,v\right\rangle|^2}.

$$

**Worked Example: Resolving a vector**

For $e_{\pm}=2^{-1/2}(1,\pm1)$ and $v=(3,1)$,

$$

P_+v=(2,2),\qquad P_-v=(1,-1),\qquad v=P_+v+P_-v.

$$

Also $\left\lVert v\right\rVert_2^2=10=|\left\langle e_+,v\right\rangle|^2+|\left\langle e_-,v\right\rangle|^2=8+2$.

## Eigenvalues and eigenvectors

**Definition**

A non-zero vector $v$ is an eigenvector of $A$ with eigenvalue $\lambda\in\mathbb R$
if

$$

\boxed{Av=\lambda v}.

$$

Equivalently, $(A-\lambda\mathrm I)v=0$.  For a matrix, eigenvalues satisfy
$\det(A-\lambda I)=0$.

**Worked Example: A coupled two-component operator**

Let

$$

A=\begin{pmatrix}2&1\\1&2\end{pmatrix}.

$$

Its characteristic polynomial is $(2-\lambda)^2-1$, giving eigenvalues
$3$ and $1$.  Corresponding normalised eigenvectors are
$e_+=2^{-1/2}(1,1)$ and $e_-=2^{-1/2}(1,-1)$.  Along these special directions,
$A$ acts only by stretching.

## Eigenspaces and degeneracy

**Definition**

The eigenspace belonging to $\lambda$ is

$$

E_\lambda=\operatorname{ker}(A-\lambda\mathrm I).

$$

Its dimension is the geometric multiplicity.  An eigenvalue is called
degenerate when its eigenspace has dimension greater than one.

**Worked Example: A degenerate eigenvalue**

For $A=\operatorname{diag}(2,2,5)$, the eigenvalue $2$ has eigenspace

$$

E_2=\operatorname{span}\{(1,0,0),(0,1,0)\},

$$

so it is doubly degenerate.  Every non-zero vector in the $xy$-plane is an
eigenvector with eigenvalue $2$.

## Adjoints and self-adjoint operators

**Definition**

The adjoint $A^*$ is characterised by

$$

\boxed{\left\langle u,Av\right\rangle=\left\langle A^*u,v\right\rangle}

$$

for all $u,v$.  In a real orthonormal basis, $A^*=A^T$.  The operator is
self-adjoint if $A^*=A$; equivalently, its matrix is symmetric.

**Worked Example: Adjoint versus self-adjoint**

If
$A=\begin{psmallmatrix}1&2\\0&3\end{psmallmatrix}$, then
$A^*=\begin{psmallmatrix}1&0\\2&3\end{psmallmatrix}$, so $A$ is not
self-adjoint.  The matrix
$B=\begin{psmallmatrix}1&2\\2&3\end{psmallmatrix}$ is self-adjoint.

## Real eigenvalues of self-adjoint operators

The following inner-product calculation will be reused in every part.

**Proposition**

If $A$ is self-adjoint and $Av=\lambda v$ for $v\ne0$, then the eigenvalue is
obtained from the real Rayleigh quotient

$$

\boxed{\lambda=\frac{\left\langle v,Av\right\rangle}{\left\langle v,v\right\rangle}}.

$$

**Proof**

Taking the inner product of $Av=\lambda v$ with $v$ gives
$\left\langle v,Av\right\rangle=\lambda\left\langle v,v\right\rangle$.  Since $A=A^*$,
$\left\langle v,Av\right\rangle=\left\langle Av,v\right\rangle$ is a real scalar, and $\left\langle v,v\right\rangle>0$.

**Worked Example: Rayleigh quotient**

For $A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}$ and
$v=(1,1)$, the quotient is
$\lambda=(v^TAv)/(v^Tv)=6/2=3$, recovering the eigenvalue without a
determinant.

## Orthogonality of eigenvectors

**Theorem**

Eigenvectors of a self-adjoint operator belonging to distinct eigenvalues are
orthogonal.

**Proof**

Suppose $Au=\lambda u$ and $Av=\mu v$.  Self-adjointness gives

$$

\mu\left\langle u,v\right\rangle=\left\langle u,Av\right\rangle=\left\langle Au,v\right\rangle=\lambda\left\langle u,v\right\rangle.

$$

Thus $(\mu-\lambda)\left\langle u,v\right\rangle=0$.  If $\lambda\ne\mu$, then
$\left\langle u,v\right\rangle=0$.

Within a degenerate eigenspace, Gram--Schmidt produces an orthonormal basis.

**Worked Example**

For the matrix in Section 1.13, the eigenvectors $(1,1)$ and $(1,-1)$ belong
to $3$ and $1$, and their inner product is zero exactly as the theorem predicts.

## The finite-dimensional spectral theorem

**Theorem: Spectral theorem over $\mathbb R$**

Let $A$ be self-adjoint on a finite-dimensional real inner-product space.

Then:
[label=(\roman*),leftmargin=2.7em]
1. every eigenvalue of $A$ is real;
1. eigenspaces for distinct eigenvalues are orthogonal;
1. the space has an orthonormal basis of eigenvectors of $A$;
1. in this basis, $A$ has the form

$$

A=QDQ^T,
\qquad Q^TQ=I,

$$

where $Q$ is orthogonal and $D$ is real diagonal.

Thus a self-adjoint operator has enough orthogonal eigenvectors to resolve
every vector.

**Worked Example: Orthogonal diagonalisation**

For $A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}$, take

$$

Q=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad D=\begin{pmatrix}3&0\\0&1\end{pmatrix}.

$$

Then $Q^TQ=I$ and $A=QDQ^T$.

## Spectral decomposition

Let $P_\lambda$ be the orthogonal projection onto $E_\lambda$.  The spectral
theorem gives

$$

\boxed{A=\sum_{\lambda}\lambda P_\lambda},
\qquad
\boxed{\mathrm I=\sum_{\lambda}P_\lambda}.

$$

If every eigenspace is one-dimensional with normalised eigenvector $e_i$, then
$P_i v=\left\langle e_i,v\right\ranglee_i$ and
$A=\sum_i\lambda_iP_i$.

### The operator only multiplies coefficients

Let $q_1,\ldots,q_N$ be an orthonormal eigenbasis and write

$$

v=c_1q_1+\cdots+c_Nq_N,
\qquad c_i=\left\langle q_i,v\right\rangle.

$$

Since $Aq_i=\lambda_iq_i$,

$$

\boxed{Av=\lambda_1c_1q_1+\cdots+\lambda_Nc_Nq_N.}

$$

The eigenvectors do not change direction.  The $i$th coordinate is simply
multiplied by $\lambda_i$:

$$

c_i\quad\longmapsto\quad \lambda_i c_i.

$$

Let $P$ be the matrix whose columns are the eigenvectors, and let

$$

E=\operatorname{diag}(\lambda_1,\ldots,\lambda_N).

$$

Then

$$

\boxed{A=PEP^{-1}}.

$$

The three actions are

$$

v\xmapsto{\ P^{-1}\ }c
\xmapsto{\ E\ }(\lambda_ic_i)_i
\xmapsto{\ P\ }Av.

$$

For a real self-adjoint operator, $P$ is orthogonal, so $P^{-1}=P^T$.
Choosing the eigenbasis turns the operator into coefficient multiplication.

Because $P_i=q_iq_i^T$,

$$

\boxed{A=\sum_{i=1}^{N}\lambda_iq_iq_i^T
=\sum_{i=1}^{N}\lambda_iP_i.}

$$

Each term extracts one eigendirection, multiplies it by its eigenvalue, and
puts it back.

**Worked Example: One matrix, two coordinate multipliers**

For

$$

A=\begin{pmatrix}2&1\\1&2\end{pmatrix},
\qquad
q_+=\frac1{\sqrt2}\binom11,
\qquad
q_-=\frac1{\sqrt2}\binom1{-1},

$$

the eigenvalues are $3$ and $1$.  If $v=(a,b)^T$, then

$$

c_+=\frac{a+b}{\sqrt2},
\qquad
c_-=\frac{a-b}{\sqrt2},

$$

and therefore

$$

\boxed{Av=3c_+q_++c_-q_-.}

$$

In the eigenbasis, the entire matrix calculation is
$(c_+,c_-)\mapsto(3c_+,c_-)$.

**Worked Example: Using the decomposition**

For the matrix above,

$$

P_+=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
P_-=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},

$$

so $A=3P_++P_-$.  Consequently

$$

A^k=3^kP_++P_-,
\qquad
\mathrm e^{tA}=\mathrm e^{3t}P_++\mathrm e^tP_-.

$$

Operator functions reduce to scalar functions of the eigenvalues.

\centering
$\displaystyle
v_i\ \longrightarrow\ \left\langle e_i,v\right\rangle\ \longrightarrow\ P_iv
\ \longrightarrow
\mathrm I=\sum_iP_i\ \longrightarrow\ A=\sum_\lambda\lambda P_\lambda.$

# Infinite-Dimensional Vectors with a Natural-Number Index

## Infinite-Dimensional Vectors (Natural): $\ell^2$

**Part II.**  Coordinates are indexed by $n\in\mathbb N$.  Infinite sums require
convergence; operators require boundedness or a stated domain.

\centering
$\displaystyle
(v_1,\ldots,v_N)
\quad\longrightarrow\quad
(a_1,a_2,a_3,\ldots),
\qquad
\sum_{i=1}^{N}\quad\longrightarrow\quad\sum_{n=1}^{\infty}.$

The algebra is unchanged.  Convergence is new.

## Vectors and sequence spaces

**Definition: $\ell^p$ spaces**

For $1\le p<\infty$,

$$

\ell^p=\left\{a=(a_n)_{n\ge1}:a_n\in\mathbb R,
\ \sum_{n=1}^{\infty}|a_n|^p<\infty\right\},

$$

and $\ell^\infty$ consists of bounded real sequences.  The space central to
this part is

$$

\boxed{\ell^2=\left\{a=(a_n):\sum_{n=1}^{\infty}a_n^2<\infty\right\}}.

$$

Operations are componentwise.  Square summability makes $\left\lVert a\right\rVert_2$ finite.

**Worked Example: Membership matters**

The sequence $a_n=1/n$ lies in $\ell^2$ because
$\sum_n1/n^2<\infty$, but it does not lie in $\ell^1$ because the harmonic
series diverges.  The constant sequence $(1,1,\ldots)$ lies in neither
$\ell^1$ nor $\ell^2$, although it lies in $\ell^\infty$.

## Linear combinations, span and linear independence

The definitions from Section 1.2 are unchanged.  Infinite expansions are
limits, not algebraic combinations.

Let $c_{00}$ denote the finitely supported sequences.  Then

$$

c_{00}=\operatorname{span}\{e_1,e_2,\ldots\},
\qquad \overline{c_{00}}=\ell^2.

$$

**Worked Example: Approximating by finite vectors**

For $a=(1,1/2,1/3,\ldots)$, define

$$

a^{(N)}=(1,1/2,\ldots,1/N,0,0,\ldots).

$$

Then

$$

\norm{a-a^{(N)}}_2^2=\sum_{n>N}\frac1{n^2}\longrightarrow0.

$$

Thus a genuinely infinite vector is the limit of finite linear combinations
of the $e_n$.

## Bases and coordinates

The standard sequence $e_n$ has a $1$ in position $n$ and zeros elsewhere.
Then $\left\langle e_n,e_m\right\rangle=\delta_{nm}$.  In Hilbert-space language,
$(e_n)_{n\ge1}$ is a complete orthonormal system, or Hilbert basis, for
$\ell^2$.

Here an orthonormal basis gives a norm-convergent series expansion.
A Hamel basis uses finite combinations.

**Worked Example: Coordinates are inner products**

For $a=(a_1,a_2,\ldots)\in\ell^2$,

$$

\left\langle e_n,a\right\rangle=a_n.

$$

The familiar coordinate-extraction formula survives unchanged.

## Decomposition and convergence

Every $a\in\ell^2$ has the norm-convergent expansion

$$

\boxed{a=\sum_{n=1}^{\infty}a_ne_n}.

$$

This equation means

$$

\norm{a-\sum_{n=1}^{N}a_ne_n}_2^2
=\sum_{n>N}|a_n|^2\longrightarrow0.

$$

**Definition: Completeness**

A normed space is complete if every Cauchy sequence of its vectors converges
to a vector in the space.  A complete inner-product space is called a Hilbert
space.  The space $\ell^2$ is a Hilbert space.

Completeness keeps Cauchy limits inside the space.

**Worked Example: A controlled truncation error**

For $a_n=2^{-n}$,

$$

\norm{a-\sum_{n=1}^{N}2^{-n}e_n}_2^2
=\sum_{n>N}4^{-n}=\frac{4^{-N}}{3}.

$$

The norm error is therefore $2^{-N}/\sqrt3$.

## Linear operators

Linearity still means $A(\alpha a+\beta b)=\alpha Aa+\beta Ab$.  In infinite
dimensions we must also ask where $A$ is defined and whether it is continuous.

**Definition: Bounded operator**

A linear operator $A:\ell^2\to\ell^2$ is bounded if there is $C<\infty$ such
that

$$

\left\lVert Aa\right\rVert_2\le C\left\lVert a\right\rVert_2

$$

for every $a\in\ell^2$.  Its operator norm is
$\left\lVert A\right\rVert=\sup_{\left\lVert a\right\rVert_2=1}\left\lVert Aa\right\rVert_2$.

Bounded linear operators are continuous.  An unbounded operator must be given
with a domain $\mathcal D(A)\subsetneq\ell^2$.

**Worked Example: Shift and an unbounded diagonal operator**

The right shift

$$

S(a_1,a_2,\ldots)=(0,a_1,a_2,\ldots)

$$

satisfies $\left\lVert Sa\right\rVert_2=\left\lVert a\right\rVert_2$, so $\left\lVert S\right\rVert=1$.  By contrast,
$D(a_1,a_2,\ldots)=(a_1,2a_2,3a_3,\ldots)$ is not defined on all of $\ell^2$.
Its natural domain is
$\mathcal D(D)=\{a:\sum_n n^2a_n^2<\infty\}$.

## Infinite matrices and operator action

Define $A_{nm}=\left\langle e_n,Ae_m\right\rangle$ whenever this is meaningful.  The matrix rule
becomes

$$

\boxed{(Aa)_n=\sum_{m=1}^{\infty}A_{nm}a_m}.

$$

The series must converge and its output must lie in $\ell^2$.  Not every array
$(A_{nm})$ defines an operator.

**Worked Example: Diagonal and shift matrices**

For $(Aa)_n=\lambda_na_n$, the infinite matrix is diagonal:
$A_{nm}=\lambda_n\delta_{nm}$.  It is bounded precisely when
$\sup_n|\lambda_n|<\infty$, and then $\left\lVert A\right\rVert=\sup_n|\lambda_n|$.
The right shift has entries $S_{nm}=\delta_{n,m+1}$.

The column index now runs forever:

$$

(Av)_i=\sum_{j=1}^{N}A_{ij}v_j
\quad\longrightarrow\quad
(Aa)_n=\sum_{m=1}^{\infty}A_{nm}a_m.

$$

Convergence is essential.

## Inner products

**Definition**

For $a,b\in\ell^2$, define

$$

\boxed{\left\langle a,b\right\rangle=\sum_{n=1}^{\infty}a_nb_n}.

$$

The series converges absolutely by Cauchy--Schwarz:
$\sum_n|a_nb_n|\le\left\lVert a\right\rVert_2\left\lVert b\right\rVert_2$.

**Worked Example: A geometric inner product**

Let $a_n=2^{-n}$ and $b_n=(-1)^{n-1}2^{-n}$.  Then

$$

\left\langle a,b\right\rangle=\sum_{n=1}^{\infty}(-1)^{n-1}4^{-n}
=\frac{1/4}{1+1/4}=\frac15.

$$

Also $\left\lVert a\right\rVert_2^2=\left\lVert b\right\rVert_2^2=\sum_n4^{-n}=1/3$.

## Norms and $p$-norms

For $1\le p<\infty$,

$$

\left\lVert a\right\rVert_p=\left(\sum_{n=1}^{\infty}|a_n|^p\right)^{1/p},
\qquad
\left\lVert a\right\rVert_\infty=\sup_n|a_n|.

$$

Each norm has its natural space $\ell^p$.  On $\ell^2$,
$\left\lVert a\right\rVert_2=\sqrt{\left\langle a,a\right\rangle}$.

**Worked Example: Power-law tails**

For $a_n=n^{-\alpha}$,

$$

a\in\ell^p \quad\Longleftrightarrow\quad \alpha p>1.

$$

Thus $a_n=n^{-3/4}$ lies in $\ell^2$ but not $\ell^1$.  The value of $p$
changes the admissible sequences.

## Normalisation and orthogonality

For non-zero $a\in\ell^2$, set $\widehat a=a/\left\lVert a\right\rVert_2$.  Two sequences are
orthogonal if $\sum_na_nb_n=0$.

**Worked Example: Normalising a geometric sequence**

Let $a=(1,1/2,1/4,\ldots)$, with the first term indexed by $n=0$ for this
example.  Then

$$

\left\lVert a\right\rVert_2^2=\sum_{n=0}^{\infty}4^{-n}=\frac43,
\qquad
\widehat a=\frac{\sqrt3}{2}(1,1/2,1/4,\ldots).

$$

The sequences $u=(1,1,0,\ldots)$ and $v=(1,-1,0,\ldots)$ are orthogonal just
as their two-dimensional versions were.

## Orthonormal bases and projections

For the standard orthonormal basis $(e_n)$,

$$

P_na=\left\langle e_n,a\right\ranglee_n=a_ne_n.

$$

More generally, for a normalised $u\in\ell^2$,
$P_ua=\left\langle u,a\right\rangleu$.  This is again a bounded, self-adjoint idempotent:
$P_u^2=P_u=P_u^*$.

**Worked Example: Projecting onto a two-dimensional model**

Let $U=\operatorname{span}\{e_1,e_2\}$.  Then

$$

P_U(a_1,a_2,a_3,\ldots)=(a_1,a_2,0,0,\ldots).

$$

The error has norm $(\sum_{n\ge3}|a_n|^2)^{1/2}$ and is orthogonal to every
vector in $U$.  Finite-mode approximation is therefore an orthogonal
projection.

## Failure of equivalence of norms in infinite dimensions

**Theorem: No dimension-independent equivalence**

The $p$-norms are not equivalent on infinite sequence spaces.  In particular,
there are no constants $c,C>0$ such that

$$

c\left\lVert a\right\rVert_1\le\left\lVert a\right\rVert_2\le C\left\lVert a\right\rVert_1

$$

on a common infinite-dimensional space in both directions, and the spaces
$\ell^p$ themselves need not contain the same sequences.

**Proof**

For each $N$, let

$$

u^{(N)}=(\underbrace{1,\ldots,1}_{N\text{ terms}},0,0,\ldots).

$$

Then $\norm{u^{(N)}}_p=N^{1/p}$ and
$\norm{u^{(N)}}_q=N^{1/q}$.  If $p<q$, the ratio

$$

\frac{\norm{u^{(N)}}_p}{\norm{u^{(N)}}_q}
=N^{1/p-1/q}\longrightarrow\infty.

$$

No constant independent of $N$ can compare these norms in the way available
on a fixed $\mathbb R^N$.

**Worked Example: The vector sets also differ**

The sequence $(1/n)$ is in $\ell^2$ but not $\ell^1$.  Therefore it is not
even meaningful to say that the $\ell^1$ and $\ell^2$ norms are two equivalent
measurements of exactly the same infinite-dimensional space.

In Section 1.11, $N$ was fixed.  Here $N^{1/p-1/q}$ is unbounded.  Norm choice
can change convergence and membership.

## Resolution of the identity and Parseval's identity

**Proposition: Basis expansion**

For each $a\in\ell^2$,

$$

a=\lim_{N\to\infty}\sum_{n=1}^{N}P_na.

$$

Equivalently,

$$

\boxed{\mathrm I=\sum_{n=1}^{\infty}P_n},

$$

meaning that the partial sums converge after acting on each fixed vector.

**Proposition: Parseval's identity**

For every $a\in\ell^2$,

$$

\boxed{\left\lVert a\right\rVert_2^2=\sum_{n=1}^{\infty}|\left\langle e_n,a\right\rangle|^2}.

$$

**Worked Example: Energy captured by the first modes**

If $a_n=1/n$, then the first $N$ coordinate projections capture energy
$\sum_{n=1}^{N}1/n^2$.  The missing energy is the tail
$\sum_{n>N}1/n^2$, which tends to zero.  In applications this is the basic
logic behind modal truncation.

## Eigenvalues and eigenvectors

The equation is unchanged:

$$

Aa=\lambda a,

$$

A solution must lie in both $\mathcal D(A)$ and $\ell^2$.

**Worked Example: Diagonal eigenvectors**

For $(Aa)_n=\lambda_na_n$, each standard basis vector satisfies
$Ae_n=\lambda_ne_n$.  If $\lambda_n\to0$, these eigenvalues may accumulate at
$0$, a phenomenon impossible for a finite matrix with only finitely many
eigenvalues.

**Worked Example: An operator with no eigenvectors**

The right shift $S(a_1,a_2,\ldots)=(0,a_1,a_2,\ldots)$ has no non-zero
eigenvector over $\ell^2$.  Indeed, $Sa=\lambda a$ forces either
$a_1=a_2=\cdots=0$ recursively or, when $\lambda=0$, again $a=0$.
An infinite-dimensional operator need not possess even one eigenvector.

## Eigenspaces and degeneracy

As before, $E_\lambda=\operatorname{ker}(A-\lambda\mathrm I)$.  Its dimension may be finite or
infinite.

**Worked Example: Infinite degeneracy**

Define $A$ by

$$

A(a_1,a_2,a_3,a_4,\ldots)=(a_1,2a_2,a_3,2a_4,\ldots).

$$

The eigenvalue $1$ has eigenspace generated by $e_1,e_3,e_5,\ldots$, while
$2$ has eigenspace generated by $e_2,e_4,e_6,\ldots$.  Both eigenvalues have
infinite degeneracy.

## Adjoints and self-adjoint operators

For bounded $A$, the adjoint satisfies

$$

\boxed{\left\langle a,Ab\right\rangle=\left\langle A^*a,b\right\rangle}.

$$

For unbounded operators, the adjoint domain is part of the definition.

**Worked Example: Adjoint shifts**

For the right shift $S$,

$$

\left\langle a,Sb\right\rangle=a_2b_1+a_3b_2+\cdots
=\left\langle (a_2,a_3,\ldots),b\right\rangle.

$$

Hence $S^*$ is the left shift $S^*(a_1,a_2,\ldots)=(a_2,a_3,\ldots)$.
Thus $S\ne S^*$.  A bounded real diagonal operator with real entries is
self-adjoint.

## Real eigenvalues of self-adjoint operators

**Proposition**

If $A$ is self-adjoint and $Aa=\lambda a$ for $a\ne0$, then

$$

\lambda=\frac{\left\langle a,Aa\right\rangle}{\left\langle a,a\right\rangle}\in\mathbb R.

$$

**Proof**

The proof is identical to Section 1.16:
$\left\langle a,Aa\right\rangle=\lambda\left\langle a,a\right\rangle$, while self-adjointness makes the quadratic
form real.  For an unbounded operator, the calculation is valid for
$a\in\mathcal D(A)$.

**Worked Example: Diagonal Rayleigh quotient**

For $(Aa)_n=\lambda_na_n$ with bounded real $(\lambda_n)$,

$$

\frac{\left\langle a,Aa\right\rangle}{\left\langle a,a\right\rangle}
=\frac{\sum_n\lambda_na_n^2}{\sum_na_n^2}.

$$

This is a weighted average of the diagonal values, with non-negative weights
$a_n^2/\left\lVert a\right\rVert_2^2$.

## Orthogonality of eigenvectors

**Theorem**

Eigenvectors of a self-adjoint operator belonging to distinct eigenvalues are
orthogonal.

**Proof**

If $Aa=\lambda a$ and $Ab=\mu b$, then

$$

\mu\left\langle a,b\right\rangle=\left\langle a,Ab\right\rangle=\left\langle Aa,b\right\rangle=\lambda\left\langle a,b\right\rangle.

$$

When $\lambda\ne\mu$, it follows that $\left\langle a,b\right\rangle=0$.

The new question is whether the eigenvectors span the space.

**Worked Example**

For Section 2.14's diagonal operator, the odd and even eigenspaces are
orthogonal.  Their products vanish coordinate by coordinate.

## Spectral theorem and spectral issues

An orthonormal eigenbasis need not exist.

**Theorem: Compact self-adjoint case, informal form**

Let $A$ be compact and self-adjoint on a real Hilbert space.

Then:
[label=(\roman*),leftmargin=2.7em]
1. every non-zero spectral value is a real eigenvalue;
1. each non-zero eigenspace is finite-dimensional;
1. non-zero eigenvalues can accumulate only at $0$;
1. the corresponding eigenvectors, together with an orthonormal basis of
$\operatorname{ker} A$, form an orthonormal basis of the space.

General self-adjoint operators require spectral projections.  The spectrum
replaces the finite eigenvalue list.

**Worked Example: A compact diagonal operator**

The operator $(Aa)_n=a_n/n$ is compact and self-adjoint.  Its eigenvalues are
$1,1/2,1/3,\ldots$, with eigenvectors $e_n$, and the only accumulation point
is $0$.

Self-adjointness gives a real spectrum, not necessarily a countable
eigenbasis.  Part III gives a continuous-spectrum example.

## Spectral decomposition

When a self-adjoint operator has a complete orthonormal eigenbasis $(e_n)$,

$$

\boxed{A=\sum_{n=1}^{\infty}\lambda_nP_n},
\qquad P_na=\left\langle e_n,a\right\ranglee_n,

$$

with the series interpreted through its action on vectors.  More generally,
the spectral theorem takes the form

$$

\boxed{A=\int_{\sigma(A)}\lambda\,\mathrm d P(\lambda)},

$$

where $P$ is a family of orthogonal spectral projections.  The sum is the
discrete special case.

**Worked Example: Functions of a diagonal operator**

For $(Aa)_n=n^{-1}a_n$,

$$

A^ka=\sum_{n=1}^{\infty}n^{-k}P_na,
\qquad
\mathrm e^{tA}a=\sum_{n=1}^{\infty}\mathrm e^{t/n}P_na.

$$

Again, operator functions reduce to scalar functions of spectral values.

\centering
$\displaystyle
a_n\ \longrightarrow\ \left\langle e_n,a\right\rangle\ \longrightarrow\ P_na
\ \longrightarrow
\mathrm I=\sum_{n=1}^{\infty}P_n
\ \longrightarrow
A=\sum_n\lambda_nP_n\ \text{when an eigenbasis exists}.$

# Infinite-Dimensional Vectors with a Real-Number Index

## Infinite-Dimensional Vectors (Real): $L^2$

**Part III.**  A function is a continuously indexed vector.  Write $f_x$
at first; then return to $f(x)$.  Sums become integrals and matrices become
kernels.

Think of a function as a continuously indexed vector:

$$

a=(a_n)_{n\in\mathbb N}
\quad\longrightarrow\quad
f=(f_x)_{x\in I}.

$$

Temporarily write

$$

\sum_x(\cdots)\quad\rightsquigarrow\quad\int_I(\cdots)\,\mathrm d x.

$$

The symbol $\sum_x$ is heuristic only.  It is not a sum over uncountably many
points; $\int_I\,\mathrm d x$ is the rigorous object.

## Vectors and function spaces

Initially write the component at $x$ as $f_x$.  Operations are componentwise:

$$

(f+g)_x=f_x+g_x,
\qquad
(\alpha f)_x=\alpha f_x.

$$

In standard notation:
$ (f+g)(x)=f(x)+g(x)$ and $(\alpha f)(x)=\alpha f(x)$.

**Definition: $L^p$ spaces**

For an interval $I$ and $1\le p<\infty$,

$$

L^p(I)=\left\{f:I\to\mathbb R:\int_I|f(x)|^p\,\mathrm d x<\infty\right\},

$$

Functions equal almost everywhere are identified.  The central space is

$$

\boxed{L^2(I)=\left\{f:\int_I|f(x)|^2\,\mathrm d x<\infty\right\}}.

$$

Changing values at isolated points does not change an $L^2$ vector.

**Worked Example: A square-integrable singularity**

On $I=(0,1)$, the function $f(x)=x^{-1/4}$ lies in $L^2$ because

$$

\int_0^1|f(x)|^2\,\mathrm d x=\int_0^1x^{-1/2}\,\mathrm d x=2.

$$

The function $x^{-1/2}$ does not lie in $L^2(0,1)$ because the resulting
integral $\int_0^1x^{-1}\,\mathrm d x$ diverges.

## Linear combinations, span and linear independence

Functions $f_1,\ldots,f_k$ are linearly independent when
$\sum_{j=1}^k\alpha_jf_j(x)=0$ for almost every $x$ implies all
$\alpha_j=0$.

**Worked Example: Independent functions**

The functions $1,x,x^2$ are linearly independent in $L^2(0,1)$.  If
$a+bx+cx^2=0$ almost everywhere, continuity makes the polynomial zero
everywhere, so $a=b=c=0$.

Finite spans produce polynomial, finite-element and Fourier approximations.

## Bases and coordinates

An orthonormal basis of $L^2(I)$ is a sequence of functions
$(\phi_n)_{n\ge1}$ satisfying

$$

\int_I\phi_n(x)\phi_m(x)\,\mathrm d x=\delta_{nm},

$$

whose convergent linear combinations approximate every $L^2$ function.  The
coordinate label $x$ is continuous; the basis may still be countable.

**Worked Example: Sine basis**

On $(0,\pi)$,

$$

\phi_n(x)=\sqrt{\frac2\pi}\sin(nx),
\qquad n=1,2,\ldots,

$$

is an orthonormal basis of $L^2(0,\pi)$.  The coefficient of $f$ in direction
$\phi_n$ is

$$

c_n=\left\langle \phi_n,f\right\rangle=\int_0^\pi\phi_n(x)f(x)\,\mathrm d x.

$$

## Decomposition and convergence

For an orthonormal basis $(\phi_n)$,

$$

\boxed{f=\sum_{n=1}^{\infty}c_n\phi_n,
\qquad c_n=\left\langle \phi_n,f\right\rangle},

$$

where equality means convergence in $L^2$ norm:

$$

\norm{f-\sum_{n=1}^{N}c_n\phi_n}_2\longrightarrow0.

$$

$L^2$ convergence need not be pointwise convergence.

**Worked Example: Fourier sine expansion of a constant**

Let $f(x)=1$ on $(0,\pi)$.  In the basis above,

$$

c_n=\sqrt{\frac2\pi}\int_0^\pi\sin(nx)\,\mathrm d x
=\sqrt{\frac2\pi}\frac{1-(-1)^n}{n}.

$$

Thus only odd modes occur, and in $L^2(0,\pi)$,

$$

1=\frac4\pi\left(\sin x+\frac{\sin3x}{3}
+\frac{\sin5x}{5}+\cdots\right).

$$

At the interval endpoints the sine series takes the boundary value zero; this
does not contradict $L^2$ equality because individual points have zero measure.

## Linear operators

A linear operator satisfies $A(\alpha f+\beta g)=\alpha Af+\beta Ag$.
Examples are

$$

\begin{aligned}
(M_Vf)(x)&=V(x)f(x),\\
(Df)(x)&=f'(x),\\
(Kf)(x)&=\int_IK(x,y)f(y)\,\mathrm d y.
\end{aligned}

$$

$M_V$ is bounded when $V$ is essentially bounded.  Differentiation is
unbounded and requires a domain.  Kernel conditions control $K$.

**Worked Example: A bounded multiplication operator**

On $L^2(0,1)$ let $(Af)(x)=x f(x)$.  Since $|x|\le1$,

$$

\left\lVert Af\right\rVert_2^2=\int_0^1x^2|f(x)|^2\,\mathrm d x\le\left\lVert f\right\rVert_2^2.

$$

Hence $A$ is bounded and $\left\lVert A\right\rVert=1$.

## Kernels and operator action

The matrix rule can be read one index set at a time:

$$

\boxed{\begin{gathered}
(Av)_i=\sum_jA_{ij}v_j
\quad\longrightarrow\quad
(Aa)_n=\sum_mA_{nm}a_m,
$$
2mm]
(Af)_x=\sum_y(A_{xy}f_y)
\quad\rightsquigarrow\quad
\int_I A(x,y)f(y)\,\mathrm d y.
\end{gathered}}

$$

A kernel $A(x,y)$ is a continuously indexed matrix.  The symbol $\sum_y$ is
again heuristic.

**Worked Example: A rank-one kernel**

On $L^2(0,1)$ let $A(x,y)=xy$.  Then

$$

(Af)(x)=\int_0^1xyf(y)\,\mathrm d y
=x\int_0^1yf(y)\,\mathrm d y.

$$

Every output is a multiple of the single function $x$, so the range is
one-dimensional.  For $f(y)=1$, $(Af)(x)=x/2$; for $f(y)=y$,
$(Af)(x)=x/3$.

**Worked Example: Composition resembles matrix multiplication**

If $A$ and $B$ have kernels $A(x,y)$ and $B(y,z)$, then formally

$$

(AB)(x,z)=\int_I A(x,y)B(y,z)\,\mathrm d y,

$$

the exact analogue of $(AB)_{ik}=\sum_jA_{ij}B_{jk}$.

## Inner products

With the continuously indexed vector picture in view, write first

$$

\left\langle f,g\right\rangle=\sum_x(f_xg_x)
\quad\rightsquigarrow\quad
\int_I f_xg_x\,\mathrm d x.

$$

The rigorous definition is therefore:

**Definition**

For real $f,g\in L^2(I)$,

$$

\boxed{\left\langle f,g\right\rangle=\int_I f(x)g(x)\,\mathrm d x}.

$$

The integral is finite by the integral form of Cauchy--Schwarz.

**Worked Example: An explicit inner product**

On $(0,1)$, let $f(x)=x$ and $g(x)=1-x$.  Then

$$

\left\langle f,g\right\rangle=\int_0^1x(1-x)\,\mathrm d x
=\frac12-\frac13=\frac16.

$$

The functions are not orthogonal, but the calculation quantifies their
overlap.

## Norms and $p$-norms

The heuristic continuous-coordinate formula is

$$

\left\lVert f\right\rVert_2^2=\sum_x(f_x^2)
\quad\rightsquigarrow\quad
\int_I f_x^2\,\mathrm d x.

$$

In standard notation,

$$

\boxed{\left\lVert f\right\rVert_p=\left(\int_I|f(x)|^p\,\mathrm d x\right)^{1/p}},
\quad 1\le p<\infty,
\qquad
\left\lVert f\right\rVert_\infty=\operatorname*{ess\,sup}_{x\in I}|f(x)|.

$$

**Worked Example: Three norms of one function**

For $f(x)=x$ on $(0,1)$,

$$

\left\lVert f\right\rVert_1=\frac12,
\qquad
\left\lVert f\right\rVert_2=\frac1{\sqrt3},
\qquad
\left\lVert f\right\rVert_\infty=1.

$$

These norms are not generally equivalent.

## Normalisation and orthogonality

For $f\ne0$, set $\widehat f=f/\left\lVert f\right\rVert_2$.

Functions are orthogonal when $\int_If(x)g(x)\,\mathrm d x=0$.

**Worked Example: Normalising a constant state**

On an interval $(0,L)$, the constant function $1$ has norm $\sqrt L$.  Its
normalised form is

$$

\phi_0(x)=\frac1{\sqrt L}.

$$

This is the normalised constant mode.

**Worked Example: Orthogonality of sine modes**

On $(0,\pi)$,

$$

\int_0^\pi\sin(nx)\sin(mx)\,\mathrm d x=0\qquad(n\ne m).

$$

After multiplication by $\sqrt{2/\pi}$, the modes are normalised as well as
orthogonal.

## Orthonormal bases and projections

For a normalised function $\phi$, projection onto its span is

$$

\begin{aligned}
P_\phi f&=\left\langle \phi,f\right\rangle\phi,\\
(P_\phi f)(x)&=\phi(x)\int_I\phi(y)f(y)\,\mathrm d y.
\end{aligned}

$$

The projection kernel is $P_\phi(x,y)=\phi(x)\phi(y)$.
For an orthonormal family, projection onto its first $N$ members is

$$

P_Nf=\sum_{n=1}^{N}\left\langle \phi_n,f\right\rangle\phi_n.

$$

**Worked Example: Best one-mode approximation**

Project $f(x)=x$ on $(0,1)$ onto the normalised constant $\phi_0(x)=1$.
Then

$$

P_0f=\left\langle 1,x\right\rangle\,1=\frac12.

$$

Among all constants $c$, the value $c=1/2$ uniquely minimises
$\int_0^1|x-c|^2\,\mathrm d x$.

Projection is the same operation in every part:

$$

P_iv=\left\langle e_i,v\right\ranglee_i,
\qquad
P_na=\left\langle e_n,a\right\ranglee_n,
\qquad
P_\phi f=\left\langle \phi,f\right\rangle\phi.

$$

Only the inner product formula changes.

## Failure of equivalence of norms in infinite dimensions

**Theorem: Failure of $L^p$ norm equivalence**

On infinite-dimensional function spaces, different $L^p$ norms are not
generally equivalent.  Even on the finite interval $(0,1)$ there are no
constants $c,C>0$ such that

$$

c\left\lVert f\right\rVert_1\le\left\lVert f\right\rVert_2\le C\left\lVert f\right\rVert_1

$$

for all functions in a common dense class.

**Proof**

Consider the increasingly concentrated spike

$$

f_n(x)=\sqrt n\,\mathbf 1_{(0,1/n)}(x).

$$

Then

$$

\left\lVert f_n\right\rVert_2^2=\int_0^{1/n}n\,\mathrm d x=1,
\qquad
\left\lVert f_n\right\rVert_1=\int_0^{1/n}\sqrt n\,\mathrm d x=\frac1{\sqrt n}.

$$

If $\left\lVert f\right\rVert_2\le C\left\lVert f\right\rVert_1$ held uniformly, we would have
$1\le C/\sqrt n$ for every $n$, which is impossible.

**Worked Example: The underlying spaces may differ**

On $(0,1)$, $f(x)=x^{-1/2}$ belongs to $L^1$ but not to $L^2$:

$$

\int_0^1x^{-1/2}\,\mathrm d x=2,
\qquad
\int_0^1x^{-1}\,\mathrm d x=\infty.

$$

Thus, as with sequence spaces, changing $p$ may change the admissible vectors,
not merely their numerical lengths.

On finite-measure intervals, $L^2(I)\subset L^1(I)$.  This one-way estimate is
not norm equivalence.

## Resolution of the identity and Parseval's identity

**Proposition: Basis expansion**

For a complete orthonormal basis $(\phi_n)$,

$$

f=\sum_{n=1}^{\infty}\left\langle \phi_n,f\right\rangle\phi_n

$$

in the $L^2$ norm.  Equivalently,

$$

\boxed{\mathrm I=\sum_{n=1}^{\infty}P_n}.

$$

**Proposition: Parseval's identity**

For every $f\in L^2(I)$,

$$

\boxed{\left\lVert f\right\rVert_2^2
=\sum_{n=1}^{\infty}|\left\langle \phi_n,f\right\rangle|^2}.

$$

In continuous-coordinate language, the identity operator has the formal
kernel $\delta(x-y)$:

$$

f(x)=\int_I\delta(x-y)f(y)\,\mathrm d y.

$$

The Dirac delta is a generalised function, not an element of $L^2$.

**Worked Example: Parseval evaluates a series**

For $f(x)=1$ on $(0,\pi)$ and the sine basis of Section 3.3,
$\left\lVert f\right\rVert_2^2=\pi$ and

$$

|c_n|^2=
\begin{cases}
8/(\pi n^2),&n\text{ odd},\\
0,&n\text{ even}.
\end{cases}

$$

Parseval therefore gives

$$

\pi=\frac8\pi\sum_{n\text{ odd}}\frac1{n^2},
\qquad
\sum_{n\text{ odd}}\frac1{n^2}=\frac{\pi^2}{8}.

$$

## Eigenvalues and eigenfunctions

An eigenfunction is a non-zero function in the operator domain satisfying

$$

\boxed{Af=\lambda f}.

$$

This is the usual eigenvector equation with a function as the vector.

**Worked Example: A boundary-value eigenproblem**

On $(0,\pi)$ consider

$$

Af=-f'',
\qquad f(0)=f(\pi)=0.

$$

The functions $f_n(x)=\sin(nx)$ satisfy

$$

Af_n=n^2f_n.

$$

Thus $\lambda_n=n^2$ and
$\phi_n(x)=\sqrt{2/\pi}\sin(nx)$.  Boundary conditions change the spectrum.

## Eigenspaces and degeneracy

The eigenspace is again $E_\lambda=\operatorname{ker}(A-\lambda\mathrm I)$.  Degeneracy means
$\dim E_\lambda>1$.

**Worked Example: Degeneracy on a periodic interval**

On real periodic functions over $(-\pi,\pi)$, let $A=-\,\mathrm d^2/\,\mathrm d x^2$ with
periodic boundary conditions.  For each $n\ge1$,

$$

A\cos(nx)=n^2\cos(nx),
\qquad
A\sin(nx)=n^2\sin(nx).

$$

Thus $n^2$ has degeneracy two.  The eigenspace for $0$ consists of constant
functions and has dimension one.

## Adjoints and self-adjoint operators

The adjoint is still defined by

$$

\boxed{\left\langle f,Ag\right\rangle=\left\langle A^*f,g\right\rangle}.

$$

For a kernel operator,

$$

(Af)(x)=\int_IA(x,y)f(y)\,\mathrm d y
\quad\Longrightarrow\quad
(A^*f)(x)=\int_IA(y,x)f(y)\,\mathrm d y

$$

under suitable hypotheses.  A symmetric real kernel $A(x,y)=A(y,x)$ therefore
suggests a self-adjoint operator.

For differential operators, integrate by parts:

$$

\int_0^\pi f(-g'')\,\mathrm d x
=\int_0^\pi(-f'')g\,\mathrm d x
+\bigl[f'g-fg'\bigr]_{0}^{\pi}.

$$

Dirichlet conditions $f(0)=f(\pi)=g(0)=g(\pi)=0$ remove the boundary term.

The differential expression, domain and boundary conditions define the
operator together.  Integration by parts tests formal symmetry; full
self-adjointness also requires a domain argument.

**Worked Example: A symmetric kernel**

The kernel $A(x,y)=\min(x,y)$ on $(0,1)$ satisfies $A(x,y)=A(y,x)$, so the
associated integral operator is self-adjoint.  By contrast, a non-symmetric
kernel and its transpose generally define different adjoint operators.

## Real eigenvalues of self-adjoint operators

**Proposition**

If $A$ is self-adjoint and $Af=\lambda f$ for non-zero
$f\in\mathcal D(A)$, then

$$

\boxed{\lambda=\frac{\left\langle f,Af\right\rangle}{\left\langle f,f\right\rangle}\in\mathbb R}.

$$

**Proof**

We have $\left\langle f,Af\right\rangle=\lambda\left\langle f,f\right\rangle$.  The numerator is real and the
denominator is positive.

**Worked Example: Rayleigh quotient for $-f''$**

For a sufficiently smooth real function with $f(0)=f(\pi)=0$, integration by
parts gives

$$

\frac{\left\langle f,-f''\right\rangle}{\left\langle f,f\right\rangle}
=\frac{\int_0^\pi|f'(x)|^2\,\mathrm d x}
{\int_0^\pi|f(x)|^2\,\mathrm d x}\ge0.

$$

Thus the Dirichlet eigenvalues of $-\,\mathrm d^2/\,\mathrm d x^2$ are not only real but
non-negative.

## Orthogonality of eigenfunctions

**Theorem**

Eigenfunctions of a self-adjoint operator belonging to distinct eigenvalues
are orthogonal in $L^2$.

**Proof**

If $Af=\lambda f$ and $Ag=\mu g$, then

$$

\mu\left\langle f,g\right\rangle=\left\langle f,Ag\right\rangle=\left\langle Af,g\right\rangle=\lambda\left\langle f,g\right\rangle.

$$

For $\lambda\ne\mu$, this gives $\left\langle f,g\right\rangle=0$.

**Worked Example: Sturm--Liouville orthogonality**

For the Dirichlet eigenfunctions $\sin(nx)$ and $\sin(mx)$ on $(0,\pi)$,
distinct eigenvalues $n^2\ne m^2$ imply

$$

\int_0^\pi\sin(nx)\sin(mx)\,\mathrm d x=0.

$$

The familiar trigonometric identity is therefore an instance of a general
self-adjoint principle.

## Spectral theorem and spectral issues

Compact self-adjoint kernels have orthonormal eigenfunction bases.
Other self-adjoint operators may have continuous spectrum.

**Worked Example: Continuous spectrum without $L^2$ eigenfunctions**

On $L^2(-1,1)$ define $(Mf)(x)=xf(x)$.  This bounded operator is
self-adjoint.  If $Mf=\lambda f$, then

$$

(x-\lambda)f(x)=0

$$

almost everywhere.  Hence $f$ could be non-zero only at the single point
$x=\lambda$, which represents the zero vector in $L^2$.  Thus $M$ has no
non-zero $L^2$ eigenfunctions, even though its spectrum is the entire interval
$[-1,1]$.

Thus self-adjointness need not give an eigenbasis.  Spectral projections replace
a countable list of eigenvectors.

Generalised eigenfunctions need not lie in $L^2$.  Their proper setting is
distribution and spectral theory.

## Spectral decomposition

In a discrete eigenfunction basis,

$$

\boxed{Af=\sum_{n=1}^{\infty}\lambda_n
\left\langle \phi_n,f\right\rangle\phi_n},
\qquad
A=\sum_{n=1}^{\infty}\lambda_nP_n.

$$

In general,

$$

\boxed{A=\int_{\sigma(A)}\lambda\,\mathrm d P(\lambda)}.

$$

**Worked Example: Dirichlet Laplacian**

Let $A=-\,\mathrm d^2/\,\mathrm d x^2$ on $(0,\pi)$.
Impose Dirichlet boundary conditions.  Then

$$

Af=\sum_{n=1}^{\infty}n^2\left\langle \phi_n,f\right\rangle\phi_n,
\qquad
\phi_n(x)=\sqrt{\frac2\pi}\sin(nx),

$$

for functions in the appropriate operator domain.  Solving
$u_t=-Au$ mode by mode gives

$$

u(t)=\sum_{n=1}^{\infty}\mathrm e^{-n^2t}\left\langle \phi_n,u(0)\right\rangle\phi_n,

$$

which is the spectral solution of the heat equation.

**Worked Example: Continuous decomposition of multiplication**

For $M f(x)=x f(x)$ on $L^2(-1,1)$, define a projection for each measurable
set $B\subset[-1,1]$ by

$$

(P(B)f)(x)=\mathbf 1_B(x)f(x).

$$

Then $M=\int_{-1}^{1}\lambda\,\mathrm d P(\lambda)$.  No ordinary eigenbasis is
required.

\centering
$\displaystyle
f_x\ \longrightarrow\ f(x),\qquad
\sum_x(f_xg_x)\ \rightsquigarrow\ \int f(x)g(x)\,\mathrm d x,
\qquad
(Af)_x=\sum_y(A_{xy}f_y)\ \rightsquigarrow
\int A(x,y)f(y)\,\mathrm d y.$

# Fourier Coordinates and Evolution Equations

## Fourier Coordinates, Heat Flow and Quantum Motion

The guiding idea is the finite-dimensional rule

$$

\boxed{\text{choose a useful basis}
\quad\Longrightarrow\quad
\text{study its coordinates}.}

$$

If the basis consists of eigenvectors, an operator acts by multiplying
coordinates.  This part develops that idea slowly for functions.

## Moving vectors and moving functions

Begin with an ordinary moving vector:

$$

v(t)=\cos(t)\,\mathbf i+\sin(t)\,\mathbf j.

$$

The basis vectors $\mathbf i$ and $\mathbf j$ are fixed.

The coordinates move:

$$

v_1(t)=\cos t,
\qquad
v_2(t)=\sin t.

$$

At each time $t$, the pair

$$

\begin{pmatrix}\cos t\\ \sin t\end{pmatrix}

$$

describes one vector.  As $t$ changes, the vector traces a circle.

Time dependence does not require a new kind of vector.

It means that the coefficients in a fixed basis now depend on time:

$$

v(t)=\sum_i c_i(t)e_i.

$$

The same interpretation applies to a function $u(x,t)$.

For each fixed $t$, the map

$$

x\longmapsto u(x,t)

$$

is one vector in a function space.

Heuristically write

$$

u(t)=\bigl(u_x(t)\bigr)_{x\in\mathbb R},
\qquad
u_x(t)=u(x,t).

$$

The number $u(x,t)$ is the coefficient in the direction labelled by $x$.

Time changes all these coefficients:

$$

t\longmapsto u(t).

$$

**Definition: A time-dependent function-vector**

A function $u(x,t)$ may be viewed as a path through a function space.

For each fixed $t$:

$$

u(\,\cdot\,,t)

$$

is one vector.

For each fixed $x$:

$$

u(x,t)

$$

is one time-dependent coefficient.

If a fixed orthonormal basis $(\phi_n)$ is used, then

$$

u(x,t)=\sum_n c_n(t)\phi_n(x).

$$

The basis functions do not move.  The coordinates $c_n(t)$ do.

Consequently,

$$

\frac{\partial u}{\partial t}(x,t)
=\sum_n c_n'(t)\phi_n(x).

$$

This simple observation is the heart of the later heat and
Schrödinger calculations.

## Position directions and narrow boxes

For $v\in\mathbb R^N$, the standard basis vector $e_i$ represents the $i$th
coordinate direction:

$$

v_i=\left\langle e_i,v\right\rangle,
\qquad
v=\sum_i v_i e_i.

$$

For a function, imagine one coordinate direction for every point $x$:

$$

f=(f_x)_{x\in\mathbb R},
\qquad
f_x=f(x).

$$

A narrow box gives a visible approximation to such a direction.

**Definition: A unit-area box centred at $x$**

For $n=1,2,\ldots$, define

$$

\psi_{x,n}(y)=
\begin{cases}
n,
&x-\dfrac1{2n}<y<x+\dfrac1{2n},
$$
2mm]
0,
&\text{otherwise}.
\end{cases}

$$

Its width is $1/n$, its height is $n$, and its area is one:

$$

\int_{-\infty}^{\infty}\psi_{x,n}(y)\,\mathrm d y=1.

$$

> Diagram: see the PDF or LaTeX edition.

{\small A narrower box is also taller, so its area remains one.}

If $f$ varies little across the box, then

$$

\int_{-\infty}^{\infty}\psi_{x,n}(y)f(y)\,\mathrm d y
\approx f(x).

$$

The box approximately extracts the coefficient at $x$.

**Worked Example: Extracting a local value**

Let $f(y)=y^2$ and let the box have width $h$.

Its average is

$$

\frac1h\int_{x-h/2}^{x+h/2}y^2\,\mathrm d y
=x^2+\frac{h^2}{12}.

$$

As $h\to0$, this tends to $x^2=f(x)$.

## The delta direction

The idealised coordinate direction at $x$ is written $\delta_x$.

**Definition: Delta direction at $x$: motivational form**

The symbol $\delta_x(y)$ is characterised heuristically by

$$

\boxed{\int_{-\infty}^{\infty}
\delta_x(y)f(y)\,\mathrm d y=f(x).}

$$

It plays the role of the basis vector for the direction labelled by $x$.

The narrow boxes motivate the notation

$$

\psi_{x,n}(y)\longrightarrow\delta_x(y).

$$

No precise meaning of this limit is required here.

Just as $e_i$ extracts $v_i$, the delta direction extracts $f_x$:

$$

\left\langle e_i,v\right\rangle=v_i,
\qquad
\left\langle \delta_x,f\right\rangle=f(x).

$$

The corresponding expansions are

$$

v=\sum_i v_i e_i,

$$

and, heuristically,

$$

\boxed{f(y)=\int_{-\infty}^{\infty}f(x)\delta_x(y)\,\mathrm d x.}

$$

### Moving the direction centred at zero

First define the direction at the origin:

$$

\delta_0(y)=\delta(y).

$$

Translate it from $0$ to $x$:

$$

\boxed{\delta_x(y)=\delta_0(y-x).}

$$

The usual delta notation therefore gives

$$

\delta_x(y)=\delta(y-x).

$$

Since the delta is symmetric,

$$

\boxed{\delta_x(y)=\delta(y-x)=\delta(x-y).}

$$

This explains why an identity kernel is written

$$

I(x,y)=\delta(x-y).

$$

Indeed,

$$

(If)(x)=\int\delta(x-y)f(y)\,\mathrm d y=f(x).

$$

The delta direction is not an ordinary $L^2$ function.

The unit-area boxes also satisfy

$$

\norm{\psi_{x,n}}_2=\sqrt n.

$$

Their norms grow as they become narrower.  The delta notation is therefore
a coordinate picture, not an orthonormal basis inside $L^2$.

A genuine orthonormal box approximation is obtained by dividing the line
into disjoint cells $I_j$ of width $h$ and setting

$$

\phi_{j,h}(y)=\frac1{\sqrt h}\mathbf 1_{I_j}(y).

$$

Then

$$

\ip{\phi_{j,h}}{\phi_{k,h}}=\delta_{jk}.

$$

The coordinate is

$$

c_j=\ip{\phi_{j,h}}{f}
=\frac1{\sqrt h}\int_{I_j}f(y)\,\mathrm d y.

$$

The reconstructed term is

$$

c_j\phi_{j,h}(y)
=\left(\frac1h\int_{I_j}f(s)\,\mathrm d s\right)\mathbf 1_{I_j}(y).

$$

Thus each cell is replaced by its average value.

## Why choose a Fourier basis?

The position directions describe where a function is located.

For differentiation, oscillating directions are more useful:

$$

\mathrm e^{\mathrm i nx}.

$$

Differentiation does not change their shape:

$$

\frac{\,\mathrm d}{\,\mathrm d x}\mathrm e^{\mathrm i nx}
=\mathrm i n\,\mathrm e^{\mathrm i nx}.

$$

This is the function-space analogue of choosing eigenvectors of a matrix.

In an eigenvector basis,

$$

A\left(\sum_i c_iq_i\right)
=\sum_i\lambda_i c_iq_i.

$$

In a Fourier basis, a differential operator will likewise multiply each
coefficient.

## The Fourier basis on $L^2(-\pi,\pi)$

Complex notation combines sine and cosine into one expression.

Use the inner product

$$

\left\langle g,f\right\rangle
=\int_{-\pi}^{\pi}\overline{g(x)}f(x)\,\mathrm d x.

$$

**Definition: Normalised complex Fourier functions**

For $n\in\mathbb Z$, define

$$

\boxed{\phi_n(x)=\frac1{\sqrt{2\pi}}\mathrm e^{\mathrm i nx}.}

$$

The factor $1/\sqrt{2\pi}$ makes every basis function have norm one:

$$

\left\lVert \phi_n\right\rVert_2^2
=\frac1{2\pi}\int_{-\pi}^{\pi}1\,\mathrm d x
=1.

$$

### Orthogonality

For $m,n\in\mathbb Z$,

$$

\begin{aligned}
\left\langle \phi_m,\phi_n\right\rangle
&=\frac1{2\pi}\int_{-\pi}^{\pi}
\mathrm e^{\mathrm i(n-m)x}\,\mathrm d x.
\end{aligned}

$$

If $m=n$, the integrand is $1$, so

$$

\left\langle \phi_n,\phi_n\right\rangle=1.

$$

If $m\ne n$, then

$$

\begin{aligned}
\left\langle \phi_m,\phi_n\right\rangle
&=\frac1{2\pi}
\left[
\frac{\mathrm e^{\mathrm i(n-m)x}}{\mathrm i(n-m)}
\right]_{-\pi}^{\pi}\\
&=0.
\end{aligned}

$$

Hence

$$

\boxed{\left\langle \phi_m,\phi_n\right\rangle=\delta_{mn}.}

$$

**Proposition: Fourier coordinates**

The coordinate of $f$ in the direction $\phi_n$ is

$$

\boxed{
c_n=\left\langle \phi_n,f\right\rangle
=\frac1{\sqrt{2\pi}}\int_{-\pi}^{\pi}
f(x)\mathrm e^{-\mathrm i nx}\,\mathrm d x.}

$$

The coordinate expansion is

$$

\boxed{f(x)=\sum_{n\in\mathbb Z}c_n\phi_n(x)}

$$

in the $L^2$ sense.

A Fourier coefficient is not a new kind of object.

It is simply a coordinate in the Fourier basis:

$$

\boxed{\text{Fourier coefficient}
=\text{coordinate in the Fourier basis}.}

$$

The phrase *Fourier series* means the corresponding basis expansion.

A second common convention uses

$$

\widehat f_n
=\frac1{2\pi}\int_{-\pi}^{\pi}
f(x)\mathrm e^{-\mathrm i nx}\,\mathrm d x.

$$

Then

$$

f(x)=\sum_{n\in\mathbb Z}\widehat f_n\mathrm e^{\mathrm i nx}.

$$

The two conventions differ only by normalisation:

$$

c_n=\sqrt{2\pi}\,\widehat f_n.

$$

### The real sine and cosine basis

Euler's formula gives

$$

\mathrm e^{\mathrm i nx}=\cos(nx)+\mathrm i\sin(nx).

$$

Also,

$$

\cos(nx)
=\frac{\mathrm e^{\mathrm i nx}+\mathrm e^{-\mathrm i nx}}2,

$$

$$

\sin(nx)
=\frac{\mathrm e^{\mathrm i nx}-\mathrm e^{-\mathrm i nx}}
{2\mathrm i}.

$$

Thus the real and complex descriptions contain the same oscillations.

A real orthonormal basis is

$$

\boxed{
\frac1{\sqrt{2\pi}},
\qquad
\frac{\cos(nx)}{\sqrt\pi},
\qquad
\frac{\sin(nx)}{\sqrt\pi},
\quad n=1,2,\ldots .}

$$

## Changing the interval to $(-L,L)$

The interval now has length $2L$.

To fit exactly across this interval, the frequencies become

$$

k_n=\frac{n\pi}{L}.

$$

**Definition: Fourier basis on $(-L,L)$**

For $n\in\mathbb Z$, define

$$

\boxed{
\phi_n^{(L)}(x)
=\frac1{\sqrt{2L}}
\mathrm e^{\mathrm i n\pi x/L}.}

$$

The normalisation again gives unit norm:

$$

\norm{\phi_n^{(L)}}_2^2
=\frac1{2L}\int_{-L}^{L}1\,\mathrm d x
=1.

$$

Orthogonality follows from

$$

\ip{\phi_m^{(L)}}{\phi_n^{(L)}}
=\frac1{2L}\int_{-L}^{L}
\mathrm e^{\mathrm i(n-m)\pi x/L}\,\mathrm d x
=\delta_{mn}.

$$

The real orthonormal basis is

$$

\boxed{
\frac1{\sqrt{2L}},
\qquad
\frac{\cos(n\pi x/L)}{\sqrt L},
\qquad
\frac{\sin(n\pi x/L)}{\sqrt L},
\quad n=1,2,\ldots .}

$$

Nothing essential has changed.

On $(-\pi,\pi)$:

$$

n\quad\text{is the wave number}.

$$

On $(-L,L)$:

$$

\frac{n\pi}{L}\quad\text{is the wave number}.

$$

The interval length changes the allowed frequencies and the normalising
constant.

## Real Fourier series and three examples

For a real function on $(-L,L)$, the conventional form is

$$

f(x)\sim
\frac{a_0}{2}
+\sum_{n=1}^{\infty}
\left[
a_n\cos\!\left(\frac{n\pi x}{L}\right)
+b_n\sin\!\left(\frac{n\pi x}{L}\right)
\right],

$$

where

$$

a_n=\frac1L\int_{-L}^{L}
f(x)\cos\!\left(\frac{n\pi x}{L}\right)\,\mathrm d x,

$$

$$

b_n=\frac1L\int_{-L}^{L}
f(x)\sin\!\left(\frac{n\pi x}{L}\right)\,\mathrm d x.

$$

These $a_n$ and $b_n$ are again coordinates, with a conventional
normalisation.

Even functions have only cosine terms.

Odd functions have only sine terms.

### What happens at a jump?

Suppose $f$ has one-sided limits at $x$:

$$

f(x^-),
\qquad
f(x^+).

$$

For a piecewise smooth function, its Fourier series converges there to

$$

\boxed{\frac{f(x^-)+f(x^+)}2.}

$$

At a continuous point this is simply $f(x)$.

At a jump it is the midpoint between the two limiting values.

This does not conflict with $L^2$ equality: changing a function at one point
does not change its $L^2$ vector.

**Worked Example: The function $x^2$ on $(-\pi,\pi)$**

The function is even, so $b_n=0$.

Its coefficients are

$$

a_0=\frac1\pi\int_{-\pi}^{\pi}x^2\,\mathrm d x
=\frac{2\pi^2}{3},

$$

$$

a_n=\frac1\pi\int_{-\pi}^{\pi}x^2\cos(nx)\,\mathrm d x
=\frac{4(-1)^n}{n^2}.

$$

Therefore

$$

\boxed{
x^2=\frac{\pi^2}{3}
+4\sum_{n=1}^{\infty}
\frac{(-1)^n}{n^2}\cos(nx).}

$$

At $x=\pi$, this gives

$$

\pi^2=\frac{\pi^2}{3}
+4\sum_{n=1}^{\infty}\frac1{n^2}.

$$

Hence

$$

\sum_{n=1}^{\infty}\frac1{n^2}
=\frac{\pi^2}{6}.

$$

**Worked Example: A step function**

On $(-\pi,\pi)$, define

$$

s(x)=
\begin{cases}
-1,&-\pi<x<0,\\
1,&0<x<\pi.
\end{cases}

$$

The function is odd, so only sine coordinates occur:

$$

\boxed{
s(x)\sim\frac4\pi
\sum_{r=0}^{\infty}
\frac{\sin((2r+1)x)}{2r+1}.}

$$

At $x=0$,

$$

s(0^- )=-1,
\qquad
s(0^+)=1.

$$

The Fourier series therefore takes the midpoint value

$$

\frac{-1+1}{2}=0.

$$

Every sine term is also zero at $x=0$.

At $x=\pi$, the periodic extension jumps from $1$ back to $-1$.
The series again converges to $0$.

**Worked Example: The tent function $1-|x|$ on $(-1,1)$**

Let

$$

f(x)=1-|x|.

$$

This function is even and has period $2$ after periodic extension.

Its Fourier series is

$$

\boxed{
1-|x|
=\frac12+\frac4{\pi^2}
\sum_{r=0}^{\infty}
\frac{\cos((2r+1)\pi x)}{(2r+1)^2}.}

$$

Only odd cosine modes occur.

At $x=0$,

$$

1=\frac12+\frac4{\pi^2}
\sum_{r=0}^{\infty}\frac1{(2r+1)^2}.

$$

At $x=1$,

$$

0=\frac12-\frac4{\pi^2}
\sum_{r=0}^{\infty}\frac1{(2r+1)^2}.

$$

Both give

$$

\sum_{r=0}^{\infty}\frac1{(2r+1)^2}
=\frac{\pi^2}{8}.

$$

## Parseval's identity

For an orthonormal basis in $\mathbb R^N$,

$$

\left\lVert v\right\rVert^2=\sum_i|c_i|^2.

$$

The length of the vector equals the length of its coordinate list.

The same statement holds for Fourier coordinates.

**Theorem: Parseval on $(-\pi,\pi)$**

If

$$

f=\sum_{n\in\mathbb Z}c_n\phi_n,

$$

then

$$

\boxed{
\int_{-\pi}^{\pi}|f(x)|^2\,\mathrm d x
=\sum_{n\in\mathbb Z}|c_n|^2.}

$$

For the conventional real coefficients on $(-L,L)$,

$$

\boxed{
\frac1L\int_{-L}^{L}|f(x)|^2\,\mathrm d x
=\frac{a_0^2}{2}
+\sum_{n=1}^{\infty}(a_n^2+b_n^2).}

$$

Parseval says that changing to Fourier coordinates does not change length.

It is the function-space version of

$$

P^{-1}=P^T

$$

for an orthogonal change of basis in $\mathbb R^N$.

**Worked Example: Parseval for the step function**

For the step function, $|s(x)|^2=1$ almost everywhere.  Hence

$$

\frac1\pi\int_{-\pi}^{\pi}|s(x)|^2\,\mathrm d x=2.

$$

Its non-zero sine coefficients are

$$

b_{2r+1}=\frac4{\pi(2r+1)}.

$$

Parseval gives

$$

2=\frac{16}{\pi^2}
\sum_{r=0}^{\infty}\frac1{(2r+1)^2},

$$

again yielding

$$

\sum_{r=0}^{\infty}\frac1{(2r+1)^2}
=\frac{\pi^2}{8}.

$$

## Differential operators multiply Fourier coordinates

On $(-L,L)$,

$$

\phi_n^{(L)}(x)
=\frac1{\sqrt{2L}}\mathrm e^{\mathrm i n\pi x/L}.

$$

Therefore

$$

\frac{\,\mathrm d}{\,\mathrm d x}\phi_n^{(L)}
=\frac{\mathrm i n\pi}{L}\phi_n^{(L)},

$$

and

$$

-\frac{\,\mathrm d^2}{\,\mathrm d x^2}\phi_n^{(L)}
=\left(\frac{n\pi}{L}\right)^2\phi_n^{(L)}.

$$

If

$$

f=\sum_{n\in\mathbb Z}c_n\phi_n^{(L)},

$$

then, formally,

$$

\boxed{
f'
=\sum_{n\in\mathbb Z}
\left(\frac{\mathrm i n\pi}{L}\right)
c_n\phi_n^{(L)},}

$$

and

$$

\boxed{
-f''
=\sum_{n\in\mathbb Z}
\left(\frac{n\pi}{L}\right)^2
c_n\phi_n^{(L)}.}

$$

Thus differentiation acts directly on the coordinates:

$$

c_n\longmapsto
\frac{\mathrm i n\pi}{L}c_n,

$$

$$

c_n\longmapsto
\left(\frac{n\pi}{L}\right)^2c_n.

$$

Compare the three calculations:

$$

\begin{aligned}
A q_i&=\lambda_iq_i,
&c_i&\longmapsto\lambda_i c_i,\\
D\phi_n^{(L)}
&=\frac{\mathrm i n\pi}{L}\phi_n^{(L)},
&c_n&\longmapsto\frac{\mathrm i n\pi}{L}c_n.
\end{aligned}

$$

The operator is complicated in the original coordinates but simple in its
eigenbasis.

**Worked Example: Differentiate one Fourier mode**

On $(-\pi,\pi)$,

$$

f(x)=\cos(3x)
=\frac12\mathrm e^{3\mathrm i x}
+\frac12\mathrm e^{-3\mathrm i x}.

$$

Differentiation multiplies the two coordinates by $3\mathrm i$ and
$-3\mathrm i$:

$$

f'(x)
=\frac{3\mathrm i}{2}\mathrm e^{3\mathrm i x}
-\frac{3\mathrm i}{2}\mathrm e^{-3\mathrm i x}.

$$

Therefore

$$

f'(x)=-3\sin(3x).

$$

## The periodic heat equation

Consider the heat equation on $(-L,L)$:

$$

\frac{\partial u}{\partial t}
=\kappa\frac{\partial^2u}{\partial x^2},
\qquad
u(x,0)=f(x),

$$

with periodic boundary conditions.

At each time $t$, expand the function-vector:

$$

\boxed{
u(x,t)=\sum_{n\in\mathbb Z}c_n(t)\phi_n^{(L)}(x).}

$$

This is exactly the form

$$

v(t)=\sum_i c_i(t)e_i

$$

from finite-dimensional linear algebra.

The coefficients are now time-dependent.

Differentiate with respect to time:

$$

u_t
=\sum_{n\in\mathbb Z}c_n'(t)\phi_n^{(L)}.

$$

Differentiate twice with respect to position:

$$

u_{xx}
=-\sum_{n\in\mathbb Z}
\left(\frac{n\pi}{L}\right)^2
c_n(t)\phi_n^{(L)}.

$$

Equality of the two function-vectors means equality of every coordinate:

$$

c_n'(t)
=-\kappa\left(\frac{n\pi}{L}\right)^2c_n(t).

$$

The partial differential equation has become one scalar ordinary
differential equation for each $n$.

**Theorem: Periodic heat flow**

Let

$$

c_n(0)=\ip{\phi_n^{(L)}}{f}.

$$

Then

$$

\boxed{
c_n(t)
=\exp\!\left[
-\kappa\left(\frac{n\pi}{L}\right)^2t
\right]c_n(0).}

$$

Hence

$$

\boxed{
u(x,t)=\sum_{n\in\mathbb Z}
\exp\!\left[
-\kappa\left(\frac{n\pi}{L}\right)^2t
\right]
c_n(0)\phi_n^{(L)}(x).}

$$

The $n=0$ coordinate is unchanged.

Coordinates with large $|n|$ decay quickly.

Large $|n|$ corresponds to rapid oscillation, so heat flow removes fine
detail first.

**Worked Example: Two temperature modes**

On $(-\pi,\pi)$, suppose

$$

u(x,0)=3+2\cos x+\frac12\cos(4x).

$$

Then

$$

\boxed{
u(x,t)=3+2\mathrm e^{-\kappa t}\cos x
+\frac12\mathrm e^{-16\kappa t}\cos(4x).}

$$

The fourth mode decays much faster than the first.

The constant coordinate $3$ is the mean temperature and remains fixed.

Let

$$

A=-\frac{\partial^2}{\partial x^2}.

$$

Then the heat equation is

$$

u_t=-\kappa Au.

$$

This mirrors the finite-dimensional equation

$$

v'(t)=-\kappa Av(t).

$$

In an eigenbasis of $A$, each coordinate evolves independently:

$$

c_n'(t)=-\kappa\lambda_n c_n(t).

$$

## From a Fourier series to a Fourier transform

Now enlarge the interval:

$$

(-L,L)\longrightarrow\mathbb R.

$$

On $(-L,L)$, the wave numbers are

$$

k_n=\frac{n\pi}{L}.

$$

The spacing between neighbouring wave numbers is

$$

\Delta k=\frac{\pi}{L}.

$$

As $L\to\infty$,

$$

\Delta k\to0.

$$

The discrete frequency label $n$ is replaced by a continuous label $k$.

For a function concentrated well inside $(-L,L)$,

$$

c_n
=\frac1{\sqrt{2L}}\int_{-L}^{L}
f(x)\mathrm e^{-\mathrm i k_nx}\,\mathrm d x.

$$

If

$$

\widehat f(k)
=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}
f(x)\mathrm e^{-\mathrm i kx}\,\mathrm d x,

$$

then heuristically

$$

c_n\approx\sqrt{\Delta k}\,\widehat f(k_n).

$$

Also,

$$

\phi_n^{(L)}(x)
=\sqrt{\frac{\Delta k}{2\pi}}\,
\mathrm e^{\mathrm i k_nx}.

$$

Therefore

$$

\sum_n c_n\phi_n^{(L)}(x)
\approx
\sum_n
\frac{\Delta k}{\sqrt{2\pi}}
\widehat f(k_n)\mathrm e^{\mathrm i k_nx}.

$$

As the spacing tends to zero, the sum suggests the integral

$$

\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}
\widehat f(k)\mathrm e^{\mathrm i kx}\,\mathrm d k.

$$

This passage from $L^2(-L,L)$ to $L^2(\mathbb R)$ is motivational.

It correctly predicts the formulas, but a rigorous proof requires care
about limits, convergence and the fact that plane waves are not in
$L^2(\mathbb R)$.

## Fourier coordinates on $L^2(\mathbb R)$

The position picture uses the continuous family $\delta_x$.

The frequency picture uses the continuous family

$$

\phi_k(x)=\frac1{\sqrt{2\pi}}\mathrm e^{\mathrm i kx},
\qquad k\in\mathbb R.

$$

These plane waves are not ordinary $L^2(\mathbb R)$ vectors.  They are generalised
basis functions.

Heuristically,

$$

\left\langle \phi_k,\phi_q\right\rangle=\delta(k-q).

$$

**Definition: Fourier transform**

The Fourier coefficient in the direction $\phi_k$ is

$$

\boxed{
\widehat f(k)
=\left\langle \phi_k,f\right\rangle
=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}
f(x)\mathrm e^{-\mathrm i kx}\,\mathrm d x.}

$$

The function $k\mapsto\widehat f(k)$ is called the Fourier transform.

The terminology changes, but the object does not.

For a discrete basis:

$$

c_n=\left\langle \phi_n,f\right\rangle
\quad\text{is a Fourier coefficient}.

$$

For a continuous basis:

$$

\widehat f(k)=\left\langle \phi_k,f\right\rangle
\quad\text{is a Fourier coefficient}.

$$

The Fourier transform is simply the continuous list of Fourier
coefficients.

**Definition: Inverse Fourier transform**

The continuous basis expansion is

$$

\boxed{
f(x)=\frac1{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
\widehat f(k)\mathrm e^{\mathrm i kx}\,\mathrm d k.}

$$

Equivalently,

$$

f=\int_{-\infty}^{\infty}\widehat f(k)\phi_k\,\mathrm d k.

$$

Compare:

$$

v=\sum_i c_i e_i,

$$

$$

f=\sum_n c_n\phi_n,

$$

$$

f=\int\widehat f(k)\phi_k\,\mathrm d k.

$$

Only the index set has changed.

The continuous Parseval identity is

$$

\boxed{
\int_{-\infty}^{\infty}|f(x)|^2\,\mathrm d x
=\int_{-\infty}^{\infty}|\widehat f(k)|^2\,\mathrm d k.}

$$

Thus the Fourier transform preserves the length of the vector.

## Differential operators in Fourier coordinates

The plane waves are eigenfunctions of differentiation:

$$

\frac{\,\mathrm d}{\,\mathrm d x}\phi_k=\mathrm i k\phi_k,

$$

$$

-\frac{\,\mathrm d^2}{\,\mathrm d x^2}\phi_k=k^2\phi_k.

$$

Therefore differentiation multiplies Fourier coefficients.

**Proposition: Fourier multipliers**

When boundary terms vanish,

$$

\boxed{\widehat{f'}(k)=\mathrm i k\,\widehat f(k),}

$$

and

$$

\boxed{\widehat{-f''}(k)=k^2\widehat f(k).}

$$

More generally,

$$

\widehat{p(D)f}(k)
=p(\mathrm i k)\widehat f(k),
\qquad
D=\frac{\,\mathrm d}{\,\mathrm d x}.

$$

The finite and continuous calculations are identical:

$$

c_i\longmapsto\lambda_i c_i,

$$

$$

c_n\longmapsto\lambda_n c_n,

$$

$$

\widehat f(k)\longmapsto\lambda(k)\widehat f(k).

$$

## The Gaussian transforms to a Gaussian

**Proposition: Gaussian Fourier transform**

For $a>0$,

$$

f(x)=\mathrm e^{-ax^2}

$$

has Fourier transform

$$

\boxed{
\widehat f(k)
=\frac1{\sqrt{2a}}\mathrm e^{-k^2/(4a)}.}

$$

**Proof**

The standard Gaussian integral gives

$$

\int_{-\infty}^{\infty}
\mathrm e^{-ax^2-\mathrm i kx}\,\mathrm d x
=\sqrt{\frac\pi a}\,
\mathrm e^{-k^2/(4a)}.

$$

Multiply by $1/\sqrt{2\pi}$.

For the unit-area Gaussian

$$

g_\sigma(x)
=\frac1{\sqrt{2\pi\sigma^2}}
\exp\!\left(-\frac{x^2}{2\sigma^2}\right),

$$

one obtains

$$

\boxed{
\widehat g_\sigma(k)
=\frac1{\sqrt{2\pi}}
\mathrm e^{-\sigma^2k^2/2}.}

$$

A narrow Gaussian in position has a broad Fourier transform.

A broad Gaussian in position has a narrow Fourier transform.

## The heat equation on the real line

Consider

$$

u_t=\kappa u_{xx},
\qquad
x\in\mathbb R,
\qquad
u(x,0)=f(x).

$$

For each time $t$, take the Fourier coefficient in the $k$ direction:

$$

\widehat u(k,t)
=\frac1{\sqrt{2\pi}}\int_{\mathbb R}
u(x,t)\mathrm e^{-\mathrm i kx}\,\mathrm d x.

$$

The transform of $u_{xx}$ is

$$

-k^2\widehat u(k,t).

$$

Hence every Fourier coordinate satisfies

$$

\frac{\partial\widehat u}{\partial t}(k,t)
=-\kappa k^2\widehat u(k,t).

$$

This is the continuous version of

$$

c_n'(t)=-\kappa\lambda_n c_n(t).

$$

**Theorem: Heat flow on $\mathbb R$**

The Fourier coefficients evolve by

$$

\boxed{
\widehat u(k,t)
=\mathrm e^{-\kappa k^2t}\widehat f(k).}

$$

After inverse transformation,

$$

\boxed{u(x,t)=(G_t*f)(x),}

$$

where

$$

\boxed{
G_t(x)=\frac1{\sqrt{4\pi\kappa t}}
\exp\!\left(-\frac{x^2}{4\kappa t}\right).}

$$

The Gaussian calculation shows that

$$

\widehat G_t(k)
=\frac1{\sqrt{2\pi}}\mathrm e^{-\kappa k^2t}.

$$

Thus convolution with $G_t$ produces exactly the required multiplier.

The kernel $G_t$ has total area one:

$$

\int_{\mathbb R}G_t(x)\,\mathrm d x=1.

$$

It is a smooth averaging box.

The value $u(x,t)$ is a weighted average of the initial temperature near
$x$.  The averaging width grows like

$$

\sqrt{\kappa t}.

$$

If the initial temperature is the ideal position direction $\delta_0$, then

$$

u(x,t)=G_t(x).

$$

A point of heat spreads into a Gaussian.

**Worked Example: A Gaussian spreads**

If

$$

f(x)=g_\sigma(x),

$$

then

$$

\boxed{
u(x,t)
=g_{\sqrt{\sigma^2+2\kappa t}}(x).}

$$

The total heat remains one.

The variance changes by

$$

\sigma^2\longmapsto\sigma^2+2\kappa t.

$$

## The infinite square well

Quantum wavefunctions are complex function-vectors on $(0,L)$:

$$

\left\langle \phi,\psi\right\rangle
=\int_0^L\overline{\phi(x)}\psi(x)\,\mathrm d x.

$$

**Definition: Infinite potential well**

The potential is zero for $0<x<L$ and infinite outside.

The wavefunction obeys

$$

\psi(0,t)=\psi(L,t)=0.

$$

Inside the well,

$$

\boxed{
H=-\frac{\hbar^2}{2m}\frac{\,\mathrm d^2}{\,\mathrm d x^2}.}

$$

First find a basis adapted to $H$:

$$

H\phi=E\phi.

$$

Thus

$$

-\frac{\hbar^2}{2m}\phi''=E\phi.

$$

Write

$$

k^2=\frac{2mE}{\hbar^2}.

$$

Then

$$

\phi(x)=A\sin(kx)+B\cos(kx).

$$

The boundary condition $\phi(0)=0$ gives

$$

B=0.

$$

The condition $\phi(L)=0$ gives

$$

\sin(kL)=0.

$$

Therefore

$$

k=\frac{n\pi}{L},
\qquad n=1,2,\ldots .

$$

**Theorem: Energy eigenbasis**

The normalised eigenfunctions are

$$

\boxed{
\phi_n(x)
=\sqrt{\frac2L}
\sin\!\left(\frac{n\pi x}{L}\right).}

$$

Their energies are

$$

\boxed{
E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}.}

$$

Moreover,

$$

H\phi_n=E_n\phi_n.

$$

Expand the initial state in the energy basis:

$$

\psi(x,0)
=\sum_{n=1}^{\infty}c_n(0)\phi_n(x),

$$

where

$$

c_n(0)=\left\langle \phi_n,\psi(\,\cdot\,,0)\right\rangle.

$$

At time $t$, allow the coordinates to move:

$$

\psi(x,t)
=\sum_{n=1}^{\infty}c_n(t)\phi_n(x).

$$

Substitute this into

$$

\mathrm i\hbar\psi_t=H\psi.

$$

The left-hand side is

$$

\mathrm i\hbar
\sum_n c_n'(t)\phi_n.

$$

The right-hand side is

$$

\sum_n E_nc_n(t)\phi_n.

$$

Equality of coordinates gives

$$

\mathrm i\hbar c_n'(t)=E_nc_n(t).

$$

**Theorem: Time evolution in the well**

Each energy coordinate evolves independently:

$$

\boxed{
c_n(t)
=\mathrm e^{-\mathrm iE_nt/\hbar}c_n(0).}

$$

Therefore

$$

\boxed{
\psi(x,t)
=\sum_{n=1}^{\infty}
c_n(0)\mathrm e^{-\mathrm iE_nt/\hbar}\phi_n(x).}

$$

The Hamiltonian multiplies the $n$th coordinate by $E_n$.

Time evolution multiplies it by a phase:

$$

\mathrm e^{-\mathrm iE_nt/\hbar}.

$$

Its magnitude is one, so

$$

|c_n(t)|=|c_n(0)|.

$$

**Worked Example: Two energy levels**

Suppose

$$

\psi(x,0)
=\frac1{\sqrt2}
\bigl(\phi_1(x)+\phi_2(x)\bigr).

$$

Then

$$

\begin{aligned}
\psi(x,t)
=\frac1{\sqrt2}\bigl(
&\mathrm e^{-\mathrm iE_1t/\hbar}\phi_1(x)\\
&+\mathrm e^{-\mathrm iE_2t/\hbar}\phi_2(x)
\bigr).
\end{aligned}

$$

The two coefficient magnitudes remain $1/\sqrt2$.

Only their phases change.

The relative phase is

$$

\frac{(E_2-E_1)t}{\hbar}.

$$

## Heat flow and quantum motion compared

Both equations become scalar equations in an eigenbasis.

{@{}>{\bfseries}p{.23\textwidth}XX@{}}
\toprule
& Heat equation & Schrödinger equation\\
\midrule
Equation
& $u_t=-Au$
& $\mathrm i\hbar\psi_t=H\psi$\\
Coordinate
& $c_n(t)$
& $c_n(t)$\\
Evolution
& $\mathrm e^{-\lambda_nt}c_n(0)$
& $\mathrm e^{-\mathrm iE_nt/\hbar}c_n(0)$\\
Effect
& Magnitudes decay
& Magnitudes remain fixed\\
Meaning
& Smoothing
& Phase rotation\\
\bottomrule

\centering

{@{}>{\raggedright\arraybackslash}X
>{\centering\arraybackslash}p{.20\linewidth}
>{\centering\arraybackslash}p{.29\linewidth}@{}}
**Basis direction** & **Coordinate** & **Multiplier**\\
\midrule
$q_i$ & $c_i$ & $\lambda_i$\\
$\mathrm e^{\mathrm i n\pi x/L}$ & $c_n$ &
$\mathrm i n\pi/L$ or $(n\pi/L)^2$\\
$\mathrm e^{\mathrm i kx}$ & $\widehat f(k)$ &
$\mathrm i k$ or $k^2$\\
$\sin(n\pi x/L)$ & $c_n$ & $E_n$

The repeated method is:

$$

\boxed{
\begin{gathered}
\text{choose a basis adapted to the operator},\\
\text{take coordinates},\\
\text{multiply each coordinate},\\
\text{reconstruct the vector}.
\end{gathered}}

$$

# Synthesis

## The Three-Part Dictionary

## One idea, three index sets

The central message can be compressed into two lines:

$$

\boxed{\text{finite indices}
\ \longrightarrow\ \text{countable indices}
\ \longrightarrow\ \text{continuous indices}},

$$

$$

\boxed{\sum_i\ \longrightarrow\ \sum_n
\longrightarrow\ \sum_x\;(\text{heuristic})
\rightsquigarrow\ \int\,\mathrm d x}.

$$

The table follows the common section numbering.

| Concept | Finite vectors: $\mathbb R^N$ | Sequences: $\ell^2$ | Functions: $L^2(I)$ |
| --- | --- | --- | --- |
| Underlying vector | $v=(v_1,\ldots,v_N)$ | $a=(a_1,a_2,\ldots)$ | $f=(f_x)_{x\in I}$ initially; then $f(x)$ |
| Index set | $i=1,\ldots,N$ | $n\in\mathbb N$ | $x\in I\subseteq\mathbb R$ |
| Natural space | $\mathbb R^N$ | $\ell^2=\{a:\sum_n a_n^2<\infty\}$ | $L^2(I)=\{f:\int_I|f|^2<\infty\}$ modulo equality almost everywhere |
| Coordinate sum | $\sum_{i=1}^{N}$ | $\sum_{n=1}^{\infty}$ | $\sum_x$ only as motivation; rigorously $\int_I\,\mathrm d x$ |
| Linear combination | $\sum_{j=1}^{k}\alpha_jv_j$ | Finite algebraic combinations; limits add infinite expansions | Finite algebraic combinations; limits produce function expansions |
| Standard or useful basis | Standard vectors $e_i$ | Standard sequences $e_n$ | Problem-adapted basis functions, e.g. $\sqrt{2/\pi}\sin(nx)$ on $(0,\pi)$ |
| Basis meaning | Finite algebraic basis | Complete orthonormal system with norm-convergent series | Complete orthonormal system with $L^2$-convergent series |
| Decomposition | $v=\sum_i v_ie_i$ | $a=\sum_n a_ne_n$ in $\ell^2$ | $f=\sum_n c_n\phi_n$ in $L^2$, $c_n=\left\langle \phi_n,f\right\rangle$ |
| New convergence issue | None: sums are finite | Series and truncation tails must converge | $L^2$ convergence need not imply pointwise convergence |
| Linear operator | $A:\mathbb R^N\to\mathbb R^N$ | Bounded $A:\ell^2\to\ell^2$, or unbounded $A$ with a domain | Multiplication, differentiation and integral operators; domains and boundary conditions matter |
| Component action | $(Av)_i=\sum_jA_{ij}v_j$ | $(Aa)_n=\sum_mA_{nm}a_m$ | $(Af)_x=\sum_y(A_{xy}f_y)\rightsquigarrow \int_IA(x,y)f(y)\,\mathrm d y$ |
| Matrix or kernel | Finite matrix $(A_{ij})$ | Infinite matrix $(A_{nm})$ when its series defines an operator | Kernel $A(x,y)$, a continuously indexed matrix |
| Inner product | $\left\langle u,v\right\rangle=\sum_i u_iv_i$ | $\left\langle a,b\right\rangle=\sum_n a_nb_n$ | $\sum_x(f_xg_x)\rightsquigarrow\left\langle f,g\right\rangle=\int_If(x)g(x)\,\mathrm d x$ |
| $p$-norm | $\left\lVert v\right\rVert_p=(\sum_i|v_i|^p)^{1/p}$ | $\left\lVert a\right\rVert_p=(\sum_n|a_n|^p)^{1/p}$ | $\left\lVert f\right\rVert_p=(\int_I|f|^p)^{1/p}$ |
| Norm equivalence | All $p$-norms equivalent on fixed $\mathbb R^N$; $C^{-1}\left\lVert v\right\rVert_p\le\left\lVert v\right\rVert_q\le C\left\lVert v\right\rVert_p$ | Fails: block-vector norm ratios grow without bound; $\ell^p$ spaces differ | Fails: concentrating spikes have incompatible norm ratios; $L^p$ spaces differ |
| Normalisation | $\widehat v=v/\left\lVert v\right\rVert_2$ | $\widehat a=a/\left\lVert a\right\rVert_2$ | $\widehat f=f/\left\lVert f\right\rVert_2$ |
| Orthogonality | $\sum_i u_iv_i=0$ | $\sum_na_nb_n=0$ | $\int_If(x)g(x)\,\mathrm d x=0$ |
| Projection onto a unit basis element | $P_iv=\left\langle e_i,v\right\ranglee_i$ | $P_na=\left\langle e_n,a\right\ranglee_n$ | $P_\phi f=\left\langle \phi,f\right\rangle\phi$ |
| Projection kernel | $P_i=e_ie_i^T$ | $(P_n)_{jk}=\delta_{jn}\delta_{kn}$ | $P_\phi(x,y)=\phi(x)\phi(y)$ |
| Resolution of identity | $I=\sum_{i=1}^{N}P_i$ | $I=\sum_{n=1}^{\infty}P_n$ strongly | $I=\sum_nP_n$ in a complete basis; formally $I(x,y)=\delta(x-y)$ |
| Parseval | $\left\lVert v\right\rVert_2^2=\sum_i|\left\langle e_i,v\right\rangle|^2$ | $\left\lVert a\right\rVert_2^2=\sum_n|\left\langle e_n,a\right\rangle|^2$ | $\left\lVert f\right\rVert_2^2=\sum_n|\left\langle \phi_n,f\right\rangle|^2$ |
| Eigen-equation | $Av=\lambda v$ | $Aa=\lambda a$ | $Af=\lambda f$ |
| Eigen-object | Eigenvector | Eigenvector (sequence) | Eigenfunction |
| Eigenspace and degeneracy | $E_\lambda=\operatorname{ker}(A-\lambda I)$; finite dimension | Eigenspace may have finite or infinite dimension | Boundary conditions influence eigenspaces; symmetry can create degeneracy |
| Adjoint | $A^*=A^T$ in a real orthonormal basis | $\left\langle a,Ab\right\rangle=\left\langle A^*a,b\right\rangle$; domains matter if unbounded | $\left\langle f,Ag\right\rangle=\left\langle A^*f,g\right\rangle$; transpose the kernel or integrate by parts |
| Self-adjoint | Real symmetric matrix | $A=A^*$ with matching domains | $A=A^*$ with boundary conditions included in the domain |
| Eigenvalue consequence | Self-adjoint eigenvalues are real | Same | Same |
| Eigenvector consequence | Distinct eigenvalues give orthogonal eigenvectors | Same, when eigenvectors exist | Distinct eigenvalues give orthogonal eigenfunctions |
| Spectral theorem | Every self-adjoint operator has an orthonormal eigenbasis | Compact self-adjoint operators have a discrete eigenbasis; general operators may require spectral measures | Compact symmetric kernels often have eigenfunction bases; multiplication and differential operators may have continuous spectrum |
| Spectral decomposition | $A=\sum_\lambda\lambda P_\lambda$ | $A=\sum_n\lambda_nP_n$ in the discrete case; generally $A=\int\lambda\,\mathrm d P(\lambda)$ | Discrete eigenfunction sums or the spectral integral $A=\int\lambda\,\mathrm d P(\lambda)$ |
| Characteristic new issue | Basis choice, but no analytical obstruction | Convergence, completeness, boundedness and domains | Integration, almost-everywhere equality, boundary conditions and continuous spectrum |

## A final worked bridge: one-dimensional projection

Choose a normalised direction in each setting:

$$

e_i\in\mathbb R^N,
\qquad e_n\in\ell^2,
\qquad \phi\in L^2(I).

$$

Projection is always ``overlap times direction'':

$$

\begin{aligned}
P_iv
&=\left(\sum_{j=1}^{N}(e_i)_jv_j\right)e_i,
$$
1mm]
P_na
&=\left(\sum_{m=1}^{\infty}(e_n)_ma_m\right)e_n,
$$
1mm]
P_\phi f
&=\left(\int_I\phi(y)f(y)\,\mathrm d y\right)\phi.
\end{aligned}

$$

In kernel notation the last line is

$$

(P_\phi f)(x)=\int_I\underbrace{\phi(x)\phi(y)}_{P_\phi(x,y)}f(y)\,\mathrm d y.

$$

Only the index set, and hence the summation rule, has changed.

\centering
\sffamily\bfseries\large
You have already seen the idea.  Only the index set has changed.

## Closing perspective

A function is a vector.  A Fourier coefficient is a coordinate.  An integral
kernel is a matrix.  A modal expansion is a spectral decomposition.

In infinite dimensions, ask:

- In which norm does a series or approximation converge?
- Is the space complete?
- Is the operator bounded, and if not, what is its domain?
- Which boundary conditions make the operator self-adjoint?
- Is the spectrum discrete, continuous, or a mixture of both?

These are the basic questions of functional analysis.

\appendix

## Deferred Proof

## Equivalence of $p$-norms on $\mathbb R^N$

**Proof: Proof of Theorem Section thm:finite-norm-equivalence**

It is enough to assume $1\le p\le q\le\infty$.

First,

$$

\norm v_q\le\norm v_p.

$$

For finite $q$, H\"older's inequality gives

$$

\sum_{i=1}^{N}|v_i|^p
\le
\left(\sum_{i=1}^{N}|v_i|^q\right)^{p/q}
N^{1-p/q}.

$$

Hence

$$

\norm v_p\le N^{1/p-1/q}\norm v_q.

$$

When $q=\infty$,

$$

\norm v_p^p
\le N\norm v_\infty^p.

$$

Thus, for fixed $N$, both norms bound one another by constants independent of
$v$.  Interchanging $p$ and $q$ covers every pair.
