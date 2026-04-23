# Green's Function Derivation for Gaussian Bump

## 1. Problem Statement

We need to solve the Dirac equation in curved space for the Green's function:

$$
i\gamma^\mu (\partial_\mu + \omega_\mu) G(x,x') = \delta(x-x')(-g)^{-1/2} \tag{5}
$$

For the Gaussian bump metric:
$$
ds^2 = (1+f(r)) dr^2 + r^2 d\theta^2
$$
where
$$
f(r) = [z'(r)]^2 = 4A^2 \frac{r^2}{b^4} e^{-2r^2/b^2}
$$

## 2. Perturbative Expansion

Define small parameter:
$$
\epsilon = \left(\frac{A}{b}\right)^2 \approx 0.01
$$

Expand metric to first order in $\epsilon$:
$$
g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu} + O(\epsilon^2)
$$

For our metric:
$$
g_{rr} = 1 + f(r) = 1 + 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}
$$
$$
g_{\theta\theta} = r^2 \quad \text{(unchanged to first order)}
$$
$$
g_{r\theta} = g_{\theta r} = 0
$$

Thus:
$$
h_{rr} = 4\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}, \quad h_{\theta\theta} = 0, \quad h_{r\theta} = 0
$$

## 3. Vielbein Expansion

The vielbein $e_a^\mu$ satisfies:
$$
e_a^\mu e_b^\nu \eta^{ab} = g^{\mu\nu}
$$

For diagonal metric, choose:
$$
e_1^r = \frac{1}{\sqrt{1+f}} \approx 1 - \frac{1}{2}f + \frac{3}{8}f^2 + \cdots
$$
$$
e_2^\theta = \frac{1}{r}
$$

To first order:
$$
e_1^r \approx 1 - 2\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}
$$
$$
e_2^\theta = \frac{1}{r} \quad \text{(exact)}
$$

## 4. Curved Gamma Matrices

$$
\gamma^\mu = e_a^\mu \gamma^a
$$

Thus:
$$
\gamma^r = e_1^r \gamma^1 \approx \left(1 - 2\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}\right) \gamma^1
$$
$$
\gamma^\theta = e_2^\theta \gamma^2 = \frac{1}{r} \gamma^2
$$

## 5. Spin Connection

The spin connection $\omega_\mu$ is given by:
$$
\omega_\mu = \frac{1}{4} \omega_\mu^{ab} \gamma_a \gamma_b
$$

For our metric, the only non-zero component is:
$$
\omega_\theta = \frac{1}{2} \left(1 - \frac{1}{\sqrt{1+f}}\right) \gamma_1 \gamma_2
$$

Expand to first order:
$$
\frac{1}{\sqrt{1+f}} \approx 1 - \frac{1}{2}f + \frac{3}{8}f^2 + \cdots
$$

Thus:
$$
\omega_\theta \approx \frac{1}{2} \left(1 - \left[1 - \frac{1}{2}f\right]\right) \gamma_1 \gamma_2 = \frac{1}{4} f \gamma_1 \gamma_2
$$

So:
$$
\omega_\theta \approx \epsilon \frac{r^2}{b^2} e^{-2r^2/b^2} \gamma_1 \gamma_2
$$

## 6. Metric Determinant

$$
\sqrt{-g} = \sqrt{\det(g_{\mu\nu})} = r\sqrt{1+f} \approx r\left(1 + \frac{1}{2}f\right)
$$

Thus:
$$
(-g)^{-1/2} \approx \frac{1}{r} \left(1 - \frac{1}{2}f\right)
$$

## 7. Dirac Operator Expansion

The full Dirac operator is:
$$
\mathcal{D} = i\gamma^\mu (\partial_\mu + \omega_\mu)
$$

Write as:
$$
\mathcal{D} = \mathcal{D}_0 + \mathcal{D}_1 + O(\epsilon^2)
$$

where $\mathcal{D}_0$ is the flat operator and $\mathcal{D}_1$ is first-order correction.

### 7.1 Flat Operator
In polar coordinates:
$$
\mathcal{D}_0 = i\gamma^1 \partial_r + i\gamma^2 \frac{1}{r} \partial_\theta
$$

### 7.2 First-Order Correction
From our expansions:
$$
\mathcal{D}_1 = i(\gamma^r - \gamma^1)\partial_r + i\gamma^\theta \omega_\theta
$$

Compute term by term:

1. **Gamma matrix correction**:
   $$
   \gamma^r - \gamma^1 = \left(1 - 2\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2} - 1\right) \gamma^1 = -2\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2} \gamma^1
   $$

2. **Spin connection term**:
   $$
   \gamma^\theta \omega_\theta = \frac{1}{r} \gamma^2 \cdot \epsilon \frac{r^2}{b^2} e^{-2r^2/b^2} \gamma_1 \gamma_2 = \epsilon \frac{r}{b^2} e^{-2r^2/b^2} \gamma^2 \gamma_1 \gamma_2
   $$
   Using $\gamma^2 \gamma_1 \gamma_2 = -\gamma_1$ (since $\gamma_2 \gamma_2 = 1$ and $\gamma_1 \gamma_2 = -\gamma_2 \gamma_1$):
   $$
   \gamma^\theta \omega_\theta = -\epsilon \frac{r}{b^2} e^{-2r^2/b^2} \gamma^1
   $$

Thus:
$$
\mathcal{D}_1 = -i\epsilon \left(2\frac{r^2}{b^2} \partial_r + \frac{r}{b^2}\right) e^{-2r^2/b^2} \gamma^1
$$

## 8. Green's Function Equation

The equation is:
$$
(\mathcal{D}_0 + \mathcal{D}_1) G(x,x') = \delta(x-x')(-g)^{-1/2}
$$

Write perturbative expansion:
$$
G = G_0 + G_1 + O(\epsilon^2)
$$

where $G_0$ satisfies:
$$
\mathcal{D}_0 G_0(x,x') = \delta(x-x')
$$

## 9. Flat-Space Green's Function

For massless Dirac in 2D, the retarded Green's function is:
$$
G_0(E, \mathbf{r}, \mathbf{r}') = -\frac{i}{4} \begin{pmatrix}
0 & H_0^{(1)}(k|\mathbf{r}-\mathbf{r}'|) e^{-i\phi} \\
H_0^{(1)}(k|\mathbf{r}-\mathbf{r}'|) e^{i\phi} & 0
\end{pmatrix}
$$

where $k = E/(\hbar v_F)$, $H_0^{(1)}$ is Hankel function, and $\phi = \arg(\mathbf{r}-\mathbf{r}')$.

In polar coordinates for coincident points ($\mathbf{r}' \to \mathbf{r}$), we need regularized expression.

## 10. First-Order Correction

From Dyson equation:
$$
\mathcal{D}_0 G_1 + \mathcal{D}_1 G_0 = \delta(x-x') \left[(-g)^{-1/2} - 1\right]
$$

The source term from metric determinant:
$$
(-g)^{-1/2} - 1 \approx -\frac{1}{2}f = -2\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2}
$$

Thus:
$$
\mathcal{D}_0 G_1 = -\mathcal{D}_1 G_0 - 2\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2} \delta(x-x')
$$

## 11. Formal Solution

Formally:
$$
G_1 = -G_0 * \mathcal{D}_1 G_0 - 2\epsilon G_0 * \left[\frac{r^2}{b^2} e^{-2r^2/b^2} \delta(x-x')\right]
$$

where $*$ denotes convolution.

For coincident points ($\mathbf{r}' = \mathbf{r}$):
$$
G_1(E, \mathbf{r}, \mathbf{r}) = - \int d^2\mathbf{r}'' \, G_0(E, \mathbf{r}, \mathbf{r}'') \mathcal{D}_1(\mathbf{r}'') G_0(E, \mathbf{r}'', \mathbf{r}) - 2\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2} G_0(E, \mathbf{r}, \mathbf{r})
$$

## 12. LDOS from Green's Function

The local density of states is:
$$
\rho(E, \mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G(E, \mathbf{r}, \mathbf{r})\gamma^0]
$$

Write:
$$
\rho = \rho_0 + \rho_1 + O(\epsilon^2)
$$

where:
$$
\rho_0(E, \mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G_0(E, \mathbf{r}, \mathbf{r})\gamma^0]
$$
$$
\rho_1(E, \mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G_1(E, \mathbf{r}, \mathbf{r})\gamma^0]
$$

## 13. Flat-Space LDOS

For massless Dirac in 2D at zero temperature:
$$
\rho_0(E, \mathbf{r}) = \frac{|E|}{2\pi (\hbar v_F)^2}
$$

This is constant in space.

## 14. First-Order LDOS Correction

We need to compute:
$$
\rho_1(E, \mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G_1(E, \mathbf{r}, \mathbf{r})\gamma^0]
$$

From our expression for $G_1$:
$$
\rho_1(E, \mathbf{r}) = \frac{1}{\pi} \text{Im Tr}\left[\int d^2\mathbf{r}'' \, G_0(E, \mathbf{r}, \mathbf{r}'') \mathcal{D}_1(\mathbf{r}'') G_0(E, \mathbf{r}'', \mathbf{r}) \gamma^0\right] + \frac{2\epsilon}{\pi} \frac{r^2}{b^2} e^{-2r^2/b^2} \text{Im Tr}[G_0(E, \mathbf{r}, \mathbf{r})\gamma^0]
$$

The second term vanishes since $G_0(E, \mathbf{r}, \mathbf{r})$ is real for $E$ real.

Thus:
$$
\rho_1(E, \mathbf{r}) = \frac{1}{\pi} \text{Im Tr}\left[\int d^2\mathbf{r}'' \, G_0(E, \mathbf{r}, \mathbf{r}'') \mathcal{D}_1(\mathbf{r}'') G_0(E, \mathbf{r}'', \mathbf{r}) \gamma^0\right]
$$

## 15. Simplification for Gaussian Bump

Substitute $\mathcal{D}_1$:
$$
\mathcal{D}_1(\mathbf{r}'') = -i\epsilon \left(2\frac{r''^2}{b^2} \partial_{r''} + \frac{r''}{b^2}\right) e^{-2r''^2/b^2} \gamma^1
$$

Thus:
$$
\rho_1(E, \mathbf{r}) = -\frac{\epsilon}{\pi b^2} \text{Im Tr}\left[\int d^2\mathbf{r}'' \, G_0(E, \mathbf{r}, \mathbf{r}'') \left(2r''^2 \partial_{r''} + r''\right) e^{-2r''^2/b^2} \gamma^1 G_0(E, \mathbf{r}'', \mathbf{r}) \gamma^0\right]
$$

## 16. Angular Integration

Due to rotational symmetry, we can perform angular integration. The Green's function depends on $|\mathbf{r}-\mathbf{r}''|$.

Let $\mathbf{r} = (r, 0)$ without loss of generality. Then:
$$
|\mathbf{r}-\mathbf{r}''| = \sqrt{r^2 + r''^2 - 2rr''\cos\theta''}
$$

The integral becomes:
$$
\rho_1(E, r) = -\frac{\epsilon}{\pi b^2} \text{Im} \int_0^\infty r'' dr'' \int_0^{2\pi} d\theta'' \, \text{Tr}\left[G_0(E, r, r'', \theta'') \left(2r''^2 \partial_{r''} + r''\right) e^{-2r''^2/b^2} \gamma^1 G_0(E, r'', r, -\theta'') \gamma^0\right]
$$

## 17. Next Steps

To complete the derivation:

1. **Explicit form of $G_0$**: Write flat Green's function in polar coordinates
2. **Perform angular integration**: Use addition theorem for Hankel functions
3. **Radial integration**: Evaluate the integral over $r''$
4. **Take imaginary part**: Extract LDOS correction
5. **Simplify**: Obtain final expression for $\rho_1(E, r)$

The paper states the final result should be of the form:
$$
\delta\rho(E_F, \mathbf{r}) \propto \frac{1}{r^2} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/2\sigma^2}
$$

We need to verify this and determine the proportionality constant.

## 18. Key Challenges

1. **Regularization**: $G_0(E, \mathbf{r}, \mathbf{r})$ is divergent, needs careful treatment
2. **Angular integration**: Non-trivial due to matrix structure
3. **Derivative operator**: $\partial_{r''}$ acting on both Green's function and Gaussian
4. **Energy dependence**: Result should be evaluated at Fermi energy $E_F$

## 19. Alternative Approach

The paper mentions: "all the corrections come from the determinant of the metric and the curved gamma matrices" and "the contribution of the effective gauge field coming from the spin connection to first order in perturbation theory vanishes."

This suggests we might simplify by considering only:
$$
\mathcal{D}_1^{\text{eff}} = i(\gamma^\mu - \gamma_0^\mu)\partial_\mu
$$
and ignoring the spin connection term at first order.

This would give:
$$
\mathcal{D}_1^{\text{eff}} = -2i\epsilon \frac{r^2}{b^2} e^{-2r^2/b^2} \gamma^1 \partial_r
$$

Then the calculation simplifies considerably.

## 20. Implementation Plan

1. Write Python code to compute the integral numerically
2. Compare with expected analytical form
3. Extract functional form and proportionality constant
4. Verify against paper's Figure 2

This derivation provides the foundation for computing the LDOS correction shown in the paper.