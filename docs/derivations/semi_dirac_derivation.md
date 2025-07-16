# Semi-Dirac Quasiparticles Derivation
## Anisotropic Dispersion from Temporal Fiber Symmetry Breaking

[← Back to Main Guide](../goe_derivations_guide.md)

---

## Overview

The Geometrodynamics of Entropy (GoE) framework naturally predicts the existence of semi-Dirac quasiparticles in certain condensed matter systems through the interplay of temporal fiber symmetries and crystal lattice structure.

## Key Result

```latex
E = \sqrt{(\hbar v_F k_x)^2+\bigl(\tfrac{\hbar^2 k_y^2}{2m^*}\bigr)^2}
```

This describes particles that are relativistic in one direction (x) and non-relativistic in the perpendicular direction (y).

## Theoretical Framework

### Anisotropic Effective Hamiltonian

In materials where the crystal symmetry couples to temporal fiber directions, the effective low-energy Hamiltonian becomes:

```latex
H_{\text{eff}} = v_F \hbar k_x \sigma_x + \frac{\hbar^2 k_y^2}{2m^*} \sigma_z
```

where σ_x,z are Pauli matrices and the anisotropy arises from temporal fiber coupling.

### Symmetry Breaking Mechanism

The temporal fiber structure breaks rotational symmetry:
- **Θ fiber**: Couples preferentially to x-direction (creating Dirac-like dispersion)
- **Ξ fiber**: Couples to y-direction (creating parabolic dispersion)

### Material Realization

**TiO₂/VO₂ Heterostructures**: The oxide interface provides the necessary symmetry breaking to realize semi-Dirac physics.

## Experimental Signatures

1. **ARPES measurements**: Distinctive band structure with mixed dispersion
2. **Transport properties**: Anisotropic conductivity σ_x ≠ σ_y
3. **Optical response**: Direction-dependent absorption

## Current Status

✅ **Theoretical prediction**: Semi-Dirac dispersion derived from GoE principles  
🔄 **Experimental search**: Ongoing in oxide heterostructures  
📋 **Material design**: GoE guides synthesis of candidate systems  

[**→ Detailed Analysis**](../articles/semi_dirac_goe/semi_dirac_goe_article.tex)

---

[← Previous: Perihelion](perihelion_correction.md) | [← Back to Main Guide](../goe_derivations_guide.md) | [Next: Inverse Coupling →](inverse_coupling_flow.md)