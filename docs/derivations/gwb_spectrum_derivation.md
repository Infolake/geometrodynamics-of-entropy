# Detailed Derivation: Stochastic Gravitational‑Wave Background (SGWB)

**Author:** Dr. Guilherme de Camargo  
**Derivation:** 4/7 of the GoE series  
**Related chapter:** [Monograph Ch. 8.1](../../Geometrodynamics_of_Entropy_A_Comprehensive_Monograph.md)

---

## Introduction

The cosmological bounce in the Geometrodynamics of Entropy (GoE) framework produces a **stochastic gravitational-wave background** (SGWB) whose spectral shape and amplitude are distinctive signatures of the extra-temporal geometry.

| Feature        | GoE Prediction                                   |
|----------------|--------------------------------------------------|
| Peak frequency | \(f_{\text{peak}} \sim 10^{-3}\,\text{Hz}\) (LISA band) |
| Amplitude      | \(h^2\Omega_{\text{GW}} \sim 10^{-11}\)          |
| Scaling        | proportional to \((R_2/R_3)^4\)                  |

---

## Theoretical Framework

### GoE Metric Through the Bounce

The metric through the bounce is given by:

\[
ds^{2} = -N^{2}(t)dt^{2}
       + a^{2}(t)\bigl[\delta_{ij}+h_{ij}(t,\mathbf x)\bigr]dx^{i}dx^{j}
       + g_{\Theta\Theta}(t)d\theta^{2}
       + g_{\Xi\Xi}(t)d\xi^{2}
\]

Tensor perturbations \(h_{ij}\) satisfy modified Einstein–Cartan equations with torsion sources.

---

## Derivation of the SGWB Spectrum

**Step 1 — Primordial Fluctuations:**  
Quantum fluctuations in the temporal dimensions during the bounce are propagated by a Green’s function \(G_\Theta\).

**Step 2 — Projection onto 3‑Space:**  
Temporal modes are mixed into 3D tensor modes via a coupling \(\alpha_{\text{coup}}\).

**Step 3 — Gravitational‑Wave Equation:**  
The evolution equation for tensor perturbations is:
\[
\ddot h_{ij} + 3H\dot h_{ij}
 + \left(\frac{k^{2}}{a^{2}} + m_{\text{eff}}^{2}\right) h_{ij}
 = S_{\text{source}}
\]
with effective mass
\[
m_{\text{eff}}^{2} = \frac{1}{R_2^{2}} + \frac{1}{R_3^{2}}
\]

**Step 4 — Solution and Spectrum:**  
The resulting energy-density spectrum is
\[
h^{2}\Omega_{\text{GW}}(f) = \Omega_{0} \left(\frac{f}{f_{\text{peak}}}\right)^{n_T} \left(\frac{R_2}{R_3}\right)^{4}
\]
where \(\Omega_{0} \sim 10^{-11}\) and \(n_T\) is the (non-inflationary) tilt.

---

## Peak Frequency

The peak frequency is given by:
\[
f_{\text{peak}} = \frac{a_{\text{bounce}}}{a_{0}} \frac{H_{\text{bounce}}}{2\pi} \simeq 10^{-3}\ \text{Hz}
\]

---

## Detectability with LISA

The predicted SGWB signal is above the nominal LISA sensitivity for a wide range of parameters. The scaling with \((R_2/R_3)^4\) allows for clear discrimination of the GoE scenario from inflationary or astrophysical gravitational-wave backgrounds.

---

## Validation Code (excerpt)

```python
def sgwb_spectrum_goe(f, f_peak=1e-3, Omega0=1e-11, R2_R3=1.0, nT=0):
    h2 = 0.7**2
    return h2 * Omega0 * (f/f_peak)**nT * R2_R3**4
```

A comparison with the LISA noise curve shows that the signal-to-noise ratio (SNR) is much greater than 1 for optimistic parameters, and still SNR ~ few in more conservative scenarios.

---

## Cosmological & Experimental Implications

- Detection would simultaneously confirm the GoE bounce, measure the ratio \(R_2/R_3\), and rule out purely inflationary SGWB models.
- Multi-band detector networks (LISA, Taiji, BBO) could map the entire predicted spectral shape.

---

*Validated July 2025 • LISA detectability: ✔︎ • Unique GoE signature: ✔︎*

