#!/usr/bin/env python3
"""
Create atomic positions for a graphene sheet with a Gaussian bump.
"""

import numpy as np

def graphene_lattice(a=2.46, nx=10, ny=10):
    """
    Generate positions for a flat graphene sheet.
    
    Parameters:
    -----------
    a : float
        Lattice constant of graphene (Å)
    nx, ny : int
        Number of unit cells in x and y directions
    
    Returns:
    --------
    positions : list of tuples
        List of (x, y, z) positions for carbon atoms
    """
    positions = []
    
    # Basis vectors
    a1 = np.array([a, 0.0])
    a2 = np.array([a/2, a*np.sqrt(3)/2])
    
    # Two atoms per unit cell
    basis = [np.array([0.0, 0.0]), np.array([a/2, a*np.sqrt(3)/6])]
    
    for i in range(nx):
        for j in range(ny):
            # Unit cell origin
            origin = i*a1 + j*a2
            
            for b in basis:
                pos = origin + b
                positions.append((pos[0], pos[1], 0.0))
    
    return positions

def apply_gaussian_bump(positions, h=10.0, sigma=50.0, center=None):
    """
    Apply Gaussian displacement to atomic positions.
    
    Parameters:
    -----------
    positions : list of tuples
        Original (x, y, z) positions
    h : float
        Maximum height of bump (Å)
    sigma : float
        Width parameter of Gaussian (Å)
    center : tuple or None
        (x, y) center of bump. If None, use center of sheet.
    
    Returns:
    --------
    new_positions : list of tuples
        Displaced positions with Gaussian bump
    """
    if center is None:
        # Find center of sheet
        xs = [p[0] for p in positions]
        ys = [p[1] for p in positions]
        center = (np.mean(xs), np.mean(ys))
    
    cx, cy = center
    new_positions = []
    
    for x, y, z in positions:
        # Distance from center
        r = np.sqrt((x - cx)**2 + (y - cy)**2)
        
        # Gaussian displacement
        dz = h * np.exp(-r**2 / (2 * sigma**2))
        
        new_positions.append((x, y, dz))
    
    return new_positions

def write_xyz(filename, positions, comment="Graphene with Gaussian bump"):
    """
    Write positions to XYZ format.
    
    Parameters:
    -----------
    filename : str
        Output filename
    positions : list of tuples
        Atomic positions
    comment : str
        Comment line for XYZ file
    """
    with open(filename, 'w') as f:
        f.write(f"{len(positions)}\n")
        f.write(f"{comment}\n")
        for x, y, z in positions:
            f.write(f"C {x:.6f} {y:.6f} {z:.6f}\n")

def main():
    """Main function to generate example structure."""
    # Parameters (in Angstroms)
    a = 2.46  # Graphene lattice constant
    nx, ny = 20, 20  # Supercell size
    h = 5.0  # Bump height (Å)
    sigma = 25.0  # Bump width (Å)
    
    print(f"Generating graphene sheet: {nx}x{ny} unit cells")
    print(f"Bump parameters: h = {h} Å, σ = {sigma} Å")
    
    # Generate flat graphene
    flat_positions = graphene_lattice(a=a, nx=nx, ny=ny)
    print(f"Total atoms: {len(flat_positions)}")
    
    # Apply Gaussian bump
    bumped_positions = apply_gaussian_bump(flat_positions, h=h, sigma=sigma)
    
    # Write to files
    write_xyz("flat_graphene.xyz", flat_positions, "Flat graphene sheet")
    write_xyz("graphene_gaussian_bump.xyz", bumped_positions, 
              f"Graphene with Gaussian bump (h={h} Å, σ={sigma} Å)")
    
    print("Files written:")
    print("  - flat_graphene.xyz")
    print("  - graphene_gaussian_bump.xyz")
    
    # Calculate some statistics
    z_values = [p[2] for p in bumped_positions]
    print(f"\nBump statistics:")
    print(f"  Max displacement: {max(z_values):.3f} Å")
    print(f"  Min displacement: {min(z_values):.3f} Å")
    print(f"  Avg displacement: {np.mean(z_values):.3f} Å")

if __name__ == "__main__":
    main()