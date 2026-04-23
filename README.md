# Reproduction of "Gauge fields and curvature in graphene" (arXiv:0807.3909)

[![arXiv](https://img.shields.io/badge/arXiv-0807.3909-b31b1b.svg)](https://arxiv.org/abs/0807.3909)

Analytical and computational reproduction of key results from **Vozmediano, de Juan & Cortijo (2008)**, which models curvature in graphene using the massless Dirac equation coupled to curved space.

## Project Structure

```
vozmediano/
├── repro_vozmediano_0807_3909/
│   ├── analytical/           # LDOS, Fermi velocity, Green's function code
│   │   ├── verify_eq15.py           # Eq. 15 — effective magnetic field
│   │   ├── ldos_calculation.py      # LDOS correction for Gaussian bump
│   │   ├── velocity_analysis.py     # Effective Fermi velocity (Eq. 13)
│   │   ├── test_ldos_simple.py      # Quick LDOS verification
│   │   ├── compute_greens_function.py  # Green's function (in progress)
│   │   └── plots/                   # Generated figures
│   ├── dft/scripts/           # DFT setup and analysis
│   │   ├── analyze_charge_density.py      # Gaussian bump LDOS
│   │   ├── analyze_topological_defects.py # Pentagon/heptagon analysis
│   │   ├── create_gaussian_bump.py        # XYZ coordinate generation
│   │   ├── flat_graphene.xyz              # Flat reference structure
│   │   └── graphene_gaussian_bump.xyz     # Bump structure
│   ├── figures/               # Topological defect plots
│   ├── paper/                 # Original PDF
│   ├── complete_derivations.tex  # Full LaTeX derivation document
│   ├── complete_derivations.html # HTML with MathJax (viewable in browser)
│   └── PROJECT_STATUS.md      # Detailed status tracking
├── CHANGELOG.md
└── README.md
```

## Reproduced Results

### ✅ Gaussian Bump (Section IV)
- **LDOS correction**: $\delta\rho(r) \propto \frac{1}{r^2}(1 - \frac{r^2}{2\sigma^2})e^{-r^2/2\sigma^2}$ — positive center, negative ring
- **Effective Fermi velocity**: $ṽ_r(r) = v_F(1+f(r))^{-1/2}$ — up to ~1.4% reduction
- **Effective magnetic field**: $B_z$ from Eq. (15)

### ✅ Topological Defects (Section V)
- **Pentagons** ($\eta > 0$): enhance local electron density — **confirmed**
- **Heptagons** ($\eta < 0$): depress local electron density — **confirmed**
- Multiple defect superposition demonstrated

### 🔄 In Progress
- Full Green's function convolution (NaN issue at coincident points)
- DFT verification (Quantum ESPRESSO / VASP)

## Quick Start

```bash
# Reproduce Gaussian bump analysis
python3 repro_vozmediano_0807_3909/analytical/verify_eq15.py

# Reproduce LDOS pattern
python3 repro_vozmediano_0807_3909/analytical/ldos_calculation.py

# Reproduce topological defects
python3 repro_vozmediano_0807_3909/dft/scripts/analyze_topological_defects.py

# View the full derivation document (HTML with MathJax)
firefox repro_vozmediano_0807_3909/complete_derivations.html
```

## Requirements

- Python 3.10+
- `numpy`, `scipy`, `matplotlib`
- (optional) `reportlab` for PDF generation

## Reference

M. A. H. Vozmediano, F. de Juan, A. Cortijo. *Gauge fields and curvature in graphene.*
arXiv:0807.3909 [cond-mat.str-el], 2008.
