# Derivation of Equation (15): Effective Magnetic Field from Gaussian Bump

This document provides a step-by-step derivation of Equation (15) from the paper "Gauge fields and curvature in graphene" (arXiv:0807.3909), Section IV.

## 1. Setup: Gaussian Bump Geometry

We consider a graphene sheet with a smooth Gaussian bump described by:

$$
z(r) = A e^{-r^2/b^2}
$$

where:
- $A$ = maximum height of the bump
- $b$ = width parameter of the Gaussian
- $r = \sqrt{x^2 + y^2}$ = radial coordinate

## 2. Induced Metric on the Deformed Surface

The line element in 3D cylindrical coordinates is:

$$
ds^2 = dr^2 + r^2 d\theta^2 + dz^2
$$

For our surface $z = z(r)$, we have:

$$
dz = \frac{dz}{dr} dr = z'(r) dr
$$

Substituting:

$$
ds^2 = dr^2 + r^2 d\theta^2 + [z'(r)]^2 dr^2
$$
$$
ds^2 = [1 + (z'(r))^2] dr^2 + r^2 d\theta^2
$$

The paper defines:

$$
f(r) \equiv [z'(r)]^2
$$

So the metric becomes:

$$
ds^2 = (1 + f(r)) dr^2 + r^2 d\theta^2
$$

In matrix form:

$$
g_{\mu\nu} = \begin{pmatrix}
1 + f(r) & 0 \\
0 & r^2
\end{pmatrix}
$$

## 3. Dirac Equation in Curved Space

The Dirac equation for massless fermions in curved space is:

$$
i \gamma^\mu (\partial_\mu + \omega_\mu) \psi = 0
$$

where $\gamma^\mu$ are the curved-space gamma matrices related to the flat ones by:

$$
\gamma^\mu = e_a^\mu \gamma^a
$$

with $e_a^\mu$ being the vielbein (tetrad) satisfying:

$$
e_a^\mu e_b^\nu \eta^{ab} = g^{\mu\nu}
$$

## 4. Vielbein for Our Metric

For the metric $ds^2 = (1+f) dr^2 + r^2 d\theta^2$, a natural choice of vielbein is:

$$
e_1^r = \frac{1}{\sqrt{1+f}}, \quad e_2^\theta = \frac{1}{r}
$$

In matrix form:

$$
e_a^\mu = \begin{pmatrix}
\frac{1}{\sqrt{1+f}} & 0 \\
0 & \frac{1}{r}
\end{pmatrix}
$$

The inverse vielbein $e_\mu^a$ satisfies $e_\mu^a e_a^\nu = \delta_\mu^\nu$:

$$
e_r^1 = \sqrt{1+f}, \quad e_\theta^2 = r
$$

## 5. Spin Connection

The spin connection $\omega_\mu$ is given by:

$$
\omega_\mu = \frac{1}{4} \omega_\mu^{ab} \gamma_a \gamma_b
$$

where $\omega_\mu^{ab}$ is computed from:

$$
\omega_\mu^{ab} = e_\nu^a (\partial_\mu e^{\nu b} + \Gamma^\nu_{\mu\lambda} e^{\lambda b})
$$

For our diagonal metric, the Christoffel symbols are:

$$
\Gamma^r_{rr} = \frac{f'}{2(1+f)}, \quad \Gamma^r_{\theta\theta} = -\frac{r}{1+f}
$$
$$
\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = \frac{1}{r}
$$

The non-zero spin connection components are:

$$
\omega_\theta^{12} = -\omega_\theta^{21} = 1 - \frac{1}{\sqrt{1+f}}
$$

Thus:

$$
\omega_\theta = \frac{1}{2} \left(1 - \frac{1}{\sqrt{1+f}}\right) \gamma_1 \gamma_2
$$

## 6. Dirac Hamiltonian in Polar Coordinates

In polar coordinates, the flat Dirac Hamiltonian is (from Eq. 10 in the paper):

$$
H_{\text{flat}} = -i\hbar v_F \begin{pmatrix}
0 & e^{-i\theta} (\partial_r - \frac{i}{r}\partial_\theta + \frac{1}{2r}) \\
e^{i\theta} (\partial_r + \frac{i}{r}\partial_\theta + \frac{1}{2r}) & 0
\end{pmatrix}
$$

For the curved case, we need to include:
1. The vielbein factors $e_a^\mu$
2. The spin connection $\omega_\mu$

The curved Hamiltonian becomes (Eq. 11):

$$
H_{\text{curved}} = -i\hbar v_F \begin{pmatrix}
0 & (1+f)^{-1/2} e^{-i\theta} (\partial_r - \frac{i}{r}\partial_\theta + A_\theta) \\
(1+f)^{-1/2} e^{i\theta} (\partial_r + \frac{i}{r}\partial_\theta + A_\theta^*) & 0
\end{pmatrix}
$$

where $A_\theta$ is the effective gauge field arising from the spin connection.

## 7. Effective Gauge Field

From the spin connection, we get an effective U(1) gauge field. Comparing with the flat Hamiltonian, we identify:

$$
A_\theta = \frac{1}{2r} (1 - (1+f)^{-1/2})
$$

This is Eq. (12) in the paper:

$$
A_\theta = \frac{1}{2r} - \frac{1}{2r} (1+f)^{-1/2}
$$

## 8. Effective Magnetic Field

The effective magnetic field perpendicular to the graphene sheet is given by:

$$
B_z = \frac{1}{r} \partial_r (r A_\theta)
$$

Substituting $A_\theta$:

$$
B_z = \frac{1}{r} \partial_r \left[ r \cdot \frac{1}{2r} (1 - (1+f)^{-1/2}) \right]
$$
$$
B_z = \frac{1}{r} \partial_r \left[ \frac{1}{2} (1 - (1+f)^{-1/2}) \right]
$$
$$
B_z = \frac{1}{r} \cdot \frac{1}{2} \cdot \frac{1}{2} (1+f)^{-3/2} f'
$$
$$
B_z = \frac{1}{4r} \frac{f'}{(1+f)^{3/2}}
$$

This is exactly Equation (15) in the paper!

## 9. For Gaussian Bump

For the specific Gaussian shape:

$$
f(r) = \left(\frac{dz}{dr}\right)^2 = \left(-2A \frac{r}{b^2} e^{-r^2/b^2}\right)^2 = 4A^2 \frac{r^2}{b^4} e^{-2r^2/b^2}
$$

The derivative is:

$$
f'(r) = 4A^2 \frac{2r}{b^4} e^{-2r^2/b^2} - 4A^2 \frac{r^2}{b^4} \cdot \frac{4r}{b^2} e^{-2r^2/b^2}
$$
$$
f'(r) = 8A^2 \frac{r}{b^4} e^{-2r^2/b^2} \left(1 - \frac{2r^2}{b^2}\right)
$$

Thus the effective magnetic field becomes:

$$
B_z(r) = \frac{1}{4r} \frac{8A^2 \frac{r}{b^4} e^{-2r^2/b^2} \left(1 - \frac{2r^2}{b^2}\right)}{\left[1 + 4A^2 \frac{r^2}{b^4} e^{-2r^2/b^2}\right]^{3/2}}
$$
$$
B_z(r) = \frac{2A^2}{b^4} \frac{e^{-2r^2/b^2} \left(1 - \frac{2r^2}{b^2}\right)}{\left[1 + 4A^2 \frac{r^2}{b^4} e^{-2r^2/b^2}\right]^{3/2}}
$$

## 10. Small Deformation Limit

For small deformations $A/b \ll 1$, we can approximate:

$$
(1+f)^{-3/2} \approx 1 - \frac{3}{2}f
$$

and keep only leading order in $A^2/b^2$:

$$
B_z(r) \approx \frac{2A^2}{b^4} e^{-2r^2/b^2} \left(1 - \frac{2r^2}{b^2}\right)
$$

This shows that the effective magnetic field:
1. Changes sign at $r = b/\sqrt{2}$
2. Is positive for $r < b/\sqrt{2}$ (outward field)
3. Is negative for $r > b/\sqrt{2}$ (inward field)
4. Has zero net flux (as expected for a bump)

## 11. Physical Interpretation

The effective magnetic field $B_z$ arises because:
1. The curvature of the graphene sheet modifies the electron hopping
2. This is equivalent to electrons experiencing a pseudo-magnetic field
3. The field is perpendicular to the graphene sheet
4. It affects electron motion, creating Landau-level-like states

This pseudo-magnetic field is responsible for the modifications to the local density of states shown in Figure 2 of the paper.

## 12. Verification Steps

To verify this derivation numerically:

1. **Plot $f(r)$ and $f'(r)$** for Gaussian parameters
2. **Compute $A_\theta(r)$** from Eq. (12)
3. **Compute $B_z(r)$** from Eq. (15)
4. **Check small deformation limit** matches approximate formula
5. **Verify zero total flux**: $\int_0^\infty r B_z(r) dr = 0$

## References

- Vozmediano, M. A. H., de Juan, F., & Cortijo, A. (2008). Gauge fields and curvature in graphene. arXiv:0807.3909
- de Juan, F., Cortijo, A., & Vozmediano, M. A. H. (2007). Phys. Rev. B 76, 165409 (reference [17] in the paper)