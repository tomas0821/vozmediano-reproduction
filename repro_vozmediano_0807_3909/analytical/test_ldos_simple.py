#!/usr/bin/env python3
"""
Simplified test of LDOS calculation.
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical constants
hbar = 1.0545718e-34  # J·s
vF = 1.0e6  # m/s, Fermi velocity

# Parameters for Gaussian bump
A = 1.0e-9  # 1 nm height
b = 5.0e-9  # 5 nm width
epsilon = (A/b)**2  # Small parameter ~0.04

def f(r):
    """Metric function f(r) = [z'(r)]^2."""
    return 4 * epsilon * (r**2 / b**2) * np.exp(-2 * r**2 / b**2)

def f_prime(r):
    """Derivative of f(r)."""
    term1 = 8 * epsilon * (r / b**2) * np.exp(-2 * r**2 / b**2)
    term2 = -16 * epsilon * (r**3 / b**4) * np.exp(-2 * r**2 / b**2)
    return term1 + term2

def effective_magnetic_field(r):
    """Effective magnetic field from Eq. 15."""
    return f_prime(r) / (4 * r * (1 + f(r))**1.5)

def expected_ldos_correction(r):
    """
    Expected form from paper (qualitative).
    
    δρ ∝ 1/r² (1 - r²/(2σ²)) exp(-r²/(2σ²))
    with σ = b/√2
    """
    sigma = b / np.sqrt(2)
    
    # Handle scalar or array input
    r = np.asarray(r)
    result = np.zeros_like(r)
    
    # Avoid division by zero
    mask = r > 0
    if np.any(mask):
        r_masked = r[mask]
        # Normalize to have maximum ~1
        prefactor = 1.0
        result[mask] = prefactor * (1/r_masked**2) * (1 - r_masked**2/(2*sigma**2)) * np.exp(-r_masked**2/(2*sigma**2))
    
    return result

# Radial points
r_vals = np.linspace(0.1*b, 3*b, 100)

# Compute functions
f_vals = f(r_vals)
f_prime_vals = f_prime(r_vals)
Bz_vals = effective_magnetic_field(r_vals)
expected_ldos = expected_ldos_correction(r_vals)

# Normalize for plotting
Bz_norm = Bz_vals / np.max(np.abs(Bz_vals))
expected_norm = expected_ldos / np.max(np.abs(expected_ldos))

# Plotting
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Metric functions
ax = axes[0, 0]
ax.plot(r_vals/b, f_vals, 'b-', linewidth=2, label='f(r)')
ax.plot(r_vals/b, f_prime_vals, 'r--', linewidth=2, label="f'(r)")
ax.set_xlabel('r/b')
ax.set_ylabel('Metric functions')
ax.set_title('Metric Function and Derivative')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 2: Effective magnetic field
ax = axes[0, 1]
ax.plot(r_vals/b, Bz_vals, 'm-', linewidth=2)
ax.set_xlabel('r/b')
ax.set_ylabel('B_z (T)')
ax.set_title('Effective Magnetic Field (Eq. 15)')
ax.grid(True, alpha=0.3)

# Plot 3: Expected LDOS correction
ax = axes[1, 0]
ax.plot(r_vals/b, expected_ldos, 'g-', linewidth=2)
ax.set_xlabel('r/b')
ax.set_ylabel('δρ (arb. units)')
ax.set_title('Expected LDOS Correction (from paper)')
ax.grid(True, alpha=0.3)

# Plot 4: Comparison
ax = axes[1, 1]
ax.plot(r_vals/b, Bz_norm, 'm-', linewidth=2, label='B_z (normalized)')
ax.plot(r_vals/b, expected_norm, 'g--', linewidth=2, label='Expected δρ (normalized)')
ax.set_xlabel('r/b')
ax.set_ylabel('Normalized amplitude')
ax.set_title('Comparison: B_z vs Expected δρ')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('analytical/plots/simple_analysis.png', dpi=150)
print("Plot saved to analytical/plots/simple_analysis.png")

# Print key features
print("\n=== Key Features ===")
print(f"Zero crossing of B_z at r = b/√2 = {b/np.sqrt(2)*1e9:.2f} nm")

# Find where B_z changes sign
sign_changes = np.where(np.diff(np.sign(Bz_vals)))[0]
if len(sign_changes) > 0:
    r_zero = r_vals[sign_changes[0]] / b
    print(f"Numerical zero crossing at r/b ≈ {r_zero:.3f}")

# Check expected LDOS form
print(f"\nExpected LDOS form:")
print("  δρ ∝ 1/r² (1 - r²/(2σ²)) exp(-r²/(2σ²))")
print(f"  with σ = b/√2 = {b/np.sqrt(2)*1e9:.2f} nm")

# Compute total flux (should be zero)
# ∫ B_z dA = ∫_0^∞ B_z(r) 2πr dr ≈ 0
r_integral = np.linspace(0.01*b, 10*b, 1000)
Bz_integral = effective_magnetic_field(r_integral)
# Simple trapezoidal integration
dr = r_integral[1] - r_integral[0]
integrand = Bz_integral * 2*np.pi*r_integral
flux = np.sum((integrand[:-1] + integrand[1:]) / 2 * dr)
print(f"\nTotal magnetic flux: {flux:.2e} (should be ~0)")

print("\nAnalysis complete.")