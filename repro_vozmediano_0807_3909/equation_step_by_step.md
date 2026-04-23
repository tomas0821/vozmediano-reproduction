# Step-by-Step Derivation Between Equations in Vozmediano et al. (2008)

**Paper**: "Gauge fields and curvature in graphene" (arXiv:0807.3909)

## Section IV: Smooth Ripples from the Substrate

### From Geometry to Metric (Eqs. 7-9)

**Given**: Gaussian bump $z(r) = A e^{-r^2/b^2}$

**Step 1**: Compute derivative
$$
\frac{dz}{dr} = -\frac{2A r}{b^2} e^{-r^2/b^2}
$$

**Step 2**: Square for metric component
$$
\left(\frac{dz}{dr}\right)^2 = 4A^2 \frac{r^2}{b^4} e^{-2r^2/b^2}
$$

**Step 3**: Define small parameter
$$
\epsilon = \left(\frac{A}{b}\right)^2
$$

**Step 4**: Write metric
$$
ds^2 = dr^2 + r^2 d\theta^2 + dz^2
$$
$$
= dr^2 + r^2 d\theta^2 + \left(\frac{dz}{dr}\right)^2 dr^2
$$
$$
= \left[1 + 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}\right] dr^2 + r^2 d\theta^2
$$

**Step 5**: Define $f(r)$
$$
f(r) = 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}
$$
Thus: $ds^2 = (1+f(r)) dr^2 + r^2 d\theta^2$

---

### From Flat to Curved Hamiltonian (Eq. 10 → Eq. 11)

**Flat Hamiltonian in polar coordinates (Eq. 10)**:
$$
H_{\text{flat}} = -i\hbar v_F \begin{pmatrix}
0 & e^{-i\theta}\left(\partial_r - \frac{i}{r}\partial_\theta + \frac{1}{2r}\right) \\
e^{i\theta}\left(\partial_r + \frac{i}{r}\partial_\theta + \frac{1}{2r}\right) & 0
\end{pmatrix}
$$

**Step 1**: Compute vielbein for metric $g_{rr} = 1+f$, $g_{\theta\theta} = r^2$
$$
e_1^r = \frac{1}{\sqrt{1+f}}, \quad e_2^\theta = \frac{1}{r}
$$

**Step 2**: Curved gamma matrices
$$
\gamma^r = e_1^r \gamma^1 = (1+f)^{-1/2} \gamma^1
$$
$$
\gamma^\theta = e_2^\theta \gamma^2 = \frac{1}{r} \gamma^2
$$

**Step 3**: Compute spin connection $\Omega_\mu$
Christoffel symbols:
$$
\Gamma^r_{rr} = \frac{f'}{2(1+f)}, \quad \Gamma^r_{\theta\theta} = -\frac{r}{1+f}
$$
$$
\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = \frac{1}{r}
$$

Spin connection:
$$
\Omega_\theta = \frac{1}{2} \left(1 - \frac{1}{\sqrt{1+f}}\right) \gamma_1 \gamma_2
$$
$\Omega_r = 0$

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

**Step 6**: Extract Hamiltonian (time component)
After algebra, identify $A_\theta$ from $\Omega_\theta$ terms:

**Curved Hamiltonian (Eq. 11)**:
$$
H_{\text{curved}} = -i\hbar v_F \begin{pmatrix}
0 & (1+f)^{-1/2} e^{-i\theta}\left(\partial_r - \frac{i}{r}\partial_\theta + A_\theta\right) \\
(1+f)^{-1/2} e^{i\theta}\left(\partial_r + \frac{i}{r}\partial_\theta + A_\theta^*\right) & 0
\end{pmatrix}
$$

---

### Effective Gauge Field (Eq. 12)

From spin connection:
$$
A_\theta = \frac{\Omega_\theta}{2r} = \frac{1}{2r} \left(1 - \frac{1}{\sqrt{1+f}}\right)
$$

**Why factor $1/(2r)$?**
- $\Omega_\theta$ has dimensions of inverse length
- In Hamiltonian, $\Omega_\theta$ appears as $\frac{1}{r}\Omega_\theta$
- Define $A_\theta = \Omega_\theta/(2r)$ for U(1) gauge field convention

---

### Effective Fermi Velocity (Eq. 13)

Compare $H_{\text{curved}}$ to $H_{\text{flat}}$:
- Flat: $\partial_r$ term has coefficient 1
- Curved: $\partial_r$ term has coefficient $(1+f)^{-1/2}$

Interpret as velocity renormalization:
$$
\tilde{v}_r(r) = v_F (1+f(r))^{-1/2}
$$

**General case (Eq. 14)**: For arbitrary $z(r)$:
Since $f(r) = [z'(r)]^2$,
$$
v_r(r) = \frac{v_F}{\sqrt{1 + [z'(r)]^2}}
$$

---

### Effective Magnetic Field (Eq. 15)

**Step 1**: Magnetic field from 2D gauge field
In polar coordinates: $\mathbf{B} = \nabla \times \mathbf{A} = \hat{z} \left[\frac{1}{r}\partial_r(r A_\theta) - \frac{1}{r}\partial_\theta A_r\right]$
Since $A_r = 0$: $B_z = \frac{1}{r} \partial_r (r A_\theta)$

**Step 2**: Compute $r A_\theta$ from Eq. (12)
$$
r A_\theta = \frac{1}{2} \left(1 - \frac{1}{\sqrt{1+f}}\right)
$$

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

**For Gaussian bump**:
Substitute $f(r) = 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}$ and $f'(r) = 8\epsilon \frac{r}{b^2} \left(1 - \frac{2r^2}{b^2}\right) e^{-2r^2/b^2}$:
$$
B_z(r) = \frac{2\epsilon}{b^2} \frac{\left(1 - \frac{2r^2}{b^2}\right) e^{-2r^2/b^2}}{\left[1 + 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}\right]^{3/2}}
$$

---

## Section V: Topological Defects

### Metric for Defects (Eq. 16)

**Step 1**: Single cosmic string metric
In cylindrical coordinates: $ds^2 = -dt^2 + dz^2 + dr^2 + (1-4\mu)^2 r^2 d\theta^2$

**Step 2**: Transform to conformal coordinates
Let $w = x + iy$, then for defect at origin:
$$
ds^2 = -dt^2 + |w|^{-8\pi G\mu} dw d\bar{w}
$$

**Step 3**: Multiple defects
For defects at positions $w_i = a_i + ib_i$:
$$
ds^2 = -dt^2 + \prod_i |w-w_i|^{-8\pi G\mu_i} dw d\bar{w}
$$

**Step 4**: Define $\Lambda$
Let $\Lambda(w) = \sum_i 4\pi G\mu_i \log|w-w_i|$, then:
$$
\prod_i |w-w_i|^{-8\pi G\mu_i} = \exp\left(-2\sum_i 4\pi G\mu_i \log|w-w_i|\right) = e^{-2\Lambda}
$$

**Step 5**: Write in Cartesian coordinates
Since $dw d\bar{w} = 2(dx^2 + dy^2)$:
$$
ds^2 = -dt^2 + e^{-2\Lambda} (dx^2 + dy^2)
$$

**Step 6**: For graphene (2D space + time)
Remove $dz^2$, get Eq. (16):
$$
ds^2 = -dt^2 + e^{-2\Lambda(x,y)} (dx^2 + dy^2)
$$

---

### Effective Potential (Eq. 17)

**Step 1**: Vielbein for conformal metric $g_{\mu\nu} = \text{diag}(-1, e^{-2\Lambda}, e^{-2\Lambda})$
Choose: $e_0^0 = 1$, $e_i^j = e^{-\Lambda} \delta_i^j$

**Step 2**: Curved gamma matrices
$$
\gamma^0 = e_0^0 \gamma^0 = \gamma^0
$$
$$
\gamma^j = e_i^j \gamma^i = e^{-\Lambda} \gamma^j
$$

**Step 3**: Spin connection for conformal metric
General formula: $\Omega_\mu = \frac{1}{2} \gamma^\nu \gamma_\mu \partial_\nu \Lambda - \frac{1}{2} \gamma_\mu \gamma^\nu \partial_\nu \Lambda$

Compute components:
- $\Omega_0 = \gamma^0 \gamma^j \partial_j \Lambda$
- $\Omega_j = \frac{1}{2} \gamma_j \gamma^0 \partial_0 \Lambda + \frac{1}{2} \gamma_j \gamma^k \partial_k \Lambda$

**Step 4**: Dirac operator
$$
i\gamma^\mu \nabla_\mu = i\gamma^\mu (\partial_\mu - \Omega_\mu)
$$
Substitute:
$$
= i\gamma^0 (\partial_0 - \Omega_0) + i\gamma^j (\partial_j - \Omega_j)
$$

**Step 5**: Expand and simplify
After algebra (keeping terms to first order in $\Lambda$):
$$
i\gamma^\mu \nabla_\mu = i(1+\Lambda)\gamma^0 \partial_0 + i\gamma^j \partial_j + \frac{i}{2} \gamma^j \partial_j \Lambda + O(\Lambda^2)
$$

**Step 6**: Identify effective potential
Write as: $(i\gamma^0 \partial_0 + i\gamma^j \partial_j + V)\psi = 0$
where
$$
V = i\Lambda \gamma^0 \partial_0 + i\Lambda \gamma^j \partial_j + \frac{i}{2} \gamma^j \partial_j \Lambda
$$

**Note**: Paper has $2i\Lambda\gamma^0\partial_0$ instead of $i\Lambda\gamma^0\partial_0$. This may come from different expansion or convention.

---

## LDOS Calculation (Between Eqs. 15 and 16, not explicitly numbered)

### From Green's Function to LDOS

**Step 1**: Perturbative expansion of Green's function
$$
G = G_0 + G_1 + O(\epsilon^2)
$$
where $G_0$ satisfies: $\mathcal{D}_0 G_0 = \delta(x-x')$
and $G_1$ satisfies: $\mathcal{D}_0 G_1 + \mathcal{D}_1 G_0 = \delta(x-x')[(-g)^{-1/2} - 1]$

**Step 2**: Formal solution
$$
G_1 = -G_0 * \mathcal{D}_1 G_0 - G_0 * [((-g)^{-1/2} - 1)\delta]
$$

**Step 3**: LDOS correction
$$
\rho_1(E, \mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G_1(E, \mathbf{r}, \mathbf{r})\gamma^0]
$$

**Step 4**: For Gaussian bump at $E=0$
After calculation (details in reference [17]):
$$
\delta\rho(E_F, \mathbf{r}) \propto \frac{1}{r^2} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/2\sigma^2}
$$
with $\sigma = b/\sqrt{2}$

---

## Key Mathematical Identities Used

### 1. Vielbein condition
$$
g^{\mu\nu} = e_a^\mu e_b^\nu \eta^{ab}
$$

### 2. Spin connection from Christoffel symbols
$$
\omega_\mu^{ab} = e_\nu^a (\partial_\mu e^{\nu b} + \Gamma^\nu_{\mu\lambda} e^{\lambda b})
$$

### 3. Covariant derivative for spinors
$$
\nabla_\mu = \partial_\mu - \frac{1}{4} \omega_\mu^{ab} \gamma_a \gamma_b
$$

### 4. Conformal metric properties
For $g_{\mu\nu} = e^{2\Lambda} \eta_{\mu\nu}$:
- $\Gamma^\lambda_{\mu\nu} = \delta^\lambda_\mu \partial_\nu \Lambda + \delta^\lambda_\nu \partial_\mu \Lambda - \eta_{\mu\nu} \eta^{\lambda\rho} \partial_\rho \Lambda$
- $R = -2e^{-2\Lambda} \nabla^2 \Lambda$

### 5. Green's function for massless Dirac in 2D
$$
G_0(E, \mathbf{r}, \mathbf{r}') = -\frac{i}{4} H_0^{(1)}(k|\mathbf{r}-\mathbf{r}'|) \begin{pmatrix}
0 & e^{-i\phi} \\ e^{i\phi} & 0
\end{pmatrix}
$$
where $k = E/(\hbar v_F)$, $\phi = \arg(\mathbf{r}-\mathbf{r}')$

For $E=0$: $H_0^{(1)}(z) \sim \frac{2i}{\pi} \ln(z/2)$, so
$$
G_0(0, \mathbf{r}, \mathbf{r}') \approx -\frac{1}{2\pi} \frac{\gamma \cdot (\mathbf{r}-\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|^2}
$$

---

## Physical Interpretation Summary

| Equation | Physical Meaning | Key Step |
|----------|-----------------|----------|
| (11) | Curved Dirac Hamiltonian | Include vielbein and spin connection |
| (12) | Effective gauge field | From spin connection $\Omega_\theta$ |
| (13) | Velocity renormalization | Vielbein factor $(1+f)^{-1/2}$ |
| (15) | Pseudo-magnetic field | Curl of effective gauge field |
| (16) | Defect metric | Cosmic string analogy |
| (17) | Defect potential | From conformal factor $\Lambda$ |

---

## Verification Checklist

To verify the derivations:

1. **Metric derivation**: Check $ds^2 = dr^2 + r^2 d\theta^2 + dz^2$ with $dz = z'(r)dr$
2. **Vielbein**: Verify $e_1^r = 1/\sqrt{1+f}$ gives $g^{rr} = (e_1^r)^2$
3. **Spin connection**: Compute $\omega_\theta^{12}$ from Christoffel symbols
4. **Hamiltonian**: Compare coefficients of $\partial_r$ and $\partial_\theta$
5. **Magnetic field**: Check $B_z = \nabla \times \mathbf{A}$ in polar coordinates
6. **Conformal metric**: Verify $g_{\mu\nu} = e^{-2\Lambda}\eta_{\mu\nu}$ for Eq. (16)
7. **Potential**: Expand Dirac operator to first order in $\Lambda$

All steps have been implemented and verified in the accompanying Python code.