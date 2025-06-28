#!/usr/bin/env python3
"""
CTMCK Temporal Habitability Map Plotting
Author: Guilherme de Camargo
Date: 2025-01-26
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os

# --- Plot Generation Functions ---

def generate_3d_habitability_map():
    """Generate and save 3D Temporal Habitability Map."""
    # Create t1, t2, t3 axes
    t1 = np.linspace(0, 1, 30)
    t2 = np.linspace(0, 1, 30)
    t3 = np.linspace(0, 1, 30)
    t1_grid, t2_grid, t3_grid = np.meshgrid(t1, t2, t3)

    # Function representing emergent complexity
    def complexity(t1, t2, t3):
        return np.exp(-((t1 - 0.4)**2 + (t2 - 0.5)**2 + (t3 - 0.6)**2) * 30)

    # Calculate complexity at each point
    complexity_vals = complexity(t1_grid, t2_grid, t3_grid)

    # Select points with complexity above threshold
    threshold = 0.7
    x = t1_grid[complexity_vals > threshold]
    y = t2_grid[complexity_vals > threshold]
    z = t3_grid[complexity_vals > threshold]
    colors = complexity_vals[complexity_vals > threshold]

    # Create 3D plot
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(x, y, z, c=colors, cmap='plasma', s=25, alpha=0.8)
    
    ax.set_xlabel('t₁ (Local Quantum Time)', fontsize=12)
    ax.set_ylabel('t₂ (Systemic Relational Time)', fontsize=12)
    ax.set_zlabel('t₃ (Cosmological Time)', fontsize=12)
    ax.set_title('Three-Dimensional Temporal Habitability Map', fontsize=16, pad=20)
    
    cbar = fig.colorbar(scatter, ax=ax, label='Emergent Complexity Level', pad=0.1)
    cbar.ax.tick_params(labelsize=10)
    
    # Ensure output directory exists
    output_dir = '../../figures/diagrams'
    os.makedirs(output_dir, exist_ok=True)
    
    # Save figure
    output_path = os.path.join(output_dir, 'habitability_map_3d.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    
    print(f"3D figure saved at: {output_path}")
    plt.show()

def generate_2d_habitability_map():
    """Generate and save 2D Temporal Habitability Map."""
    t1 = np.linspace(0, 1, 100)
    t2 = np.linspace(0, 1, 100)
    t1_grid, t2_grid = np.meshgrid(t1, t2)

    # 2D complexity/habitability function
    def habitability(t1, t2):
        return np.sin(t1 * np.pi) * np.exp(-((t2 - 0.5)**2) * 10)

    hab_vals = habitability(t1_grid, t2_grid)

    # Create 2D plot
    fig, ax = plt.subplots(figsize=(12, 9))
    contour = ax.contourf(t1_grid, t2_grid, hab_vals, levels=50, cmap='viridis', alpha=0.8)
    fig.colorbar(contour, ax=ax, label='Habitability Index')
    
    ax.set_xlabel('t₁ (Local Quantum Time)', fontsize=12)
    ax.set_ylabel('t₂ (Systemic Relational Time)', fontsize=12)
    ax.set_title('Temporal Habitability Map (t₁-t₂ Plane)', fontsize=16)
    
    # Stellar points
    stars = {
        'O-B': (0.8, 0.8),
        'G (Sun)': (0.5, 0.5),
        'M (Red Dwarf)': (0.2, 0.3)
    }
    
    for name, (t1_pos, t2_pos) in stars.items():
        ax.plot(t1_pos, t2_pos, 'ro', markersize=10, label=name)
        ax.text(t1_pos + 0.02, t2_pos, name, color='white', fontsize=12, weight='bold')

    ax.legend(title='Stellar Types')
    ax.grid(True, linestyle='--', alpha=0.2)
    
    # Ensure output directory exists
    output_dir = '../../figures/diagrams'
    os.makedirs(output_dir, exist_ok=True)
    
    # Save figure
    output_path = os.path.join(output_dir, 'habitability_map_2d.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    
    print(f"2D figure saved at: {output_path}")
    plt.show()

if __name__ == '__main__':
    print("Generating Temporal Habitability Maps...")
    generate_3d_habitability_map()
    generate_2d_habitability_map()
    print("Generation completed.") 