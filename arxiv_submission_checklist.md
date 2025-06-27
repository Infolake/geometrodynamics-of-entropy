# arXiv Submission Checklist - CTMCK Theory

## ✅ **Manuscript Corrections Applied**

### **1. Title Format**
- ✅ Line break added: `Observable Signatures of a Three-Temporal\\ Bounce-Universe Inside a Black Hole`
- ✅ Descriptive and concise
- ✅ Under 200 characters

### **2. RevTeX 4-2 Compliance**
- ✅ Correct document class: `\documentclass[reprint,amsmath,amssymb,aps,prd,nofootinbib]{revtex4-2}`
- ✅ Metadata moved after `\begin{document}`
- ✅ Preprint identifier: `\preprint{CTMCK-v0.1}`

### **3. Author Information**
- ✅ Email: `guilherme@medsuite.com.br`
- ✅ Affiliation format: `Independent Researcher, Londrina, PR 86010-260, Brazil\\ORCID: 0009-0004-8913-9419`
- ✅ ORCID included
- ✅ No line breaks in affiliation

### **4. Keywords and Metadata**
- ✅ Keywords added: `multidimensional time, bounce cosmology, Einstein-Cartan, JWST anomalies, neutrino mass`
- ✅ Proper hyperref setup
- ✅ PDF metadata configured

### **5. Units and Constants**
- ✅ `siunitx` package included
- ✅ Proper unit formatting: `\SI{0.29}{\electronvolt}`
- ✅ Constants defined: `\kappa \equiv 8\pi G/c^4`

### **6. Bibliography**
- ✅ DOI format: `doi:10.3847/2041-8213/ac9b22`
- ✅ Recent references (2022-2023)
- ✅ Proper citation format

### **7. Mathematical Formatting**
- ✅ Proper equation numbering
- ✅ Physics package for derivatives
- ✅ Clear mathematical notation

## 📋 **Pre-Submission Checklist**

### **Technical Requirements**
- [ ] **LaTeX compilation successful** (run `./compile_check.sh`)
- [ ] **PDF size ≤ 10 MB**
- [ ] **No "draft" watermark**
- [ ] **All figures included** in submission package
- [ ] **No overfull hbox warnings > 5pt**

### **Content Review**
- [ ] **Abstract ≤ 1920 characters**
- [ ] **References complete and accurate**
- [ ] **Equations properly numbered**
- [ ] **Figures referenced in text**
- [ ] **No undefined references**

### **arXiv Submission Form**
- [ ] **Primary subject**: `physics.gen-ph` (General Physics)
- [ ] **Secondary subjects**: `gr-qc` (General Relativity), `hep-th` (High Energy Physics - Theory)
- [ ] **License**: CC-BY-4.0
- [ ] **Comments**: "10 pages, 0 figures. Presents testable predictions for neutrino masses, gravitational waves, and particle resonances."

## 📤 **Submission Package Contents**

### **Required Files**
```
ctmck_submission.zip
├── ctmck_article_v0.1b.tex    # Main manuscript
├── ctmck_article_v0.1b.bbl    # Bibliography (if using BibTeX)
└── figures/                   # Figure directory (if any)
    └── (no figures in current version)
```

### **Submission Steps**
1. **Create account** at arxiv.org
2. **Start new submission**
3. **Upload files**: Select `ctmck_article_v0.1b.tex`
4. **Set metadata**:
   - Title: "Observable Signatures of a Three-Temporal Bounce-Universe Inside a Black Hole"
   - Authors: "Guilherme de Camargo"
   - Abstract: Copy from LaTeX file
   - Comments: "10 pages. CTMCK theory with testable predictions."
5. **Select subjects**: physics.gen-ph, gr-qc, hep-th
6. **Choose license**: CC-BY-4.0
7. **Review and submit**

## 🎯 **Expected Timeline**

- **Submission**: Immediate (after LaTeX compilation)
- **Processing**: 1-2 business days
- **Publication**: 3-5 business days
- **arXiv ID**: Format `arXiv:YYMM.NNNNN`

## 🔄 **Post-Submission Actions**

1. **Update repository badges** with arXiv ID
2. **Execute `./update_doi.sh`** script
3. **Update CITATION.cff** with arXiv reference
4. **Announce on social media** using templates
5. **Submit to journals** (Physical Review D, etc.)

## 📞 **Contact Information**

- **Author**: Dr. Guilherme de Camargo
- **Email**: guilherme@medsuite.com.br
- **ORCID**: 0009-0004-8913-9419
- **Repository**: https://github.com/Infolake/guilherme-ctmck

## 🚨 **Emergency Contacts**

If submission issues arise:
- **arXiv help**: help@arxiv.org
- **Technical support**: Include error messages and submission ID

---

**Status**: ✅ Ready for submission after LaTeX compilation check 