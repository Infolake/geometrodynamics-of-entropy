# Notebook 3 — GoE Parameter Fitting
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

# df, hbar já definidos no Notebook 2
def fit_func(X, v_F, m_eff):
    kx, ky = X
    return np.sqrt((v_F * kx)**2 + (hbar**2 * ky**2)/(2 * m_eff)**2)

popt, pcov = curve_fit(
    fit_func, (df['kx'].values, df['ky'].values),
    df['E_exp'].values, p0=[1.0, 1.0]
)
v_F_fit, m_eff_fit = popt

E_fit = fit_func((df['kx'].values, df['ky'].values), *popt)

plt.figure(figsize=(6, 5))
plt.scatter(df['E_exp'], E_fit, alpha=0.7, label='Fit')
plt.plot(
    [min(df['E_exp']), max(df['E_exp'])],
    [min(df['E_exp']), max(df['E_exp'])],
    'r--', label='Ideal'
)
plt.xlabel("Experimental Energy")
plt.ylabel("GoE Fitted Energy")
plt.title("GoE Parameter Fit to ARPES Data")
plt.legend()
plt.tight_layout()
plt.savefig("goe_fit_parameters.png", dpi=300)
plt.show()

print("Figura 3 - GoE Parameter Fitting gerada com sucesso!")
print(f"Parâmetros ajustados:")
print(f"  v_F  = {v_F_fit:.3f}")
print(f"  m_eff = {m_eff_fit:.3f}")
print(f"Parâmetros originais:")
print(f"  v_F  = {v_F:.3f}")
print(f"  m_eff = {m_eff:.3f}")

# Calcular erro quadrático médio
mse = np.mean((df['E_exp'] - E_fit)**2)
print(f"Erro quadrático médio: {mse:.4f}")

# Calcular coeficiente de correlação
corr_coef = np.corrcoef(df['E_exp'], E_fit)[0, 1]
print(f"Coeficiente de correlação: {corr_coef:.4f}")