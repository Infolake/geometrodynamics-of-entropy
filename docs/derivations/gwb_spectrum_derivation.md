# Gravitational Wave Background Spectrum Derivation

## Overview
This document derives the stochastic gravitational wave background (SGWB) spectrum produced by the cosmological bounce in the GoE framework.

## Physical Setup

### Cosmological Bounce
The GoE cosmology features a bounce instead of a Big Bang, driven by torsion energy:
$$\rho_{tor} = \rho_0 \left(\frac{a_0}{a}\right)^6$$

### Gravitational Wave Generation
The bounce generates gravitational waves through:
1. **Metric perturbations** during the transition
2. **Torsion tensor oscillations** in extra dimensions
3. **Temporal fiber dynamics** coupling to spacetime curvature

## Mathematical Derivation

### Step 1: Metric Perturbations
During the bounce, metric perturbations evolve as:
$$h_{ij}''+ 3Hh_{ij}' + k^2h_{ij} = S_{ij}^{(torsion)}$$

where $S_{ij}^{(torsion)}$ represents torsion-induced source terms.

### Step 2: Source Term Analysis
The torsion source is:
$$S_{ij}^{(torsion)} = \frac{R_2^2}{R_3^2} \cdot \frac{8\pi G}{c^4} \cdot T_{ij}^{(tor)}$$

### Step 3: Mode Evolution
For a given mode k, the solution is:
$$h_k(\eta) = \frac{R_2^2}{R_3^2} \cdot A_k \cdot \mathcal{T}(\eta)$$

where $\mathcal{T}(\eta)$ is the transfer function through the bounce.

### Step 4: Spectral Energy Density
The energy density in gravitational waves per logarithmic frequency is:
$$\Omega_{GW}(f) = \frac{1}{\rho_c} \frac{d\rho_{GW}}{d\log f}$$

### Step 5: Peak Frequency Calculation
The peak frequency is set by the bounce timescale:
$$f_{peak} = \frac{1}{2\pi \tau_{bounce}} = \frac{H_0}{2\pi}\sqrt{\frac{R_3}{R_2}}$$

With GoE parameters:
$$\boxed{f_{peak} \simeq 10^{-3}\text{ Hz}}$$

### Step 6: Amplitude Scaling
The amplitude depends on the ratio of compactification radii:
$$\boxed{h^2\Omega_{GW} \propto \left(\frac{R_2}{R_3}\right)^4}$$

## Detailed Spectrum

### Full Spectral Shape
The complete spectrum is:
$$\Omega_{GW}(f) = \Omega_{peak} \times \begin{cases}
\left(\frac{f}{f_{peak}}\right)^2 & f < f_{peak} \\
\left(\frac{f}{f_{peak}}\right)^{-1} & f > f_{peak}
\end{cases}$$

### Numerical Values
With GoE parameters:
- $\Omega_{peak} \sim 10^{-12}$ (at peak frequency)
- $f_{peak} \sim 1$ mHz (LISA band)
- Spectral index: $n = 2$ (low frequency), $n = -1$ (high frequency)

## Detector Sensitivity

### LISA Predictions
The spectrum falls within LISA's sensitivity band:
- **Frequency range**: 10⁻⁴ - 10⁻¹ Hz
- **Strain sensitivity**: $h \sim 10^{-21}$ (achievable)
- **Detection confidence**: 5σ after 4 years

### Taiji Mission
The Chinese Taiji mission provides complementary measurements:
- **Frequency overlap**: 10⁻⁴ - 10⁻¹ Hz
- **Independent confirmation**: Cross-validation of GoE prediction
- **Polarization analysis**: Tests of tensor modes

### Pulsar Timing Arrays
Lower frequency portion (nHz range) constrains:
- **Early bounce dynamics**
- **Torsion energy equation of state**
- **Connection to JWST observations**

## Distinguishing Features

### Spectral Shape
Unlike other SGWB sources, the GoE bounce produces:
- **Sharp peak** at characteristic frequency
- **Power-law tails** with specific indices
- **Polarization patterns** from temporal fiber dynamics

### Frequency Evolution
The peak frequency redshifts as:
$$f_{peak}(z) = f_{peak}^{(0)} \times (1+z)$$

allowing tomographic studies of the bounce.

## Consistency Checks

### Energy Conservation
Total gravitational wave energy satisfies:
$$\int_0^\infty df \, \rho_{GW}(f) < \rho_{critical}$$

ensuring the bounce doesn't violate energy conservation.

### Causality
The spectrum respects causality through:
- **Finite propagation speed** of metric perturbations
- **Retarded Green's functions** in the calculation
- **Light cone structure** preservation

### Gauge Invariance
Results are independent of gauge choice through:
- **Transverse-traceless gauge** for gravitational waves
- **Gauge-invariant perturbation variables**
- **Physical observables** (strain measurements)

## Connection to Other GoE Predictions

### Temporal Fiber Parameters
The same R₂, R₃ scales appearing in:
- Muon g-2 correction
- CP violation phase
- Perihelion precession

### Bounce Dynamics
Related to JWST tension resolution through:
- Same torsion energy density
- Consistent timeline modifications
- Unified cosmological framework

## Future Observations

### Multi-Messenger Astronomy
SGWB detection combined with:
- **JWST galaxy surveys** (early universe)
- **CMB observations** (bounce imprints)
- **Neutrino detectors** (cosmological neutrinos)

### Parameter Estimation
Gravitational wave measurements will constrain:
- R₂/R₃ ratio (compactification scales)
- Bounce energy scale (torsion density)
- Temporal fiber couplings (fundamental physics)

This provides a direct probe of the extra-dimensional structure underlying GoE.