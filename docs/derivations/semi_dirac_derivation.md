# Semi-Dirac Quasiparticles from GoE Framework

## Overview

GoE predicts that electron coupling to temporal fibers generates semi-Dirac dispersion relations in certain condensed matter systems.

## 1. Theoretical Foundation

### 1.1 Electron-Fiber Coupling

Electrons couple differently to the two temporal fibers:
- **Θ fiber (circular):** Linear dispersion (Dirac-like)
- **Ξ fiber (torsional):** Quadratic dispersion (Schrödinger-like)

### 1.2 Effective Hamiltonian

The anisotropic coupling yields:
```latex
\boxed{H_{\text{eff}} = \hbar v_F \sigma_x k_x + \frac{\hbar^2 k_y^2}{2m^*} \sigma_z}
```

### 1.3 Dispersion Relation

```latex
\boxed{E = \sqrt{(\hbar v_F k_x)^2+\bigl(\tfrac{\hbar^2 k_y^2}{2m^*}\bigr)^2}}
```

## 2. Connection to TiO₂/VO₂ Heterostructures

### 2.1 Material Realization

**System:** TiO₂/VO₂ interface  
**Mechanism:** Orbital hybridization mimics temporal fiber coupling

### 2.2 Parameter Mapping

```latex
v_F \leftrightarrow \frac{c R_\Theta}{\hbar}, \quad m^* \leftrightarrow \frac{\hbar^2}{2 E_\Xi R_\Xi^2}
```

## 3. Experimental Signatures

### 3.1 Transport Properties

**Anisotropic conductivity:**
```latex
\frac{\sigma_x}{\sigma_y} = \frac{v_F m^*}{\hbar k_F} \propto \frac{R_\Theta}{R_\Xi^2}
```

### 3.2 Quantum Oscillations

Mixed 1/B and 1/√B dependence from hybrid dispersion.

## Code Implementation

```python
import numpy as np

def semi_dirac_dispersion(kx, ky, v_F=1e6, m_star=0.1):
    """
    Calculate semi-Dirac dispersion relation
    
    Parameters:
    -----------
    kx, ky : array
        Momentum components in 1/m
    v_F : float
        Fermi velocity in m/s
    m_star : float
        Effective mass in electron masses
        
    Returns:
    --------
    array : Energy in eV
    """
    hbar = 1.055e-34  # J⋅s
    m_e = 9.109e-31   # kg
    eV = 1.602e-19    # J
    
    # Convert effective mass
    m_eff = m_star * m_e
    
    # Dispersion relation
    E_x = hbar * v_F * np.abs(kx)
    E_y = (hbar**2 * ky**2) / (2 * m_eff)
    
    E_total = np.sqrt(E_x**2 + E_y**2)
    
    return E_total / eV  # Convert to eV

# Example calculation
kx = np.linspace(-1e8, 1e8, 100)  # 1/m
ky = np.linspace(-1e8, 1e8, 100)  # 1/m
KX, KY = np.meshgrid(kx, ky)

E = semi_dirac_dispersion(KX, KY)

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.contourf(KX/1e8, KY/1e8, E, levels=20, cmap='viridis')
plt.colorbar(label='Energy (eV)')
plt.xlabel('kₓ (10⁸ m⁻¹)')
plt.ylabel('kᵧ (10⁸ m⁻¹)')
plt.title('Semi-Dirac Dispersion Relation')
plt.show()
```

## References

1. Peres, N.M.R. et al., Phys. Rev. B 73, 125411 (2006)
2. Banerjee, S. et al., Phys. Rev. Lett. 103, 016402 (2009)
3. Camargo, G. "Geometrodynamics of Entropy" Appendix J (2025)