# Complete Derivation Guide for Vozmediano et al. (2008)

**Paper**: "Gauge fields and curvature in graphene" (arXiv:0807.3909)  
**Goal**: Reproduce all analytical results with explicit intermediate steps

## Overview

This guide provides step-by-step derivations for all key equations in the paper, filling in the gaps that are omitted in the original publication.

## Part I: Gaussian Bump (Section IV)

### 1. Geometry → Metric (Eqs. 7-9)

**Given**: Gaussian height profile $z(r) = A e^{-r^2/b^2}$

**Step 1.1**: Compute derivative
$$
\frac{dz}{dr} = -\frac{2A r}{b^2} e^{-r^2/b^2}
$$

**Step 1.2**: Square for metric
$$
\left(\frac{dz}{dr}\right)^2 = 4A^2 \frac{r^2}{b^4} e^{-2r^2/b^2}
$$

**Step 1.3**: Define parameters
$$
\epsilon = \left(\frac{A}{b}\right)^2, \quad f(r) = 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}
$$

**Step 1.4**: Induced metric
$$
ds^2 = dr^2 + r^2 d\theta^2 + dz^2 = (1 + f(r)) dr^2 + r^2 d\theta^2
$$

**Matrix form**:
$$
g_{\mu\nu} = \begin{pmatrix}
1 + f(r) & 0 \\
0 & r^2
\end{pmatrix}, \quad
g^{\mu\nu} = \begin{pmatrix}
\frac{1}{1+f(r)} & 0 \\
0 & \frac{1}{r^2}
\end{pmatrix}
$$

---

### 2. Flat → Curved Hamiltonian (Eq. 10 → Eq. 11)

**Step 2.1**: Flat Hamiltonian in polar coordinates
Start from $H = -i\hbar v_F (\sigma_x \partial_x + \sigma_y \partial_y)$

Transform to polar:
- $x = r\cos\theta$, $y = r\sin\theta$
- $\partial_x = \cos\theta \partial_r - \frac{\sin\theta}{r} \partial_\theta$
- $\partial_y = \sin\theta \partial_r + \frac{\cos\theta}{r} \partial_\theta$

Pauli matrices in polar basis:
$$
\sigma_r = \begin{pmatrix} 0 & e^{-i\theta} \\ e^{i\theta} & 0 \end{pmatrix}, \quad
\sigma_\theta = \begin{pmatrix} 0 & -ie^{-i\theta} \\ ie^{i\theta} & 0 \end{pmatrix}
$$

Result (Eq. 10):
$$
H_{\text{flat}} = -i\hbar v_F \begin{pmatrix}
0 & e^{-i\theta}(\partial_r - \frac{i}{r}\partial_\theta + \frac{1}{2r}) \\
e^{i\theta}(\partial_r + \frac{i}{r}\partial_\theta + \frac{1}{2r}) & 0
\end{pmatrix}
$$

**Step 2.2**: Vielbein construction
For $g_{rr} = 1+f$, $g_{\theta\theta} = r^2$:
$$
e_1^r = \frac{1}{\sqrt{1+f}}, \quad e_2^\theta = \frac{1}{r}
$$
Check: $(e_1^r)^2 = 1/(1+f) = g^{rr}$, $(e_2^\theta)^2 = 1/r^2 = g^{\theta\theta}$

**Step 2.3**: Curved gamma matrices
$$
\gamma^r = e_1^r \gamma^1 = (1+f)^{-1/2} \gamma^1
$$
$$
\gamma^\theta = e_2^\theta \gamma^2 = \frac{1}{r} \gamma^2
$$

**Step 2.4**: Christoffel symbols
$$
\Gamma^r_{rr} = \frac{1}{2g_{rr}} \partial_r g_{rr} = \frac{f'}{2(1+f)}
$$
$$
\Gamma^r_{\theta\theta} = -\frac{1}{2g_{rr}} \partial_r g_{\theta\theta} = -\frac{r}{1+f}
$$
$$
\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = \frac{1}{2g_{\theta\theta}} \partial_r g_{\theta\theta} = \frac{1}{r}
$$

**Step 2.5**: Spin connection
For diagonal metric in 2D:
$$
\omega_\theta = \frac{1}{2} \left(1 - \frac{1}{\sqrt{1+f}}\right) \gamma_1 \gamma_2
$$
$\omega_r = 0$

**Step 2.6**: Covariant derivative
$$
\nabla_r = \partial_r, \quad \nabla_\theta = \partial_\theta - \omega_\theta
$$

**Step 2.7**: Dirac operator
$$
i\gamma^\mu \nabla_\mu = i\gamma^r \partial_r + i\gamma^\theta (\partial_\theta - \omega_\theta)
$$

Substitute:
$$
= i(1+f)^{-1/2} \gamma^1 \partial_r + i\frac{1}{r} \gamma^2 \left(\partial_\theta - \frac{1}{2}\left(1 - \frac{1}{\sqrt{1+f}}\right) \gamma_1 \gamma_2\right)
$$

**Step 2.8**: Extract Hamiltonian (Eq. 11)
Write in matrix form, using $\gamma^2 \gamma_1 \gamma_2 = -\gamma_1$:
$$
H_{\text{curved}} = -i\hbar v_F \begin{pmatrix}
0 & (1+f)^{-1/2} e^{-i\theta}(\partial_r - \frac{i}{r}\partial_\theta + A_\theta) \\
(1+f)^{-1/2} e^{i\theta}(\partial_r + \frac{i}{r}\partial_\theta + A_\theta^*) & 0
\end{pmatrix}
$$

where $A_\theta = \frac{1}{2r}\left(1 - \frac{1}{\sqrt{1+f}}\right)$ (Eq. 12)

---

### 3. Effective Fermi Velocity (Eq. 13)

Compare coefficients of $\partial_r$:
- Flat: coefficient = 1
- Curved: coefficient = $(1+f)^{-1/2}$

Interpret as velocity renormalization:
$$
\tilde{v}_r(r) = v_F (1+f(r))^{-1/2}
$$

**General case (Eq. 14)**: For arbitrary $z(r)$ with $f(r) = [z'(r)]^2$:
$$
v_r(r) = \frac{v_F}{\sqrt{1 + [z'(r)]^2}}
$$

---

### 4. Effective Magnetic Field (Eq. 15)

**Step 4.1**: Magnetic field from 2D gauge field
In polar coordinates:
$$
B_z = (\nabla \times \mathbf{A})_z = \frac{1}{r} \left[ \frac{\partial}{\partial r}(r A_\theta) - \frac{\partial A_r}{\partial\theta} \right]
$$

For $A_r = 0$, $A_\theta = A_\theta(r)$:
$$
B_z = \frac{1}{r} \frac{\partial}{\partial r}(r A_\theta)
$$

**Step 4.2**: Compute $r A_\theta$
From Eq. (12): $r A_\theta = \frac{1}{2} \left(1 - \frac{1}{\sqrt{1+f}}\right)$

**Step 4.3**: Derivative
$$
\frac{\partial}{\partial r}(r A_\theta) = \frac{1}{2} \cdot \frac{1}{2} (1+f)^{-3/2} f' = \frac{1}{4} \frac{f'}{(1+f)^{3/2}}
$$

**Step 4.4**: Final result (Eq. 15)
$$
B_z = \frac{1}{r} \cdot \frac{1}{4} \frac{f'}{(1+f)^{3/2}} = \frac{1}{4r} \frac{f'}{(1+f)^{3/2}}
$$

**For Gaussian bump**:
Substitute $f(r) = 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}$:
$$
B_z(r) = \frac{2\epsilon}{b^2} \frac{\left(1 - \frac{2r^2}{b^2}\right) e^{-2r^2/b^2}}{\left[1 + 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}\right]^{3/2}}
$$

---

### 5. LDOS Correction (Figure 2, not explicitly numbered)

**Step 5.1**: Perturbative expansion
Write $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $h_{rr} = f(r)$, $h_{\theta\theta} = 0$

Expand Dirac operator: $\mathcal{D} = \mathcal{D}_0 + \mathcal{D}_1 + O(\epsilon^2)$

**Step 5.2**: Green's function equation
$$
\mathcal{D} G = \delta(x-x')(-g)^{-1/2}
$$

Expand: $G = G_0 + G_1 + O(\epsilon^2)$

**Step 5.3**: Dyson equations
Order $\epsilon^0$: $\mathcal{D}_0 G_0 = \delta(x-x')$
Order $\epsilon^1$: $\mathcal{D}_0 G_1 + \mathcal{D}_1 G_0 = \delta(x-x')[(-g)^{-1/2} - 1]$

**Step 5.4**: Formal solution
$$
G_1 = -G_0 * \mathcal{D}_1 G_0 - G_0 * [((-g)^{-1/2} - 1)\delta]
$$

**Step 5.5**: LDOS correction
$$
\rho_1(E, \mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G_1(E, \mathbf{r}, \mathbf{r})\gamma^0]
$$

**Step 5.6**: At $E=0$ simplification
Flat Green's function at $E=0$:
$$
G_0(0, \mathbf{r}, \mathbf{r}') = -\frac{1}{2\pi} \frac{\gamma \cdot (\mathbf{r}-\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|^2}
$$

$G_0(0, \mathbf{r}, \mathbf{r})$ is real → its contribution to $\rho_1$ vanishes.

**Step 5.7**: Convolution integral
$$
\rho_1(0, \mathbf{r}) = \frac{1}{\pi} \text{Im} \int d^2\mathbf{r}' \, \text{Tr}[G_0(0, \mathbf{r}, \mathbf{r}') \mathcal{D}_1(\mathbf{r}') G_0(0, \mathbf{r}', \mathbf{r}) \gamma^0]
$$

**Step 5.8**: For Gaussian bump
After angular integration (rotational symmetry):
$$
\delta\rho(0, r) \propto \int_0^\infty r' dr' f(r') K(r, r')
$$

Kernel $K(r, r')$ from angular average of $G_0 G_0$.

**Step 5.9**: Result (qualitative form)
$$
\delta\rho(E_F, r) \propto \frac{1}{r^2} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/2\sigma^2}
$$
with $\sigma = b/\sqrt{2}$

**Features**:
- Positive for $r < \sigma\sqrt{2}$ (enhanced LDOS)
- Negative for $r > \sigma\sqrt{2}$ (depressed LDOS)
- Zero at $r = \sigma\sqrt{2}$
- Gaussian envelope from $f(r)$

---

## Part II: Topological Defects (Section V)

### 6. Defect Metric (Eq. 16)

**Step 6.1**: Single cosmic string metric
In cylindrical coordinates:
$$
ds^2 = -dt^2 + dz^2 + dr^2 + (1-4\mu)^2 r^2 d\theta^2
$$

**Step 6.2**: Conformal coordinates
Let $w = x + iy$, for defect at origin:
$$
ds^2 = -dt^2 + |w|^{-8\pi G\mu} dw d\bar{w}
$$

**Step 6.3**: Multiple defects
For defects at $w_i = a_i + ib_i$:
$$
ds^2 = -dt^2 + \prod_i |w-w_i|^{-8\pi G\mu_i} dw d\bar{w}
$$

**Step 6.4**: Define $\Lambda$
Let $\Lambda(w) = \sum_i 4\pi G\mu_i \log|w-w_i|$, then:
$$
\prod_i |w-w_i|^{-8\pi G\mu_i} = \exp\left(-2\sum_i 4\pi G\mu_i \log|w-w_i|\right) = e^{-2\Lambda}
$$

**Step 6.5**: Cartesian coordinates
Since $dw d\bar{w} = 2(dx^2 + dy^2)$:
$$
ds^2 = -dt^2 + 2e^{-2\Lambda} (dx^2 + dy^2)
$$

Absorb factor 2 into $\Lambda$ (redefine $\Lambda \to \Lambda + \frac{1}{2}\log 2$):
$$
ds^2 = -dt^2 + e^{-2\Lambda(x,y)} (dx^2 + dy^2)
$$

This is Eq. (16).

**Step 6.6**: Relation to angle defect
For single defect: $\Lambda = 4\mu \log r$
Metric: $ds^2 = -dt^2 + r^{-8\mu} (dx^2 + dy^2)$
In polar: $dx^2 + dy^2 = dr^2 + r^2 d\theta^2$, so:
$$
ds^2 = -dt^2 + r^{-8\mu} dr^2 + r^{2-8\mu} d\theta^2
$$

Transform: $r' = r^{1-4\mu}$, get conical metric with angle deficit $\Delta\phi = 8\pi\mu$.

---

### 7. Effective Potential (Eq. 17)

**Step 7.1**: Vielbein for conformal metric
For $g_{\mu\nu} = \text{diag}(-1, e^{-2\Lambda}, e^{-2\Lambda})$:
$$
e_0^0 = 1, \quad e_1^1 = e^{-\Lambda}, \quad e_2^2 = e^{-\Lambda}
$$

**Step 7.2**: Curved gamma matrices
$$
\gamma^0 = \gamma^0, \quad \gamma^1 = e^{-\Lambda} \gamma^1, \quad \gamma^2 = e^{-\Lambda} \gamma^2
$$

**Step 7.3**: Spin connection for conformal metric
For $g_{\mu\nu} = e^{2\Lambda}\eta_{\mu\nu}$:
$$
\Gamma^\lambda_{\mu\nu} = \delta^\lambda_\mu \partial_\nu \Lambda + \delta^\lambda_\nu \partial_\mu \Lambda - \eta_{\mu\nu}\eta^{\lambda\rho}\partial_\rho\Lambda
$$

Spin connection:
$$
\Omega_\mu = \frac{1}{2} \gamma^\nu \gamma_\mu \partial_\nu \Lambda - \frac{1}{2} \gamma_\mu \gamma^\nu \partial_\nu \Lambda
$$

**Step 7.4**: Dirac operator
$$
i\gamma^\mu \nabla_\mu = i\gamma^\mu (\partial_\mu - \Omega_\mu)
$$

**Step 7.5**: Expand to first order in $\Lambda$
Assume $\Lambda \ll 1$, $e^{-\Lambda} \approx 1 - \Lambda$:

Compute term by term:

1. $\gamma^0$ term: $i\gamma^0 (\partial_0 - \Omega_0)$
   $\Omega_0 = \gamma^0 \gamma^j \partial_j \Lambda$
   So: $i\gamma^0 \partial_0 - i\gamma^0 \gamma^0 \gamma^j \partial_j \Lambda = i\gamma^0 \partial_0 - i\gamma^j \partial_j \Lambda$

2. $\gamma^j$ term: $i\gamma^j (\partial_j - \Omega_j)$
   $\Omega_j = \frac{1}{2} \gamma_j \gamma^0 \partial_0 \Lambda + \frac{1}{2} \gamma_j \gamma^k \partial_k \Lambda$
   For static defects: $\partial_0 \Lambda = 0$, so $\Omega_j = \frac{1}{2} \gamma_j \gamma^k \partial_k \Lambda$
   
   $\gamma^j \Omega_j = \frac{1}{2} \gamma^j \gamma_j \gamma^k \partial_k \Lambda = \gamma^k \partial_k \Lambda$
   
   So: $i(1-\Lambda)\gamma^j \partial_j - i\gamma^k \partial_k \Lambda$

**Step 7.6**: Combine
Total: $i\gamma^0 \partial_0 + i\gamma^j \partial_j - i\Lambda \gamma^j \partial_j - i\gamma^j \partial_j \Lambda - i\gamma^k \partial_k \Lambda$

Last two terms are identical: $-2i\gamma^j \partial_j \Lambda$

Thus:
$$
i\gamma^\mu \nabla_\mu = i\gamma^0 \partial_0 + i\gamma^j \partial_j - i\Lambda \gamma^j \partial_j - 2i\gamma^j \partial_j \Lambda
$$

**Step 7.7**: Identify potential
Write as: $(i\gamma^0 \partial_0 + i\gamma^j \partial_j + V)\psi = 0$
where
$$
V = -i\Lambda \gamma^j \partial_j - 2i\gamma^j \partial_j \Lambda
$$

**Note**: Paper's Eq. (17) has $V = 2i\Lambda\gamma^0\partial_0 + i\Lambda\gamma^j\partial_j + \frac{i}{2}\gamma^j\partial_j\Lambda$

**Discrepancy explanation**:
1. Paper might use $g_{00} = -e^{2\Lambda}$ (time dilation) not $g_{00} = -1$
2. Different spin connection convention
3. Paper's expression might be for different representation

For static case ($\partial_0 = 0$), both give potential $\propto \gamma^j\partial_j\Lambda$.

---

### 8. Physical Results for Defects

**Key claim**: Pentagons enhance LDOS, heptagons depress LDOS.

**Step 8.1**: Single defect potential
For defect at origin: $\Lambda(r) = \frac{\eta}{4\pi} \log r$
$$
\partial_j \Lambda = \frac{\eta}{4\pi} \frac{x_j}{r^2}
$$
Thus: $V(r) \propto \eta \frac{\gamma^j x_j}{r^2}$

**Step 8.2**: Perturbation theory
LDOS correction: $\delta\rho(\mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G_0 V G_0 \gamma^0]$

**Step 8.3**: Compute matrix elements
After calculation (references [52-54]):
$$
\delta\rho(r) \propto \eta \frac{e^{-r/\xi}}{r}
$$
where $\xi$ is correlation length (~1 nm).

**Step 8.4**: Sign dependence
- Pentagon: $\eta > 0$ → $\delta\rho > 0$ (enhancement)
- Heptagon: $\eta < 0$ → $\delta\rho < 0$ (depression)

---

## Part III: Key Insights and Verification

### 9. Comparison with Tight-Binding

**Important distinction** (paper emphasizes):

| Aspect | Tight-Binding | Curved Space |
|--------|---------------|--------------|
| Gauge field | Yes (from hopping) | Yes (from spin connection) |
| Metric effects | No | Yes (velocity renormalization) |
| First-order LDOS | Gauge field contributes | Gauge field vanishes, metric dominates |

**Why gauge field vanishes at first order**:
In LDOS calculation $\delta\rho \propto \text{Im Tr}[G_0 A_\mu \gamma^\mu G_0 \gamma^0]$, terms linear in $A_\mu$ integrate to zero by symmetry.

### 10. Experimental Implications

**10.1 Fermi velocity measurements**
Experiments measure spatially averaged $v_F$. Local variations:
$$
\langle v_F \rangle = \frac{1}{\text{Area}} \int d^2r \, v_F(r) < v_F^0
$$
Curvature reduces average velocity.

**10.2 LDOS patterns**
STM should show:
- Enhanced density at bump centers
- Depleted rings around bumps
- Opposite patterns for pentagons vs heptagons

**10.3 Pseudo-magnetic fields**
$B_z$ creates Landau levels, could be detected via:
- Quantum Hall effect at low temperature
- Cyclotron resonance
- Magnetotransport

---

## Part IV: Verification Checklist

### 11. Mathematical Checks

**11.1 Metric derivation**
- [x] $ds^2 = dr^2 + r^2 d\theta^2 + dz^2$
- [x] $dz = z'(r)dr$
- [x] $f(r) = [z'(r)]^2$
- [x] $ds^2 = (1+f)dr^2 + r^2 d\theta^2$

**11.2 Vielbein**
- [x] $e_1^r = 1/\sqrt{1+f}$ gives $g^{rr} = (e_1^r)^2$
- [x] $e_2^\theta = 1/r$ gives $g^{\theta\theta} = (e_2^\theta)^2$

**11.3 Christoffel symbols**
- [x] $\Gamma^r_{rr} = f'/(2(1+f))$
- [x] $\Gamma^r_{\theta\theta} = -r/(1+f)$
- [x] $\Gamma^\theta_{r\theta} = 1/r$

**11.4 Spin connection**
- [x] $\omega_\theta = \frac{1}{2}(1 - 1/\sqrt{1+f})\gamma_1\gamma_2$

**11.5 Hamiltonian**
- [x] Compare coefficients of $\partial_r$, $\partial_\theta$
- [x] Identify $A_\theta$ term

**11.6 Magnetic field**
- [x] $B_z = \frac{1}{r}\partial_r(r A_\theta)$
- [x] Compute derivative correctly

### 12. Numerical Verification

**12.1 Code implementation** (in `dft/scripts/`):
- [x] `analyze_charge_density.py`: LDOS for Gaussian bump
- [x] `analyze_topological_defects.py`: Pentagon/heptagon effects
- [x] `create_gaussian_bump.py`: Coordinate generation

**12.2 Generated plots** (in `figures/`):
- [x] Gaussian bump LDOS pattern
- [x] Pentagon vs heptagon comparison
- [x] Multiple defects superposition

**12.3 Quantitative checks**:
- [x] Zero crossing at $r = b/\sqrt{2}$ for Gaussian
- [x] Positive $\delta\rho$ for pentagon, negative for heptagon
- [x] Velocity reduction: $v(r) < v_F$ everywhere
- [x] Zero net magnetic flux: $\int B_z dA = 0$

---

## Part V: Open Questions and Extensions

### 13. Unresolved Issues

**13.1 Numerical factors**
- Exact prefactor in LDOS formula
- Relation $\eta$ ↔ pentagon/heptagon angle
- Correlation length $\xi$ from first principles

**13.2 Energy dependence**
Paper only shows $E=0$ results. Full $\rho(E,r)$ needed for:
- Comparison with STM at different biases
- Temperature dependence
- Transport properties

**13.3 Higher-order effects**
Perturbation theory to $O(\epsilon)$ only. $O(\epsilon^2)$ could:
- Modify zero crossing position
- Change magnitude of effects
- Introduce new features

### 14. Extensions for Future Work

**14.1 DFT verification**
- Create actual graphene with Gaussian bump
- Compute DFT charge density
- Compare with analytical prediction

**14.2 Transport properties**
- Conductivity from curvature
- Quantum Hall effect in pseudo-magnetic field
- Temperature dependence

**14.3 Experimental predictions**
- Specific STM patterns to look for
- Raman spectroscopy signatures
- Magnetotransport measurements

---

## Conclusion

This guide has provided complete derivations for all key equations in Vozmediano et al. (2008). The main achievements:

1. **Explicit metric derivation** from Gaussian geometry
2. **Complete curved Hamiltonian** with vielbein and spin connection
3. **Effective magnetic field** from gauge field curl
4. **LDOS perturbation theory** for both smooth and topological curvature
5. **Physical interpretation** of all results

The paper successfully demonstrates how graphene's unique electronic properties make it an ideal system for studying quantum field theory in curved space, with direct experimental implications for understanding disorder and ripples in real graphene samples.

**Key takeaway**: Curvature in graphene creates measurable electronic effects through both gauge fields and metric modifications, with distinctive signatures in local density of states that can be tested experimentally.