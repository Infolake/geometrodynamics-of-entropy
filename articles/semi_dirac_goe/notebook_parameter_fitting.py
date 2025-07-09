# GoE Parameter Fitting Analysis
# Notebook 3: Fitting GoE parameters to experimental data

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

# Constants
hbar = 1.055e-34  # J·s
e = 1.602e-19     # elementary charge

def semi_dirac_dispersion_fit(kx_ky, vF, m_star):
    """
    Semi-Dirac dispersion for fitting
    Input: kx_ky is a tuple (kx, ky)
    """
    kx, ky = kx_ky
    linear_term = (vF * hbar * kx)**2
    quadratic_term = (hbar**2 * ky**2 / (2 * m_star))**2
    return np.sqrt(linear_term + quadratic_term)

# Generate synthetic experimental data (same as notebook 2)
np.random.seed(42)
n_points = 300

# True parameters
vF_true = 5e5  # m/s
m_star_true = 0.3 * 9.109e-31  # kg

# Generate data
kx_exp = np.random.uniform(-8e9, 8e9, n_points)
ky_exp = np.random.uniform(-8e9, 8e9, n_points)
E_true = semi_dirac_dispersion_fit((kx_exp, ky_exp), vF_true, m_star_true)
E_exp = E_true * (1 + 0.05 * np.random.randn(n_points))  # 5% noise

# Perform fitting
initial_guess = [4e5, 0.4 * 9.109e-31]  # Slightly off initial guess

try:
    popt, pcov = curve_fit(
        semi_dirac_dispersion_fit,
        (kx_exp, ky_exp),
        E_exp,
        p0=initial_guess,
        maxfev=5000
    )
    
    vF_fit, m_star_fit = popt
    
    # Calculate fitted energies
    E_fit = semi_dirac_dispersion_fit((kx_exp, ky_exp), vF_fit, m_star_fit)
    
    # Calculate fit quality
    r2 = r2_score(E_exp, E_fit)
    
    # Create fitting plot
    plt.figure(figsize=(10, 6))
    
    # Subplot 1: Experimental vs Fitted
    plt.subplot(1, 2, 1)
    plt.scatter(E_exp/e, E_fit/e, alpha=0.6, s=20)
    
    # Perfect fit line
    E_range = np.array([np.min(E_exp), np.max(E_exp)])
    plt.plot(E_range/e, E_range/e, 'r--', linewidth=2, label='Perfect fit')
    
    plt.xlabel('Experimental Energy (eV)')
    plt.ylabel('GoE Fitted Energy (eV)')
    plt.title(f'Parameter Fitting (R² = {r2:.4f})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Subplot 2: Residuals
    plt.subplot(1, 2, 2)
    residuals = (E_fit - E_exp) / E_exp * 100  # percentage residuals
    plt.scatter(E_exp/e, residuals, alpha=0.6, s=20)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel('Experimental Energy (eV)')
    plt.ylabel('Residuals (%)')
    plt.title('Fit Residuals')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('goe_fit_parameters.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print results
    print("✅ Figure saved as goe_fit_parameters.png")
    print(f"\n🎯 Fitting Results:")
    print(f"True vF:     {vF_true:.2e} m/s")
    print(f"Fitted vF:   {vF_fit:.2e} m/s")
    print(f"vF error:    {abs(vF_fit - vF_true)/vF_true*100:.2f}%")
    print(f"\nTrue m*:     {m_star_true:.2e} kg = {m_star_true/(9.109e-31):.2f} me")
    print(f"Fitted m*:   {m_star_fit:.2e} kg = {m_star_fit/(9.109e-31):.2f} me")
    print(f"m* error:    {abs(m_star_fit - m_star_true)/m_star_true*100:.2f}%")
    print(f"\n📊 Fit Quality:")
    print(f"R² score:    {r2:.6f}")
    print(f"RMSE:        {np.sqrt(np.mean((E_fit - E_exp)**2))/e:.6f} eV")
    print(f"Mean |residual|: {np.mean(np.abs(residuals)):.2f}%")
    
    # GoE parameter uncertainties (from covariance matrix)
    param_errors = np.sqrt(np.diag(pcov))
    vF_error, m_star_error = param_errors
    
    print(f"\n🔬 Parameter Uncertainties:")
    print(f"σ(vF) = {vF_error:.2e} m/s ({vF_error/vF_fit*100:.2f}%)")
    print(f"σ(m*) = {m_star_error:.2e} kg ({m_star_error/m_star_fit*100:.2f}%)")

except Exception as e:
    print(f"❌ Fitting failed: {e}")
    print("Using default parameters for visualization")
    
    # Create basic plot with original data
    plt.figure(figsize=(6, 5))
    plt.scatter(E_exp/e, E_true/e, alpha=0.6)
    plt.plot([np.min(E_exp/e), np.max(E_exp/e)], 
             [np.min(E_exp/e), np.max(E_exp/e)], 'r--')
    plt.xlabel('Experimental Energy (eV)')
    plt.ylabel('Theoretical Energy (eV)')
    plt.title('GoE Theory vs Experiment')
    plt.grid(True, alpha=0.3)
    plt.savefig('goe_fit_parameters.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✅ Basic comparison figure saved as goe_fit_parameters.png")
