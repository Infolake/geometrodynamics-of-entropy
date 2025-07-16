# Stochastic Gravitational Wave Background Derivation
## Bounce Signature Detection with LISA/Taiji

[← Back to Main Guide](../goe_derivations_guide.md)

---

## Overview

The Geometrodynamics of Entropy (GoE) framework predicts a distinctive stochastic gravitational wave background (SGWB) arising from the cosmological bounce. This signal provides a unique observational signature that can be detected by space-based interferometers like LISA and Taiji.

## Key Result

```latex
\boxed{f_{\text{peak}} \simeq 10^{-3}\,\text{Hz}, \quad h^{2}\Omega_{\text{GW}} \propto \bigl(\tfrac{R_2}{R_3}\bigr)^{4}}
```

## Theoretical Framework

### Bounce-Generated Gravitational Waves

During the cosmological bounce, metric perturbations are amplified by the rapid change in the equation of state from w ≈ -1 to w ≈ +1/3. The tensor perturbations follow:

```latex
\ddot{h}_{ij} + 3H\dot{h}_{ij} - \frac{\nabla^2}{a^2}h_{ij} = 16\pi G \Pi_{ij}^{\text{TT}}
```

where Π_ij^TT is the transverse-traceless part of the anisotropic stress tensor.

### Spectral Density

The gravitational wave spectral density today is:

```latex
\Omega_{\text{GW}}(f) h^2 = \frac{2\pi^2}{3H_0^2} f^3 \mathcal{P}_h(f)
```

where P_h(f) is the primordial tensor power spectrum.

## Derivation Summary

The bounce mechanism produces:
1. **Peak frequency**: Set by bounce time scale f_peak ~ 1/t_bounce
2. **Amplitude scaling**: Depends on temporal fiber radius ratio
3. **Spectral shape**: Distinctive blue spectrum at high frequencies

**Detection Prospects**: LISA optimal sensitivity range overlaps with predicted peak frequency.

[**→ Full Derivation Details**](../notebooks/sgwb_spectrum.ipynb)

---

[← Previous: JWST Tension](jwst_tension_resolution.md) | [← Back to Main Guide](../goe_derivations_guide.md) | [Next: Perihelion →](perihelion_correction.md)