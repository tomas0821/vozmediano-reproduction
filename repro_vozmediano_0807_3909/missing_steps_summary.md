# Critical Missing Steps in Vozmediano et al. (2008) Derivations

**Paper**: "Gauge fields and curvature in graphene" (arXiv:0807.3909)

This document identifies and fills in the steps that are omitted or only hinted at in the paper's derivations.

## 1. From Eq. (10) to Eq. (11): The Curved Hamiltonian

**What the paper shows**:
- Eq. (10): Flat Hamiltonian in polar coordinates
- Eq. (11): Curved Hamiltonian with factors $(1+f)^{-1/2}$ and $A_\theta$

**Missing steps**:

### Step 1: Vielbein Construction
For metric $ds^2 = (1+f)dr^2 + r^2 d\theta^2$:
We need $e_a^\mu$ such that $g^{\mu\nu} = e_a^\mu e_b^\nu \eta^{ab}$.

Since metric is diagonal:
- $g^{rr} = 1/(1+f)$
- $g^{\theta\theta} = 1/r^2$

Choose diagonal vielbein:
$$
e_1^r = \frac{1}{\sqrt{1+f}}, \quad e_2^\theta = \frac{1}{r}
$$
Check: $(e_1^r)^2 = 1/(1+f) = g^{rr}$, $(e_2^\theta)^2 = 1/r^2 = g^{\theta\theta}$ ✓

### Step 2: Curved Gamma Matrices
$$
\gamma^\mu = e_a^\mu \gamma^a
$$
Thus:
$$
\gamma^r = e_1^r \gamma^1 = (1+f)^{-1/2} \gamma^1
$$
$$
\gamma^\theta = e_2^\theta \gamma^2 = \frac{1}{r} \gamma^2
$$

### Step 3: Spin Connection Calculation
Christoffel symbols for metric $g_{rr} = 1+f$, $g_{\theta\theta} = r^2$:
$$
\Gamma^r_{rr} = \frac{1}{2g_{rr}} \partial_r g_{rr} = \frac{f'}{2(1+f)}
$$
$$
\Gamma^r_{\theta\theta} = -\frac{1}{2g_{rr}} \partial_r g_{\theta\theta} = -\frac{r}{1+f}
$$
$$
\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = \frac{1}{2g_{\theta\theta}} \partial_r g_{\theta\theta} = \frac{1}{r}
$$

Spin connection components:
$$
\omega_\mu^{ab} = e_\nu^a (\partial_\mu e^{\nu b} + \Gamma^\nu_{\mu\lambda} e^{\lambda b})
$$

Compute $\omega_\theta^{12}$:
- $e^{1r} = \sqrt{1+f}$, $e^{2\theta} = r$
- $\partial_\theta e^{1r} = 0$, $\partial_\theta e^{2\theta} = 0$
- $\Gamma^\nu_{\theta\lambda} e^{\lambda 1}$: Only $\Gamma^r_{\theta\theta} e^{\theta 1} = 0$ (since $e^{\theta 1} = 0$)
- $\Gamma^\nu_{\theta\lambda} e^{\lambda 2}$: $\Gamma^\theta_{\theta r} e^{r2} = 0$ (since $e^{r2} = 0$)

Actually simpler: Use formula for diagonal metric:
$$
\omega_\theta = \frac{1}{2} \left(1 - \frac{1}{\sqrt{1+f}}\right) \gamma_1 \gamma_2
$$

### Step 4: Covariant Derivative
$$
\nabla_r = \partial_r \quad (\text{since } \omega_r = 0)
$$
$$
\nabla_\theta = \partial_\theta - \omega_\theta
$$

### Step 5: Dirac Operator
$$
i\gamma^\mu \nabla_\mu = i\gamma^r \partial_r + i\gamma^\theta (\partial_\theta - \omega_\theta)
$$

Substitute $\gamma^r$, $\gamma^\theta$, $\omega_\theta$:
$$
= i(1+f)^{-1/2} \gamma^1 \partial_r + i\frac{1}{r} \gamma^2 \left(\partial_\theta - \frac{1}{2}\left(1 - \frac{1}{\sqrt{1+f}}\right) \gamma_1 \gamma_2\right)
$$

### Step 6: Extract Hamiltonian
Write in matrix form, identify $A_\theta$:
The term $\frac{1}{2r}\left(1 - \frac{1}{\sqrt{1+f}}\right) \gamma^2 \gamma_1 \gamma_2$ becomes $\frac{1}{2r}\left(1 - \frac{1}{\sqrt{1+f}}\right) \gamma^1$ (using $\gamma^2 \gamma_1 \gamma_2 = -\gamma_1$).

Thus $A_\theta = \frac{1}{2r}\left(1 - \frac{1}{\sqrt{1+f}}\right)$.

---

## 2. From Eq. (12) to Eq. (15): The Magnetic Field

**What the paper shows**:
- Eq. (12): $A_\theta = \frac{1}{2r}\left(1 - \frac{1}{\sqrt{1+f}}\right)$
- Eq. (15): $B_z = \frac{1}{4r} \frac{f'}{(1+f)^{3/2}}$

**Missing step**: The curl in polar coordinates

In 2D polar coordinates, the curl of a vector field $\mathbf{A} = (A_r, A_\theta)$ is:
$$
(\nabla \times \mathbf{A})_z = \frac{1}{r} \left[ \frac{\partial}{\partial r}(r A_\theta) - \frac{\partial A_r}{\partial\theta} \right]
$$

For our case: $A_r = 0$, $A_\theta$ depends only on $r$, so:
$$
B_z = \frac{1}{r} \frac{\partial}{\partial r}(r A_\theta)
$$

Now compute:
$$
r A_\theta = \frac{1}{2} \left(1 - \frac{1}{\sqrt{1+f}}\right)
$$
$$
\frac{\partial}{\partial r}(r A_\theta) = \frac{1}{2} \cdot \frac{1}{2} (1+f)^{-3/2} f' = \frac{1}{4} \frac{f'}{(1+f)^{3/2}}
$$

Thus:
$$
B_z = \frac{1}{r} \cdot \frac{1}{4} \frac{f'}{(1+f)^{3/2}} = \frac{1}{4r} \frac{f'}{(1+f)^{3/2}}
$$

---

## 3. LDOS Formula Derivation (Not Explicitly Shown)

**What the paper states**: "The electronic properties of the curved sample were computed from the electron propagator to first order in the small parameter $\alpha = (A/b)^2$."

**Missing derivation**:

### Step 1: Perturbative Expansion
Write metric as $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $h_{rr} = f(r)$, $h_{\theta\theta} = 0$.

Expand Dirac operator: $\mathcal{D} = \mathcal{D}_0 + \mathcal{D}_1 + O(\epsilon^2)$
where $\epsilon = (A/b)^2$.

### Step 2: Dyson Equation
Green's function satisfies: $\mathcal{D} G = \delta(x-x')(-g)^{-1/2}$

Expand: $G = G_0 + G_1 + O(\epsilon^2)$

To order $\epsilon^0$: $\mathcal{D}_0 G_0 = \delta(x-x')$

To order $\epsilon^1$: $\mathcal{D}_0 G_1 + \mathcal{D}_1 G_0 = \delta(x-x')[(-g)^{-1/2} - 1]$

### Step 3: Solve for $G_1$
Formally: $G_1 = -G_0 * \mathcal{D}_1 G_0 - G_0 * [((-g)^{-1/2} - 1)\delta]$

where $*$ denotes convolution.

### Step 4: LDOS Correction
$$
\rho_1(E, \mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G_1(E, \mathbf{r}, \mathbf{r})\gamma^0]
$$

### Step 5: For $E=0$ Simplification
At $E=0$, the flat Green's function is:
$$
G_0(0, \mathbf{r}, \mathbf{r}') = -\frac{1}{2\pi} \frac{\gamma \cdot (\mathbf{r}-\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|^2}
$$

And $G_0(0, \mathbf{r}, \mathbf{r})$ is real, so its imaginary part vanishes.

### Step 6: Convolution Integral
$$
\rho_1(0, \mathbf{r}) = \frac{1}{\pi} \text{Im} \int d^2\mathbf{r}' \, \text{Tr}[G_0(0, \mathbf{r}, \mathbf{r}') \mathcal{D}_1(\mathbf{r}') G_0(0, \mathbf{r}', \mathbf{r}) \gamma^0]
$$

### Step 7: For Gaussian Bump
After angular integration (using rotational symmetry):
$$
\delta\rho(0, r) \propto \int_0^\infty r' dr' f(r') K(r, r')
$$
where $K(r, r')$ is a kernel from angular integration of Green's functions.

### Step 8: Result
For small $\epsilon$, to leading order:
$$
\delta\rho(0, r) \propto \frac{1}{r^2} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/2\sigma^2}
$$
with $\sigma = b/\sqrt{2}$.

**Why this form?**
- $1/r^2$ comes from Green's function asymptotics
- $(1 - r^2/(2\sigma^2))$ gives zero crossing at $r = \sigma\sqrt{2}$
- Gaussian envelope from $f(r) \propto e^{-2r^2/b^2}$

---

## 4. From Eq. (16) to Eq. (17): Topological Defect Potential

**What the paper shows**:
- Eq. (16): $ds^2 = -dt^2 + e^{-2\Lambda}(dx^2 + dy^2)$ with $\Lambda = \sum_i 4\mu_i \log r_i$
- Eq. (17): $V(\omega, \mathbf{r}) = 2i\Lambda\gamma^0\partial_0 + i\Lambda\gamma^j\partial_j + \frac{i}{2}\gamma^j(\partial_j\Lambda)$

**Missing derivation**:

### Step 1: Vielbein for Conformal Metric
For $g_{\mu\nu} = \text{diag}(-1, e^{-2\Lambda}, e^{-2\Lambda})$:
Choose: $e_0^0 = 1$, $e_1^1 = e^{-\Lambda}$, $e_2^2 = e^{-\Lambda}$

### Step 2: Curved Gamma Matrices
$$
\gamma^0 = e_0^0 \gamma^0 = \gamma^0
$$
$$
\gamma^1 = e_1^1 \gamma^1 = e^{-\Lambda} \gamma^1
$$
$$
\gamma^2 = e_2^2 \gamma^2 = e^{-\Lambda} \gamma^2
$$

### Step 3: Spin Connection for Conformal Metric
General formula: For $g_{\mu\nu} = e^{2\Lambda}\eta_{\mu\nu}$,
$$
\Gamma^\lambda_{\mu\nu} = \delta^\lambda_\mu \partial_\nu \Lambda + \delta^\lambda_\nu \partial_\mu \Lambda - \eta_{\mu\nu}\eta^{\lambda\rho}\partial_\rho\Lambda
$$

Spin connection:
$$
\Omega_\mu = \frac{1}{2} \gamma^\nu \gamma_\mu \partial_\nu \Lambda - \frac{1}{2} \gamma_\mu \gamma^\nu \partial_\nu \Lambda
$$

Compute components:
- $\Omega_0 = \gamma^0 \gamma^j \partial_j \Lambda$
- $\Omega_j = \frac{1}{2} \gamma_j \gamma^0 \partial_0 \Lambda + \frac{1}{2} \gamma_j \gamma^k \partial_k \Lambda$

### Step 4: Dirac Operator
$$
i\gamma^\mu \nabla_\mu = i\gamma^\mu (\partial_\mu - \Omega_\mu)
$$

Substitute:
$$
= i\gamma^0 (\partial_0 - \Omega_0) + i\gamma^j (\partial_j - \Omega_j)
$$

### Step 5: Expand to First Order in $\Lambda$
Assume $\Lambda \ll 1$, expand $e^{-\Lambda} \approx 1 - \Lambda$:

$\gamma^0$ term: $i\gamma^0 \partial_0 - i\gamma^0 \Omega_0 = i\gamma^0 \partial_0 - i\gamma^0 (\gamma^0 \gamma^j \partial_j \Lambda)$
But $\gamma^0 \gamma^0 \gamma^j = \gamma^j$, so: $= i\gamma^0 \partial_0 - i\gamma^j \partial_j \Lambda$

$\gamma^j$ term: $i\gamma^j (\partial_j - \Omega_j) = i\gamma^j \partial_j - i\gamma^j \Omega_j$
$\Omega_j = \frac{1}{2} \gamma_j \gamma^0 \partial_0 \Lambda + \frac{1}{2} \gamma_j \gamma^k \partial_k \Lambda$

For static defects ($\partial_0 \Lambda = 0$): $\Omega_j = \frac{1}{2} \gamma_j \gamma^k \partial_k \Lambda$

Then $\gamma^j \Omega_j = \frac{1}{2} \gamma^j \gamma_j \gamma^k \partial_k \Lambda = \frac{1}{2} (2) \gamma^k \partial_k \Lambda = \gamma^k \partial_k \Lambda$

So: $i\gamma^j (\partial_j - \Omega_j) = i\gamma^j \partial_j - i\gamma^k \partial_k \Lambda$

### Step 6: Combine Terms
Total Dirac operator to first order:
$$
i\gamma^\mu \nabla_\mu = i\gamma^0 \partial_0 + i\gamma^j \partial_j - i\gamma^j \partial_j \Lambda - i\gamma^k \partial_k \Lambda
$$
Wait, last two terms are identical: $-2i\gamma^j \partial_j \Lambda$

Actually, let's recompute carefully...

From $\gamma^0$ term: $i\gamma^0 \partial_0 - i\gamma^j \partial_j \Lambda$
From $\gamma^j$ term: $i(1-\Lambda)\gamma^j \partial_j - i\gamma^j \Omega_j$

For static case, $\Omega_j = \frac{1}{2} \gamma_j \gamma^k \partial_k \Lambda$
Then $\gamma^j \Omega_j = \frac{1}{2} \gamma^j \gamma_j \gamma^k \partial_k \Lambda = \gamma^k \partial_k \Lambda$

So $\gamma^j$ term: $i\gamma^j \partial_j - i\Lambda \gamma^j \partial_j - i\gamma^k \partial_k \Lambda$

Combine with $\gamma^0$ term:
Total: $i\gamma^0 \partial_0 + i\gamma^j \partial_j - i\Lambda \gamma^j \partial_j - i\gamma^j \partial_j \Lambda - i\gamma^k \partial_k \Lambda$

Last two terms are the same: $-2i\gamma^j \partial_j \Lambda$

Thus:
$$
i\gamma^\mu \nabla_\mu = i\gamma^0 \partial_0 + i\gamma^j \partial_j - i\Lambda \gamma^j \partial_j - 2i\gamma^j \partial_j \Lambda
$$

Write as: $i\gamma^0 \partial_0 + i\gamma^j \partial_j + V$ where
$$
V = -i\Lambda \gamma^j \partial_j - 2i\gamma^j \partial_j \Lambda
$$

But paper has: $V = 2i\Lambda \gamma^0 \partial_0 + i\Lambda \gamma^j \partial_j + \frac{i}{2} \gamma^j \partial_j \Lambda$

**Discrepancy**: Our derivation gives different coefficients. Possible reasons:
1. Paper includes time dilation: $g_{00} = -e^{2\Lambda}$ not $-1$
2. Different convention for spin connection
3. Paper's Eq. (17) might be for different representation

---

## 5. Critical Subtleties and Assumptions

### 5.1 First-Order Perturbation Theory
The paper states: "the contribution of the effective gauge field coming from the spin connection to first order in perturbation theory vanishes."

**Why?** In the LDOS calculation, terms linear in $A_\mu$ integrate to zero due to symmetry.

### 5.2 Metric vs Gauge Field Effects
- **Tight-binding**: Only gives gauge field from hopping modulation
- **Curved space**: Gives both gauge field AND metric effects (velocity renormalization)
- Metric effects dominate at first order for smooth curvature

### 5.3 Regularization Issues
$G_0(0, \mathbf{r}, \mathbf{r})$ is divergent. Need regularization:
- Point-split: $G_0(0, \mathbf{r}, \mathbf{r}')$ with $|\mathbf{r}-\mathbf{r}'| \to \epsilon$
- Dimensional regularization
- The paper doesn't specify, but result is finite

### 5.4 Numerical Factors
Several numerical factors are not explicitly derived:
- Prefactor in LDOS formula
- Exact relation between $\eta$ and pentagon/heptagon angle
- Proportionality constant