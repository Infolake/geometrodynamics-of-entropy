# GoE Semi-Dirac Dispersion Visualization
# Notebook 1: Basic dispersion surface

import numpy as np
import matplotlib.pyplot as plt

# Constants and parameters
hbar = 1.055e-34  # J·s
e = 1.602e-19     # elementary charge
vF = 5e5          # m/s, Fermi velocity  
m_star = 0.3 * 9.109e-31  # kg, effective mass

def semi_dirac_dispersion(kx, ky, vF, m_star):
    """Semi-Dirac energy dispersion"""
    linear_term = (vF * hbar * kx)**2
    quadratic_term = (hbar**2 * ky**2 / (2 * m_star))**2
    return np.sqrt(linear_term + quadratic_term)

# Create k-space grid
kx = np.linspace(-1e10, 1e10, 100)
ky = np.linspace(-1e10, 1e10, 100)
KX, KY = np.meshgrid(kx, ky)

# Calculate energy surface
E = semi_dirac_dispersion(KX, KY, vF, m_star)

# Create contour plot
plt.figure(figsize=(8, 6))
contour = plt.contour(KX/1e9, KY/1e9, E/e, levels=20, cmap='plasma')
plt.clabel(contour, inline=True, fontsize=8)
plt.xlabel(r'$k_x$ (×10⁹ m⁻¹)')
plt.ylabel(r'$k_y$ (×10⁹ m⁻¹)')
plt.title('GoE Semi-Dirac Dispersion')
plt.colorbar(label='Energy (eV)')
plt.axis('equal')
plt.tight_layout()

# Save high-resolution figure
plt.savefig('goe_dispersion.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Figure saved as goe_dispersion.png")
print(f"Energy at (1e9, 0): {semi_dirac_dispersion(1e9, 0, vF, m_star)/e:.4f} eV")
print(f"Energy at (0, 1e9): {semi_dirac_dispersion(0, 1e9, vF, m_star)/e:.4f} eV")
