# Solving the Schrödinger Equation

> Recovered and sanitised reading edition. The PDF and HTML editions preserve the diagrams and print layout.

This discussion-first volume contains thirteen worked solution demonstrations, followed by coordinate-system and eigenbasis appendices.

## The thirteen solution demonstrations

*Worked-model index*

There is no single universal list, but these are thirteen solution patterns commonly encountered by the middle of an undergraduate quantum-mechanics sequence.

1. **One-dimensional infinite well.** Boundary quantisation and normalisation.

2. **Potential step with $E>V_0$.** Matching and flux transmission.

3. **Potential step with $E<V_0$.** Evanescent penetration and total reflection.

4. **Finite barrier with $E<V_0$.** Quantum tunnelling.

5. **Finite barrier with $E>V_0$.** Resonant transmission.

6. **Semi-infinite finite well.** Transcendental energy conditions.

7. **One-dimensional harmonic oscillator.** Asymptotics and power-series termination.

8. **Harmonic oscillator by ladder operators.** Factorisation and algebraic spectrum.

9. **Three-dimensional rectangular box.** Cartesian separation and product states.

10. **Three-dimensional harmonic oscillator.** Separable Hamiltonians and degeneracy.

11. **General central potential.** Radial-angular separation and spherical harmonics.

12. **Spherical infinite well.** Spherical Bessel functions and radial boundary conditions.

13. **Hydrogen-like atom.** Endpoint behaviour, series termination, and the bound spectrum.

#### What this list is for

The point is not to memorise thirteen answers. It is to recognise a small number of recurring moves: separation, admissible asymptotics, boundary matching, normalisation, flux ratios, series termination, and operator factorisation.

## One method, repeated

*How to use these notes*

Every exact solution in this guide follows the same six moves.

#### What “solving the Schrödinger equation” means

It does not mean finding just any function that satisfies a differential equation.

We must find functions that satisfy the differential equation *and* the physical conditions of the problem.

Those physical conditions are usually what select the allowed energies.

1. **Write the potential.** Divide space into regions if the potential changes abruptly.

2. **Write the TISE.** Use the correct equation in each region.

3. **Choose the admissible form.** Reject any piece that diverges or violates the physical direction of travel.

4. **Apply boundary conditions.** These are what quantise bound-state energies.

5. **Normalise or compare fluxes.** Bound states are normalised; scattering states use amplitude and current ratios.

6. **Read the physics.** Identify allowed energies, reflection, transmission, degeneracy and limiting behaviour.

## From the TDSE to the TISE

*Foundation*

When the potential has no explicit time dependence, the time dependence separates completely.

#### What is assumed here?

- **Starting equation:** $$i\hbar\frac{\partial\psi}{\partial t}=\left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)\right]\psi.$$

- **Assumption:** The potential $V$ depends on position but not explicitly on time.

- **Aim:** Separate the time dependence and obtain an ordinary differential equation for the spatial part.

#### 1. Start from the time-dependent equation

$$ i\hbar\frac{\partial\psi}{\partial t}=\left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)\right]\psi. $$

#### 2. Assume a separated solution

$$ \psi(x,t)=T(t)\,\phi(x). $$

This is an ansatz: we first look for states whose time and position dependence can be written as a product.

Later, linear combinations of these separated states describe more general wavefunctions.

Substitute and divide by $T\phi$:

$$ i\hbar\frac{1}{T}\frac{dT}{dt} =-\frac{\hbar^2}{2m}\frac{1}{\phi}\frac{d^2\phi}{dx^2}+V(x). $$

#### 3. Separate the independent variables

The left side depends only on $t$.

The right side depends only on $x$.

Therefore both sides must equal the same constant, called $E$.

Hold $x$ fixed and vary $t$. The right side cannot change, so the left side cannot change either.

Now hold $t$ fixed and vary $x$. The same argument shows the right side is constant.

The constant has dimensions of energy, so we name it $E$.

#### Time equation

$$ i\hbar\frac{dT}{dt}=ET $$

$$ T(t)=e^{-iEt/\hbar}. $$

#### Spatial equation

$$ -\frac{\hbar^2}{2m}\frac{d^2\phi}{dx^2}+V\phi=E\phi. $$

This is the time-independent Schrödinger equation.

#### Stationary state

$$ \psi(x,t)=\phi(x)e^{-iEt/\hbar},\qquad |\psi(x,t)|^2=|\phi(x)|^2. $$

The phase changes with time, but the probability density does not.

#### How a general state is built

If the spatial eigenfunctions form an orthonormal basis, an initial wavefunction can be expanded as

$$\psi(x,0)=\sum_n c_n\phi_n(x),\qquad c_n=\int\phi_n^*(x)\psi(x,0)\,dx.$$

Each basis component then acquires its own phase:

$$\psi(x,t)=\sum_n c_n\phi_n(x)e^{-iE_nt/\hbar}.$$

## Model 1: Particle in a one-dimensional infinite well

This is the cleanest example of boundary conditions turning a continuous parameter into discrete energies.

#### Problem specification

- **Equation:** $$-\frac{\hbar^2}{2m}\frac{d^2\phi}{dx^2}+V(x)\phi=E\phi.$$

- **Potential:** $$V(x)=0\ \text{for }0\le x\le L,\qquad V(x)=\infty\ \text{otherwise}.$$

- **Boundary conditions:** $\phi(0)=0$, $\phi(L)=0$, and $\int_0^L|\phi|^2\,dx=1$.

- **Find:** The allowed wavefunctions $\phi_n(x)$ and energies $E_n$.

> Diagram preserved in the PDF and HTML editions.

#### 1. Define the potential

$$ V(x)=\begin{cases}0,&0\le x\le L,\\[2pt]\infty,&\text{otherwise.}\end{cases} $$

Finite energy requires $\phi=0$ outside the well.

Continuity therefore gives $\phi(0)=\phi(L)=0$.

#### 2. Solve inside the well

$$ -\frac{\hbar^2}{2m}\phi''=E\phi \quad\Longrightarrow\quad \phi''+k^2\phi=0,\qquad k^2=\frac{2mE}{\hbar^2}. $$

$$ \phi(x)=A\sin kx+B\cos kx. $$

This is the complete two-parameter solution of a second-order linear differential equation.

We need two constants because two independent boundary conditions will be imposed.

#### 3. Apply both walls

$$ \phi(0)=0\Rightarrow B=0, \qquad \phi(L)=0\Rightarrow A\sin(kL)=0. $$

A non-zero state needs $\sin(kL)=0$.

$$ kL=n\pi,\qquad k_n=\frac{n\pi}{L},\qquad n=1,2,3,\ldots $$

The choice $n=0$ gives $\phi=0$ everywhere, which cannot be normalised.

Negative $n$ changes only the overall sign of the sine function, so it does not produce a new physical state.

#### 4. Normalise

$$ 1=\int_0^L |A|^2\sin^2\!\left(\frac{n\pi x}{L}\right)dx=|A|^2\frac{L}{2}. $$

$$ A=\sqrt{\frac{2}{L}}. $$

An overall complex phase would not change any probability. We choose $A$ real and positive.

#### Allowed stationary states

$$ \phi_n(x)=\sqrt{\frac{2}{L}}\sin\!\left(\frac{n\pi x}{L}\right), \qquad E_n=\frac{\hbar^2\pi^2 n^2}{2mL^2}. $$

The walls allow only an integer number of half-wavelengths inside the well.

The full stationary state is $\psi_n(x,t)=\phi_n(x)e^{-iE_nt/\hbar}$.

#### Checks before moving on

- **Dimensions:** $E_n$ has units $\hbar^2/(mL^2)$, which are energy units.

- **Boundary values:** The sine vanishes at $x=0$ and $x=L$.

- **Orthogonality:** $\int_0^L\phi_m^*\phi_n\,dx=\delta_{mn}$.

- **Large box:** As $L$ grows, adjacent energy levels become closer together.

## Model 2: Potential step with $E>V_0$

A classically allowed step still reflects part of a quantum wave.

#### Problem specification

- **Equation:** $$-\frac{\hbar^2}{2m}\phi''+V(x)\phi=E\phi.$$

- **Potential:** $$V(x)=\begin{cases}0,&x<0,\\V_0,&x>0,\end{cases}\qquad E>V_0.$$

- **Physical conditions:** A wave is incident from the left. There is no wave incident from $+\infty$. Both $\phi$ and $\phi'$ are continuous at $x=0$.

- **Find:** The reflection probability $R$ and transmission probability $T$.

> Diagram preserved in the PDF and HTML editions.

#### 1. Write one solution in each region

$$ V(x)=\begin{cases}0,&x<0,\\V_0,&x>0,\end{cases} \qquad k_1=\frac{\sqrt{2mE}}{\hbar}, \quad k_2=\frac{\sqrt{2m(E-V_0)}}{\hbar}. $$

$$ \phi_1=Ae^{ik_1x}+Be^{-ik_1x}, \qquad \phi_2=Ce^{ik_2x}. $$

$A$ is incident, $B$ reflected, and $C$ transmitted.

There is no incoming wave from $+\infty$.

#### Why do we match both $\phi$ and $\phi'$?

Integrate the TISE across a very small interval from $-\epsilon$ to $+\epsilon$ around the finite step:

$$-\frac{\hbar^2}{2m}\left[\phi'(+\epsilon)-\phi'(-\epsilon)\right]+\int_{-\epsilon}^{+\epsilon}(V-E)\phi\,dx=0.$$

For a finite jump in $V$, the integral tends to zero as $\epsilon\to0$.

Therefore $\phi'$ is continuous. The wavefunction itself must also be continuous; otherwise its derivatives would contain singular delta-function terms not present in this potential.

#### 2. Match the wave and its derivative at $x=0$

$$ A+B=C,\qquad k_1(A-B)=k_2C. $$

Insert $C=A+B$ into the second equation:

$$ (k_1-k_2)A=(k_1+k_2)B. $$

$$ \frac{B}{A}=\frac{k_1-k_2}{k_1+k_2},\qquad \frac{C}{A}=\frac{2k_1}{k_1+k_2}. $$

#### 3. Convert amplitudes into flux probabilities

Probability current for a plane wave is proportional to $k\,|\text{amplitude}|^2$.

$$ R=\frac{|B|^2}{|A|^2}, \qquad T=\frac{k_2|C|^2}{k_1|A|^2}. $$

More explicitly, the one-dimensional probability current is

$$j=\frac{\hbar}{2mi}\left(\psi^*\frac{\partial\psi}{\partial x}-\psi\frac{\partial\psi^*}{\partial x}\right).$$

For $\psi=Ae^{i(kx-Et/\hbar)}$, this becomes $j=(\hbar k/m)|A|^2$.

That extra factor of $k$ is why the transmission probability is not simply $|C/A|^2$ when the wavenumbers differ.

#### Reflection and transmission

$$ R=\left(\frac{k_1-k_2}{k_1+k_2}\right)^2, \qquad T=\frac{4k_1k_2}{(k_1+k_2)^2}, \qquad R+T=1. $$

Even though the step is classically allowed, $R\ne0$ whenever $k_1\ne k_2$.

#### Checks

If $V_0\to0$, then $k_2\to k_1$, so $R\to0$ and $T\to1$.

The identity $R+T=1$ confirms conservation of probability.

## Model 3: Potential step with $E<V_0$

The wave enters the forbidden region, but no probability flux travels to infinity.

#### Problem specification

- **Equation:** $$-\frac{\hbar^2}{2m}\phi''+V(x)\phi=E\phi.$$

- **Potential:** $$V(x)=\begin{cases}0,&x<0,\\V_0,&x>0,\end{cases}\qquad 0<E<V_0.$$

- **Physical conditions:** A wave is incident from the left. The wavefunction must remain bounded as $x\to+\infty$. Match $\phi$ and $\phi'$ at $x=0$.

- **Find:** The reflected amplitude, the evanescent tail, and the penetration length.

#### 1. The right-hand wavenumber becomes imaginary

$$ \kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}, \qquad \phi_1=Ae^{ikx}+Be^{-ikx}. $$

$$ \phi_2=Ce^{-\kappa x}+De^{+\kappa x}. $$

The term $De^{+\kappa x}$ diverges as $x\to+\infty$.

Physical boundedness forces $D=0$.

This is not an arbitrary change of solution type. In Region 2,

$$q^2=\frac{2m(E-V_0)}{\hbar^2}=-\kappa^2,$$

so $e^{\pm iqx}=e^{\mp\kappa x}$.

#### 2. Match at the step

$$ A+B=C,\qquad ik(A-B)=-\kappa C. $$

Eliminate $C$:

$$ ik(A-B)=-\kappa(A+B). $$

$$ \frac{B}{A}=\frac{k-i\kappa}{k+i\kappa}, \qquad \frac{C}{A}=\frac{2k}{k+i\kappa}. $$

#### What the result means

$$ R=\left|\frac{k-i\kappa}{k+i\kappa}\right|^2=1, \qquad \phi_2(x)=Ce^{-\kappa x}. $$

The particle is totally reflected.

Nevertheless, $|\phi_2|^2\ne0$ close to the boundary.

The penetration depth is of order $1/\kappa$.

#### Why the tail carries no transmitted current

For a single real exponential $\phi=Ce^{-\kappa x}$, the two terms in the current cancel:

$$j=\frac{\hbar}{2mi}(\phi^*\phi'-\phi\phi'^*)=0.$$

There is probability density inside the classically forbidden region, but there is no steady flux travelling to $+infty$.

## Model 4: Finite barrier with $E<V_0$: tunnelling

A forbidden region of finite width can be crossed because the evanescent wave reaches the far boundary.

#### Problem specification

- **Equation:** $$-\frac{\hbar^2}{2m}\phi''+V(x)\phi=E\phi.$$

- **Potential:** $$V(x)=\begin{cases}V_0,&0\le x\le L,\\0,&x<0\ \text{or}\ x>L,\end{cases}\qquad 0<E<V_0.$$

- **Physical conditions:** Incident wave from the left; no incoming wave from the right; $\phi$ and $\phi'$ continuous at both $x=0$ and $x=L$.

- **Find:** The exact transmission probability and its wide-barrier approximation.

> Diagram preserved in the PDF and HTML editions.

#### 1. Write all admissible pieces

$$ k=\frac{\sqrt{2mE}}{\hbar}, \qquad \kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}. $$

$$ \phi_I=Ae^{ikx}+Be^{-ikx},\quad \phi_{II}=Ce^{\kappa x}+De^{-\kappa x},\quad \phi_{III}=Fe^{ikx}. $$

Do not discard $Ce^{\kappa x}$ inside the barrier.

The barrier occupies only $0\le x\le L$, so this term never reaches $x=+\infty$ and does not diverge on its finite domain.

Both internal exponentials are needed to satisfy conditions at two separate faces.

#### 2. Match at both faces

$$ \begin{aligned} A+B &= C+D,\\ ik(A-B) &= \kappa(C-D),\\ Ce^{\kappa L}+De^{-\kappa L} &= Fe^{ikL},\\ \kappa\!\left(Ce^{\kappa L}-De^{-\kappa L}\right) &= ikFe^{ikL}. \end{aligned} $$

#### 3. Eliminate the internal amplitudes

The two equations at $x=L$ first express $C$ and $D$ in terms of $F$.

$$ C=\frac{F}{2}\left(1+\frac{ik}{\kappa}\right)e^{(ik-\kappa)L}, \qquad D=\frac{F}{2}\left(1-\frac{ik}{\kappa}\right)e^{(ik+\kappa)L}. $$

Insert these into the two equations at $x=0$, then eliminate $B$.

$$ \frac{A}{F}=e^{ikL}\left[ \cosh(\kappa L)+i\frac{\kappa^2-k^2}{2k\kappa}\sinh(\kappa L) \right]. $$

#### 4. Take the modulus squared

The wavenumber is the same on both sides, so $T=|F/A|^2$.

$$ T=\left[1+\frac{(k^2+\kappa^2)^2}{4k^2\kappa^2}\sinh^2(\kappa L)\right]^{-1}. $$

$$ \boxed{T=\left[1+\frac{V_0^2}{4E(V_0-E)}\sinh^2(\kappa L)\right]^{-1}}. $$

#### Wide or high barrier

When $\kappa L\gg1$, $\sinh(\kappa L)\simeq \tfrac12e^{\kappa L}$.

$$ T\simeq \frac{16E(V_0-E)}{V_0^2}e^{-2\kappa L}. $$

The exponential is the dominant dependence on width, mass and barrier height.

#### Read the exponent before the prefactor

The factor $e^{-2\kappa L}$ explains most of the physics.

$$2\kappa L=\frac{2L}{\hbar}\sqrt{2m(V_0-E)}.$$

A wider barrier, a heavier particle, or a larger energy deficit all suppress tunnelling exponentially.

As $L\to\infty$, the result approaches the semi-infinite step: $T\to0$.

## Model 5: Finite barrier with $E>V_0$

Inside the barrier the solution oscillates. Multiple internal reflections can interfere constructively.

#### Problem specification

- **Equation:** $$-\frac{\hbar^2}{2m}\phi''+V(x)\phi=E\phi.$$

- **Potential:** $$V(x)=\begin{cases}V_0,&0\le x\le L,\\0,&x<0\ \text{or}\ x>L,\end{cases}\qquad E>V_0.$$

- **Physical conditions:** Incident wave from the left; no incoming wave from the right; match $\phi$ and $\phi'$ at both faces.

- **Find:** The transmission probability and the condition for perfect transmission.

#### 1. Replace decay by oscillation

$$ k=\frac{\sqrt{2mE}}{\hbar}, \qquad q=\frac{\sqrt{2m(E-V_0)}}{\hbar}. $$

$$ \phi_I=Ae^{ikx}+Be^{-ikx},\quad \phi_{II}=Ce^{iqx}+De^{-iqx},\quad \phi_{III}=Fe^{ikx}. $$

#### 2. Use the same four matching equations

The algebra is the tunnelling calculation with $\kappa\mapsto iq$.

$$ \frac{A}{F}=e^{ikL}\left[ \cos(qL)-i\frac{k^2+q^2}{2kq}\sin(qL) \right]. $$

This replacement turns $\cosh(\kappa L)$ into $\cos(qL)$ and $\sinh(\kappa L)$ into $i\sin(qL)$.

The result therefore oscillates with the barrier width instead of decaying monotonically.

#### Transmission probability

$$ T=\left[ \cos^2(qL)+\frac14\left(\frac{k}{q}+\frac{q}{k}\right)^2\sin^2(qL) \right]^{-1}. $$

$$ T=\left[1+\frac{V_0^2}{4E(E-V_0)}\sin^2(qL)\right]^{-1}. $$

#### Perfect-transmission resonances

$$ qL=n\pi\quad\Longrightarrow\quad T=1. $$

An integer number of half-wavelengths fits inside the barrier.

The reflected contributions cancel.

#### Wave interpretation

At $qL=n\pi$, the barrier contains an integer number of half-wavelengths.

Successive reflected waves return with phases that make the net reflected amplitude zero.

This is the same interference mechanism that produces resonances in optical cavities.

## Model 6: Semi-infinite finite well

One hard wall and one finite wall produce bound states whose energies must be found graphically or numerically.

#### Problem specification

- **Equation:** $$-\frac{\hbar^2}{2m}\phi''+V(x)\phi=E\phi.$$

- **Potential:** $$V(x)=\begin{cases}\infty,&x<0,\\0,&0\le x\le L,\\V_0,&x>L,\end{cases}\qquad E<V_0.$$

- **Boundary conditions:** $\phi(0)=0$; $\phi$ remains bounded as $x\to\infty$; $\phi,\phi'$ are continuous at $x=L$.

- **Find:** The transcendental equation that selects the bound-state energies.

> Diagram preserved in the PDF and HTML editions.

#### 1. Define the potential and bound-state parameters

$$ V(x)=\begin{cases} \infty,&x<0,\\0,&0\le x\le L,\\V_0,&x>L, \end{cases} \qquad E<V_0. $$

$$ k^2=\frac{2mE}{\hbar^2},\qquad \kappa^2=\frac{2m(V_0-E)}{\hbar^2}. $$

#### 2. Choose admissible forms

The hard wall gives $\phi(0)=0$.

The far-right solution must decay.

$$ \phi(x)=\begin{cases} A\sin(kx),&0\le x\le L,\\[2pt] \alpha e^{-\kappa(x-L)},&x>L. \end{cases} $$

#### 3. Match at the finite wall

$$ A\sin(kL)=\alpha,\qquad Ak\cos(kL)=-\kappa\alpha. $$

Divide the derivative equation by the wavefunction equation:

$$ k\cot(kL)=-\kappa \qquad\Longleftrightarrow\qquad \tan(kL)=-\frac{k}{\kappa}. $$

#### Energy condition

$$ k^2+\kappa^2=\frac{2mV_0}{\hbar^2}, \qquad \tan(kL)=-\frac{k}{\sqrt{2mV_0/\hbar^2-k^2}}. $$

The intersections of the two sides give the allowed $k$, hence $E=\hbar^2k^2/(2m)$.

The wave leaks into the finite wall, so each energy lies below the corresponding infinite-well energy.

#### How to obtain the energies in practice

Define $z=kL$ and $z_0=L\sqrt{2mV_0}/\hbar$.

Because $k^2+\kappa^2=2mV_0/\hbar^2$, we have $\kappa L=\sqrt{z_0^2-z^2}$.

The energy condition becomes

$$\tan z=-\frac{z}{\sqrt{z_0^2-z^2}},\qquad 0<z<z_0.$$

Plot both sides against $z$. Each intersection gives an allowed $z$, then $E=\hbar^2z^2/(2mL^2)$.

A finite well supports only finitely many intersections and therefore finitely many bound states.

## Model 7: One-dimensional harmonic oscillator

Here the potential varies everywhere. Normalisability replaces a hard-wall boundary condition.

#### Problem specification

- **Equation:** $$-\frac{\hbar^2}{2m}\frac{d^2\phi}{dx^2}+\frac12m\omega^2x^2\phi=E\phi.$$

- **Potential:** $$V(x)=\frac12m\omega^2x^2,\qquad -\infty<x<\infty.$$

- **Boundary conditions:** $\phi$ and $\phi'$ are continuous; $\phi(x)$ remains finite; $\phi(x)\to0$ as $|x|\to\infty$; $\int_{-\infty}^{\infty}|\phi|^2\,dx=1$.

- **Find:** The discrete energies, the normalised eigenfunctions, and the basis expansion of a general state.

> Diagram preserved in the PDF and HTML editions.

#### 1. Make the equation dimensionless

$$ -\frac{\hbar^2}{2m}\frac{d^2\phi}{dx^2}+\frac12m\omega^2x^2\phi=E\phi. $$

Define

$$ y=\sqrt{\frac{m\omega}{\hbar}}x, \qquad \alpha=\frac{2E}{\hbar\omega}. $$

The chain rule gives

$$\frac{d}{dx}=\sqrt{\frac{m\omega}{\hbar}}\frac{d}{dy},\qquad \frac{d^2}{dx^2}=\frac{m\omega}{\hbar}\frac{d^2}{dy^2}.$$

Substituting these expressions and multiplying through by $2/(\hbar\omega)$ removes all physical constants from the differential equation.

Then

$$ \frac{d^2\phi}{dy^2}+(\alpha-y^2)\phi=0. $$

#### 2. Find the large-$|y|$ behaviour

For $|y|$ large, $y^2\gg\alpha$.

$$ \phi''-y^2\phi\simeq0. $$

Try a Gaussian form $\phi\sim e^{sy^2/2}$.

$$\phi''=(s+s^2y^2)\phi.$$

At large $|y|$, the $y^2$ terms dominate, so $s^2=1$.

The choice $s=+1$ gives $e^{+y^2/2}$ and cannot be normalised.

The admissible behaviour is therefore the decaying Gaussian $e^{-y^2/2}$.

$$ \phi(y)=H(y)e^{-y^2/2}. $$

The growing alternative is rejected because it cannot be normalised.

#### 3. Derive the equation for $H$

$$ \phi'=e^{-y^2/2}(H'-yH), \qquad \phi''=e^{-y^2/2}\!\left[H''-2yH'+(y^2-1)H\right]. $$

Substitute into the dimensionless equation and cancel the Gaussian:

$$ H''-2yH'+(\alpha-1)H=0. $$

#### 4. Use a power series

#### Why a power series?

The equation for $H$ has coefficients that are polynomials in $y$ and are analytic everywhere.

There is no remaining singular point and no elementary function is obvious.

For an analytic linear differential equation, a power series is the systematic way to construct the solution: substitute a general series and let the equation determine every coefficient.

The calculation will also reveal, rather than assume, why only special energies are allowed.

$$ H(y)=\sum_{p=0}^{\infty}a_p y^p. $$

$$ H'=\sum_{p=0}^{\infty}p a_p y^{p-1}, \qquad H''=\sum_{p=0}^{\infty}(p+2)(p+1)a_{p+2}y^p. $$

The second derivative has been re-indexed so that every sum contains the same power $y^p$.

Substitution gives

$$\sum_{p=0}^{\infty}\left[(p+2)(p+1)a_{p+2}+(\alpha-1-2p)a_p\right]y^p=0.$$

A power series can vanish for every $y$ only if the coefficient of each power vanishes separately.

Matching the coefficient of every $y^p$ gives

$$ a_{p+2}=\frac{2p+1-\alpha}{(p+1)(p+2)}a_p. $$

The recurrence links $a_0$ only to $a_2,a_4,\ldots$ and $a_1$ only to $a_3,a_5,\ldots$.

Thus there are two independent series: one even and one odd. This is exactly what we expect from the symmetry $V(-x)=V(x)$.

#### 5. Force the series to terminate

For large $p$, the recurrence behaves like

$$\frac{a_{p+2}}{a_p}\simeq\frac{2}{p}.$$

These are the coefficient ratios of a series that grows like $e^{y^2}$.

Therefore, if the series continues forever, $H(y)$ grows like $e^{y^2}$.

Then $\phi\sim e^{+y^2/2}$, which is not normalisable.

Therefore the numerator must vanish at some non-negative integer $p=n$:

$$ 2n+1-\alpha=0. $$

$$ \alpha=2n+1 \quad\Longrightarrow\quad \boxed{E_n=\left(n+\frac12\right)\hbar\omega}. $$

#### Normalised eigenfunctions

$$ \phi_n(x)=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4} \frac{1}{\sqrt{2^n n!}}\, H_n\!\left(\sqrt{\frac{m\omega}{\hbar}}x\right) e^{-m\omega x^2/(2\hbar)}. $$

$$ H_0=1,\qquad H_1=2y,\qquad H_2=4y^2-2,\qquad H_3=8y^3-12y. $$

Writing $a=\sqrt{\hbar/(m\omega)}$ for the oscillator length, the first three functions are

$$ \phi_0(x)=\frac{1}{\pi^{1/4}\sqrt a}e^{-x^2/(2a^2)}, $$

$$ \phi_1(x)=\frac{\sqrt2}{\pi^{1/4}\sqrt a}\frac{x}{a}e^{-x^2/(2a^2)}, $$

$$ \phi_2(x)=\frac{1}{\sqrt2\,\pi^{1/4}\sqrt a}\left(2\frac{x^2}{a^2}-1\right)e^{-x^2/(2a^2)}. $$

The ground state has non-zero energy $E_0=\tfrac12\hbar\omega$.

#### The eigenfunctions as an orthonormal basis

The Hermite-Gaussian functions satisfy

$$\int_{-\infty}^{\infty}\phi_m^*(x)\phi_n(x)\,dx=\delta_{mn}.$$

They are also complete in $L^2(\mathbb R)$. Therefore any square-integrable oscillator wavefunction can be expanded as

$$\psi(x,0)=\sum_{n=0}^{\infty}c_n\phi_n(x),\qquad c_n=\langle\phi_n,\psi(0)\rangle=\int_{-\infty}^{\infty}\phi_n^*(x)\psi(x,0)\,dx.$$

The coefficient $c_n$ is the component of the state along the $n$-th orthonormal basis vector.

If the energy is measured, the probability of obtaining $E_n$ is $|c_n|^2$.

Time evolution changes only the phase of each basis component:

$$\psi(x,t)=\sum_{n=0}^{\infty}c_n\phi_n(x)e^{-iE_nt/\hbar}.$$

#### How to recognise the basis functions

$\phi_n$ has parity $(-1)^n$: even $n$ gives an even function and odd $n$ gives an odd function.

$\phi_n$ has exactly $n$ nodes on the real line.

The Gaussian makes every state decay, while the Hermite polynomial supplies the oscillations and nodes.

Increasing $n$ therefore adds one node and raises the energy by exactly $\hbar\omega$.

## Harmonic oscillator by ladder operators

*Alternative method*

The energy spectrum can be found without solving a second-order differential equation.

#### Problem specification

- **Hamiltonian:** $$H=\frac{P^2}{2m}+\frac12m\omega^2X^2.$$

- **Algebraic condition:** $[X,P]=i\hbar$ and the ground state must have the smallest allowed energy.

- **Find:** The same energy spectrum and eigenstate ladder obtained by the differential-equation method.

#### 1. Define lowering and raising operators

$$ a=\sqrt{\frac{m\omega}{2\hbar}}\,X+\frac{i}{\sqrt{2m\hbar\omega}}\,P, \qquad a^\dagger=\sqrt{\frac{m\omega}{2\hbar}}\,X-\frac{i}{\sqrt{2m\hbar\omega}}\,P. $$

$$ [a,a^\dagger]=1. $$

#### 2. Factorise the Hamiltonian

$$ H=\frac{P^2}{2m}+\frac12m\omega^2X^2 =\hbar\omega\left(a^\dagger a+\frac12\right). $$

#### 3. Identify the ground state

The operator $a^\dagger a$ has non-negative expectation value.

The lowest possible state therefore satisfies

$$ a|0\rangle=0. $$

$$ H|0\rangle=\frac12\hbar\omega|0\rangle. $$

#### 4. Climb the spectrum

$$ [H,a^\dagger]=\hbar\omega a^\dagger. $$

If $H|n\rangle=E_n|n\rangle$, then

$$ H(a^\dagger|n\rangle)=(E_n+\hbar\omega)(a^\dagger|n\rangle). $$

#### Spectrum and states

$$ E_n=\left(n+\frac12\right)\hbar\omega, \qquad |n\rangle=\frac{(a^\dagger)^n}{\sqrt{n!}}|0\rangle. $$

$$a|n\rangle=\sqrt n\,|n-1\rangle, \qquad a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle.$$

This agrees with the power-series solution and explains the equal energy spacing directly.

The vectors $|0\rangle,|1\rangle,|2\rangle,\ldots$ are the same orthonormal basis as the Hermite-Gaussian functions $\phi_0(x),\phi_1(x),\phi_2(x),\ldots$.

The operator method changes the basis label $n$ without requiring the differential equation to be solved again.

## Model 8: Particle in a three-dimensional rectangular box

A three-dimensional problem becomes three copies of the one-dimensional infinite well.

#### Problem specification

- **Equation:** $$-\frac{\hbar^2}{2M}\nabla^2\phi+V(x,y,z)\phi=E\phi.$$

- **Potential:** $V=0$ inside $-a\le x\le a$, $-b\le y\le b$, $-c\le z\le c$; $V=\infty$ outside.

- **Boundary conditions:** $\phi=0$ on all six faces and outside the box; $\iiint|\phi|^2\,dV=1$.

- **Find:** The product eigenfunctions, energy levels, and degeneracies.

#### 1. Write the TISE inside the box

The box is $-a\le x\le a$, $-b\le y\le b$, $-c\le z\le c$.

$$ -\frac{\hbar^2}{2M}\left( \frac{\partial^2}{\partial x^2}+ \frac{\partial^2}{\partial y^2}+ \frac{\partial^2}{\partial z^2}\right)u=Eu. $$

#### 2. Separate the coordinates

$$ u(x,y,z)=X(x)Y(y)Z(z). $$

Divide by $XYZ$:

$$ -\frac{\hbar^2}{2M}\frac{X''}{X} -\frac{\hbar^2}{2M}\frac{Y''}{Y} -\frac{\hbar^2}{2M}\frac{Z''}{Z}=E. $$

Each term depends on a different coordinate.

Set them equal to $E_x,E_y,E_z$, with $E=E_x+E_y+E_z$.

#### 3. Reuse the one-dimensional solution

$$ X_{n_x}(x)=\frac{1}{\sqrt a} \begin{cases} \cos\!\left(\dfrac{n_x\pi x}{2a}\right),&n_x\ \text{odd},\\[4pt] \sin\!\left(\dfrac{n_x\pi x}{2a}\right),&n_x\ \text{even}, \end{cases} $$

The functions $Y_{n_y}$ and $Z_{n_z}$ have the same form with $a\to b,c$.

#### Product states and energies

$$ \phi_{n_xn_yn_z}=X_{n_x}Y_{n_y}Z_{n_z}, $$

$$ E_{n_xn_yn_z}=\frac{\hbar^2\pi^2}{8M} \left(\frac{n_x^2}{a^2}+\frac{n_y^2}{b^2}+\frac{n_z^2}{c^2}\right). $$

If two side lengths are equal, exchanging the corresponding quantum numbers leaves the energy unchanged.

That produces degeneracy.

#### Why the product construction is complete

The sets $\{X_{n_x}\}$, $\{Y_{n_y}\}$ and $\{Z_{n_z}\}$ are orthonormal bases in their separate one-dimensional intervals.

The products $X_{n_x}Y_{n_y}Z_{n_z}$ therefore form an orthonormal basis for square-integrable functions in the box.

$$\iiint \phi_{n_xn_yn_z}^*\phi_{m_xm_ym_z}\,dV= \delta_{n_xm_x}\delta_{n_ym_y}\delta_{n_zm_z}.$$

A general state is a triple basis expansion with coefficients obtained from three-dimensional inner products.

## Model 9: Three-dimensional harmonic oscillator

A sum of three independent quadratic potentials gives a product of three one-dimensional oscillator states.

#### Problem specification

- **Equation:** $$\left[-\frac{\hbar^2}{2M}\nabla^2+\frac12k_xx^2+\frac12k_yy^2+\frac12k_zz^2\right]\phi=E\phi.$$

- **Domain:** All of $\mathbb R^3$.

- **Boundary conditions:** $\phi\to0$ when any coordinate tends to $\pm\infty$; $\iiint|\phi|^2\,dV=1$.

- **Find:** The product eigenfunctions and additive energy spectrum.

#### 1. Recognise the separable Hamiltonian

$$ V(x,y,z)=\frac12k_xx^2+\frac12k_yy^2+\frac12k_zz^2. $$

$$ \phi(x,y,z)=X(x)Y(y)Z(z). $$

#### 2. Divide by the product

$$ \left[-\frac{\hbar^2}{2M}\frac{X''}{X}+\frac12k_xx^2\right] +\left[-\frac{\hbar^2}{2M}\frac{Y''}{Y}+\frac12k_yy^2\right] +\left[-\frac{\hbar^2}{2M}\frac{Z''}{Z}+\frac12k_zz^2\right]=E. $$

Each bracket is a one-dimensional oscillator equation.

#### Separated solution

$$ E_{n_xn_yn_z}=\left(n_x+\frac12\right)\hbar\omega_x +\left(n_y+\frac12\right)\hbar\omega_y +\left(n_z+\frac12\right)\hbar\omega_z, $$

$$ \omega_i=\sqrt{\frac{k_i}{M}}. $$

$$ \phi_{n_xn_yn_z}\propto H_{n_x}(x')H_{n_y}(y')H_{n_z}(z') e^{-(x'^2+y'^2+z'^2)/2}, $$

$$ x'=\sqrt{\frac{M\omega_x}{\hbar}}x, \quad y'=\sqrt{\frac{M\omega_y}{\hbar}}y, \quad z'=\sqrt{\frac{M\omega_z}{\hbar}}z. $$

Equal frequencies create degeneracies because different triples can have the same total excitation.

#### Basis interpretation

Each factor is one of the one-dimensional Hermite-Gaussian basis functions.

The three-dimensional eigenfunctions are tensor-product basis vectors:

$$|n_x,n_y,n_z\rangle=|n_x\rangle\otimes|n_y\rangle\otimes|n_z\rangle.$$

If $\omega_x=\omega_y=\omega_z=\omega$, the energy depends only on $N=n_x+n_y+n_z$:

$$E_N=\left(N+\frac32\right)\hbar\omega.$$

Many different triples can have the same $N$, which is the origin of the degeneracy.

## The spherical Laplacian used below

*Spherical-coordinate toolkit*

Central potentials depend only on distance from one point. This section collects the operator needed immediately; Appendix A.4 gives the full line-by-line derivation.

#### 1. Write the coordinate map

$$ x=r\sin\theta\cos\varphi, \qquad y=r\sin\theta\sin\varphi, \qquad z=r\cos\theta. $$

Here $r\ge0$, $0\le\theta\le\pi$, and $0\le\varphi<2\pi$.

#### 2. Find the scale factors from a small displacement

Differentiate the position vector $\mathbf r(r,\theta,\varphi)$.

$$ d\mathbf r=\mathbf e_r\,dr+\mathbf e_\theta\,r\,d\theta+\mathbf e_\varphi\,r\sin\theta\,d\varphi. $$

Because the three unit vectors are mutually perpendicular,

$$ ds^2=dr^2+r^2d\theta^2+r^2\sin^2\theta\,d\varphi^2. $$

Therefore the orthogonal-coordinate scale factors are

$$ h_r=1,\qquad h_\theta=r,\qquad h_\varphi=r\sin\theta. $$

#### 3. Use the gradient formula

For orthogonal coordinates $q_1,q_2,q_3$,

$$ \nabla f=\sum_i\mathbf e_i\frac{1}{h_i}\frac{\partial f}{\partial q_i}. $$

Hence

$$ \nabla f= \mathbf e_r\frac{\partial f}{\partial r} +\mathbf e_\theta\frac1r\frac{\partial f}{\partial\theta} +\mathbf e_\varphi\frac{1}{r\sin\theta}\frac{\partial f}{\partial\varphi}. $$

#### 4. Use the divergence formula

For $\mathbf A=A_1\mathbf e_1+A_2\mathbf e_2+A_3\mathbf e_3$,

$$ \nabla\!\cdot\!\mathbf A= \frac{1}{h_1h_2h_3} \left[ \frac{\partial}{\partial q_1}(h_2h_3A_1)+ \frac{\partial}{\partial q_2}(h_3h_1A_2)+ \frac{\partial}{\partial q_3}(h_1h_2A_3) \right]. $$

Set $\mathbf A=\nabla f$.

Then $A_r=f_r$, $A_\theta=f_\theta/r$, and $A_\varphi=f_\varphi/(r\sin\theta)$.

#### The spherical-coordinate Laplacian

$$ \boxed{ \nabla^2f= \frac1{r^2}\frac{\partial}{\partial r}\!\left(r^2\frac{\partial f}{\partial r}\right) +\frac1{r^2\sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\frac{\partial f}{\partial\theta}\right) +\frac1{r^2\sin^2\theta}\frac{\partial^2f}{\partial\varphi^2}} $$

## Separate the radial and angular equations

*Central-potential method*

The same angular solution works for every spherically symmetric potential $V(r)$.

#### Problem specification

- **Equation:** $$\left[-\frac{\hbar^2}{2M}\nabla^2+V(r)\right]\phi=E\phi.$$

- **Symmetry:** The potential depends on $r$ only, so spherical coordinates match the geometry.

- **Boundary conditions:** The wavefunction is single-valued in $\varphi$, regular on the polar axis, finite at $r=0$, and normalisable as $r\to\infty$.

- **Find:** A universal angular equation and a radial equation containing the particular $V(r)$.

#### 1. Start with a central potential

$$ \left[-\frac{\hbar^2}{2M}\nabla^2+V(r)\right]\phi=E\phi. $$

$$ \phi(r,\theta,\varphi)=R(r)Y(\theta,\varphi). $$

#### 2. Separate radial and angular terms

Insert the spherical Laplacian, divide by $RY$, and multiply by $r^2$.

$$ \left[-\frac{\hbar^2}{2M}\frac1R\frac{d}{dr}\left(r^2\frac{dR}{dr}\right)+r^2(V-E)\right] -\frac{\hbar^2}{2M}\frac1Y\left[ \frac1{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial Y}{\partial\theta}\right) +\frac1{\sin^2\theta}\frac{\partial^2Y}{\partial\varphi^2} \right]=0. $$

The first bracket depends only on $r$.

The second depends only on the angles.

Each must equal a constant.

#### 3. Solve the azimuthal angle

Separate again: $Y(\theta,\varphi)=\Theta(\theta)\Phi(\varphi)$.

$$ \frac{d^2\Phi}{d\varphi^2}+m^2\Phi=0. $$

$$ \Phi_m(\varphi)=\frac1{\sqrt{2\pi}}e^{im\varphi}. $$

Single-valuedness, $\Phi(\varphi+2\pi)=\Phi(\varphi)$, forces $m\in\mathbb Z$.

#### 4. Solve the polar angle

With $u=\cos\theta$, the remaining equation is

$$ \frac{d}{du}\left[(1-u^2)\frac{d\Theta}{du}\right] +\left[l(l+1)-\frac{m^2}{1-u^2}\right]\Theta=0. $$

Regularity at $u=\pm1$ requires

$$ l=0,1,2,\ldots,\qquad m=-l,-l+1,\ldots,l. $$

The regular solutions are associated Legendre functions.

#### Angular solution

$$ Y_{lm}(\theta,\varphi)=(-1)^m \sqrt{\frac{2l+1}{4\pi}\frac{(l-|m|)!}{(l+|m|)!}} P_l^{|m|}(\cos\theta)e^{im\varphi}. $$

$$ L^2Y_{lm}=\hbar^2l(l+1)Y_{lm},\qquad L_zY_{lm}=\hbar mY_{lm}. $$

#### The angular functions are themselves a basis

The spherical harmonics are orthonormal on the unit sphere:

$$\int_0^{2\pi}\int_0^{\pi}Y_{lm}^*(\theta,\varphi)Y_{l'm'}(\theta,\varphi)\sin\theta\,d\theta\,d\varphi =\delta_{ll'}\delta_{mm'}.$$

They form a complete basis for square-integrable angular functions.

Thus the separation is a basis expansion adapted to rotational symmetry: radial functions multiply angular basis vectors $Y_{lm}$.

#### 5. Obtain the radial equation

$$ -\frac{\hbar^2}{2M}\frac1{r^2}\frac{d}{dr}\left(r^2\frac{dR}{dr}\right) +\left[V(r)+\frac{\hbar^2l(l+1)}{2Mr^2}\right]R=ER. $$

Set $u(r)=rR(r)$.

This substitution removes the first derivative. Indeed, if $R=u/r$, then

$$r^2\frac{dR}{dr}=ru'-u,\qquad \frac{d}{dr}\left(r^2\frac{dR}{dr}\right)=ru''.$$

Substitute this into the radial equation and multiply through by $r$.

$$ \boxed{-\frac{\hbar^2}{2M}\frac{d^2u}{dr^2} +\left[V(r)+\frac{\hbar^2l(l+1)}{2Mr^2}\right]u=Eu} $$

The boundary condition is $u(0)=0$.

The additional $l(l+1)/r^2$ term is the centrifugal effective potential.

## Model 10: Particle in a spherical infinite well

The spherical analogue of the infinite box quantises the zeros of spherical Bessel functions.

#### Problem specification

- **Equation:** $$\left[-\frac{\hbar^2}{2M}\nabla^2+V(r)\right]\phi=E\phi.$$

- **Potential:** $$V(r)=0\ \text{for }0\le r\le a,\qquad V(r)=\infty\ \text{for }r>a.$$

- **Boundary conditions:** Regularity at $r=0$; $R(a)=0$; angular single-valuedness; full three-dimensional normalisation.

- **Find:** The allowed radial wavenumbers, energies and quantum-number labels.

#### 1. State the potential and boundary

$$ V(r)=\begin{cases}0,&r\le a,\\\infty,&r>a,\end{cases} \qquad R(a)=0. $$

#### 2. Scale the radial equation

$$ E=\frac{\hbar^2k^2}{2M},\qquad x=kr. $$

$$ \frac{d^2R}{dx^2}+\frac2x\frac{dR}{dx} +\left[1-\frac{l(l+1)}{x^2}\right]R=0. $$

This is the spherical Bessel equation.

#### 3. Reject the singular family

$$ R(x)=A j_l(x)+B n_l(x). $$

The spherical Neumann functions $n_l$ diverge at $x=0$.

Normalisability and regularity force $B=0$.

$$ j_0(x)=\frac{\sin x}{x}, \qquad j_1(x)=\frac{\sin x}{x^2}-\frac{\cos x}{x}, $$

$$ j_2(x)=\left(\frac{3}{x^3}-\frac1x\right)\sin x-\frac{3}{x^2}\cos x. $$

#### 4. Apply the wall

$$ j_l(ka)=0. $$

Let $\alpha_{nl}$ be the $n$-th positive zero of $j_l$.

$$ k_{nl}=\frac{\alpha_{nl}}{a}. $$

#### Eigenvalues and eigenfunctions

$$ E_{nl}=\frac{\hbar^2\alpha_{nl}^2}{2Ma^2}. $$

$$ \phi_{nlm}(r,\theta,\varphi)=N_{nl}\, j_l\!\left(\alpha_{nl}\frac{r}{a}\right)Y_{lm}(\theta,\varphi). $$

The energy depends on $n$ and $l$, but not on $m$.

Each $(n,l)$ energy is therefore $2l+1$ times degenerate.

#### Check the simplest angular sector: $l=0$

For $l=0$, $j_0(kr)=\sin(kr)/(kr)$.

The wall condition becomes

$$j_0(ka)=0\quad\Longrightarrow\quad\sin(ka)=0\quad\Longrightarrow\quad ka=n\pi.$$

Hence $E_{n0}=\hbar^2n^2\pi^2/(2Ma^2)$.

This resembles the one-dimensional infinite well, but the radial wavefunction carries the extra factor $1/r$ required by three-dimensional geometry.

## Model 11: Hydrogen-like atom

This is the most involved exact solution in the sequence. It combines spherical separation, asymptotic analysis and a terminating power series.

#### Problem specification

- **Equation:** $$\left[-\frac{\hbar^2}{2\mu}\nabla^2-\frac{Ze^2}{4\pi\varepsilon_0r}\right]\phi=E\phi.$$

- **Potential:** $V(r)=-Ze^2/(4\pi\varepsilon_0r)$ for $r>0$.

- **Boundary conditions:** For bound states $E<0$; $u(0)=0$; $u(r)\to0$ as $r\to\infty$; angular part single-valued and regular; $\iiint|\phi|^2\,dV=1$.

- **Find:** The energy spectrum, radial functions and allowed values of $n,l,m$.

#### 1. Write the radial Coulomb equation

$$ V(r)=-\frac{Ze^2}{4\pi\varepsilon_0r}. $$

Use the reduced mass $\mu$ and set $u=rR$:

The reduced mass allows the electron and nucleus to move while reducing their relative motion to a one-particle equation.

$$ -\frac{\hbar^2}{2\mu}\frac{d^2u}{dr^2} +\left[-\frac{Ze^2}{4\pi\varepsilon_0r} +\frac{\hbar^2l(l+1)}{2\mu r^2}\right]u=Eu. $$

Bound states have $E<0$, $u(0)=0$, and $u(\infty)=0$.

#### 2. Make the equation dimensionless

$$ \kappa=\frac{\sqrt{-2\mu E}}{\hbar}, \qquad \rho=2\kappa r, \qquad \eta=\frac{\mu Ze^2}{4\pi\varepsilon_0\hbar^2\kappa}. $$

Because $\rho=2\kappa r$, differentiation changes according to

$$\frac{d}{dr}=2\kappa\frac{d}{d\rho},\qquad \frac{d^2}{dr^2}=4\kappa^2\frac{d^2}{d\rho^2}.$$

The parameter $\eta$ contains the energy through $\kappa$. Quantising $\eta$ will therefore quantise $E$.

The radial equation becomes

$$ \frac{d^2u}{d\rho^2}+\left[-\frac14+\frac{\eta}{\rho}-\frac{l(l+1)}{\rho^2}\right]u=0. $$

#### 3. Find both endpoint behaviours

#### As $\rho\to\infty$

$$ u''-\frac14u\simeq0 \quad\Longrightarrow\quad u\propto e^{-\rho/2}. $$

The growing exponential is rejected.

#### As $\rho\to0$

$$ u''-\frac{l(l+1)}{\rho^2}u\simeq0. $$

Trying $u\sim\rho^s$ gives $s(s-1)=l(l+1)$.

The two roots are $s=l+1$ and $s=-l$.

The second root diverges at the origin for $l>0$ and fails the physical boundary condition.

The regular root is therefore $s=l+1$.

#### 4. Factor out the known behaviour

$$ u(\rho)=\rho^{l+1}e^{-\rho/2}v(\rho). $$

Substitution gives

$$ \rho v''+(2l+2-\rho)v'+(\eta-l-1)v=0. $$

#### 5. Use a power series

#### Why use a series again?

We have already removed the only two difficult endpoint behaviours: $\rho^{l+1}$ at the origin and $e^{-\rho/2}$ at infinity.

The remaining function $v(\rho)$ is regular and satisfies an equation with analytic coefficients after multiplication by $\rho$.

A power series is therefore the natural systematic representation. As with the oscillator, its recurrence relation will expose the allowed energies.

$$ v(\rho)=\sum_{p=0}^{\infty}a_p\rho^p. $$

$$v'=\sum_{p=0}^{\infty}(p+1)a_{p+1}\rho^p,\qquad \rho v''=\sum_{p=0}^{\infty}p(p+1)a_{p+1}\rho^p.$$

Substituting these into the equation for $v$ and matching the coefficient of each $\rho^p$ gives

Matching powers gives the recurrence

$$ a_{p+1}=\frac{p+l+1-\eta}{(p+1)(p+2l+2)}a_p. $$

An infinite series grows fast enough to destroy normalisability.

More precisely, the non-terminating solution contains an $e^{+\rho}$ contribution. Combined with the factor $e^{-\rho/2}$, it would behave as $e^{+\rho/2}$.

The series must terminate at $p=p_{\max}$.

#### 6. Quantise the energy

Termination requires the numerator to vanish:

$$ p_{\max}+l+1-\eta=0. $$

Define the principal quantum number

$$ n=p_{\max}+l+1,\qquad n=1,2,3,\ldots $$

Therefore $\eta=n$, with $l=0,1,\ldots,n-1$.

The relation $n=p_{\max}+l+1$ automatically gives $l<n$ because $p_{\max}\ge0$.

Insert the definitions of $\eta$ and $\kappa$:

$$ \boxed{E_n=-\frac{\mu Z^2e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac1{n^2}}. $$

#### Complete bound-state wavefunctions

Define the Bohr radius using the reduced mass:

$$ a_0=\frac{4\pi\varepsilon_0\hbar^2}{\mu e^2}, \qquad \rho=\frac{2Zr}{na_0}. $$

$$ R_{nl}(r)=N_{nl}\,e^{-\rho/2}\rho^lL_{n-l-1}^{\,2l+1}(\rho), \qquad \phi_{nlm}=R_{nl}(r)Y_{lm}(\theta,\varphi). $$

The three quantum numbers obey

$$ n=1,2,\ldots,\qquad l=0,\ldots,n-1,\qquad m=-l,\ldots,l. $$

#### Basis interpretation of the hydrogen states

The angular factors $Y_{lm}$ form an orthonormal basis on the sphere.

For each allowed $l$, the radial functions form an orthonormal family with the radial measure $r^2dr$.

$$\int_0^{\infty}R_{nl}^*(r)R_{n'l}(r)r^2\,dr=\delta_{nn'}.$$

The products $R_{nl}Y_{lm}$ form the bound-state basis. A general bound state is

$$\psi(\mathbf r,0)=\sum_{n=1}^{\infty}\sum_{l=0}^{n-1}\sum_{m=-l}^{l}c_{nlm}\phi_{nlm}(\mathbf r).$$

Each coefficient is found by the three-dimensional inner product, and each energy measurement yields $E_n$ with probability obtained by summing $|c_{nlm}|^2$ over the degenerate $l,m$ states.

#### $1s$ state

$$ \phi_{100}=\left(\frac{Z^3}{\pi a_0^3}\right)^{1/2}e^{-Zr/a_0}. $$

#### $2s$ state

$$ \phi_{200}=\left(\frac{Z^3}{32\pi a_0^3}\right)^{1/2} \left(2-\frac{Zr}{a_0}\right)e^{-Zr/(2a_0)}. $$

#### $2p,\ m=0$ state

$$ \phi_{210}=\left(\frac{Z^3}{32\pi a_0^3}\right)^{1/2} \frac{Zr}{a_0}\cos\theta\,e^{-Zr/(2a_0)}. $$

#### $2p,\ m=\pm1$ states

$$ \phi_{21\pm1}=\mp\left(\frac{Z^3}{64\pi a_0^3}\right)^{1/2} \frac{Zr}{a_0}\sin\theta\,e^{\pm i\varphi}e^{-Zr/(2a_0)}. $$

#### Why the energy depends only on $n$

For the pure Coulomb potential, states with different $l$ and $m$ but the same $n$ share the same energy.

The degeneracy of a fixed-$n$ shell, excluding spin, is $n^2$.

## What changes from problem to problem?

*Revision map*

| Problem | New move | What selects the answer? |

| --- | --- | --- |

| Infinite well | Sinusoidal solution | Zeros at both walls |

| Potential step | Match two regions | Continuity of $\phi,\phi'$ |

| Tunnelling barrier | Match three regions | Two interfaces |

| Semi-infinite well | Transcendental condition | Graphical/numerical root |

| Harmonic oscillator | Asymptotic factor + series | Series termination |

| 3D box/oscillator | Cartesian separation | Three 1D solutions |

| Central potentials | Spherical separation | Angular regularity |

| Spherical well | Bessel functions | Zeros of $j_l$ |

| Hydrogen-like atom | Two endpoint factors + series | Series termination |

#### The shortest useful checklist

**Region → equation → admissible form → boundary conditions → normalisation or flux → interpretation.**

## Deriving Laplacians in common coordinate systems

*Appendix*

The Laplacian changes appearance because the coordinate grid stretches and bends. The operator itself has not changed.

#### Why this matters in quantum mechanics

The kinetic-energy operator is $-\hbar^2\nabla^2/(2m)$.

Choosing coordinates that match the symmetry of the potential can turn one difficult partial differential equation into several ordinary differential equations.

| Coordinates | Best suited to | Typical potential |

| --- | --- | --- |

| Cartesian $(x,y,z)$ | Rectangular boundaries | $V_x(x)+V_y(y)+V_z(z)$ |

| Polar $(r,\varphi)$ | Two-dimensional circular symmetry | $V(r)$ in a plane |

| Cylindrical $(\rho,\varphi,z)$ | Axial symmetry | Wires, cylinders, uniform axes |

| Spherical $(r,\theta,\varphi)$ | Central symmetry | Atoms and spherical wells |

#### The route used in every derivation

Coordinate map → tangent vectors → scale factors → gradient → divergence → Laplacian.

## General orthogonal-coordinate formula

*Appendix A.1*

Derive the formula once, then substitute the scale factors for each coordinate system.

#### 1. Describe the coordinate grid

Let a position in space be written as a vector-valued function

$$\mathbf r=\mathbf r(q_1,q_2,q_3).$$

Changing only $q_i$ moves along the coordinate curve whose tangent vector is

$$\mathbf a_i=\frac{\partial\mathbf r}{\partial q_i}.$$

For orthogonal coordinates, the three tangent vectors are mutually perpendicular.

#### 2. Define scale factors

$$h_i=|\mathbf a_i|,\qquad \mathbf e_i=\frac{\mathbf a_i}{h_i}.$$

A small displacement is therefore

$$d\mathbf r=h_1\mathbf e_1dq_1+h_2\mathbf e_2dq_2+h_3\mathbf e_3dq_3.$$

The physical edge lengths of a small coordinate cell are $h_1dq_1$, $h_2dq_2$ and $h_3dq_3$.

$$dV=h_1h_2h_3\,dq_1dq_2dq_3.$$

#### 3. Derive the gradient

By definition, the first-order change in a scalar function is

$$df=\nabla f\cdot d\mathbf r.$$

It is also

$$df=\frac{\partial f}{\partial q_1}dq_1+\frac{\partial f}{\partial q_2}dq_2+\frac{\partial f}{\partial q_3}dq_3.$$

Compare the coefficient of each independent $dq_i$:

$$\boxed{\nabla f=\sum_{i=1}^{3}\mathbf e_i\frac1{h_i}\frac{\partial f}{\partial q_i}}.$$

#### 4. Derive the divergence from flux

Write $\mathbf A=A_1\mathbf e_1+A_2\mathbf e_2+A_3\mathbf e_3$.

The face perpendicular to $\mathbf e_1$ has area $h_2h_3dq_2dq_3$.

The net outward flux through the pair of $q_1$ faces is

$$\frac{\partial}{\partial q_1}(h_2h_3A_1)dq_1dq_2dq_3.$$

Add the analogous contributions from the other two pairs of faces and divide by the cell volume.

$$\boxed{\nabla\cdot\mathbf A= \frac1{h_1h_2h_3}\left[ \frac{\partial}{\partial q_1}(h_2h_3A_1)+ \frac{\partial}{\partial q_2}(h_3h_1A_2)+ \frac{\partial}{\partial q_3}(h_1h_2A_3) \right]}.$$

#### Apply divergence to the gradient

Set $\mathbf A=\nabla f$, so $A_i=(1/h_i)\partial f/\partial q_i$.

$$\boxed{ \nabla^2f=\frac1{h_1h_2h_3}\left[ \frac{\partial}{\partial q_1}\left(\frac{h_2h_3}{h_1}\frac{\partial f}{\partial q_1}\right)+ \frac{\partial}{\partial q_2}\left(\frac{h_3h_1}{h_2}\frac{\partial f}{\partial q_2}\right)+ \frac{\partial}{\partial q_3}\left(\frac{h_1h_2}{h_3}\frac{\partial f}{\partial q_3}\right) \right]}.$$

Every formula below follows by inserting the appropriate scale factors.

## Polar coordinates in two dimensions

*Appendix A.2*

#### Coordinate map

$$x=r\cos\varphi,\qquad y=r\sin\varphi.$$

Here $r\ge0$ and $0\le\varphi<2\pi$.

> Diagram preserved in the PDF and HTML editions.

#### 1. Differentiate the position vector

$$\mathbf r(r,\varphi)=r\cos\varphi\,\mathbf e_x+r\sin\varphi\,\mathbf e_y.$$

$$ \frac{\partial\mathbf r}{\partial r}=(\cos\varphi,\sin\varphi)=\mathbf e_r, \qquad \frac{\partial\mathbf r}{\partial\varphi}=(-r\sin\varphi,r\cos\varphi)=r\mathbf e_\varphi. $$

The vectors are perpendicular and have lengths $1$ and $r$.

$$h_r=1,\qquad h_\varphi=r.$$

#### 2. Read the geometry

$$d\mathbf r=\mathbf e_rdr+\mathbf e_\varphi r\,d\varphi,$$

$$ds^2=dr^2+r^2d\varphi^2,\qquad dA=r\,dr\,d\varphi.$$

A small angular change covers a physical arc length $r\,d\varphi$, not merely $d\varphi$.

#### Gradient, divergence and Laplacian

$$\nabla f=\mathbf e_r\frac{\partial f}{\partial r}+\mathbf e_\varphi\frac1r\frac{\partial f}{\partial\varphi},$$

$$\nabla\cdot\mathbf A=\frac1r\frac{\partial}{\partial r}(rA_r)+\frac1r\frac{\partial A_\varphi}{\partial\varphi},$$

$$\boxed{\nabla^2f=\frac1r\frac{\partial}{\partial r}\left(r\frac{\partial f}{\partial r}\right)+\frac1{r^2}\frac{\partial^2f}{\partial\varphi^2}}.$$

## Cylindrical coordinates

*Appendix A.3*

#### Coordinate map

$$x=\rho\cos\varphi,\qquad y=\rho\sin\varphi,\qquad z=z.$$

The symbol $\rho$ is the perpendicular distance from the $z$-axis.

#### 1. Find the coordinate tangent vectors

$$ \frac{\partial\mathbf r}{\partial\rho}=(\cos\varphi,\sin\varphi,0)=\mathbf e_\rho, $$

$$ \frac{\partial\mathbf r}{\partial\varphi}=(-\rho\sin\varphi,\rho\cos\varphi,0)=\rho\mathbf e_\varphi, \qquad \frac{\partial\mathbf r}{\partial z}=\mathbf e_z. $$

$$h_\rho=1,\qquad h_\varphi=\rho,\qquad h_z=1.$$

#### 2. Read the line and volume elements

$$ds^2=d\rho^2+\rho^2d\varphi^2+dz^2,$$

$$dV=\rho\,d\rho\,d\varphi\,dz.$$

The factor $\rho$ is the Jacobian. It records the increasing arc length as we move away from the axis.

#### Cylindrical Laplacian

$$\boxed{ \nabla^2f= \frac1\rho\frac{\partial}{\partial\rho}\left(\rho\frac{\partial f}{\partial\rho}\right) +\frac1{\rho^2}\frac{\partial^2f}{\partial\varphi^2} +\frac{\partial^2f}{\partial z^2}} $$

If $f$ is independent of $z$, this reduces exactly to the two-dimensional polar Laplacian after replacing $\rho$ by $r$.

## Spherical coordinates

*Appendix A.4*

#### Coordinate map

$$x=r\sin\theta\cos\varphi,\qquad y=r\sin\theta\sin\varphi,\qquad z=r\cos\theta.$$

Here $r\ge0$, $0\le\theta\le\pi$, and $0\le\varphi<2\pi$.

#### 1. Differentiate with respect to $r$

$$ \frac{\partial\mathbf r}{\partial r}= (\sin\theta\cos\varphi,\sin\theta\sin\varphi,\cos\theta)=\mathbf e_r. $$

$$h_r=\left|\frac{\partial\mathbf r}{\partial r}\right|=1.$$

A change $dr$ is already a physical radial distance.

#### 2. Differentiate with respect to $\theta$

$$ \frac{\partial\mathbf r}{\partial\theta}= (r\cos\theta\cos\varphi,r\cos\theta\sin\varphi,-r\sin\theta)=r\mathbf e_\theta. $$

$$h_\theta=\left|\frac{\partial\mathbf r}{\partial\theta}\right|=r.$$

At radius $r$, a small polar angle $d\theta$ corresponds to an arc length $r\,d\theta$.

#### 3. Differentiate with respect to $\varphi$

$$ \frac{\partial\mathbf r}{\partial\varphi}= (-r\sin\theta\sin\varphi,r\sin\theta\cos\varphi,0)=r\sin\theta\,\mathbf e_\varphi. $$

$$h_\varphi=\left|\frac{\partial\mathbf r}{\partial\varphi}\right|=r\sin\theta.$$

The circle swept out by changing $\varphi$ has radius $r\sin\theta$, not $r$.

#### 4. Build the geometric elements

$$d\mathbf r=\mathbf e_rdr+\mathbf e_\theta r\,d\theta+\mathbf e_\varphi r\sin\theta\,d\varphi,$$

$$ds^2=dr^2+r^2d\theta^2+r^2\sin^2\theta\,d\varphi^2,$$

$$dV=r^2\sin\theta\,dr\,d\theta\,d\varphi.$$

#### 5. Substitute the scale factors into the gradient

$$ \nabla f=\mathbf e_r\frac{\partial f}{\partial r} +\mathbf e_\theta\frac1r\frac{\partial f}{\partial\theta} +\mathbf e_\varphi\frac1{r\sin\theta}\frac{\partial f}{\partial\varphi}. $$

#### 6. Substitute them into the divergence

$$ \nabla\cdot\mathbf A= \frac1{r^2}\frac{\partial}{\partial r}(r^2A_r) +\frac1{r\sin\theta}\frac{\partial}{\partial\theta}(\sin\theta A_\theta) +\frac1{r\sin\theta}\frac{\partial A_\varphi}{\partial\varphi}. $$

#### Spherical-coordinate Laplacian

Set $\mathbf A=\nabla f$ and substitute its three components into the divergence formula:

$$\boxed{ \nabla^2f= \frac1{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial f}{\partial r}\right) +\frac1{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial f}{\partial\theta}\right) +\frac1{r^2\sin^2\theta}\frac{\partial^2f}{\partial\varphi^2}} $$

#### Two important reductions

#### Radial function only

If $f=f(r)$, both angular derivatives vanish:

$$\nabla^2f=\frac1{r^2}\frac{d}{dr}\left(r^2\frac{df}{dr}\right).$$

#### Radial times angular

For $f=R(r)Y(\theta,\varphi)$, the angular part is related to orbital angular momentum:

$$\nabla^2=\frac1{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right)-\frac{L^2}{\hbar^2r^2}.$$

This identity is the reason central-potential Schrödinger equations separate into radial functions and spherical harmonics.

## Why separation of variables reveals the eigenbasis

*Appendix B*

For a time-independent Hamiltonian, separation of variables is the route from the evolution equation to the eigenfunctions of the spatial operator.

#### The precise statement

**The Hamiltonian is the self-adjoint operator.**

**Its eigenfunctions form the orthonormal basis.**

We separate variables because those eigenfunctions are not known in advance.

#### 1. Isolate the spatial operator

Start with a Hamiltonian that has no explicit time dependence:

$$i\hbar\frac{\partial\Psi}{\partial t}=\hat H\Psi, \qquad \hat H=-\frac{\hbar^2}{2m}\nabla^2+V.$$

Write one separated mode as $\Psi(\mathbf r,t)=\phi(\mathbf r)T(t)$.

Substitution isolates two eigenvalue equations with the same separation constant $E$:

$$\boxed{\hat H\phi=E\phi} \qquad\text{and}\qquad i\hbar\frac{dT}{dt}=ET.$$

The spatial equation is therefore not merely an ordinary differential equation to be solved.

It is the eigenvalue problem for the spatial Hamiltonian on the domain fixed by the boundary conditions.

#### 2. Boundary conditions determine the operator domain

Hard walls, decay at infinity, regularity at the origin and matching conditions are part of the definition of the operator.

With the correct domain, the Hamiltonian is self-adjoint.

Consequently its eigenvalues are real, eigenfunctions belonging to distinct eigenvalues are orthogonal, and its eigenfunctions give a complete discrete or generalised basis.

#### 3. Further separation finds a joint eigenbasis

In more than one coordinate, we separate again only when the Hamiltonian exposes commuting self-adjoint pieces.

For a rectangular box these are the one-dimensional Cartesian operators.

For a central potential the commuting set is $\hat H$, $\hat L^2$ and $\hat L_z$.

$$ \hat H\phi_{nlm}=E_n\phi_{nlm},\qquad \hat L^2\phi_{nlm}=\hbar^2l(l+1)\phi_{nlm},\qquad \hat L_z\phi_{nlm}=\hbar m\phi_{nlm}. $$

The product functions obtained by separation are therefore joint eigenvectors that label the orthonormal basis.

## Where the time dependence lives

*Appendix B · continued*

Once the spatial eigenbasis is known, the full solution is its expansion with time-dependent coefficients.

#### Discrete spectrum

$$ \Psi(\mathbf r,t)=\sum_n c_n(t)\phi_n(\mathbf r), \qquad c_n(t)=c_n(0)e^{-iE_nt/\hbar}. $$

$$ c_n(0)=\langle\phi_n,\Psi(0)\rangle =\int\phi_n^*(\mathbf r)\Psi(\mathbf r,0)\,d\tau. $$

The basis functions $\phi_n(\mathbf r)$ are fixed in space.

In this stationary eigenbasis, all time dependence appears in the coefficient phases $e^{-iE_nt/\hbar}$.

#### Continuous spectrum

$$ \Psi(\mathbf r,t)=\sum_\alpha\int c_\alpha(E)\,e^{-iEt/\hbar}\phi_{E,\alpha}(\mathbf r)\,dE. $$

The label $\alpha$ distinguishes independent scattering channels such as incidence from the left or from the right.

The continuum eigenfunctions are delta-normalised rather than square-normalised.

#### Mixed spectrum

If bound and scattering states both occur, completeness requires both parts:

$$ \Psi(t)= \sum_{\text{bound }n}c_n(0)e^{-iE_nt/\hbar}\phi_n +\sum_\alpha\int_{\text{continuum}} c_\alpha(E)e^{-iEt/\hbar}\phi_{E,\alpha}\,dE. $$

| Spectrum | Normalisation | Expansion |

| --- | --- | --- |

| Discrete | $\langle\phi_m,\phi_n\rangle=\delta_{mn}$ | Sum over $n$ |

| Continuous | $\langle\phi_{E,\alpha},\phi_{E',\beta}\rangle=\delta_{\alpha\beta}\delta(E-E')$ | Integral over $E$ |

| Mixed | Discrete and delta normalisation | Sum plus integral |

**Separation isolates the self-adjoint eigenvalue problem.**

**Solving that problem finds the basis.**

**Expanding in that basis solves the time evolution.**

## 1. One-dimensional infinite well

*Appendix C · Master solution tables*

| Potential and domain | $V=0$ for $0\le x\le L$ and $V=\infty$ otherwise; $\phi(0)=\phi(L)=0$. |

| --- | --- |

| Spatial eigenproblem | $-\frac{\hbar^2}{2m}\phi''=E\phi$, hence $\phi''+k^2\phi=0$ with $k^2=2mE/\hbar^2$. |

| General form | $\phi=A\sin kx+B\cos kx$. |

| Selection steps | $\phi(0)=0\Rightarrow B=0$; $\phi(L)=0\Rightarrow \sin(kL)=0$; therefore $k_n=n\pi/L$ with $n=1,2,\ldots$. |

| Orthonormal basis | $\displaystyle \phi_n(x)=\sqrt{\frac2L}\sin\!\left(\frac{n\pi x}{L}\right)$ and $\int_0^L\phi_m^*\phi_n\,dx=\delta_{mn}$. |

| Spectrum | $\displaystyle E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}$. |

| Full solution | $\displaystyle \Psi(x,t)=\sum_{n=1}^{\infty}c_n(0)e^{-iE_nt/\hbar}\phi_n(x)$, where $c_n(0)=\int_0^L\phi_n^*(x)\Psi(x,0)\,dx$. |

## 2. Potential step with $E>V_0$

*Appendix C · Master solution tables*

| Potential | $V=0$ for $x<0$ and $V=V_0$ for $x>0$. |

| --- | --- |

| Regional wavenumbers | $\displaystyle k_1=\frac{\sqrt{2mE}}{\hbar}$ and $\displaystyle k_2=\frac{\sqrt{2m(E-V_0)}}{\hbar}$. |

| Admissible form | For incidence from the left, $\phi_1=Ae^{ik_1x}+Be^{-ik_1x}$ and $\phi_2=Ce^{ik_2x}$. |

| Matching | $A+B=C$ and $k_1(A-B)=k_2C$. |

| Amplitudes | $\displaystyle r=\frac BA=\frac{k_1-k_2}{k_1+k_2}$ and $\displaystyle t=\frac CA=\frac{2k_1}{k_1+k_2}$. |

| Flux result | $\displaystyle R=\|r\|^2$, $\displaystyle T=\frac{k_2}{k_1}\|t\|^2$, and $R+T=1$. |

| Generalised basis | The self-adjoint Hamiltonian has continuum eigenfunctions $\phi_{E,\alpha}$, with channel label $\alpha$ for incidence from the left or right. They are unit-flux or delta normalised. |

| Wave packet | $\displaystyle \Psi(x,t)=\sum_\alpha\int c_\alpha(E)e^{-iEt/\hbar}\phi_{E,\alpha}(x)\,dE$. |

## 3. Potential step with $0<E<V_0$

*Appendix C · Master solution tables*

| Parameters | $\displaystyle k=\frac{\sqrt{2mE}}{\hbar}$ and $\displaystyle \kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}$. |

| --- | --- |

| Admissible form | $\phi_1=Ae^{ikx}+Be^{-ikx}$ for $x<0$; boundedness gives $\phi_2=Ce^{-\kappa x}$ for $x>0$. |

| Matching | $A+B=C$ and $ik(A-B)=-\kappa C$. |

| Amplitudes | $\displaystyle \frac BA=\frac{k-i\kappa}{k+i\kappa}$ and $\displaystyle \frac CA=\frac{2k}{k+i\kappa}$. |

| Physical result | $R=1$. The right-hand tail has penetration length of order $1/\kappa$ and carries no steady transmitted current. |

| Generalised basis | These are continuum scattering eigenfunctions with an evanescent component. They are delta normalised, not square normalised. |

| Wave packet | $\displaystyle \Psi(x,t)=\int c(E)e^{-iEt/\hbar}\phi_E(x)\,dE$ over the relevant continuum energies. |

## 4. Finite barrier with $0<E<V_0$

*Appendix C · Master solution tables*

| Potential | $V=V_0$ for $0\le x\le L$ and $V=0$ outside. |

| --- | --- |

| Parameters | $\displaystyle k=\frac{\sqrt{2mE}}{\hbar}$ and $\displaystyle \kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}$. |

| Three regional forms | $\phi_I=Ae^{ikx}+Be^{-ikx}$, $\phi_{II}=Ce^{\kappa x}+De^{-\kappa x}$, and $\phi_{III}=Fe^{ikx}$. |

| Intermediary step | Match $\phi$ and $\phi'$ at both $x=0$ and $x=L$, then eliminate $B,C,D$ in favour of $A,F$. |

| Transmission | $\displaystyle T=\left[1+\frac{V_0^2}{4E(V_0-E)}\sinh^2(\kappa L)\right]^{-1}$. |

| Wide barrier | $\displaystyle T\simeq\frac{16E(V_0-E)}{V_0^2}e^{-2\kappa L}$ when $\kappa L\gg1$. |

| Generalised basis | The barrier has a continuous, two-channel scattering basis $\phi_{E,\alpha}$ for $E>0$. |

| Wave packet | $\displaystyle \Psi(x,t)=\sum_\alpha\int_0^\infty c_\alpha(E)e^{-iEt/\hbar}\phi_{E,\alpha}(x)\,dE$. |

## 5. Finite barrier with $E>V_0$

*Appendix C · Master solution tables*

| Parameters | $\displaystyle k=\frac{\sqrt{2mE}}{\hbar}$ and $\displaystyle q=\frac{\sqrt{2m(E-V_0)}}{\hbar}$. |

| --- | --- |

| Regional forms | $\phi_I=Ae^{ikx}+Be^{-ikx}$, $\phi_{II}=Ce^{iqx}+De^{-iqx}$, and $\phi_{III}=Fe^{ikx}$. |

| Intermediary step | Use the same four matching equations as for tunnelling, with $\kappa\mapsto iq$. |

| Transmission | $\displaystyle T=\left[1+\frac{V_0^2}{4E(E-V_0)}\sin^2(qL)\right]^{-1}$. |

| Resonance condition | $qL=n\pi$ gives $T=1$ because the reflected contributions cancel. |

| Generalised basis | The continuum eigenfunctions form two delta-normalised scattering channels. |

| Wave packet | $\displaystyle \Psi(x,t)=\sum_\alpha\int c_\alpha(E)e^{-iEt/\hbar}\phi_{E,\alpha}(x)\,dE$. |

## 6. Semi-infinite finite well

*Appendix C · Master solution tables*

| Potential | $V=\infty$ for $x<0$, $V=0$ for $0\le x\le L$, and $V=V_0$ for $x>L$. |

| --- | --- |

| Bound-state parameters | $k^2=2mE/\hbar^2$, $\kappa^2=2m(V_0-E)/\hbar^2$, and $k^2+\kappa^2=2mV_0/\hbar^2$. |

| Admissible form | $\displaystyle \phi_n(x)=N_n\begin{cases}\sin(k_nx),&0\le x\le L,\\ \sin(k_nL)e^{-\kappa_n(x-L)},&x\ge L.\end{cases}$ |

| Quantisation | Matching the logarithmic derivative at $L$ gives $\displaystyle k\cot(kL)=-\kappa$. |

| Normalisation | $\displaystyle N_n^{-2}=\frac L2-\frac{\sin(2k_nL)}{4k_n}+\frac{\sin^2(k_nL)}{2\kappa_n}$. |

| Basis status | The discrete bound states are orthonormal, but the complete basis also includes continuum states with $E\ge V_0$. |

| Full solution | A sum over bound states plus an integral over continuum states, each coefficient acquiring $e^{-iEt/\hbar}$. |

## 7. One-dimensional harmonic oscillator

*Appendix C · Master solution tables*

| Potential | $V(x)=\frac12m\omega^2x^2$ on $\mathbb R$. |

| --- | --- |

| Scaled equation | With $y=\sqrt{m\omega/\hbar}\,x$ and $\alpha=2E/(\hbar\omega)$, $\displaystyle \phi_{yy}+(\alpha-y^2)\phi=0$. |

| Endpoint factor | Normalisability selects $\phi=e^{-y^2/2}H(y)$. |

| Series step | $H''-2yH'+(\alpha-1)H=0$; the recurrence terminates only when $\alpha=2n+1$. |

| Operator step | $a\|0\rangle=0$ and $\displaystyle \|n\rangle=(a^\dagger)^n\|0\rangle/\sqrt{n!}$ give the same states. |

| Orthonormal basis | $\displaystyle \phi_n(x)=\frac{(m\omega/\pi\hbar)^{1/4}}{\sqrt{2^nn!}}H_n\!\left(\sqrt{\frac{m\omega}{\hbar}}x\right)e^{-m\omega x^2/(2\hbar)}$. |

| Spectrum | $\displaystyle E_n=\left(n+\frac12\right)\hbar\omega$, $n=0,1,2,\ldots$. |

| Full solution | $\displaystyle \Psi(x,t)=\sum_{n=0}^{\infty}c_n(0)e^{-iE_nt/\hbar}\phi_n(x)$. |

## 8. Three-dimensional rectangular box

*Appendix C · Master solution tables*

| Domain | $-a\le x\le a$, $-b\le y\le b$, $-c\le z\le c$, with the wavefunction zero on all six faces. |

| --- | --- |

| Separated form | $\phi(x,y,z)=X(x)Y(y)Z(z)$ isolates three one-dimensional self-adjoint box operators. |

| One-dimensional basis | $\displaystyle X_n(x)=\frac1{\sqrt a}\begin{cases}\cos(n\pi x/2a),&n\ \text{odd},\\ \sin(n\pi x/2a),&n\ \text{even},\end{cases}$ with analogous $Y_n,Z_n$. |

| Product basis | $\phi_{n_xn_yn_z}=X_{n_x}Y_{n_y}Z_{n_z}$ and $\iiint\phi_{\mathbf n}^*\phi_{\mathbf m}\,dV=\delta_{\mathbf n\mathbf m}$. |

| Spectrum | $\displaystyle E_{\mathbf n}=\frac{\hbar^2\pi^2}{8M}\left(\frac{n_x^2}{a^2}+\frac{n_y^2}{b^2}+\frac{n_z^2}{c^2}\right)$. |

| Full solution | $\displaystyle \Psi(\mathbf r,t)=\sum_{n_x,n_y,n_z}c_{n_xn_yn_z}(0)e^{-iE_{\mathbf n}t/\hbar}\phi_{n_xn_yn_z}(\mathbf r)$. |

## 9. Three-dimensional harmonic oscillator

*Appendix C · Master solution tables*

| Potential | $\displaystyle V=\frac12k_xx^2+\frac12k_yy^2+\frac12k_zz^2$, with $\omega_i=\sqrt{k_i/M}$. |

| --- | --- |

| Separated form | $\phi(x,y,z)=X(x)Y(y)Z(z)$ gives three one-dimensional oscillator eigenproblems. |

| Orthonormal basis | $\displaystyle \phi_{n_xn_yn_z}=X_{n_x}^{(\omega_x)}Y_{n_y}^{(\omega_y)}Z_{n_z}^{(\omega_z)}$, the tensor product of three Hermite-Gaussian bases. |

| Spectrum | $\displaystyle E_{\mathbf n}=\left(n_x+\frac12\right)\hbar\omega_x+\left(n_y+\frac12\right)\hbar\omega_y+\left(n_z+\frac12\right)\hbar\omega_z$. |

| Isotropic case | If $\omega_x=\omega_y=\omega_z=\omega$, then $E_N=(N+\frac32)\hbar\omega$ with $N=n_x+n_y+n_z$. |

| Full solution | $\displaystyle \Psi(\mathbf r,t)=\sum_{n_x,n_y,n_z}c_{\mathbf n}(0)e^{-iE_{\mathbf n}t/\hbar}\phi_{\mathbf n}(\mathbf r)$. |

## Central-potential template

*Appendix C · Master solution tables*

| Commuting operators | $\hat H$, $\hat L^2$ and $\hat L_z$ share a joint eigenbasis. |

| --- | --- |

| Separated form | $\phi(r,\theta,\varphi)=R_{El}(r)Y_{lm}(\theta,\varphi)$. |

| Angular basis | $\int Y_{lm}^*Y_{l'm'}\,d\Omega=\delta_{ll'}\delta_{mm'}$; $L^2Y_{lm}=\hbar^2l(l+1)Y_{lm}$ and $L_zY_{lm}=\hbar mY_{lm}$. |

| Radial reduction | With $u=rR$, $\displaystyle -\frac{\hbar^2}{2M}u''+\left[V(r)+\frac{\hbar^2l(l+1)}{2Mr^2}\right]u=Eu$ and $u(0)=0$. |

| Radial inner product | $\int_0^\infty R_{El}^*R_{E'l}\,r^2dr=\int_0^\infty u_{El}^*u_{E'l}\,dr$. |

| Complete expansion | Sum over discrete radial labels and $l,m$, plus an energy integral when the radial spectrum has a continuum. |

| Time dependence | Every joint eigenfunction is multiplied by $e^{-iEt/\hbar}$ in the final expansion. |

## 10. Spherical infinite well

*Appendix C · Master solution tables*

| Potential and domain | $V=0$ for $0\le r\le a$ and $V=\infty$ for $r>a$. |

| --- | --- |

| Radial equation | $\displaystyle R''+\frac2rR'+\left[k^2-\frac{l(l+1)}{r^2}\right]R=0$. |

| Admissible form | $R=A j_l(kr)+B n_l(kr)$; regularity at $r=0$ forces $B=0$. |

| Quantisation | $R(a)=0$ gives $j_l(ka)=0$; if $\alpha_{nl}$ is the $n$-th positive zero, $k_{nl}=\alpha_{nl}/a$. |

| Orthonormal basis | $\displaystyle \phi_{nlm}=\frac{\sqrt2}{a^{3/2}\|j_{l+1}(\alpha_{nl})\|}j_l\!\left(\alpha_{nl}\frac ra\right)Y_{lm}(\theta,\varphi)$. |

| Spectrum | $\displaystyle E_{nl}=\frac{\hbar^2\alpha_{nl}^2}{2Ma^2}$, independent of $m$. |

| Full solution | $\displaystyle \Psi(\mathbf r,t)=\sum_{n,l,m}c_{nlm}(0)e^{-iE_{nl}t/\hbar}\phi_{nlm}(\mathbf r)$. |

## 11. Hydrogen-like atom

*Appendix C · Master solution tables*

| Potential | $\displaystyle V(r)=-\frac{Ze^2}{4\pi\varepsilon_0r}$, with reduced mass $\mu$. |

| --- | --- |

| Scaled radial equation | $\rho=2\kappa r$, $\kappa=\sqrt{-2\mu E}/\hbar$ and $\eta=\mu Ze^2/(4\pi\varepsilon_0\hbar^2\kappa)$. |

| Endpoint factors | Regularity and decay select $u(\rho)=\rho^{l+1}e^{-\rho/2}v(\rho)$. |

| Series step | $\rho v''+(2l+2-\rho)v'+(\eta-l-1)v=0$; termination requires $\eta=n=p_{\max}+l+1$. |

| Orthonormal basis | With $\rho=2Zr/(na_0)$, $\displaystyle R_{nl}=\left(\frac{2Z}{na_0}\right)^{3/2} \sqrt{\frac{(n-l-1)!}{2n(n+l)!}}\, e^{-\rho/2}\rho^lL_{n-l-1}^{2l+1}(\rho)$, and $\phi_{nlm}=R_{nl}Y_{lm}$. |

| Spectrum | $\displaystyle E_n=-\frac{\mu Z^2e^4}{2(4\pi\varepsilon_0)^2\hbar^2n^2}$, with $n\ge1$, $0\le l\le n-1$, $-l\le m\le l$. |

| Full solution | $\displaystyle \Psi(\mathbf r,t)=\sum_{n,l,m}c_{nlm}(0)e^{-iE_nt/\hbar}\phi_{nlm}(\mathbf r)$ for the bound-state subspace; continuum states must be added for a completely general state. |
