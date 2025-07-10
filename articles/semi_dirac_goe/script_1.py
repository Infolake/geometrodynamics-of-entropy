# Notebook 2 — Theory vs. Simulated ARPES Data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Parameters must match Notebook 1
v_F, m_eff, hbar = 1.1, 0.9, 1.0

# Simulate ARPES-like experimental data
np.random.seed(42)  # For reproducibility
n_exp = 250
kx_exp = np.random.uniform(-2, 2, n_exp)
ky_exp = np.random.uniform(-2, 2, n_exp)
E_exp = (
    np.sqrt((v_F * kx_exp)**2 + (hbar**2 * ky_exp**2)/(2 * m_eff)**2)
    + 0.05 * np.random.randn(n_exp)
)
df = pd.DataFrame({'kx': kx_exp, 'ky': ky_exp, 'E_exp': E_exp})

# Grid for theoretical contours (re-use KX, KY, E from Notebook 1)
kx = np.linspace(-2, 2, 300)
ky = np.linspace(-2, 2, 300)
KX, KY = np.meshgrid(kx, ky)
E = np.sqrt((v_F * KX)**2 + (hbar**2 * KY**2)/(2 * m_eff)**2)

plt.figure(figsize=(7, 5))
sc = plt.scatter(df['kx'], df['ky'], c=df['E_exp'], cmap='plasma',
                 s=22, label='Simulated ARPES', alpha=0.8)
plt.contour(KX, KY, E, levels=10, colors='black',
            linewidths=0.8, alpha=0.6)
plt.colorbar(sc, label='Energy')
plt.xlabel(r'$k_x$')
plt.ylabel(r'$k_y$')
plt.title("Experimental (ARPES) vs GoE Theory")
plt.legend()
plt.tight_layout()
plt.savefig("goe_arpes_compare.png", dpi=300)
plt.show()

print("Figura 2 - Comparação ARPES vs GoE Theory gerada com sucesso!")
print(f"Dados simulados: {len(df)} pontos experimentais")