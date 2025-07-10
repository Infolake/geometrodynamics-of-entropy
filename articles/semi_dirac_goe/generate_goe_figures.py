#!/usr/bin/env python3
"""
Script completo para gerar figuras e artigo LaTeX
Semi-Dirac Fermions as Low-Energy Probes of GoE
Dr. Guilherme de Camargo - 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import os

def main():
    print("=== GERANDO FIGURAS PARA ARTIGO GoE ===\n")

    # Parâmetros GoE
    v_F = 1.1   # Fermi velocity
    m_eff = 0.9 # Effective mass
    hbar = 1.0

    # ===== NOTEBOOK 1: GoE Semi-Dirac Dispersion =====
    print("1. Gerando dispersão semi-Dirac GoE...")

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
    plt.savefig("goe_dispersion.png", dpi=300, bbox_inches='tight')
    plt.close()

    # ===== NOTEBOOK 2: Theory vs Simulated ARPES =====
    print("2. Gerando dados ARPES simulados...")

    np.random.seed(42)  # Reproducibilidade
    n_exp = 250
    kx_exp = np.random.uniform(-2, 2, n_exp)
    ky_exp = np.random.uniform(-2, 2, n_exp)
    E_exp = (
        np.sqrt((v_F * kx_exp)**2 + (hbar**2 * ky_exp**2)/(2 * m_eff)**2)
        + 0.05 * np.random.randn(n_exp)
    )
    df = pd.DataFrame({'kx': kx_exp, 'ky': ky_exp, 'E_exp': E_exp})

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
    plt.savefig("goe_arpes_compare.png", dpi=300, bbox_inches='tight')
    plt.close()

    # ===== NOTEBOOK 3: Parameter Fitting =====
    print("3. Ajustando parâmetros GoE...")

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
    plt.scatter(df['E_exp'], E_fit, alpha=0.7, label='Fit', color='blue')
    plt.plot(
        [min(df['E_exp']), max(df['E_exp'])],
        [min(df['E_exp']), max(df['E_exp'])],
        'r--', label='Ideal', linewidth=2
    )
    plt.xlabel("Experimental Energy")
    plt.ylabel("GoE Fitted Energy")
    plt.title("GoE Parameter Fit to ARPES Data")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("goe_fit_parameters.png", dpi=300, bbox_inches='tight')
    plt.close()

    # ===== RESULTADOS =====
    mse = np.mean((df['E_exp'] - E_fit)**2)
    corr_coef = np.corrcoef(df['E_exp'], E_fit)[0, 1]

    print(f"\n=== RESULTADOS DO AJUSTE ===")
    print(f"Parâmetros originais: v_F = {v_F:.3f}, m_eff = {m_eff:.3f}")
    print(f"Parâmetros ajustados: v_F = {v_F_fit:.3f}, m_eff = {m_eff_fit:.3f}")
    print(f"Erro quadrático médio: {mse:.6f}")
    print(f"Coeficiente de correlação: {corr_coef:.6f}")
    print(f"Precisão do ajuste: {100*(1-abs(v_F_fit-v_F)/v_F):.1f}%")

    print(f"\n=== ARQUIVOS GERADOS ===")
    files = ["goe_dispersion.png", "goe_arpes_compare.png", "goe_fit_parameters.png"]
    for file in files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"✓ {file} ({size/1024:.1f} KB)")

    print(f"\n=== CONCLUÍDO ===")
    print("Todas as figuras foram geradas com sucesso!")
    print("Execute o arquivo .tex com pdflatex para gerar o PDF final.")

    return v_F_fit, m_eff_fit, mse, corr_coef

if __name__ == "__main__":
    main()
