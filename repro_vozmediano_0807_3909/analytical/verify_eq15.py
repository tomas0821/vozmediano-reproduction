#!/usr/bin/env python3
"""
Numerical verification of Equation (15) from Vozmediano et al. (2008).
Computes the effective magnetic field for a Gaussian bump in graphene.
"""

import numpy as np
import matplotlib.pyplot as plt

def gaussian_bump(r, A=1.0, b=5.0):
    """
    Gaussian bump profile: z(r) = A * exp(-r^2/b^2)
    
    Parameters:
    -----------
    r : array_like
        Radial coordinate
    A : float
        Maximum height of bump
    b : float
        Width parameter
    
    Returns:
    --------
    z : array_like
        Height at position r
    dz_dr : array_like
        Derivative dz/dr
    """
    z = A * np.exp(-r**2 / b**2)
    dz_dr = -2 * A * r / b**2 * np.exp(-r**2 / b**2)
    return z, dz_dr

def compute_f(r, A=1.0, b=5.0):
    """
    Compute f(r) = (dz/dr)^2 for Gaussian bump.
    
    Parameters:
    -----------
    r : array_like
        Radial coordinate
    A, b : float
        Gaussian parameters
    
    Returns:
    --------
    f : array_like
        f(r) = (dz/dr)^2
    f_prime : array_like
        Derivative f'(r)
    """
    _, dz_dr = gaussian_bump(r, A, b)
    f = dz_dr**2
    
    # Compute derivative analytically
    # f(r) = 4A^2 r^2/b^4 * exp(-2r^2/b^2)
    # f'(r) = 8A^2 r/b^4 * exp(-2r^2/b^2) * (1 - 2r^2/b^2)
    f_prime = 8 * A**2 * r / b**4 * np.exp(-2 * r**2 / b**2) * (1 - 2 * r**2 / b**2)
    
    return f, f_prime

def compute_A_theta(r, f):
    """
    Compute effective gauge field A_theta from Eq. (12).
    
    Parameters:
    -----------
    r : array_like
        Radial coordinate
    f : array_like
        f(r) = (dz/dr)^2
    
    Returns:
    --------
    A_theta : array_like
        Effective gauge field component
    """
    # Avoid division by zero at r=0
    r_safe = np.where(r == 0, 1e-10, r)
    
    # Eq. (12): A_theta = 1/(2r) - 1/(2r) * (1+f)^{-1/2}
    A_theta = 1/(2*r_safe) - 1/(2*r_safe) * (1 + f)**(-0.5)
    
    # Handle r=0 separately using limit
    if np.isscalar(r):
        if r == 0:
            # Use L'Hopital's rule or series expansion
            # For small r, f ~ 0, so A_theta ~ f/(4r) ~ 0
            A_theta = 0.0
    else:
        mask = (r == 0)
        A_theta[mask] = 0.0
    
    return A_theta

def compute_B_z(r, f, f_prime):
    """
    Compute effective magnetic field B_z from Eq. (15).
    
    Parameters:
    -----------
    r : array_like
        Radial coordinate
    f : array_like
        f(r) = (dz/dr)^2
    f_prime : array_like
        Derivative f'(r)
    
    Returns:
    --------
    B_z : array_like
        Effective magnetic field (perpendicular to sheet)
    """
    # Avoid division by zero at r=0
    r_safe = np.where(r == 0, 1e-10, r)
    
    # Eq. (15): B_z = (1/(4r)) * f' / (1+f)^{3/2}
    B_z = (1/(4 * r_safe)) * f_prime / (1 + f)**1.5
    
    # Handle r=0 separately using limit
    if np.isscalar(r):
        if r == 0:
            # For small r: f ~ 0, f' ~ 0
            # Use series expansion: B_z ~ f'/(4r) ~ constant
            # Actually, for Gaussian: f ~ r^2, f' ~ r, so B_z ~ constant
            B_z = f_prime / (4 * 1e-10)  # Use small r approximation
    else:
        mask = (r == 0)
        # For r=0, use the limit from small r expansion
        B_z[mask] = f_prime[mask] / (4 * 1e-10)
    
    return B_z

def compute_B_z_from_A_theta(r, A_theta):
    """
    Compute B_z from A_theta using B_z = (1/r) * d/dr (r * A_theta).
    Alternative method to verify Eq. (15).
    
    Parameters:
    -----------
    r : array_like
        Radial coordinate
    A_theta : array_like
        Effective gauge field
    
    Returns:
    --------
    B_z_alt : array_like
        Effective magnetic field computed from A_theta
    """
    # Compute derivative numerically
    if np.isscalar(r):
        # For scalar, need array for derivative
        return 0.0
    
    # Ensure r is sorted for derivative
    sort_idx = np.argsort(r)
    r_sorted = r[sort_idx]
    A_sorted = A_theta[sort_idx]
    
    # Compute d/dr (r * A_theta)
    rA = r_sorted * A_sorted
    drA_dr = np.gradient(rA, r_sorted)
    
    # B_z = (1/r) * d/dr (r * A_theta)
    # Avoid division by zero at r=0
    r_safe = np.where(r_sorted == 0, 1e-10, r_sorted)
    B_z_alt = drA_dr / r_safe
    
    # Return to original order
    unsort_idx = np.argsort(sort_idx)
    return B_z_alt[unsort_idx]

def main():
    """Main function to compute and plot results."""
    # Parameters (in nanometers)
    A = 1.0  # Height of bump (nm)
    b = 5.0  # Width parameter (nm)
    
    print(f"Gaussian bump parameters:")
    print(f"  Height A = {A} nm")
    print(f"  Width b = {b} nm")
    print(f"  Aspect ratio A/b = {A/b:.3f}")
    print(f"  Small parameter ε = (A/b)^2 = {(A/b)**2:.6f}")
    
    # Radial grid
    r_max = 3 * b  # Go out to 3 times the width
    r = np.linspace(0, r_max, 1000)
    
    # Compute quantities
    z, dz_dr = gaussian_bump(r, A, b)
    f, f_prime = compute_f(r, A, b)
    A_theta = compute_A_theta(r, f)
    B_z_eq15 = compute_B_z(r, f, f_prime)
    B_z_from_A = compute_B_z_from_A_theta(r, A_theta)
    
    # Small deformation approximation
    B_z_approx = (2 * A**2 / b**4) * np.exp(-2 * r**2 / b**2) * (1 - 2 * r**2 / b**2)
    
    # Check zero total flux
    flux = np.trapezoid(r * B_z_eq15, r, axis=0)
    print(f"\nTotal magnetic flux: {flux:.6e} (should be ~0)")
    
    # Create plots
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    
    # Plot 1: Gaussian bump profile
    ax = axes[0, 0]
    ax.plot(r, z, 'b-', linewidth=2)
    ax.set_xlabel('r (nm)')
    ax.set_ylabel('z(r) (nm)')
    ax.set_title('Gaussian Bump Profile')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    
    # Plot 2: Derivative dz/dr
    ax = axes[0, 1]
    ax.plot(r, dz_dr, 'r-', linewidth=2)
    ax.set_xlabel('r (nm)')
    ax.set_ylabel('dz/dr')
    ax.set_title('Slope of Bump')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    
    # Plot 3: f(r) = (dz/dr)^2
    ax = axes[1, 0]
    ax.plot(r, f, 'g-', linewidth=2)
    ax.set_xlabel('r (nm)')
    ax.set_ylabel('f(r) = (dz/dr)$^2$')
    ax.set_title('Metric Function f(r)')
    ax.grid(True, alpha=0.3)
    
    # Plot 4: Effective gauge field A_theta
    ax = axes[1, 1]
    ax.plot(r, A_theta, 'm-', linewidth=2)
    ax.set_xlabel('r (nm)')
    ax.set_ylabel('A$_\\theta$(r)')
    ax.set_title('Effective Gauge Field (Eq. 12)')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    
    # Plot 5: Effective magnetic field B_z
    ax = axes[2, 0]
    ax.plot(r, B_z_eq15, 'b-', linewidth=2, label='Exact (Eq. 15)')
    ax.plot(r, B_z_approx, 'r--', linewidth=1.5, label='Small deformation approx')
    ax.set_xlabel('r (nm)')
    ax.set_ylabel('B$_z$(r)')
    ax.set_title('Effective Magnetic Field')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    ax.legend()
    
    # Plot 6: Comparison of two methods for B_z
    ax = axes[2, 1]
    ax.plot(r, B_z_eq15, 'b-', linewidth=2, label='From Eq. (15)')
    ax.plot(r, B_z_from_A, 'g--', linewidth=1.5, label='From A_θ derivative')
    ax.set_xlabel('r (nm)')
    ax.set_ylabel('B$_z$(r)')
    ax.set_title('Verification: Two Methods for B$_z$')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('gaussian_bump_analysis.png', dpi=150, bbox_inches='tight')
    print(f"\nPlots saved to 'gaussian_bump_analysis.png'")
    
    # Print key features
    print("\nKey features of B_z(r):")
    max_B = np.max(B_z_eq15)
    min_B = np.min(B_z_eq15)
    zero_crossing_idx = np.where(np.diff(np.sign(B_z_eq15)))[0]
    if len(zero_crossing_idx) > 0:
        zero_crossing = r[zero_crossing_idx[0]]
        print(f"  Maximum B_z: {max_B:.6f} at r = {r[np.argmax(B_z_eq15)]:.3f} nm")
        print(f"  Minimum B_z: {min_B:.6f} at r = {r[np.argmin(B_z_eq15)]:.3f} nm")
        print(f"  Zero crossing at r ≈ {zero_crossing:.3f} nm")
        print(f"  Theoretical zero crossing: r = b/√2 = {b/np.sqrt(2):.3f} nm")
    else:
        print(f"  Maximum B_z: {max_B:.6f}")
        print(f"  Minimum B_z: {min_B:.6f}")
    
    # Save data for comparison
    data = np.column_stack((r, z, f, A_theta, B_z_eq15, B_z_approx))
    np.savetxt('gaussian_bump_data.csv', data, 
               delimiter=',', 
               header='r (nm), z (nm), f(r), A_theta(r), B_z_exact, B_z_approx',
               fmt='%.6f')
    print(f"Data saved to 'gaussian_bump_data.csv'")

if __name__ == "__main__":
    main()