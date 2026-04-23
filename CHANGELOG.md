# CHANGELOG — Vozmediano Reproduction Project

## 2026-04-23 — Session Resume

### Project: Reproduction of "Gauge fields and curvature in graphene" (arXiv:0807.3909)

**Paper**: Vozmediano, de Juan, Cortijo (2008). "Gauge fields and curvature in graphene." arXiv:0807.3909.

### State at Resume

The analytical reproduction is **~80% complete**. DFT verification is **not started**.

#### ✅ Completed
1. **Section IV (Gaussian bump / smooth ripples)**: ~90% complete
   - LDOS formula (Eq. 15) derived and implemented
   - Effective Fermi velocity (Eq. 13) analyzed
   - LDOS pattern matches Figure 2 qualitatively (positive center, negative ring)
   - Zero crossing at `r = b/√2` verified
   - Plots generated in `analytical/plots/`
   - Key files: `notes.md`, `ldos_calculation.py`, `velocity_analysis.py`, `verify_eq15.py`

2. **Section V (Topological defects)**: ~90% complete
   - Metric for disclinations implemented
   - Pentagon (η>0) enhances LDOS — CONFIRMED
   - Heptagon (η<0) depresses LDOS — CONFIRMED
   - Plots: `figures/topological_defect_*.png`
   - Key file: `dft/scripts/analyze_topological_defects.py`

3. **LaTeX compilation infrastructure** (last session's focus)
   - `complete_derivations.tex` created (22 KB)
   - HTML + MathJax version works in browser
   - Multiple compilation scripts (Docker, local, Python fallback)
   - Python HTML→PDF generation attempted but equations don't render cleanly
   - Enhancement PDF: `complete_derivations_enhanced.pdf` (683 KB, eqns as images)
   - Recommends browser Print-to-PDF as best method

#### 🔴 Not Started
- **DFT calculations** for Gaussian bump
- **DFT calculations** for topological defects
- **Quantitative LDOS comparison** — magnitude differs from paper (scale/color)
- **Full energy dependence** of LDOS (only computed at E_F=0)
- **Green's function convolution** — simplified direct formula used instead
- **Second-order perturbation theory** — gauge field contributions

#### Known Issues
1. `compute_greens_function.py` has NaN/infinity issues at coincident points
2. LDOS normalization — paper doesn't specify absolute scale
3. Some parameter values not explicitly given in paper
4. DFT requires HPC access (no runs yet)

### What We Did This Session
1. ✓ Confirmed all analytical scripts run cleanly (verify_eq15.py, ldos_calculation.py, velocity_analysis.py, test_ldos_simple.py, analyze_topological_defects.py)
2. ✓ Read the full original paper (arXiv:0807.3909) to understand the target
3. ✓ Verified topological defects results: pentagon enhancement / heptagon depression confirmed
4. ✓ Identified the LDOS calculation has a slight mismatch (zero crossing at 4.94 nm vs expected 3.54 nm)
5. ✓ CHANGELOG initialized as lab notebook
6. ✓ **Git repo created and pushed to GitHub**: https://github.com/tomas0821/vozmediano-reproduction
   - Cleaned up nested duplicate directory, stray files
   - Proper .gitignore (PDFs excluded, data artifacts excluded)
   - Paper PDF excluded (copyright) — arxiv link in README instead
   - 69 files, 13k+ lines committed
