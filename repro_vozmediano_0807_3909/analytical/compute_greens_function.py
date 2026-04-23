#!/usr/bin/env python3
"""
Compute Green's function and LDOS for Gaussian bump in graphene.

Based on derivation in "Gauge fields and curvature in graphene" (arXiv:0807.3909)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import special
from scipy.integrate import quad, dblquad
import cmath

# Physical constants
hbar = 1.0545718e-34  # J·s
vF = 1.0e6  # m/s, Fermi velocity
e_charge = 1.60217662e-19  # C

# Parameters for Gaussian bump
A = 1.0e-9  # 1 nm height
b = 5.0e-9  # 5 nm width
epsilon = (A/b)**2  # Small parameter ~0.04

# Fermi energy (neutral graphene)
E_F = 0.0  # eV
k_F = E_F / (hbar * vF)  # Fermi wavevector

# Pauli matrices
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)

# Gamma matrices in chiral representation
gamma0 = np.array([[1, 0], [0, -1]], dtype=complex)  # Actually sigma_z for 2D
gamma1 = sigma_x
gamma2 = sigma_y

def f(r):
    """Metric function f(r) = [z'(r)]^2."""
    return 4 * epsilon * (r**2 / b**2) * np.exp(-2 * r**2 / b**2)

def f_prime(r):
    """Derivative of f(r)."""
    term1 = 8 * epsilon * (r / b**2) * np.exp(-2 * r**2 / b**2)
    term2 = -16 * epsilon * (r**3 / b**4) * np.exp(-2 * r**2 / b**2)
    return term1 + term2

def flat_greens_function(E, r1, r2, theta1=0, theta2=0):
    """
    Flat-space retarded Green's function for massless Dirac in 2D.
    
    Parameters:
    -----------
    E : float
        Energy (J)
    r1, r2 : float
        Radial coordinates (m)
    theta1, theta2 : float
        Angular coordinates (rad)
        
    Returns:
    --------
    G0 : 2x2 complex array
        Green's function matrix
    """
    k = E / (hbar * vF)
    
    # Distance between points
    dr = np.sqrt(r1**2 + r2**2 - 2*r1*r2*np.cos(theta1 - theta2))
    
    if dr == 0:
        # Regularized expression for coincident points
        # Using small-distance expansion
        # G0 ~ -i/(4π) [γ·∇ ln(kr) + ...]
        # For LDOS calculation, we need Im[G0] which is finite
        # At E=0, G0 ~ -i/(4πr) γ·r̂
        # We'll return 0 for now and handle separately
        return np.zeros((2, 2), dtype=complex)
    
    # Hankel function of first kind H0^(1)(k*dr)
    H0 = special.hankel1(0, k*dr)
    
    # Phase factor
    phi = np.arctan2(r1*np.sin(theta1) - r2*np.sin(theta2),
                     r1*np.cos(theta1) - r2*np.cos(theta2))
    
    # Green's function matrix
    # G0 = -i/4 * H0(k*dr) * [cos(phi)γ1 + sin(ϕ)γ2]
    prefactor = -0.25j * H0
    G0 = prefactor * (np.cos(phi) * gamma1 + np.sin(phi) * gamma2)
    
    return G0

def D1_operator(r, theta):
    """
    First-order correction to Dirac operator.
    
    Returns matrix representation of D1 acting on spinors.
    """
    # D1 = -iε (2r²/b² ∂_r + r/b²) e^{-2r²/b²} γ¹
    coeff = -1j * epsilon * (2*r**2/b**2 + r/b**2) * np.exp(-2*r**2/b**2)
    return coeff * gamma1

def metric_determinant_factor(r):
    """Factor from metric determinant: (-g)^{-1/2} - 1."""
    return -0.5 * f(r)

def compute_G1_integral(E, r, theta=0, r_max=5*b):
    """
    Compute first-order correction to Green's function via integral.
    
    G1(r,r) = -∫ d²r'' G0(r,r'') D1(r'') G0(r'',r)
             - [(-g)^{-1/2} - 1] G0(r,r)
    """
    # Precompute G0 at observation point (regularized)
    G0_rr = flat_greens_function(E, r, r, theta, theta)
    
    # Second term: metric determinant contribution
    term2 = metric_determinant_factor(r) * G0_rr
    
    # First term: convolution integral
    # Use polar coordinates: r'' from 0 to r_max, theta'' from 0 to 2π
    term1 = np.zeros((2, 2), dtype=complex)
    
    # Numerical integration (simplified for testing)
    # We'll use a coarse grid for initial testing
    n_r = 50
    n_theta = 50
    
    r_vals = np.linspace(0.01*b, r_max, n_r)
    theta_vals = np.linspace(0, 2*np.pi, n_theta, endpoint=False)
    
    dr = r_vals[1] - r_vals[0]
    dtheta = theta_vals[1] - theta_vals[0]
    
    for i, r2 in enumerate(r_vals):
        for j, theta2 in enumerate(theta_vals):
            # Jacobian: r'' dr'' dtheta''
            jacobian = r2 * dr * dtheta
            
            # G0(r, r'')
            G0_1 = flat_greens_function(E, r, r2, theta, theta2)
            
            # D1(r'')
            D1_mat = D1_operator(r2, theta2)
            
            # G0(r'', r)
            G0_2 = flat_greens_function(E, r2, r, theta2, theta)
            
            # Add contribution
            term1 -= jacobian * G0_1 @ D1_mat @ G0_2
    
    G1 = term1 + term2
    return G1

def compute_ldos(E, r, theta=0):
    """
    Compute local density of states.
    
    ρ(E, r) = -1/π Im Tr[G(E, r, r) γ^0]
    """
    # Zeroth order (flat)
    G0 = flat_greens_function(E, r, r, theta, theta)
    rho0 = -1/np.pi * np.imag(np.trace(G0 @ gamma0))
    
    # First order correction
    G1 = compute_G1_integral(E, r, theta)
    rho1 = -1/np.pi * np.imag(np.trace(G1 @ gamma0))
    
    return rho0 + rho1, rho0, rho1

def expected_ldos_correction(r):
    """
    Expected form from paper (qualitative).
    
    δρ ∝ 1/r² (1 - r²/(2σ²)) exp(-r²/(2σ²))
    with σ = b/√2
    """
    sigma = b / np.sqrt(2)
    if r == 0:
        return 0  # Handle singularity
    
    prefactor = epsilon / (np.pi * b**2)  # Guess
    return prefactor * (1/r**2) * (1 - r**2/(2*sigma**2)) * np.exp(-r**2/(2*sigma**2))

def plot_results():
    """Compute and plot LDOS corrections."""
    # Radial points
    r_vals = np.linspace(0.1*b, 3*b, 50)
    
    # Energy (at Fermi level)
    E = E_F * e_charge  # Convert to Joules
    
    # Compute LDOS
    rho_vals = []
    rho0_vals = []
    rho1_vals = []
    expected_vals = []
    
    print("Computing LDOS corrections...")
    for i, r in enumerate(r_vals):
        if i % 10 == 0:
            print(f"  Progress: {i}/{len(r_vals)}")
        
        rho, rho0, rho1 = compute_ldos(E, r)
        rho_vals.append(rho)
        rho0_vals.append(rho0)
        rho1_vals.append(rho1)
        expected_vals.append(expected_ldos_correction(r))
    
    # Convert to arrays
    rho_vals = np.array(rho_vals)
    rho0_vals = np.array(rho0_vals)
    rho1_vals = np.array(rho1_vals)
    expected_vals = np.array(expected_vals)
    
    # Plotting
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot 1: LDOS correction
    ax = axes[0, 0]
    ax.plot(r_vals/b, rho1_vals, 'b-', linewidth=2, label='Computed δρ')
    ax.plot(r_vals/b, expected_vals, 'r--', linewidth=2, label='Expected form')
    ax.set_xlabel('r/b')
    ax.set_ylabel('δρ (arb. units)')
    ax.set_title('LDOS Correction for Gaussian Bump')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 2: Total LDOS
    ax = axes[0, 1]
    ax.plot(r_vals/b, rho_vals, 'g-', linewidth=2, label='Total ρ')
    ax.plot(r_vals/b, rho0_vals, 'k--', linewidth=1, label='Flat ρ₀')
    ax.set_xlabel('r/b')
    ax.set_ylabel('ρ (arb. units)')
    ax.set_title('Total LDOS')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 3: Effective magnetic field (from Eq. 15)
    ax = axes[1, 0]
    Bz_vals = f_prime(r_vals) / (4 * r_vals * (1 + f(r_vals))**1.5)
    ax.plot(r_vals/b, Bz_vals, 'm-', linewidth=2)
    ax.set_xlabel('r/b')
    ax.set_ylabel('B_z (arb. units)')
    ax.set_title('Effective Magnetic Field (Eq. 15)')
    ax.grid(True, alpha=0.3)
    
    # Plot 4: Metric function
    ax = axes[1, 1]
    ax.plot(r_vals/b, f(r_vals), 'c-', linewidth=2, label='f(r)')
    ax.plot(r_vals/b, f_prime(r_vals), 'y--', linewidth=2, label="f'(r)")
    ax.set_xlabel('r/b')
    ax.set_ylabel('Metric functions')
    ax.set_title('Metric Function and Derivative')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('analytical/plots/ldos_plots.png', dpi=150)
    # plt.show()  # Disabled for headless environment
    
    # Print summary
    print("\n=== Summary ===")
    print(f"Parameters: A = {A*1e9:.1f} nm, b = {b*1e9:.1f} nm, ε = {epsilon:.4f}")
    print(f"Maximum LDOS correction: {np.max(np.abs(rho1_vals)):.2e}")
    print(f"Expected zero crossing at r = b/√2 = {b/np.sqrt(2)*1e9:.1f} nm")
    
    # Check if correction changes sign
    sign_changes = np.sum(np.diff(np.sign(rho1_vals)) != 0)
    print(f"Sign changes in δρ: {sign_changes}")
    
    return rho_vals, rho1_vals

def test_greens_function():
    """Test basic properties of Green's function."""
    print("Testing Green's function properties...")
    
    # Test at different distances
    r_test = 1.0e-9  # 1 nm
    E_test = 0.1 * e_charge  # 0.1 eV
    
    # Test 1: G0 at different points
    G0_11 = flat_greens_function(E_test, r_test, r_test, 0, 0)
    G0_12 = flat_greens_function(E_test, r_test, 2*r_test, 0, 0)
    
    print(f"G0(r,r):\n{np.real(G0_11)}")
    print(f"Imaginary part:\n{np.imag(G0_11)}")
    print(f"G0(r,2r):\n{np.real(G0_12)}")
    
    # Test 2: D1 operator
    D1_test = D1_operator(r_test, 0)
    print(f"D1 operator at r={r_test*1e9:.1f} nm:\n{D1_test}")
    
    # Test 3: Metric functions
    print(f"\nMetric function f({r_test*1e9:.1f} nm) = {f(r_test):.4e}")
    print(f"f'({r_test*1e9:.1f} nm) = {f_prime(r_test):.4e}")
    
    return True

if __name__ == "__main__":
    print("=== Green's Function Calculation for Gaussian Bump ===")
    print(f"Parameters: A = {A*1e9} nm, b = {b*1e9} nm")
    print(f"Small parameter ε = (A/b)² = {epsilon:.4f}")
    
    # Run tests
    test_greens_function()
    
    # Compute and plot results
    rho, delta_rho = plot_results()
    
    print("\nAnalysis complete. Results saved to ldos_plots.png")