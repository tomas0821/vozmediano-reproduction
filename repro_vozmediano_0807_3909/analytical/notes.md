# Analytical Derivation: Gaussian Bump in Graphene

## Goal
Reproduce the derivation of the LDOS correction for a Gaussian bump from Section IV of "Gauge fields and curvature in graphene" (arXiv:0807.3909).

## 1. Geometry of the Bump

The graphene sheet is deformed with a Gaussian profile:
$$
z(r) = h e^{-r^2/2\sigma^2}
$$
where:
- $h$ = maximum height of the bump
- $\sigma$ = width parameter
- $r = \sqrt{x^2 + y^2}$

## 2. Induced Metric

From the paper, the induced metric on the deformed surface is:
$$
g_{\mu\nu} = \delta_{\mu\nu} + \partial_\mu z \partial_\nu z
$$

For the Gaussian bump:
$$
\partial_x z = -\frac{h x}{\sigma^2} e^{-r^2/2\sigma^2}, \quad \partial_y z = -\frac{h y}{\sigma^2} e^{-r^2/2\sigma^2}
$$

Thus:
$$
g_{xx} = 1 + \left(\frac{h x}{\sigma^2}\right)^2 e^{-r^2/\sigma^2}
$$
$$
g_{yy} = 1 + \left(\frac{h y}{\sigma^2}\right)^2 e^{-r^2/\sigma^2}
$$
$$
g_{xy} = g_{yx} = \frac{h^2 x y}{\sigma^4} e^{-r^2/\sigma^2}
$$

## 3. Dirac Equation in Curved Space

The Dirac equation for massless fermions in curved space is:
$$
i \gamma^a e_a^\mu (\partial_\mu + \omega_\mu) \psi = 0
$$
where:
- $\gamma^a$ are flat-space Dirac matrices
- $e_a^\mu$ is the vielbein (tetrad)
- $\omega_\mu$ is the spin connection

## 4. Effective Potential

The key result from the paper (Eq. 15) is the LDOS correction at the Fermi energy:
$$
\delta \rho(E_F, \mathbf{r}) = -\frac{1}{4\pi v_F^2} \nabla^2 V(\mathbf{r})
$$
where $V(\mathbf{r})$ is the effective potential arising from the curvature.

For the Gaussian bump:
$$
V(\mathbf{r}) = \frac{v_F^2 h^2}{2\sigma^4} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/\sigma^2}
$$

## 5. LDOS Correction

Substituting into the expression:
$$
\delta \rho(E_F, \mathbf{r}) = -\frac{1}{4\pi v_F^2} \nabla^2 \left[ \frac{v_F^2 h^2}{2\sigma^4} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/\sigma^2} \right]
$$

After calculation (to be completed):
$$
\delta \rho(E_F, \mathbf{r}) \propto \frac{1}{r^2} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/2\sigma^2}
$$

## 6. Steps to Complete

1. **Derive the spin connection** $\omega_\mu$ from the metric
2. **Calculate the effective potential** $V(\mathbf{r})$ from the spin connection
3. **Apply perturbation theory** to get the Green's function correction
4. **Compute the LDOS** from the imaginary part of the Green's function
5. **Simplify to obtain Eq. (15)** and the final expression
6. **Numerically evaluate** for specific parameters $h, \sigma$
7. **Plot the result** to match Figure 2

## 7. Parameters for Numerical Evaluation

Suggested values (to match paper/realistic):
- $h = 1 \, \text{nm}$
- $\sigma = 5 \, \text{nm}$
- $v_F = 10^6 \, \text{m/s}$

## 8. Open Questions

1. What is the exact proportionality constant in the final expression?
2. How does the result depend on the Fermi energy $E_F$?
3. What are the boundary conditions for the perturbation calculation?

# Section V: Topological Defects in Graphene

## 1. Introduction to Topological Defects

From Section V of the paper: In the absence of a substrate or strain fields, intrinsic curvature in graphene arises from topological defects. The two main types are:

1. **Disclinations**: Replace a hexagon with an n-sided polygon
   - Pentagon: $n=5$ (most common, forms fullerenes)
   - Heptagon: $n=7$ (negative curvature)

2. **Dislocations**: Pentagon-heptagon pairs (disclination dipoles)

## 2. Metric for Topological Defects

The paper uses the cosmic string metric (Eq. 16):
$$
ds^2 = dt^2 + e^{2\Lambda(x,y)}(dx^2 + dy^2)
$$

where:
$$
\Lambda(\mathbf{r}) = \sum_{i=1}^N \frac{\eta_i}{4\pi} \log(|\mathbf{r} - \mathbf{r}_i|)
$$

with:
- $\mathbf{r}_i = (a_i, b_i)$: position of defect $i$
- $\eta_i$: strength parameter related to angle defect/surplus
- For pentagon: $\eta > 0$ (positive curvature)
- For heptagon: $\eta < 0$ (negative curvature)

## 3. Relation to Angle Defect

The angle defect/surplus $c_i$ is related to $\eta_i$ by:
$$
c_i = 1 - 4\eta_i
$$

For a perfect hexagon: $c=1$ (no defect)
For pentagon: $c < 1$, so $\eta > 0$
For heptagon: $c > 1$, so $\eta < 0$

## 4. Effective Potential from Curvature

From Eq. (17) in the paper, the Green's function is modified by the potential:
$$
V(\omega, \mathbf{r}) = 2i\gamma^0\partial_0 + i\gamma^j\partial_j + 2i\gamma^j(\partial_j\Lambda)
$$

For static defects ($\partial_0 = 0$), the effective potential simplifies to:
$$
V(\mathbf{r}) = i\gamma^j\partial_j + 2i\gamma^j(\partial_j\Lambda)
$$

## 5. LDOS Correction for Topological Defects

The paper states (without explicit formula):
- Pentagonal rings **enhance** electron density
- Heptagonal rings **depress** electron density

This matches numerical simulations [52] and ab initio calculations [53].

## 6. Derivation Plan

1. **Compute the metric** $g_{\mu\nu} = e^{2\Lambda}\delta_{\mu\nu}$
2. **Calculate spin connection** $\omega_\mu$ from the metric
3. **Derive effective Hamiltonian** $H = H_0 + V$
4. **Compute Green's function** $G = G_0 + G_0 V G_0 + \cdots$
5. **Extract LDOS** $\rho(E,\mathbf{r}) = -\frac{1}{\pi}\text{Im Tr}[G(E,\mathbf{r},\mathbf{r})\gamma^0]$

## 7. Numerical Implementation

We need to:
1. Implement the metric function $\Lambda(\mathbf{r})$ for single/multiple defects
2. Compute derivatives $\partial_j\Lambda$
3. Solve Dirac equation numerically or use perturbation theory
4. Compare pentagon vs heptagon effects

## 8. Parameters

Typical values from literature:
- Single pentagon: $\eta \approx 0.1$ (angle deficit $\sim 0.6$ rad)
- Single heptagon: $\eta \approx -0.1$ (angle surplus $\sim 1.4$ rad)
- Cutoff radius: $r_c \sim 1$ nm (defect core size)