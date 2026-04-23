# Next Steps: Fixing Green's Function Implementation

## Current Issues

1. **NaN in LDOS calculation** - Division by zero or similar issue
2. **Coincident point regularization** - $G_0(E, \mathbf{r}, \mathbf{r})$ needs careful treatment
3. **Numerical integration instability** - 2D integral may be problematic
4. **Energy dependence** - Need proper handling of $E=0$ (Fermi level)

## Immediate Fixes Needed

### 1. Regularized Flat Green's Function

The current implementation returns 0 for coincident points, but we need the regularized expression:

For massless Dirac in 2D, the retarded Green's function at coincident points needs regularization:

**Option 1:** Small-distance expansion
$$
G_0(E, \mathbf{r}, \mathbf{r}') \approx -\frac{i}{4} \left[ \gamma \cdot \nabla \left( \frac{i}{2} H_0^{(1)}(k|\mathbf{r}-\mathbf{r}'|) \right) \right]
$$

For $|\mathbf{r}-\mathbf{r}'| \to 0$:
$$
G_0(E, \mathbf{r}, \mathbf{r}) \approx -\frac{1}{4\pi} \frac{\gamma \cdot \hat{r}}{r} \quad \text{(divergent)}
$$

But for LDOS: $\rho(E, \mathbf{r}) = -\frac{1}{\pi} \text{Im Tr}[G(E, \mathbf{r}, \mathbf{r})\gamma^0]$

At $E=0$, $G_0(0, \mathbf{r}, \mathbf{r})$ is real, so $\rho_0(0, \mathbf{r}) = 0$.

**Implementation fix:**
```python
def flat_greens_function_regularized(E, r1, r2, theta1=0, theta2=0):
    """Regularized version for coincident and near-coincident points."""
    k = E / (hbar * vF)
    dr = np.sqrt(r1**2 + r2**2 - 2*r1*r2*np.cos(theta1 - theta2))
    
    if dr < 1e-12:  # Coincident points
        # At E=0, G0 is real, so Im[G0] = 0 for LDOS
        if abs(E) < 1e-12:
            return np.zeros((2, 2), dtype=complex)
        else:
            # Small regularization parameter
            dr = 1e-12
    
    # Rest of calculation as before
    H0 = special.hankel1(0, k*dr)
    phi = np.arctan2(r1*np.sin(theta1) - r2*np.sin(theta2),
                     r1*np.cos(theta1) - r2*np.cos(theta2))
    
    prefactor = -0.25j * H0
    G0 = prefactor * (np.cos(phi) * gamma1 + np.sin(phi) * gamma2)
    
    return G0
```

### 2. Simplified D1 Operator

Current D1 operator may have issues. Let's derive simpler form:

From paper discussion: "all the corrections come from the determinant of the metric and the curved gamma matrices"

Thus at first order:
$$
\mathcal{D}_1 \approx i(\gamma^\mu - \gamma_0^\mu)\partial_\mu
$$

For our metric:
$$
\gamma^r - \gamma_0^r = \left(\frac{1}{\sqrt{1+f}} - 1\right) \gamma^1 \approx -\frac{1}{2}f \gamma^1
$$

So:
$$
\mathcal{D}_1 \approx -\frac{i}{2} f(r) \gamma^1 \partial_r
$$

Much simpler than previous expression!

### 3. Alternative Approach: Direct LDOS Formula

The paper gives a formula connecting LDOS to effective potential:

From discussion: $\delta\rho(E_F, \mathbf{r}) = -\frac{1}{4\pi v_F^2} \nabla^2 V(\mathbf{r})$

Where $V(\mathbf{r})$ is effective potential from curvature.

For Gaussian bump, paper states:
$$
V(\mathbf{r}) = \frac{v_F^2 h^2}{2\sigma^4} \left(1 - \frac{r^2}{2\sigma^2}\right) e^{-r^2/\sigma^2}
$$

Then:
$$
\delta\rho(E_F, \mathbf{r}) = -\frac{1}{4\pi v_F^2} \nabla^2 V(\mathbf{r})
$$

This might be easier to compute directly!

### 4. Implementation Plan

**Step 1:** Fix Green's function regularization
**Step 2:** Simplify D1 operator
**Step 3:** Test with direct LDOS formula as benchmark
**Step 4:** Compare Green's function result with direct formula

### 5. Test Script

Create test to verify:
1. Flat LDOS at $E=0$ should be 0
2. First-order correction should match expected form
3. Sign change at $r = b/\sqrt{2}$
4. Total integrated correction should be 0 (charge conservation)

### 6. Debugging Strategy

1. **Test flat case:** Verify $G_0$ properties
2. **Test small deformation:** Compare with analytical expansion
3. **Check matrix traces:** Verify $\text{Tr}[G\gamma^0]$ gives real result
4. **Monitor numerical stability:** Check for NaNs and infinities

Let's implement these fixes and continue!