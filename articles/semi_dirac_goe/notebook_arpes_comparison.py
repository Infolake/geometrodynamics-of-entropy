# GoE Semi-Dirac vs ARPES Comparison
# Notebook 2: Theory vs experimental simulation

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Physical parameters (same as notebook 1)
hbar = 1.055e-34  # J·s
e = 1.602e-19     # elementary charge
vF = 5e5          # m/s
m_star = 0.3 * 9.109e-31  # kg

def semi_dirac_dispersion(kx, ky, vF, m_star):
    """Semi-Dirac energy dispersion"""
    linear_term = (vF * hbar * kx)**2
    quadratic_term = (hbar**2 * ky**2 / (2 * m_star))**2
    return np.sqrt(linear_term + quadratic_term)

# Simulate ARPES-like experimental data
np.random.seed(42)  # For reproducibility
n_points = 300

# Generate random k-points
kx_exp = np.random.uniform(-8e9, 8e9, n_points)
ky_exp = np.random.uniform(-8e9, 8e9, n_points)

# Calculate "experimental" energies with realistic noise
E_theory = semi_dirac_dispersion(kx_exp, ky_exp, vF, m_star)
noise_level = 0.05  # 5% noise
E_exp = E_theory * (1 + noise_level * np.random.randn(n_points))

# Create DataFrame for easier handling
df_arpes = pd.DataFrame({
    'kx': kx_exp,
    'ky': ky_exp, 
    'E_exp': E_exp
})

# Theoretical grid for contours
kx_grid = np.linspace(-8e9, 8e9, 50)
ky_grid = np.linspace(-8e9, 8e9, 50)
KX, KY = np.meshgrid(kx_grid, ky_grid)
E_grid = semi_dirac_dispersion(KX, KY, vF, m_star)

# Create comparison plot
plt.figure(figsize=(10, 8))

# Plot simulated ARPES data
scatter = plt.scatter(df_arpes['kx']/1e9, df_arpes['ky']/1e9, 
                     c=df_arpes['E_exp']/e, cmap='plasma', 
                     s=25, alpha=0.7, label='Simulated ARPES')

# Overlay theoretical contours
contours = plt.contour(KX/1e9, KY/1e9, E_grid/e, 
                      levels=12, colors='black', 
                      linewidths=1.2, alpha=0.8)

plt.colorbar(scatter, label='Energy (eV)')
plt.xlabel(r'$k_x$ (×10⁹ m⁻¹)')
plt.ylabel(r'$k_y$ (×10⁹ m⁻¹)')
plt.title('GoE Theory vs Simulated ARPES Data')
plt.legend(loc='upper right')
plt.axis('equal')
plt.tight_layout()

# Save figure
plt.savefig('goe_arpes_compare.png', dpi=300, bbox_inches='tight')
plt.show()

# Calculate correlation
correlation = np.corrcoef(E_theory, E_exp)[0,1]

print("✅ Figure saved as goe_arpes_compare.png")
print(f"📊 Data Statistics:")
print(f"Number of ARPES points: {n_points}")
print(f"Correlation coefficient: {correlation:.4f}")
print(f"Mean experimental energy: {np.mean(E_exp)/e:.4f} eV")
print(f"Energy range: {np.min(E_exp)/e:.4f} - {np.max(E_exp)/e:.4f} eV")
print(f"Noise level: {noise_level*100:.1f}%")
