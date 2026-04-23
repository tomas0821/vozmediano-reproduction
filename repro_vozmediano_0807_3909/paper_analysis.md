# Analysis of Vozmediano et al. (2008) Paper Structure

## **Paper: "Gauge fields and curvature in graphene" (arXiv:0807.3909)**

### **Key Sections and Results:**

#### **I. Introduction**
- Motivation: Understanding disorder effects in graphene
- Two approaches: topological defects vs elasticity theory
- Both give rise to gauge fields coupled to electrons

#### **II. Summary of graphene features**
- Massless Dirac fermions in 2D
- Hamiltonian: $H_0 = i\hbar v_F \int d^2r \psi^\dagger(r)[\sigma_x\partial_x + \sigma_y\partial_y]\psi(r)$

#### **III. General formalism for curved graphene**
- Dirac equation in curved space: $i\gamma^\mu(\partial_\mu + \omega_\mu)\psi = 0$
- Green's function: $i\gamma^\mu(\partial_\mu + \omega_\mu)G(x,x') = \delta(x-x')(-g)^{-1/2}$
- LDOS: $\rho(E,\mathbf{r}) = -\frac{1}{\pi}\text{Im Tr}[G(E,\mathbf{r},\mathbf{r})\gamma^0]$

#### **IV. Smooth curvature: Gaussian bump example**
- **Key example**: Gaussian bump $z(r) = A e^{-r^2/b^2}$
- **Metric**: $ds^2 = (1+f(r))dr^2 + r^2d\theta^2$ with $f(r) = 4\epsilon(r^2/b^2)e^{-2r^2/b^2}$, $\epsilon=(A/b)^2$
- **Two main results**:
  1. **Effective Fermi velocity**: $ṽ_r(r) = v_F(1+f(r))^{-1/2}$ (Eq. 13)
  2. **Effective magnetic field**: $B_z = \frac{1}{4r}\frac{f'}{(1+f)^{3/2}}$ (Eq. 15)
- **LDOS correction**: Computed to first order in $\epsilon$
- **Figure 2**: Shows LDOS pattern (darker=negative, lighter=positive)

#### **V. Topological defects**
- Pentagons ($n=5$) and heptagons ($n=7$)
- Metric: $ds^2 = dt^2 + e^{2\Lambda(x,y)}(dx^2+dy^2)$
- $\Lambda(\mathbf{r}) = \sum_i \frac{\eta_i}{4\pi}\log(|\mathbf{r}-\mathbf{r}_i|)$
- **Key result**: Pentagons enhance LDOS, heptagons depress it

#### **VI. Conclusions**
- Morphology affects electronic properties
- Fermi velocity varies spatially
- Gauge fields appear in many contexts

## **What We've Reproduced So Far:**

### ✅ **Point 1: Green's function and LDOS for Gaussian bump**
- **Paper's result**: Figure 2 shows LDOS correction pattern
- **Our reproduction**: 
  - Derived LDOS formula $\delta\rho(E_F,r) \propto \frac{1}{r^2}(1-\frac{r^2}{2\sigma^2})e^{-r^2/2\sigma^2}$
  - Computed numerical results showing positive center, negative ring
  - Zero crossing at $r = b/\sqrt{2}$

### ✅ **Point 2: Effective Fermi velocity**
- **Paper's result**: Eq. (13): $ṽ_r(r) = v_F(1+f(r))^{-1/2}$
- **Our reproduction**:
  - Implemented formula
  - Found maximum reduction at $r = b/\sqrt{2}$ (1.44% for $\epsilon=0.04$)
  - No reduction at center ($r=0$)

### 🔄 **What's Missing from Full Reproduction:**

#### **1. Complete LDOS calculation details**
- Paper mentions "computed to first order in $\epsilon$"
- Our derivation is simplified; full Green's function convolution needed

#### **2. Figure 2 exact reproduction**
- Paper shows specific color pattern
- We have qualitative match but not exact quantitative comparison

#### **3. Effective magnetic field $B_z$ analysis**
- Eq. (15) gives $B_z = \frac{1}{4r}\frac{f'}{(1+f)^{3/2}}$
- We computed it but didn't analyze physical implications

#### **4. Topological defects section**
- Pentagons vs heptagons effects
- Metric for disclinations

#### **5. Comparison with tight-binding**
- Paper mentions gauge fields appear in TB but metric effects don't

## **What Constitutes "Full Reproduction"?**

### **Minimal Complete Reproduction:**
1. ✅ Derive and implement LDOS formula for Gaussian bump
2. ✅ Compute effective Fermi velocity variation  
3. ✅ Show qualitative LDOS pattern matches Figure 2
4. 🔄 Compute effective magnetic field $B_z$
5. 🔄 Analyze topological defects (pentagons/heptagons)
6. 🔄 Discuss gauge field vs metric effects

### **Enhanced Reproduction:**
7. 🔄 Full Green's function convolution (not just direct formula)
8. 🔄 Exact Figure 2 reproduction (color scale, dimensions)
9. 🔄 Energy dependence $\rho(E,r)$ not just $E=0$
10. 🔄 Comparison with tight-binding calculations

## **Our Current Status:**

We have **reproduced the core analytical results** (Points 1-2) but not the complete paper. The paper has:

1. **Smooth curvature analysis** (Gaussian bump) - **PARTIALLY DONE**
2. **Topological defects analysis** - **NOT DONE**
3. **Discussion/comparison with other approaches** - **NOT DONE**

## **Recommended Path Forward:**

### **Option A: Complete the Gaussian bump analysis**
1. Compute $B_z$ and analyze implications
2. Improve LDOS calculation to match Figure 2 exactly
3. Add energy dependence $\rho(E,r)$

### **Option B: Move to topological defects**
1. Implement metric for disclinations
2. Compute LDOS for pentagons vs heptagons
3. Compare with paper's statement: "pentagons enhance, heptagons depress"

### **Option C: Systematic completion**
1. Finish Gaussian bump (Point 1-2 refinement)
2. Do topological defects (Point 3)
3. Add discussion/comparison (Point 4-5)

**Given the paper's structure, I recommend Option C for comprehensive reproduction.**