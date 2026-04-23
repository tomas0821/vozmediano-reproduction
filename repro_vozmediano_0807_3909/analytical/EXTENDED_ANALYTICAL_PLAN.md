# Extended Analytical Plan: Beyond Equation 15

## Overview
The paper "Gauge fields and curvature in graphene" (arXiv:0807.3909) contains several analytical targets beyond Equation 15. This document outlines a comprehensive plan for additional analytical work.

## 1. Green's Function Derivation

### Goal
Solve Equation (5) for the Gaussian bump metric to obtain the electron propagator $G(x,x')$ to first order in perturbation theory.

### Key Equations
$$
i\gamma^\mu (\partial_\mu + \omega_\mu) G(x,x') = \delta(x-x')(-g)^{-1/2} \tag{5}
$$

### Steps
1. **Write metric perturbation**: $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ where $h_{\mu\nu} = \partial_\mu z \partial_\nu z$
2. **Expand Dirac operator**: $i\gamma^\mu(\partial_\mu + \omega_\mu) = i\gamma^\mu\partial_\mu + V_{\text{eff}}$
3. **Compute effective potential** $V_{\text{eff}}$ from spin connection and metric determinant
4. **Use Dyson series**: $G = G_0 + G_0 V_{\text{eff}} G_0 + \cdots$
5. **Extract first-order correction** in $\epsilon = (A/b)^2$

### Expected Result
$$
G(x,x') = G_0(x-x') + \epsilon G_1(x,x') + O(\epsilon^2)
$$
where $G_0$ is the flat-space Dirac propagator.

## 2. Local Density of States (LDOS) Calculation

### Goal
Derive the explicit expression for $\delta\rho(E_F, \mathbf{r})$ shown in Figure 2 of the paper.

### Key Equations
$$
\rho(E, \mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G(E, \mathbf{r}, \mathbf{r})\gamma^0] \tag{6}
$$

### Steps
1. **Compute $G(E, \mathbf{r}, \mathbf{r})$** from Green's function derivation
2. **Take imaginary part** and trace with $\gamma^0$
3. **Expand to first order** in $\epsilon$
4. **Simplify for Gaussian bump**: $z(r) = A e^{-r^2/b^2}$

### Expected Result
From paper discussion:
$$
\delta\rho(E_F, \mathbf{r}) \propto \frac{1}{r^2} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/2\sigma^2}
$$
Need to derive proportionality constant and exact functional form.

## 3. Effective Fermi Velocity Analysis

### Goal
Analyze spatial variation of Fermi velocity and its physical implications.

### Key Equations
$$
\tilde{v}_r(r, \theta) = v_F (1+f(r))^{-1/2} \tag{13}
$$
More generally:
$$
\tilde{v}_i(\mathbf{r}) = \frac{v_F}{\sqrt{1 + (\partial_i z)^2}}
$$

### Steps
1. **Compute velocity components** for Gaussian bump
2. **Analyze anisotropy**: $v_r(r) \neq v_\theta(r)$
3. **Compute average velocity** over sample
4. **Connect to experimental measurements** where $v_F$ is used as fitting parameter

### Physical Implications
- Reduced velocity near bump peak
- Anisotropic transport properties
- Possible interpretation of experimental $v_F$ variations

## 4. Topological Defects Analysis

### Goal
Extend analysis to topological defects (disclinations, dislocations).

### Key Equations
**Metric for cosmic string analogy**:
$$
ds^2 = dt^2 + e^{2\Lambda(x,y)}(dx^2 + dy^2) \tag{16}
$$
where
$$
\Lambda(\mathbf{r}) = \sum_{i=1}^N 4\pi\mu_i \log(|\mathbf{r}-\mathbf{r}_i|)
$$

**Effective potential**:
$$
V(\omega, \mathbf{r}) = 2i\gamma^0\partial_0 + i\gamma^j\partial_j + 2i\gamma^j(\partial_j\Lambda) \tag{17}
$$

### Steps for Pentagon/Heptagon Defects
1. **Parameter mapping**: $\mu_i$ for pentagon ($n=5$) vs heptagon ($n=7$)
2. **Compute Green's function** for single defect
3. **Calculate LDOS correction**
4. **Compare pentagon (enhancement) vs heptagon (depression)** effects
5. **Analyze multiple defect configurations**

## 5. Perturbation Theory Framework

### Goal
Develop systematic perturbation theory in small deformation parameter.

### Expansion Parameter
$$
\epsilon = \left(\frac{A}{b}\right)^2 \approx 0.01 \text{ for typical ripples}
$$

### Order Analysis
1. **Zeroth order**: Flat Dirac equation
2. **First order**: 
   - Metric determinant contribution: $\sqrt{-g} \approx 1 + \frac{1}{2}h + \cdots$
   - Curved gamma matrices: $\gamma^\mu = e_a^\mu \gamma^a$
   - **Note**: Paper states gauge field contribution vanishes at first order
3. **Second order**: Include gauge field contributions

### Systematic Procedure
1. Expand metric: $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu} + h_{\mu\alpha}h^\alpha_\nu + \cdots$
2. Expand vielbein: $e_a^\mu = \delta_a^\mu - \frac{1}{2}h_a^\mu + \frac{3}{8}h_a^\alpha h_\alpha^\mu + \cdots$
3. Expand spin connection: $\omega_\mu = \omega_\mu^{(1)} + \omega_\mu^{(2)} + \cdots$
4. Expand Dirac operator order by order

## 6. Comparison with Tight-Binding Models

### Goal
Understand relationship between continuum geometric approach and discrete lattice models.

### Key Questions
1. Why do gauge fields appear in both approaches?
2. Why are metric determinant effects unique to continuum approach?
3. How to map geometric parameters to tight-binding parameters?

### Connection Points
- **Gauge fields**: Arise from modulation of hopping parameters $t_{ij}$ in tight-binding
- **Metric effects**: No direct tight-binding analogue
- **Elasticity theory**: Connection through strain tensor $\epsilon_{ij}$

## 7. Numerical Implementation Plan

### Code Structure
```python
# 1. Green's function solver
def green_function_curved(metric, energy, order=1):
    # Implement perturbative solution
    
# 2. LDOS calculator  
def compute_ldos(green_func, energy_range):
    # Compute density of states
    
# 3. Velocity analyzer
def effective_velocity(metric, position):
    # Compute local Fermi velocity
    
# 4. Topological defect module
def topological_defect_ldos(defect_type, positions):
    # Compute LDOS for pentagons/heptagons
```

### Validation Tests
1. **Flat limit**: Recover standard Dirac propagator
2. **Small deformation**: Match perturbative results
3. **Symmetry checks**: Rotational symmetry for Gaussian bump
4. **Conservation laws**: Charge conservation, zero total flux

## 8. Physical Predictions to Test

### Experimental Connections
1. **STM measurements**: Compare predicted LDOS patterns with experiments
2. **Transport properties**: Anisotropic conductivity from velocity variations
3. **Raman spectroscopy**: Strain effects on phonon modes
4. **Quantum Hall effect**: Modified Landau levels in curved graphene

### Parameter Ranges
- **Height**: $A = 0.1-1.0$ nm
- **Width**: $b = 1-10$ nm  
- **Aspect ratio**: $A/b = 0.01-0.1$
- **Fermi energy**: $E_F = 0-0.5$ eV

## Timeline and Priorities

### Phase 1: Core Extensions (1-2 weeks)
1. Green's function derivation (Section 1)
2. LDOS calculation (Section 2)
3. Velocity analysis (Section 3)

### Phase 2: Advanced Topics (2-3 weeks)
4. Topological defects (Section 4)
5. Second-order perturbation theory (Section 5)

### Phase 3: Connections and Applications (1-2 weeks)
6. Tight-binding comparison (Section 6)
7. Experimental predictions (Section 8)

## Expected Deliverables

1. **Analytical derivations**: Complete mathematical derivations
2. **Python code**: Implementation of all calculations
3. **Visualizations**: LDOS maps, velocity fields, etc.
4. **Comparison with paper**: Verification of published results
5. **Extensions**: New results beyond original paper

## References from Paper

1. Equation (5): Green's function in curved space
2. Equation (6): LDOS definition
3. Equation (13): Effective Fermi velocity
4. Equation (15): Effective magnetic field (already derived)
5. Equation (16): Metric for topological defects
6. Equation (17): Effective potential for defects
7. Figure 2: LDOS pattern for Gaussian bump

This extended analytical plan provides a roadmap for comprehensive reproduction and extension of the paper's results.