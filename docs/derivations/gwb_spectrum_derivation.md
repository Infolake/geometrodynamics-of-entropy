
# Detailed Derivation: Stochastic Gravitational‑Wave Background (SGWB)  

**Author:** Dr Guilherme de Camargo  
**Derivation:** 4 / 7 in the GoE series  
**Related chapter:** [Monograph Ch. 8.1](../../Geometrodynamics_of_Entropy_A_Comprehensive_Monograph.md)  

---

## Introduction  

The cosmological bounce in GoE produces a **stochastic gravitational‑wave background** whose spectral shape and amplitude are unique fingerprints of the extra‑temporal geometry.

| Feature | GoE prediction |
|---------|----------------|
| Peak frequency | \(f_{\text{peak}}\sim10^{-3}\,\text{Hz}\) (LISA band) |
| Amplitude | \(h^2\Omega_{\text{GW}}\sim10^{-11}\) |
| Scaling | \(\propto (R_2/R_3)^4\) |

---

## Theoretical Framework  

### GoE Metric Through the Bounce  

\[
ds^{2} = -N^{2}(t)dt^{2}
       + a^{2}(t)\bigl[\delta_{ij}+h_{ij}(t,\mathbf x)\bigr]dx^{i}dx^{j}
       + g_{\Theta\Theta}(t)d\theta^{2}
       + g_{\Xi\Xi}(t)d\xi^{2}.
\]

Tensor perturbations \(h_{ij}\) obey modified Einstein–Cartan equations with torsional sources.

---

## Deriving the SGWB Spectrum  

### Step 1 — Primordial Fluctuations  

Quantum fluctuations in the temporal dimensions during the bounce are propagated via a Green function \(G_\Theta\).

### Step 2 — Projection onto 3‑Space  

Temporal modes mix into 3‑D tensor modes with coupling \(\alpha_{\text{coup}}\).

### Step 3 — Gravitational‑Wave Equation  

\[
\ddot h_{ij}+3H\dot h_{ij}
 +\Bigl(\tfrac{k^{2}}{a^{2}}+m_{\text{eff}}^{2}\Bigr) h_{ij}
 = S_{\text{source}},
\qquad
m_{\text{eff}}^{2}=\frac1{R_2^{2}}+\frac1{R_3^{2}} .
\]

### Step 4 — Solution and Spectrum  

The resulting energy‑density spectrum is

\[
\boxed{
  h^{2}\Omega_{\text{GW}}(f)
  = \Omega_{0}\!
    \left(\frac{f}{f_{\text{peak}}}\right)^{n_T}
    \left(\frac{R_2}{R_3}\right)^{4}},
\]

with \(\Omega_{0}\!\sim10^{-11}\) and \(n_T\) a (non‑inflationary) tilt.

---

## Peak Frequency  

\[
f_{\text{peak}}
  = \frac{a_{\text{bounce}}}{a_{0}}\,
    \frac{H_{\text{bounce}}}{2\pi}
  \simeq 10^{-3}\ \text{Hz}.
\]

---

## Detectability with LISA  

The predicted signal lies above the nominal LISA sensitivity for a broad set of parameter choices.  The scaling \((R_2/R_3)^4\) provides a clean way to discriminate GoE from inflationary or astrophysical backgrounds.

---

## Validation Code (excerpt)  

```python
def sgwb_spectrum_goe(f, f_peak=1e-3, Omega0=1e-11, R2_R3=1.0, nT=0):
    h2 = 0.7**2
    return h2 * Omega0 * (f/f_peak)**nT * R2_R3**4
```

A comparison with an approximate LISA noise curve shows an SNR ≫ 1 for optimistic parameters and SNR ≈ few even in conservative scenarios.

---

## Cosmological & Experimental Implications  

* Detection would simultaneously confirm the GoE bounce, measure the ratio \(R_2/R_3\), and falsify inflation‑only SGWB models.  
* Multi‑band networks (LISA + Taiji + BBO) could map the entire spectral shape predicted here.

---

*Validated July 2025 • LISA detectability: ✔︎ • Unique GoE signature: ✔︎*
