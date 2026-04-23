#!/usr/bin/env python3
"""Debug velocity calculation."""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1.0e-9  # 1 nm
b = 5.0e-9  # 5 nm
epsilon = (A/b)**2

def f(r):
    """Metric function f(r) = [z'(r)]^2."""
    return 4 * epsilon * (r**2 / b**2) * np.exp(-2 * r**2 / b**2)

# Check f(r) properties
r_vals = np.linspace(0, 3*b, 1000)
f_vals = f(r_vals)

print(f"epsilon = {epsilon:.6f}")
print(f"f(0) = {f(0):.6f}")
print(f"max(f) = {np.max(f_vals):.6f} at r = {r_vals[np.argmax(f_vals)]*1e9:.2f} nm")

# Find where f is maximum analytically
# f(r) = 4ε (r²/b²) exp(-2r²/b²)
# df/dr = 0 => 2r/b² - 4r³/b⁴ = 0 => r² = b²/2 => r = b/√2
r_max = b / np.sqrt(2)
f_max = f(r_max)
print(f"\nAnalytical maximum:")
print(f"  r_max = b/√2 = {r_max*1e9:.2f} nm")
print(f"  f_max = 4ε * (1/2) * exp(-1) = {4*epsilon*0.5*np.exp(-1):.6f}")
print(f"  f(r_max) computed = {f_max:.6f}")

# Velocity reduction
vF = 1.0e6
v_r = vF / np.sqrt(1 + f_vals)
reduction = 1 - v_r / vF

print(f"\nVelocity reduction at r_max:")
print(f"  v_r(r_max)/vF = {1/np.sqrt(1 + f_max):.6f}")
print(f"  Reduction = {100*(1 - 1/np.sqrt(1 + f_max)):.4f}%")

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot f(r)
ax1.plot(r_vals*1e9, f_vals, 'b-', linewidth=2)
ax1.axvline(x=r_max*1e9, color='r', linestyle='--', alpha=0.5, label=f'r = b/√2 = {r_max*1e9:.1f} nm')
ax1.set_xlabel('r (nm)')
ax1.set_ylabel('f(r)')
ax1.set_title('Metric function f(r) = [z\'(r)]²')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot velocity reduction
ax2.plot(r_vals*1e9, 100*reduction, 'g-', linewidth=2)
ax2.axvline(x=r_max*1e9, color='r', linestyle='--', alpha=0.5)
ax2.set_xlabel('r (nm)')
ax2.set_ylabel('Velocity reduction (%)')
ax2.set_title('Fractional velocity reduction: 1 - ṽ_r/v_F')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('analytical/plots/debug_velocity.png', dpi=150)
plt.show()

print("\n=== Summary ===")
print(f"For A={A*1e9} nm, b={b*1e9} nm:")
print(f"  Maximum f(r) at r = b/√2 = {r_max*1e9:.2f} nm")
print(f"  f_max = {f_max:.6f}")
print(f"  Maximum velocity reduction = {100*np.max(reduction):.4f}%")
print(f"  This occurs at r = {r_vals[np.argmax(reduction)]*1e9:.2f} nm")