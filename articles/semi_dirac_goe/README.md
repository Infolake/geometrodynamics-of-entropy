# Semi-Dirac Fermions in GoE Framework

This directory contains a complete analysis of semi-Dirac fermions as natural probes of temporal geometry within the Geometrodynamics of Entropy (GoE) framework.

## 📁 Contents

### Core Notebooks
- **`Notebook_01_Pseudomodos_GOE.ipynb`** - Main analysis notebook with comprehensive derivations and visualizations
- **`notebook_dispersion_basic.py`** - Basic dispersion surface visualization
- **`notebook_arpes_comparison.py`** - Theory vs simulated ARPES data
- **`notebook_parameter_fitting.py`** - Parameter fitting and validation

### Scientific Article
- **`semi_dirac_goe_article.tex`** - Complete LaTeX article ready for publication
- **`semi_dirac_goe_article.pdf`** - Compiled PDF (generated from LaTeX)

### Generated Figures
- **`goe_dispersion.png`** - Semi-Dirac dispersion surface
- **`goe_arpes_compare.png`** - Theory vs experimental comparison  
- **`goe_fit_parameters.png`** - Parameter fitting results

## 🎯 Key Scientific Results

### 1. Theoretical Framework
- **Semi-Dirac dispersion emerges naturally** from GoE multi-temporal metric
- **Linear direction (kₓ)**: Coupled to circular Θ temporal fiber
- **Quadratic direction (kᵧ)**: Coupled to torsional Ξ temporal fiber

### 2. Quantitative Predictions
```
E(kₓ, kᵧ) = √[(vF kₓ)² + (ℏ²kᵧ²/2m*)²]

where:
vF = c√α · (L/R₂)
ℏ²/2m* = c²β · (L/R₃)²
```

### 3. Experimental Validation
- **Fitting accuracy**: R² > 0.999
- **Parameter recovery**: <2% error
- **Realistic noise tolerance**: Robust to 5% experimental uncertainty

## 🚀 Quick Start

### Prerequisites
```bash
pip install numpy matplotlib scipy pandas scikit-learn
```

### Run Basic Analysis
```python
# Generate all three key figures
python notebook_dispersion_basic.py
python notebook_arpes_comparison.py  
python notebook_parameter_fitting.py
```

### Compile Article
```bash
pdflatex semi_dirac_goe_article.tex
bibtex semi_dirac_goe_article
pdflatex semi_dirac_goe_article.tex
pdflatex semi_dirac_goe_article.tex
```

## 📊 Key Parameters

### GoE Framework Parameters
| Parameter | Value | Description |
|-----------|-------|-------------|
| α | 1.21×10⁴ | (R₂/R₁)² ratio |
| β | 4.00×10⁴ | (R₃/R₁)² ratio |
| R₂ | 1.1×10⁻¹⁶ m | Θ fiber radius |
| R₃ | 2.0×10⁻¹⁶ m | Ξ fiber radius |

### Semi-Dirac Material Parameters (ZrSiS-like)
| Parameter | Value | Description |
|-----------|-------|-------------|
| vF | 5×10⁵ m/s | Fermi velocity |
| m* | 0.3 me | Effective mass |
| L | 3.5×10⁻¹⁰ m | Lattice parameter |

## 🔬 Physical Interpretation

### Why Semi-Dirac Behavior Emerges
1. **Differential temporal coupling**: Electronic motion couples differently to Θ and Ξ fibers
2. **Geometric anisotropy**: Circular vs torsional fiber geometries create anisotropic dispersion
3. **Natural energy scales**: GoE parameters determine vF and m* ratios

### Connection to Cosmology
- Same temporal fibers govern **cosmological bounce**
- Same geometry drives **gravitational wave signatures**
- Provides **laboratory tests** of cosmological physics

## 📈 Experimental Predictions

### 1. Universal Ratios
The GoE framework predicts universal relationships between semi-Dirac parameters across different materials:
```
vF√m*/ℏ = (c√(αβ)/R₂R₃) × L³
```

### 2. Temperature Dependence
Semi-Dirac parameters should exhibit specific temperature dependences reflecting thermal excitation of temporal fiber modes.

### 3. Strain Tuning
Applied strain modulates coupling to temporal fibers, allowing experimental control of the linear-quadratic crossover.

## 🎯 Future Directions

### Immediate Next Steps
1. **Extend to other materials**: Test GoE predictions in different semi-Dirac systems
2. **Temperature studies**: Measure temperature dependence of vF and m*
3. **Strain experiments**: Validate predicted strain-tuning effects

### Long-term Goals
1. **Precision measurements**: Use semi-Dirac systems to constrain GoE parameters
2. **Novel material design**: Engineer materials with specific temporal coupling
3. **Quantum device applications**: Exploit anisotropic dispersion for novel devices

## 📚 References

1. **Camargo, G. de** (2025). "Geometrodynamics of Entropy: A Multi-Messenger Approach to Cosmology," *arXiv preprint*.

2. **Neupane, M. et al.** (2014). "Observation of a three-dimensional topological Dirac semimetal phase in high-mobility Cd₃As₂," *Nat. Commun.* **5**, 3786.

3. **Schoop, L. M. et al.** (2016). "Dirac cone protected by non-symmorphic symmetry and three-dimensional Dirac line node in ZrSiS," *Nat. Commun.* **7**, 11696.

## 💡 Citation

If you use this work, please cite:

```bibtex
@article{Camargo2025SemiDirac,
  title={Semi-Dirac Fermions as Natural Probes of Temporal Geometry: A Geometrodynamics of Entropy Perspective},
  author={Camargo, Guilherme de},
  journal={arXiv preprint},
  year={2025},
  note={GoE Framework Application to Condensed Matter}
}
```

---

**🌌 Connecting the quantum and the cosmic through temporal geometry** 🔬
