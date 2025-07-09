# Notebook 1 — GoE Semi-Dirac Dispersion
import numpy as np
import matplotlib.pyplot as plt

# GoE parameters (adjust as needed)
v_F  = 1.1   # Fermi velocity (linear direction)
m_eff = 0.9  # Effective mass (quadratic direction)
hbar = 1.0

kx = np.linspace(-2, 2, 300)
ky = np.linspace(-2, 2, 300)
KX, KY = np.meshgrid(kx, ky)
E = np.sqrt((v_F * KX)**2 + (hbar**2 * KY**2)/(2 * m_eff)**2)

plt.figure(figsize=(7, 5))
cs = plt.contourf(KX, KY, E, levels=30, cmap='plasma')
plt.xlabel(r'$k_x$')
plt.ylabel(r'$k_y$')
plt.title("GoE Semi-Dirac Dispersion")
cbar = plt.colorbar(cs)
cbar.set_label('Energy (arb. units)')
plt.tight_layout()
plt.savefig("goe_dispersion.png", dpi=300)
plt.show()

print("Figura 1 - GoE Semi-Dirac Dispersion gerada com sucesso!")