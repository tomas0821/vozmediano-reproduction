# Reproduction of "Gauge fields and curvature in graphene" (arXiv:0807.3909)

This project aims to reproduce key results from the paper **"Gauge fields and curvature in graphene"** by María A. H. Vozmediano, Fernando de Juan, and Alberto Cortijo (2008).

## Project Goal

Reproduce the analytical and computational results from **Section IV: "Smooth Ripples from the Substrate"** and **Section V: "Topological Defects"** of the paper, which model:
1. **Gaussian bump** on graphene sheet and its effect on LDOS
2. **Topological defects** (pentagons/heptagons) and their effect on LDOS

## Project Structure

```
repro_vozmediano_0807_3909/
├── README.md                 # This file
├── paper/
│   └── vozmediano_gauge_fields_curvature_graphene_2008.pdf  # The paper
├── analytical/               # Analytical derivations and calculations
│   ├── notes.md             # Step-by-step analytical derivation
│   ├── calculations/        # Mathematica/Python notebooks for calculations
│   └── figures/             # Generated analytical plots
└── dft/                     # DFT simulation files
    ├── inputs/              # DFT input files (Quantum ESPRESSO, VASP, etc.)
    ├── scripts/             # Python/bash scripts for setup and analysis
    ├── outputs/             # Raw DFT output files
    └── analysis/            # Processed results and plots
```

## Target Results

### **Section IV: Gaussian Bump**
Reproduce **Figure 2** from the paper, which shows the LDOS correction $\delta \rho(E_F, \mathbf{r})$ for a Gaussian bump. The analytical expression (Eq. 15) predicts:

\[
\delta \rho(E_F, \mathbf{r}) \propto \frac{1}{r^2} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/2\sigma^2}
\]

where $\sigma$ is the Gaussian width parameter.

### **Section V: Topological Defects**
Reproduce the key finding that:
- **Pentagon defects** ($\eta > 0$) **enhance** local electron density
- **Heptagon defects** ($\eta < 0$) **depress** local electron density

The metric for topological defects is:
\[
ds^2 = dt^2 + e^{2\Lambda(x,y)}(dx^2 + dy^2)
\]
with $\Lambda(\mathbf{r}) = \sum_i \frac{\eta_i}{4\pi} \log(|\mathbf{r} - \mathbf{r}_i|)$

## Work Plan

### Phase 1: Analytical Reproduction - Gaussian Bump
1. ✅ **Derive the metric** for the Gaussian bump from Eqs. (7)-(9)
2. ✅ **Calculate the effective potential** from the spin connection and metric
3. ✅ **Use perturbation theory** to compute the Green's function correction
4. ✅ **Derive the LDOS correction** and reproduce Eq. (15)
5. ✅ **Generate the plot** matching Figure 2 (qualitative match)

### Phase 2: Analytical Reproduction - Topological Defects
1. ✅ **Implement metric** for topological defects: $ds^2 = dt^2 + e^{2\Lambda}(dx^2+dy^2)$
2. ✅ **Compute effective potential** $V(\omega, \mathbf{r})$ from Eq. (17)
3. ✅ **Calculate LDOS correction** for pentagons vs heptagons
4. ✅ **Verify key result**: Pentagons enhance LDOS, heptagons depress LDOS
5. ✅ **Generate plots** showing defect effects

### Phase 3: DFT Reproduction
1. **Create graphene supercell** with Gaussian displacement $z(r) = h e^{-r^2/2\sigma^2}$
2. **Perform structural relaxation** to find ground state geometry
3. **Run DFT calculation** to compute charge density/LDOS
4. **Analyze spatial variation** of charge density
5. **Compare with analytical prediction**

### Phase 4: Comparison and Validation
1. **Compare analytical and DFT results**
2. **Quantify agreement/discrepancies**
3. **Document findings and insights**

## Current Status

### ✅ **COMPLETED: Analytical Reproduction**
1. **Gaussian bump analysis** (`analytical/notes.md`, `dft/scripts/analyze_charge_density.py`)
   - Derived LDOS formula matching Eq. (15)
   - Computed effective Fermi velocity $ṽ_r(r) = v_F(1+f(r))^{-1/2}$
   - Generated plots showing LDOS pattern (positive center, negative ring)
   - Verified zero crossing at $r = b/\sqrt{2}$

2. **Topological defects analysis** (`dft/scripts/analyze_topological_defects.py`)
   - Implemented metric for disclinations: $g_{\mu\nu} = e^{2\Lambda}\delta_{\mu\nu}$
   - Computed LDOS corrections for pentagons ($\eta>0$) vs heptagons ($\eta<0$)
   - **Verified key paper claim**: Pentagons enhance LDOS, heptagons depress LDOS
   - Generated comparison plots showing opposite effects

### 🔄 **IN PROGRESS: DFT Reproduction**
1. **Gaussian bump DFT setup** (`dft/scripts/create_gaussian_bump.py`)
   - Script to create displaced graphene coordinates
   - Ready for DFT calculations

### 📋 **NEXT STEPS**
1. **Run DFT calculations** for Gaussian bump
2. **Compare DFT LDOS** with analytical prediction
3. **Extend topological defects** to DFT simulations
4. **Write comprehensive report** comparing all results

## References

- Paper: [arXiv:0807.3909](https://arxiv.org/abs/0807.3909)
- Vozmediano's related work: [arXiv:1003.5179](https://arxiv.org/abs/1003.5179) (review paper)

## Notes

- The Gaussian bump parameters: height $h$ and width $\sigma$ should be chosen to match experimental/realistic values
- DFT calculations may require careful convergence testing for strained systems
- Both approaches should converge to the same qualitative picture of charge redistribution around the bump