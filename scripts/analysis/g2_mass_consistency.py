#!/usr/bin/env python3
"""
g2_mass_consistency.py
Validation of internal consistency between g-2 anomaly and fermion mass hierarchy
Part of the Geometrodynamics of Entropy (GoE) framework
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from scipy.optimize import minimize

# Physical constants
c = 2.99792458e8  # m/s
hbar = 1.054571817e-34  # J⋅s
e = 1.602176634e-19  # C
me = 9.1093837015e-31  # kg
alpha_em = 7.2973525693e-3  # fine structure constant

# Load GoE parameters
def load_goe_parameters():
    """Load consolidated GoE parameters"""
    try:
        with open('../../data/goe_consolidated_dataset.json', 'r') as f:
            data = json.load(f)
        return data['parametros_fisicos']['metrica_camargo']
    except:
        # Fallback values
        return {
            'alpha': 1.21e4,
            'beta': 4.00e4,
            'R1': 1e-18,
            'R2': 1.1e-16,
            'R3': 2e-16
        }

def calculate_g2_anomaly(R2, alpha):
    """
    Calculate muon g-2 anomaly from GoE framework
    
    Parameters:
    - R2: Θ fiber radius (m)
    - alpha: metric parameter
    
    Returns:
    - delta_a_mu: theoretical g-2 anomaly
    """
    # Energy scale associated with Θ fiber
    Lambda_tau = hbar * c / R2
    
    # Geometric coupling coefficient
    kappa_tau = alpha_em / (4 * np.pi) * (R2 / (1e-16))**(-1)
    
    # Muon mass
    m_mu = 105.6583745 * 1e6 * e / c**2  # kg
    
    # One-loop correction
    delta_a_mu = (kappa_tau / np.pi) * (m_mu**2 * c**4 / Lambda_tau**2) * np.log(Lambda_tau**2 / (m_mu**2 * c**4))
    
    return delta_a_mu

def calculate_fermion_masses(R2, alpha, beta):
    """
    Calculate fermion masses from Cumulative Axiom
    
    Parameters:
    - R2, R3: fiber radii
    - alpha, beta: metric parameters
    
    Returns:
    - masses: dictionary of calculated masses
    """
    # Fundamental energy quantum from Θ fiber
    E_theta = hbar * c / R2
    
    # Fundamental energy quantum from Ξ fiber  
    E_xi = hbar * c / (beta**(1/4) * R2)
    
    # Cumulative mass calculation
    masses = {}
    
    # Leptons
    E_base = E_theta * alpha_em  # electromagnetic coupling
    masses['electron'] = E_base / c**2
    masses['muon'] = (E_base + E_xi) / c**2
    masses['tau'] = (E_base + E_xi + E_xi * beta**(1/8)) / c**2
    
    return masses

def consistency_check():
    """
    Check internal consistency between g-2 and mass hierarchy
    """
    params = load_goe_parameters()
    
    # Experimental values
    delta_a_mu_exp = 2.49e-9  # experimental anomaly
    delta_a_mu_err = 0.48e-9  # error
    
    m_mu_exp = 105.6583745  # MeV
    m_e_exp = 0.5109989461  # MeV
    
    print("🔬 GoE Internal Consistency Check: g-2 vs Mass Hierarchy")
    print("="*60)
    
    # Calculate theoretical g-2 anomaly
    delta_a_mu_theo = calculate_g2_anomaly(params['R2'], params['alpha'])
    
    print(f"Experimental g-2 anomaly: {delta_a_mu_exp:.2e} ± {delta_a_mu_err:.2e}")
    print(f"Theoretical g-2 anomaly: {delta_a_mu_theo:.2e}")
    print(f"Difference: {abs(delta_a_mu_theo - delta_a_mu_exp):.2e}")
    print(f"Significance: {abs(delta_a_mu_theo - delta_a_mu_exp)/delta_a_mu_err:.1f}σ")
    
    # Calculate fermion masses
    masses = calculate_fermion_masses(params['R2'], params['alpha'], params['beta'])
    
    print(f"\nFermion Mass Predictions:")
    print(f"Electron: {masses['electron']*c**2/e/1e6:.3f} MeV (exp: {m_e_exp:.3f} MeV)")
    print(f"Muon: {masses['muon']*c**2/e/1e6:.1f} MeV (exp: {m_mu_exp:.1f} MeV)")
    print(f"Tau: {masses['tau']*c**2/e/1e6:.0f} MeV (exp: ~1777 MeV)")
    
    # Consistency metric
    g2_consistency = abs(delta_a_mu_theo - delta_a_mu_exp) < 2 * delta_a_mu_err
    mass_consistency = abs(masses['muon']*c**2/e/1e6 - m_mu_exp) < 0.1 * m_mu_exp
    
    print(f"\n✅ Consistency Assessment:")
    print(f"g-2 anomaly: {'✓' if g2_consistency else '✗'}")
    print(f"Mass hierarchy: {'✓' if mass_consistency else '✗'}")
    print(f"Overall: {'✓ CONSISTENT' if g2_consistency and mass_consistency else '⚠ NEEDS REFINEMENT'}")
    
    return g2_consistency and mass_consistency

def plot_consistency_analysis():
    """
    Create visualization of consistency analysis
    """
    params = load_goe_parameters()
    
    # Range of R2 values to test
    R2_values = np.linspace(0.8e-16, 1.4e-16, 100)
    
    # Calculate g-2 anomaly for each R2
    g2_anomalies = [calculate_g2_anomaly(R2, params['alpha']) for R2 in R2_values]
    
    # Calculate corresponding muon masses
    muon_masses = []
    for R2 in R2_values:
        masses = calculate_fermion_masses(R2, params['alpha'], params['beta'])
        muon_masses.append(masses['muon'] * c**2 / e / 1e6)  # Convert to MeV
    
    # Create plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # g-2 anomaly plot
    ax1.plot(R2_values*1e16, np.array(g2_anomalies)*1e9, 'b-', linewidth=2)
    ax1.axhline(y=2.49, color='r', linestyle='--', label='Experimental value')
    ax1.fill_between(R2_values*1e16, 2.49-0.48, 2.49+0.48, alpha=0.3, color='r', label='±1σ error')
    ax1.axvline(x=params['R2']*1e16, color='g', linestyle=':', label='GoE prediction')
    ax1.set_xlabel('R₂ (×10⁻¹⁶ m)')
    ax1.set_ylabel('δa_μ (×10⁻⁹)')
    ax1.set_title('g-2 Anomaly vs Θ Fiber Radius')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Muon mass plot
    ax2.plot(R2_values*1e16, muon_masses, 'b-', linewidth=2)
    ax2.axhline(y=105.658, color='r', linestyle='--', label='Experimental value')
    ax2.fill_between(R2_values*1e16, 105.658-0.002, 105.658+0.002, alpha=0.3, color='r', label='±1σ error')
    ax2.axvline(x=params['R2']*1e16, color='g', linestyle=':', label='GoE prediction')
    ax2.set_xlabel('R₂ (×10⁻¹⁶ m)')
    ax2.set_ylabel('m_μ (MeV)')
    ax2.set_title('Muon Mass vs Θ Fiber Radius')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../../figures/g2_mass_consistency.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("📊 Consistency analysis plot saved to figures/g2_mass_consistency.png")

if __name__ == "__main__":
    print("🎯 Running GoE Internal Consistency Analysis")
    print("="*60)
    
    # Run consistency check
    is_consistent = consistency_check()
    
    # Create visualization
    plot_consistency_analysis()
    
    print(f"\n🎉 Analysis complete! Overall consistency: {'✓' if is_consistent else '✗'}")
