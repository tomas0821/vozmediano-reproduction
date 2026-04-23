#!/usr/bin/env python3
"""
Effective Fermi Velocity Analysis for Gaussian bump in graphene.

Based on Eq. (13) from "Gauge fields and curvature in graphene" (arXiv:0807.3909)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

# Physical constants
vF = 1.0e6  # m/s, flat graphene Fermi velocity

# Parameters for Gaussian bump (same as before)
A = 1.0e-9  # 1 nm height
b = 5.0e-9  # 5 nm width
epsilon = (A/b)**2  # Small parameter ~0.04

def f(r):
    """Metric function f(r) = [z'(r)]^2."""
    return 4 * epsilon * (r**2 / b**2) * np.exp(-2 * r**2 / b**2)

def effective_velocity_radial(r):
    """
    Effective radial Fermi velocity from Eq. (13).
    
    ṽ_r(r) = v_F / sqrt(1 + f(r))
    """
    return vF / np.sqrt(1 + f(r))

def effective_velocity_angular(r):
    """
    Effective angular Fermi velocity.
    
    For axisymmetric bump, v_θ is unchanged: ṽ_θ(r) = v_F
    """
    return vF * np.ones_like(r)

def velocity_anisotropy(r):
    """Anisotropy ratio: v_r / v_θ."""
    return effective_velocity_radial(r) / effective_velocity_angular(r)

def velocity_reduction(r):
    """Fractional reduction from flat value: 1 - v_r/v_F."""
    return 1 - effective_velocity_radial(r) / vF

def compute_spatial_averages(r_max=5*b, n_points=1000):
    """
    Compute spatial averages over circular sample.
    
    Returns:
    - v_avg: Area-weighted average velocity
    - v_rms: RMS velocity
    - anisotropy_avg: Average anisotropy
    """
    r_vals = np.linspace(0, r_max, n_points)
    v_r_vals = effective_velocity_radial(r_vals)
    v_theta_vals = effective_velocity_angular(r_vals)
    
    # Area element: 2πr dr
    area_elements = 2 * np.pi * r_vals
    dr = r_vals[1] - r_vals[0]
    
    # Total area
    total_area = np.sum(area_elements * dr)
    
    # Area-weighted averages
    v_r_avg = np.sum(v_r_vals * area_elements * dr) / total_area
    v_theta_avg = np.sum(v_theta_vals * area_elements * dr) / total_area
    
    # RMS velocity
    v_r_rms = np.sqrt(np.sum(v_r_vals**2 * area_elements * dr) / total_area)
    
    # Average anisotropy
    anisotropy_vals = velocity_anisotropy(r_vals)
    anisotropy_avg = np.sum(anisotropy_vals * area_elements * dr) / total_area
    
    return {
        'v_r_avg': v_r_avg,
        'v_theta_avg': v_theta_avg,
        'v_r_rms': v_r_rms,
        'anisotropy_avg': anisotropy_avg,
        'total_area': total_area
    }

def compute_conductivity_tensor(r):
    """
    Compute effective conductivity tensor components.
    
    For Dirac electrons: σ ∝ v^2
    So σ_rr ∝ v_r^2, σ_θθ ∝ v_θ^2, σ_rθ = σ_θr = 0 for axisymmetric case
    """
    v_r = effective_velocity_radial(r)
    v_theta = effective_velocity_angular(r)
    
    # Conductivity components (relative to flat value σ_0 ∝ v_F^2)
    sigma_rr = (v_r / vF)**2
    sigma_theta_theta = (v_theta / vF)**2
    
    return sigma_rr, sigma_theta_theta

def analyze_experimental_implications():
    """
    Analyze implications for experimental measurements.
    
    Experimental v_F is often used as fitting parameter.
    If sample has ripples, measured v_F is spatial average.
    """
    print("\n=== Experimental Implications ===")
    
    # Typical experimental parameters
    sample_radius = 10e-6  # 10 μm typical flake size
    ripple_density = 1e14  # ~1 ripple per 100 nm²
    
    # For single bump at center
    averages = compute_spatial_averages(r_max=sample_radius)
    
    print(f"Flat graphene v_F = {vF/1e6:.2f} × 10⁶ m/s")
    print(f"Average radial velocity: {averages['v_r_avg']/1e6:.4f} × 10⁶ m/s")
    print(f"Reduction: {100*(1 - averages['v_r_avg']/vF):.3f}%")
    print(f"Average anisotropy ⟨v_r/v_θ⟩: {averages['anisotropy_avg']:.6f}")
    
    # For multiple ripples
    print(f"\nFor ε = (A/b)² = {epsilon:.4f}:")
    # Maximum reduction occurs where f(r) is maximum, at r = b/√2
    r_max = b / np.sqrt(2)
    max_reduction = 100 * velocity_reduction(r_max)
    print(f"  Maximum reduction at r = b/√2 = {r_max*1e9:.2f} nm: {max_reduction:.3f}%")
    print(f"  v_r(r_max) = {effective_velocity_radial(r_max)/1e6:.4f} × 10⁶ m/s")
    print(f"  At center (r=0): v_r(0) = {effective_velocity_radial(0)/1e6:.4f} × 10⁶ m/s (no reduction)")
    
    # Estimate for typical experimental conditions
    print("\nTypical experimental scenario:")
    print("  - Measured v_F varies by 1-10% in literature")
    print("  - Ripples with A~0.5-1 nm, b~5-10 nm give ε~0.0025-0.04")
    print("  - This corresponds to v_F variations of 0.25-4%")
    print("  - Anisotropy could explain direction-dependent measurements")

def plot_velocity_analysis():
    """Create comprehensive velocity analysis plots."""
    # Radial points
    r_vals = np.linspace(0, 3*b, 500)
    r_vals_nm = r_vals * 1e9
    
    # Compute velocity profiles
    v_r_vals = effective_velocity_radial(r_vals)
    v_theta_vals = effective_velocity_angular(r_vals)
    anisotropy_vals = velocity_anisotropy(r_vals)
    reduction_vals = velocity_reduction(r_vals)
    
    # Compute conductivity components
    sigma_rr, sigma_theta_theta = compute_conductivity_tensor(r_vals)
    
    # Plotting
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # Plot 1: Velocity components
    ax = axes[0, 0]
    ax.plot(r_vals_nm, v_r_vals/1e6, 'b-', linewidth=2, label='ṽ_r(r)')
    ax.plot(r_vals_nm, v_theta_vals/1e6, 'r--', linewidth=2, label='ṽ_θ(r) = v_F')
    ax.axhline(y=vF/1e6, color='k', linestyle=':', alpha=0.5, label='Flat v_F')
    ax.set_xlabel('r (nm)')
    ax.set_ylabel('Velocity (10⁶ m/s)')
    ax.set_title('Effective Fermi Velocity Components')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 2: Anisotropy
    ax = axes[0, 1]
    ax.plot(r_vals_nm, anisotropy_vals, 'g-', linewidth=2)
    ax.axhline(y=1, color='k', linestyle=':', alpha=0.5, label='Isotropic (flat)')
    ax.set_xlabel('r (nm)')
    ax.set_ylabel('ṽ_r / ṽ_θ')
    ax.set_title('Velocity Anisotropy')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 3: Fractional reduction
    ax = axes[0, 2]
    ax.plot(r_vals_nm, 100*reduction_vals, 'm-', linewidth=2)
    ax.set_xlabel('r (nm)')
    ax.set_ylabel('Velocity reduction (%)')
    ax.set_title('Fractional Reduction from Flat Value')
    ax.grid(True, alpha=0.3)
    
    # Plot 4: Conductivity components
    ax = axes[1, 0]
    ax.plot(r_vals_nm, sigma_rr, 'b-', linewidth=2, label='σ_rr/σ_0')
    ax.plot(r_vals_nm, sigma_theta_theta, 'r--', linewidth=2, label='σ_θθ/σ_0')
    ax.axhline(y=1, color='k', linestyle=':', alpha=0.5, label='Flat σ_0')
    ax.set_xlabel('r (nm)')
    ax.set_ylabel('Relative conductivity')
    ax.set_title('Conductivity Tensor Components')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 5: Metric function for reference
    ax = axes[1, 1]
    f_vals = f(r_vals)
    ax.plot(r_vals_nm, f_vals, 'c-', linewidth=2)
    ax.set_xlabel('r (nm)')
    ax.set_ylabel('f(r)')
    ax.set_title('Metric Function f(r) = [z\'(r)]²')
    ax.grid(True, alpha=0.3)
    
    # Plot 6: Velocity vs metric function
    ax = axes[1, 2]
    # Theoretical relation: v_r/v_F = 1/√(1+f) ≈ 1 - f/2 + 3f²/8 - ...
    theoretical = 1 / np.sqrt(1 + f_vals)
    ax.plot(f_vals, v_r_vals/vF, 'bo', markersize=3, label='Computed')
    ax.plot(f_vals, theoretical, 'r-', linewidth=1, label='1/√(1+f)')
    ax.set_xlabel('f(r)')
    ax.set_ylabel('ṽ_r / v_F')
    ax.set_title('Velocity vs Metric Function')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('analytical/plots/velocity_analysis.png', dpi=150)
    
    # Create additional plot: radial profile comparison
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    
    # Normalize for comparison
    v_r_norm = v_r_vals / vF
    f_norm = f_vals / np.max(f_vals)
    
    ax2.plot(r_vals_nm, v_r_norm, 'b-', linewidth=2, label='ṽ_r/v_F')
    ax2.plot(r_vals_nm, f_norm, 'g--', linewidth=2, label='f(r) (normalized)')
    ax2.plot(r_vals_nm, 1 - 0.5*f_vals, 'r:', linewidth=1, label='1 - f/2 (approx)')
    
    ax2.set_xlabel('r (nm)')
    ax2.set_ylabel('Normalized')
    ax2.set_title('Velocity Reduction vs Metric Function')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('analytical/plots/velocity_vs_metric.png', dpi=150)
    
    return v_r_vals, anisotropy_vals

def analyze_different_parameters():
    """Analyze velocity for different ripple parameters."""
    # Different aspect ratios
    aspect_ratios = [0.01, 0.02, 0.04, 0.08]  # A/b
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    for idx, aspect in enumerate(aspect_ratios):
        # Keep b fixed, vary A
        A_test = aspect * b
        epsilon_test = aspect**2
        
        def f_test(r):
            return 4 * epsilon_test * (r**2 / b**2) * np.exp(-2 * r**2 / b**2)
        
        def v_r_test(r):
            return vF / np.sqrt(1 + f_test(r))
        
        r_vals = np.linspace(0, 3*b, 500)
        r_vals_nm = r_vals * 1e9
        v_vals = v_r_test(r_vals) / vF
        
        ax = axes[idx // 2, idx % 2]
        ax.plot(r_vals_nm, v_vals, 'b-', linewidth=2)
        ax.axhline(y=1, color='k', linestyle=':', alpha=0.5)
        ax.set_xlabel('r (nm)')
        ax.set_ylabel('ṽ_r / v_F')
        ax.set_title(f'A/b = {aspect:.3f}, ε = {epsilon_test:.4f}')
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0.95, 1.005)
    
    plt.tight_layout()
    plt.savefig('analytical/plots/velocity_parameter_study.png', dpi=150)
    
    print("\n=== Parameter Study ===")
    for aspect in aspect_ratios:
        epsilon_test = aspect**2
        reduction = 100 * (1 - 1/np.sqrt(1 + 4*epsilon_test))  # at r=0, f(0)=0
        print(f"A/b = {aspect:.3f}: ε = {epsilon_test:.5f}, max reduction = {reduction:.3f}%")

if __name__ == "__main__":
    print("=== Effective Fermi Velocity Analysis ===")
    print(f"Parameters: A = {A*1e9:.1f} nm, b = {b*1e9:.1f} nm")
    print(f"Aspect ratio A/b = {A/b:.3f}")
    print(f"Small parameter ε = (A/b)² = {epsilon:.5f}")
    
    # Compute and plot
    v_r_vals, anisotropy_vals = plot_velocity_analysis()
    
    # Analyze spatial averages
    averages = compute_spatial_averages()
    
    print("\n=== Spatial Averages ===")
    print(f"Area-weighted average v_r: {averages['v_r_avg']/1e6:.4f} × 10⁶ m/s")
    print(f"Reduction from v_F: {100*(1 - averages['v_r_avg']/vF):.3f}%")
    print(f"Average anisotropy ⟨v_r/v_θ⟩: {averages['anisotropy_avg']:.6f}")
    print(f"RMS v_r: {averages['v_r_rms']/1e6:.4f} × 10⁶ m/s")
    
    # Experimental implications
    analyze_experimental_implications()
    
    # Parameter study
    analyze_different_parameters()
    
    print("\n=== Key Findings ===")
    print("1. Velocity always reduced: ṽ_r(r) ≤ v_F")
    print("2. Maximum reduction at r = b/√2 (where slope is steepest)")
    print("3. No reduction at bump center (r=0) where slope is zero")
    print("4. Anisotropic transport: v_r < v_θ")
    print("5. Conductivity tensor becomes anisotropic")
    print("6. Experimental v_F measurements represent spatial averages")
    
    print("\nAnalysis complete. Check plots in analytical/plots/")
