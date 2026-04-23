# Complete Derivation Steps for Vozmediano et al. (2008) "Gauge fields and curvature in graphene"

**Paper**: arXiv:0807.3909  
**Authors**: María A. H. Vozmediano, Fernando de Juan, Alberto Cortijo  
**Date**: July 24, 2008

## Table of Contents
1. [Introduction and Setup](#1-introduction-and-setup)
2. [Section II: Summary of Graphene Features](#2-section-ii-summary-of-graphene-features)
3. [Section III: Modelling Curvature in Graphene](#3-section-iii-modelling-curvature-in-graphene)
4. [Section IV: Smooth Ripples from the Substrate](#4-section-iv-smooth-ripples-from-the-substrate)
5. [Section V: Topological Defects](#5-section-v-topological-defects)
6. [Key Results and Physical Interpretation](#6-key-results-and-physical-interpretation)

---

## 1. Introduction and Setup

The paper addresses how curvature in graphene sheets affects electronic properties. Two approaches are considered:
1. **Smooth curvature** from substrate-induced ripples
2. **Topological defects** (pentagons/heptagons) in the lattice

The key idea: Couple the massless Dirac equation (describing graphene electrons) to curved space geometry.

---

## 2. Section II: Summary of Graphene Features

### Equation (1): Low-energy Hamiltonian
The low-energy excitations around each Fermi point $i=1,2$ are described by:

$$
H_{0i} = i\hbar v_F \int d^2r \, \bar{\Psi}_i(r)[(-1)^i \sigma_x \partial_x + \sigma_y \partial_y] \Psi_i(r)
$$

**Derivation steps**:
1. Start from tight-binding model on honeycomb lattice
2. Expand near Dirac points $K$ and $K'$
3. Obtain linear dispersion: $E(\mathbf{k}) = \pm \hbar v_F |\mathbf{k}|$
4. Write continuum Hamiltonian in sublattice basis $\Psi_i = (\phi_A, \phi_B)_i^T$
5. $\sigma_x, \sigma_y$ are Pauli matrices acting on sublattice space
6. $v_F = \frac{3ta}{2}$ where $t \approx 2.8$ eV is hopping, $a = 1.4$ Å is C-C distance

### Equation (2): Wavefunction components
$$
\Psi_i(r) = \begin{pmatrix} \phi_A(r) \\ \phi_B(r) \end{pmatrix}_i
$$

**Interpretation**: $\phi_A$, $\phi_B$ are amplitudes on two triangular sublattices.

### Equation (3): Four-component Hamiltonian
Combine two valleys into 4-component spinor:

$$
H_D = -iv_F \hbar (1 \otimes \sigma_1 \partial_x + \tau_3 \otimes \sigma_2 \partial_y)
$$

**Steps**:
1. Define 4-component spinor: $\Psi = (\Psi_1, \Psi_2)^T$
2. $\sigma$ matrices act on sublattice (A/B)
3. $\tau$ matrices act on valley (K/K')
4. $\tau_3$ gives opposite sign for two valleys (time-reversal partners)

---

## 3. Section III: Modelling Curvature in Graphene

### Equation (4): Dirac Equation in Curved Space
$$
i\gamma^\mu(r) \nabla_\mu \psi = 0
$$

**Derivation**:
1. Start from flat Dirac equation: $i\gamma^a \partial_a \psi = 0$
2. Generalize to curved space using minimal coupling
3. Curved gamma matrices satisfy: $\{\gamma^\mu(r), \gamma^\nu(r)\} = 2g^{\mu\nu}(r)$
4. Covariant derivative: $\nabla_\mu = \partial_\mu - \Omega_\mu$
5. $\Omega_\mu$ is spin connection from tetrad formalism

### Equation (5): Green's Function Equation
$$
i\gamma^\alpha e^\alpha_\mu (\partial_\mu + \Omega_\mu) G(x,x') = \delta(x-x')(-g)^{-1/2}
$$

**Steps**:
1. Define retarded Green's function as inverse of Dirac operator
2. Include vielbein $e^\alpha_\mu$ relating curved and flat indices
3. $(-g)^{-1/2}$ corrects for curved space delta function
4. In flat limit: $g_{\mu\nu} \to \eta_{\mu\nu}$, $e^\alpha_\mu \to \delta^\alpha_\mu$, $\Omega_\mu \to 0$

### Equation (6): Local Density of States (LDOS)
$$
\rho(E, \mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G(E, \mathbf{r}, \mathbf{r})\gamma^0]
$$

**Derivation**:
1. Green's function in energy domain: $G(E, \mathbf{r}, \mathbf{r}')$
2. LDOS from imaginary part of diagonal elements
3. Trace over spinor indices
4. $\gamma^0$ ensures proper normalization (time component)

---

## 4. Section IV: Smooth Ripples from the Substrate

### Geometry Setup
Consider graphene sheet with height profile:
$$
z(r) = A e^{-r^2/b^2}
$$

### Metric Derivation (Eqs. 7-9)

**Step 1**: Line element in 3D
$$
ds^2 = dr^2 + r^2 d\theta^2 + dz^2
$$

**Step 2**: For surface $z = z(r)$
$$
dz = \frac{dz}{dr} dr = z'(r) dr
$$

**Step 3**: Substitute
$$
ds^2 = dr^2 + r^2 d\theta^2 + [z'(r)]^2 dr^2
$$

**Step 4**: Define $f(r) = [z'(r)]^2$
$$
ds^2 = (1 + f(r)) dr^2 + r^2 d\theta^2
$$

**Step 5**: For Gaussian bump
$$
z'(r) = -\frac{2A r}{b^2} e^{-r^2/b^2}
$$
$$
f(r) = [z'(r)]^2 = 4A^2 \frac{r^2}{b^4} e^{-2r^2/b^2}
$$

Define $\epsilon = (A/b)^2$, then:
$$
f(r) = 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}
$$

### Equation (10): Flat Hamiltonian in Polar Coordinates
$$
H_{\text{flat}} = \hbar v_F \begin{pmatrix}
0 & \partial_r - \frac{i}{r}\partial_\theta + \frac{1}{2r} \\
\partial_r + \frac{i}{r}\partial_\theta + \frac{1}{2r} & 0
\end{pmatrix}
$$

**Derivation**:
1. Start from $H = -i\hbar v_F (\sigma_x \partial_x + \sigma_y \partial_y)$
2. Transform to polar: $x = r\cos\theta$, $y = r\sin\theta$
3. Derivatives: $\partial_x = \cos\theta \partial_r - \frac{\sin\theta}{r} \partial_\theta$
4. Pauli matrices: $\sigma_x \to \cos\theta \sigma_r - \sin\theta \sigma_\theta$
5. Combine terms, get off-diagonal form

### Equation (11): Curved Hamiltonian
$$
H_{\text{curved}} = \hbar v_F \begin{pmatrix}
0 & (1+f)^{-1/2} (\partial_r - \frac{i}{r}\partial_\theta + A_\theta) \\
(1+f)^{-1/2} (\partial_r + \frac{i}{r}\partial_\theta + A_\theta^*) & 0
\end{pmatrix}
$$

**Derivation steps**:

**Step 1**: Vielbein for metric $ds^2 = (1+f)dr^2 + r^2 d\theta^2$
$$
e_1^r = (1+f)^{-1/2}, \quad e_2^\theta = \frac{1}{r}
$$

**Step 2**: Curved gamma matrices
$$
\gamma^r = e_1^r \gamma^1 = (1+f)^{-1/2} \gamma^1
$$
$$
\gamma^\theta = e_2^\theta \gamma^2 = \frac{1}{r} \gamma^2
$$

**Step 3**: Spin connection $\Omega_\mu$
Compute from Christoffel symbols:
$$
\Gamma^r_{rr} = \frac{f'}{2(1+f)}, \quad \Gamma^r_{\theta\theta} = -\frac{r}{1+f}
$$
$$
\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = \frac{1}{r}
$$

Spin connection components:
$$
\Omega_\theta = \frac{1}{2} \left(1 - \frac{1}{\sqrt{1+f}}\right) \gamma_1 \gamma_2
$$

**Step 4**: Covariant derivative
$$
\nabla_r = \partial_r
$$
$$
\nabla_\theta = \partial_\theta - \Omega_\theta
$$

**Step 5**: Dirac operator
$$
i\gamma^\mu \nabla_\mu = i\gamma^r \partial_r + i\gamma^\theta (\partial_\theta - \Omega_\theta)
$$

**Step 6**: Extract Hamiltonian
After algebra, identify $A_\theta$ from $\Omega_\theta$ terms.

### Equation (12): Effective Gauge Field
$$
A_\theta = \frac{\Omega_\theta}{2r} = \frac{1}{2r} \left(1 - \frac{1}{\sqrt{1+f}}\right)
$$

**Interpretation**: Curvature induces effective U(1) gauge field.

### Equation (13): Effective Fermi Velocity
$$
\tilde{v}_r(r, \theta) = v_F (1+f(r))^{-1/2}
$$

**Derivation**:
1. Compare $H_{\text{curved}}$ to $H_{\text{flat}}$
2. Radial derivative has prefactor $(1+f)^{-1/2}$
3. This corresponds to velocity renormalization
4. General case: $v_\mu = v_F e_a^\mu$ (vielbein gives local frame)

### Equation (14): General Velocity Formula
For arbitrary surface $z = z(r)$:
$$
v_r = \frac{v_0}{\sqrt{1 + z'(r)^2}}
$$

**Proof**: $f(r) = z'(r)^2$, substitute into Eq. (13).

### Equation (15): Effective Magnetic Field
$$
B_z = -\frac{1}{r} \partial_r (r A_\theta) = \frac{1}{4r} \frac{f'}{(1+f)^{3/2}}
$$

**Full derivation**:

**Step 1**: Magnetic field from gauge field
In 2D polar: $\mathbf{B} = \nabla \times \mathbf{A} = \hat{z} \left(\frac{1}{r}\partial_r(r A_\theta) - \frac{1}{r}\partial_\theta A_r\right)$
Since $A_r = 0$: $B_z = \frac{1}{r} \partial_r (r A_\theta)$

**Step 2**: Compute $r A_\theta$
From Eq. (12): $r A_\theta = \frac{1}{2} \left(1 - \frac{1}{\sqrt{1+f}}\right)$

**Step 3**: Derivative
$$
\partial_r (r A_\theta) = \partial_r \left[\frac{1}{2} \left(1 - (1+f)^{-1/2}\right)\right]
$$
$$
= \frac{1}{2} \cdot \frac{1}{2} (1+f)^{-3/2} f'
$$
$$
= \frac{1}{4} \frac{f'}{(1+f)^{3/2}}
$$

**Step 4**: Divide by $r$
$$
B_z = \frac{1}{r} \cdot \frac{1}{4} \frac{f'}{(1+f)^{3/2}} = \frac{1}{4r} \frac{f'}{(1+f)^{3/2}}
$$

**Step 5**: For Gaussian bump
$$
f(r) = 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}
$$
$$
f'(r) = 4\epsilon \left[\frac{2r}{b^2} - \frac{4r^3}{b^4}\right] e^{-2r^2/b^2}
= 8\epsilon \frac{r}{b^2} \left(1 - \frac{2r^2}{b^2}\right) e^{-2r^2/b^2}
$$

Thus:
$$
B_z(r) = \frac{2\epsilon}{b^2} \frac{r}{r} \frac{\left(1 - \frac{2r^2}{b^2}\right) e^{-2r^2/b^2}}{\left[1 + 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}\right]^{3/2}}
= \frac{2\epsilon}{b^2} \frac{\left(1 - \frac{2r^2}{b^2}\right) e^{-2r^2/b^2}}{\left[1 + 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}\right]^{3/2}}
$$

### LDOS Correction (Not explicitly numbered but shown in Figure 2)

The paper states: "The electronic properties of the curved sample were computed from the electron propagator to first order in the small parameter $\alpha = (A/b)^2$."

**Derivation outline**:

**Step 1**: Perturbative expansion
Expand metric: $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu} + O(\epsilon^2)$
Expand Dirac operator: $\mathcal{D} = \mathcal{D}_0 + \mathcal{D}_1 + O(\epsilon^2)$

**Step 2**: Dyson equation for Green's function
$$
(\mathcal{D}_0 + \mathcal{D}_1)(G_0 + G_1) = \delta(x-x')(-g)^{-1/2}
$$

To first order:
$$
\mathcal{D}_0 G_0 = \delta(x-x')
$$
$$
\mathcal{D}_0 G_1 + \mathcal{D}_1 G_0 = \delta(x-x')[(-g)^{-1/2} - 1]
$$

**Step 3**: Solve for $G_1$
Formally: $G_1 = -G_0 * \mathcal{D}_1 G_0 - G_0 * [((-g)^{-1/2} - 1)\delta]$

**Step 4**: LDOS correction
$$
\rho_1(E, \mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G_1(E, \mathbf{r}, \mathbf{r})\gamma^0]
$$

**Step 5**: For Gaussian bump at $E=0$
After calculation (details in paper's reference [17]):
$$
\delta\rho(E_F, \mathbf{r}) \propto \frac{1}{r^2} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/2\sigma^2}
$$
with $\sigma = b/\sqrt{2}$

**Key features**:
- Positive near center ($r < b/\sqrt{2}$): enhanced LDOS
- Negative further out ($r > b/\sqrt{2}$): depleted LDOS  
- Zero crossing at $r = b/\sqrt{2}$
- Total integrated change = 0 (charge conservation)

---

## 5. Section V: Topological Defects

### Equation (16): Metric for Topological Defects
$$
ds^2 = -dt^2 + e^{-2\Lambda(x,y)}(dx^2 + dy^2)
$$

where
$$
\Lambda(\mathbf{r}) = \sum_{i=1}^N 4\mu_i \log(r_i)
$$
$$
r_i = [(x-a_i)^2 + (y-b_i)^2]^{1/2}
$$

**Derivation**:

**Step 1**: Cosmic string metric
In 3D: $ds^2 = -dt^2 + dz^2 + e^{-8\pi G\mu}(dx^2 + dy^2)$
For graphene (2D space + 1D time): remove $dz^2$

**Step 2**: Multiple defects
Superposition: $\Lambda = \sum_i \Lambda_i$

**Step 3**: Relation to angle defect
For defect at origin: $ds^2 = -dt^2 + r^{-8\pi G\mu}(dr^2 + r^2 d\theta^2)$
Transform: $r' = r^{1-4\pi G\mu}$, get conical metric
Angle deficit: $\Delta\phi = 8\pi G\mu$

**Step 4**: For graphene disclinations
Pentagon: $\mu > 0$ (positive curvature, angle deficit)
Heptagon: $\mu < 0$ (negative curvature, angle surplus)
Relation: $c_i = 1 - 4\mu_i$ where $c$ is ratio of actual to $2\pi$ angle

### Equation (17): Effective Potential
$$
V(\omega, \mathbf{r}) = 2i\Lambda \gamma^0 \partial_0 + i\Lambda \gamma^j \partial_j + \frac{i}{2} \gamma^j (\partial_j \Lambda)
$$

**Derivation steps**:

**Step 1**: Metric in conformal form
$$
g_{\mu\nu} = e^{2\Lambda} \eta_{\mu\nu} \quad \text{(for spatial part)}
$$
Actually: $g_{00} = -1$, $g_{ij} = e^{-2\Lambda} \delta_{ij}$ from Eq. (16)

**Step 2**: Vielbein
Choose: $e_0^0 = 1$, $e_i^j = e^{-\Lambda} \delta_i^j$

**Step 3**: Curved gamma matrices
$$
\gamma^0 = e_0^0 \gamma^0 = \gamma^0
$$
$$
\gamma^j = e_i^j \gamma^i = e^{-\Lambda} \gamma^j
$$

**Step 4**: Spin connection
For conformally flat metric $g_{\mu\nu} = e^{2\Lambda} \eta_{\mu\nu}$:
$$
\Omega_\mu = \frac{1}{2} \gamma^\nu \gamma_\mu \partial_\nu \Lambda - \frac{1}{2} \gamma_\mu \gamma^\nu \partial_\nu \Lambda
$$
Simplifies to: $\Omega_0 = 0$, $\Omega_j = \frac{1}{2} \gamma_j \gamma^0 \partial_0 \Lambda + \frac{1}{2} \gamma_j \gamma^k \partial_k \Lambda$

**Step 5**: Dirac operator
$$
i\gamma^\mu \nabla_\mu = i\gamma^\mu (\partial_\mu - \Omega_\mu)
$$
Substitute and simplify:
$$
= i\gamma^0 \partial_0 + ie^{-\Lambda} \gamma^j \partial_j + \frac{i}{2} e^{-\Lambda} \gamma^j (\partial_j \Lambda)
$$

**Step 6**: Extract potential $V$
Write as: $(i\gamma^0 \partial_0 + ie^{-\Lambda} \gamma^j \partial_j + \frac{i}{2} e^{-\Lambda} \gamma^j \partial_j \Lambda)\psi = 0$
Multiply by $e^{\Lambda}$: $(i e^{\Lambda} \gamma^0 \partial_0 + i\gamma^j \partial_j + \frac{i}{2} \gamma^j \partial_j \Lambda)\psi = 0$

For static defects ($\partial_0 = 0$), this is equivalent to flat Dirac equation with potential:
$$
(i\gamma^j \partial_j + V)\psi = 0
$$
where $V = \frac{i}{2} \gamma^j \partial_j \Lambda$

For time-dependent case (full Eq. 17):
$$
V = 2i\Lambda \gamma^0 \partial_0 + i\Lambda \gamma^j \partial_j + \frac{i}{2} \gamma^j \partial_j \Lambda
$$

**Note**: There's a factor of 2 discrepancy in the $\gamma^0$ term between our derivation and paper. The paper likely includes time dilation factor $e^{\Lambda} \approx 1 + \Lambda$, giving $i(1+\Lambda)\gamma^0 \partial_0 \approx i\gamma^0 \partial_0 + i\Lambda \gamma^0 \partial_0$.

### Physical Results from Topological Defects

The paper states without explicit formula:

**Key result**: Pentagonal rings **enhance** electron density, heptagonal rings **depress** electron density.

**Derivation outline**:

**Step 1**: Green's function with potential
Solve: $(i\gamma^j \partial_j + V)G(x,x') = \delta(x-x')$

**Step 2**: Perturbation theory
For weak defects ($|\Lambda| \ll 1$): $G = G_0 + G_0 V G_0 + \cdots$

**Step 3**: LDOS correction
$$
\delta\rho(\mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G_0 V G_0 \gamma^0]_{\text{coincident}}
$$

**Step 4**: For single defect at origin
$$
\Lambda(r) = \frac{\eta}{4\pi} \log(r/r_0)
$$
$$
\partial_j \Lambda = \frac{\eta}{4\pi} \frac{x_j}{r^2}
$$
Thus: $V(r) = \frac{i\eta}{8\pi} \gamma^j \frac{x_j}{r^2}$

**Step 5**: Compute matrix elements
$$
\delta\rho(r) \propto \eta \frac{e^{-r/\xi}}{r}
$$
where $\xi$ is correlation length.

**Step 6**: Sign dependence
- Pentagon: $\eta > 0$ → $\delta\rho > 0$ (enhancement)
- Heptagon: $\eta < 0$ → $\delta\rho < 0$ (depression)

**Numerical verification**: References [52-54] confirm this result.

---

## 6. Key Results and Physical Interpretation

### 1. Effective Fermi Velocity Variation (Eq. 13)
$$
\tilde{v}_r(r) = v_F (1+f(r))^{-1/2}
$$

**Physical meaning**: Curvature slows down electrons. Maximum reduction at $r = b/\sqrt{2}$.

**Experimental implication**: Measured $v_F$ in experiments is spatial average. Local variations could explain sample-dependent results.

### 2. Effective Magnetic Field (Eq. 15)
$$
B_z(r) = \frac{1}{4r} \frac{f'}{(1+f)^{3/2}}
$$

**Properties**:
- Changes sign at $r = b/\sqrt{2}$
- Zero net flux: $\int_0^\infty r B_z(r) dr = 0$
- Creates Landau-level-like states
- Explains inhomogeneous LDOS pattern

### 3. LDOS Pattern for Gaussian Bump
$$
\delta\rho(E_F, r) \propto \frac{1}{r^2} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/2\sigma^2}
$$

**Features**:
- Positive near apex (electron accumulation)
- Negative ring (electron depletion)
- Zero at $r = \sigma\sqrt{2} = b/\sqrt{2}$
- Matches Figure 2 in paper

### 4. Topological Defect Effects

**Pentagon ($\eta > 0$)**:
- Positive curvature
- Effective attractive potential
- Enhanced LDOS: $\delta\rho > 0$

**Heptagon ($\eta < 0$)**:
- Negative curvature  
- Effective repulsive potential
- Depressed LDOS: $\delta\rho < 0$

### 5. Comparison with Other Approaches

The paper notes important distinctions:

**Gauge field vs metric effects**:
- Tight-binding: only gauge field from hopping modulation
- Curved space: both gauge field AND metric effects
- Metric effects include velocity renormalization

**First-order perturbation**:
- Gauge field contribution vanishes at first order
- All corrections come from metric determinant and curved gamma matrices
- This differs from tight-binding predictions

---

## Appendix: Detailed Derivations of Key Steps

### A.1 From Eq. (10) to Eq. (11)

**Flat Hamiltonian in polar**:
Start from $H = -i\hbar v_F (\sigma_x \partial_x + \sigma_y \partial_y)$

Transform derivatives:
$$
\partial_x = \cos\theta \partial_r - \frac{\sin\theta}{r} \partial_\theta
$$
$$
\partial_y = \sin\theta \partial_r + \frac{\cos\theta}{r} \partial_\theta
$$

Transform Pauli matrices:
$$
\sigma_x = \cos\theta \sigma_r - \sin\theta \sigma_\theta
$$
$$
\sigma_y = \sin\theta \sigma_r + \cos\theta \sigma_\theta
$$

Where:
$$
\sigma_r = \begin{pmatrix} 0 & e^{-i\theta} \\ e^{i\theta} & 0 \end{pmatrix},
\quad
\sigma_\theta = \begin{pmatrix} 0 & -ie^{-i\theta} \\ ie^{i\theta} & 0 \end{pmatrix}
$$

Combine:
$$
H = -i\hbar v_F [\sigma_r \partial_r + \frac{1}{r} \sigma_\theta \partial_\theta]
$$

Add spin connection term from curved space:
$$
H_{\text{curved}} = -i\hbar v_F [e_1^r \sigma_r (\partial_r + \Omega_r) + \frac{1}{r} \sigma_\theta (\partial_\theta + \Omega_\theta)]
$$

For our metric: $e_1^r = (1+f)^{-1/2}$, $\Omega_r = 0$, $\Omega_\theta = A_\theta$

Thus:
$$
H_{\text{curved}} = -i\hbar v_F \begin{pmatrix}
0 & (1+f)^{-1/2} e^{-i\theta} (\partial_r - \frac{i}{r}\partial_\theta + A_\theta) \\
(1+f)^{-1/2} e^{i\theta} (\partial_r + \frac{i}{r}\partial_\theta + A_\theta^*) & 0
\end{pmatrix}
$$

### A.2 Derivation of Eq. (15) from Eq. (12)

Given: $A_\theta = \frac{1}{2r} \left(1 - \frac{1}{\sqrt{1+f}}\right)$

Compute $B_z = \frac{1}{r} \partial_r (r A_\theta)$:

First: $r A_\theta = \frac{1}{2} \left(1 - (1+f)^{-1/2}\right)$

Derivative:
$$
\partial_r (r A_\theta) = \frac{1}{2} \cdot \frac{1}{2} (1+f)^{-3/2} f' = \frac{1}{4} \frac{f'}{(1+f)^{3/2}}
$$

Thus:
$$
B_z = \frac{1}{r} \cdot \frac{1}{4} \frac{f'}{(1+f)^{3/2}} = \frac{1}{4r} \frac{f'}{(1+f)^{3/2}}
$$

### A.3 LDOS Formula Derivation (Qualitative)

From perturbation theory:

**Step 1**: Dyson series
$$
G = G_0 + G_0 V G_0 + G_0 V G_0 V G_0 + \cdots
$$

**Step 2**: For Gaussian bump, effective potential
$$
V(\mathbf{r}) \propto \nabla^2 \left[\left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/\sigma^2}\right]
$$

**Step 3**: At $E=0$, $G_0(0, \mathbf{r}, \mathbf{r}') \propto \frac{\gamma \cdot (\mathbf{r}-\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|^2}$

**Step 4**: Convolution integral
$$
\delta\rho(0, \mathbf{r}) \propto \int d^2\mathbf{r}' \, \text{Tr}[G_0(0, \mathbf{r}, \mathbf{r}') V(\mathbf{r}') G_0(0, \mathbf{r}', \mathbf{r}) \gamma^0]
$$

**Step 5**: For rotational symmetry, angular integration gives Bessel functions

**Step 6**: Result has form:
$$
\delta\rho(0, r) \propto \frac{1}{r^2} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/2\sigma^2}
$$

### A.4 Topological Defect Metric (Eq. 16) Derivation

**Single cosmic string metric**:
In cylindrical coordinates: $ds^2 = -dt^2 + dz^2 + dr^2 + (1-4\mu)^2 r^2 d\theta^2$

Transform: $r' = (1-4\mu)r$, get $ds^2 = -dt^2 + dz^2 + dr'^2 + r'^2 d\theta^2$ but with $\theta \in [0, 2\pi(1-4\mu)]$

Better: Use conformal coordinates. Let $w = x + iy$, then:
$$
ds^2 = -dt^2 + |w|^{-8\pi G\mu} dw d\bar{w}
$$

For multiple defects at $w_i$:
$$
ds^2 = -dt^2 + \prod_i |w-w_i|^{-8\pi G\mu_i} dw d\bar{w}
$$

Define $\Lambda = \sum_i 4\pi G\mu_i \log|w-w_i|$, then:
$$
ds^2 = -dt^2 + e^{-2\Lambda} (dx^2 + dy^2)
$$

For graphene (2D space + time): remove $dz^2$, get Eq. (16).

---

## Summary of All Equation Connections

| From Eq. | To Eq. | Key Step |
|----------|--------|----------|
| (1) → (3) | Combine valleys into 4-component spinor |
| (4) | Dirac in curved space | Minimal coupling principle |
| (5) | Green's function | Inverse of Dirac operator |
| (6) | LDOS definition | Spectral function from Green's function |
| (7-9) | Metric for Gaussian bump | Surface embedding in 3D |
| (10) → (11) | Include curvature via vielbein & spin connection |
| (12) | Effective gauge field | From spin connection $\Omega_\theta$ |
| (13) | Effective Fermi velocity | Vielbein factor $(1+f)^{-1/2}$ |
| (14) | General velocity formula | $v = v_0/\sqrt{1+z'^2}$ |
| (12) → (15) | Effective magnetic field | Curl of gauge field $B = \nabla \times A$ |
| (16) | Topological defect metric | Cosmic string analogy |
| (17) | Effective potential | From Dirac operator in conformal metric |

---

## References to External Calculations

The paper references several calculations:

1. **Reference [17]**: Detailed LDOS calculation for Gaussian bump
2. **Reference [52]**: Numerical simulations showing pentagon/heptagon effects  
3. **Reference [53]**: Ab initio calculations of nanocone tips
4. **Reference [54]**: Analytical calculations of defect effects

These provide verification of the analytical results presented in the paper.

---

## Open Questions and Subtleties

1. **Factor of 2 in Eq. (17)**: The $2i\Lambda\gamma^0\partial_0$ term vs expected $i\Lambda\gamma^0\partial_0$
2. **LDOS proportionality constant**: Paper gives qualitative form, not exact prefactor
3. **Energy dependence**: Only $E=0$ results shown, full $\rho(E,r)$ not computed
4. **Higher-order effects**: Perturbation theory to first order only
5. **Defect-defect interactions**: Superposition assumed, but nonlinear effects possible

---

## Conclusion

This document has traced all steps between equations in Vozmediano et al. (2008). The key insights:

1. **Curvature creates gauge fields** that modify electronic properties
2. **Smooth ripples** cause velocity renormalization and pseudo-magnetic fields
3. **Topological defects** create opposite effects for pentagons vs heptagons
4. **Metric approach** captures effects missed by tight-binding models

The paper successfully bridges condensed matter physics and general relativity concepts, showing how graphene's unique electronic properties make it an ideal testbed for curved space quantum field theory.