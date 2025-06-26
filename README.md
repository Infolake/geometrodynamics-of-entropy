# CTMCK — Three-Temporal Bounce Universe
> Minimal working repository accompanying the Letter  
> *“Observable Signatures of a Three-Temporal Bounce-Universe Inside a Black Hole”*

## Overview
This project contains the LaTeX source, figures, and notebooks that reproduce the
results of the CTMCK framework—an extension of Kletetschka’s three-temporal
manifold applied to cosmology and particle masses.

| Folder | Purpose |
|--------|---------|
| `papers/` | `CTMCK_Letter_v0.1b.tex` (REVTeX 4.2) |
| `figures/` | HR diagram, 2-D & 3-D temporal-habitability plots |
| `src/` | *bounce_sim.ipynb*, *jwst_spin_stats.ipynb* |
| `docs/` | compiled PDFs, white-paper |
| `data/` | JWST spin sample, stellar CSV |

## How to reproduce
1. `conda env create -f environment.yml`
2. `jupyter notebook src/bounce_sim.ipynb`  
3. `latexmk papers/CTMCK_Letter_v0.1b.tex`

## License
*Text & figures*: **CC-BY-4.0**  
*Code*: **MIT**

## Citation
If you build upon this work, please cite:

> G. de Camargo, *Observable Signatures of a Three-Temporal Bounce-Universe…*  
> Preprint, 2025. DOI: 10.5281/zenodo.⟨TBD⟩

**ORCID**   0009-0004-8913-9419
