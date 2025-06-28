# Índice Geral do Projeto CTMCK

**Projeto:** Teoria da Cosmogênese Temporal Multidimensional Camargo-Kletetschka  
**Autor:** Dr. Guilherme de Camargo  
**Data de Criação:** 26 de Janeiro de 2025  
**Status:** Limpo e pronto para submissão acadêmica

---

## 📁 **Estrutura Simplificada**

### **📄 Documento Principal**

#### **Manuscrito Científico**
- `ctmck_article_v0.1b.tex` - Manuscrito principal RevTeX 4.2 (pronto para arXiv)
- `references.bib` - Bibliografia completa em formato BibTeX

#### **Documentação**
- `README.md` - Apresentação do projeto
- `CITATION.cff` - Metadados para citação e Zenodo
- `ZENODO_SETUP_GUIDE.md` - Guia para obtenção de DOI

### **🔬 Scripts de Análise**

#### **Análise Principal**
- `scripts/analysis/ctmck_analysis.py` - Análise fundamental CTMCK
- `scripts/analysis/stellar_temporal_correlation.py` - Correlação estelar-temporal

#### **Visualizações**
- `scripts/plotting/ctmck_plots.py` - Gráficos principais da teoria
- `scripts/plotting/generate_habitability_maps.py` - Mapas de habitabilidade
- `scripts/plotting/habitability_map_plot.py` - Plotagem específica de habitabilidade

#### **Simulações**
- `scripts/simulations/ctmck_simulations.py` - Simulações numéricas completas

### **📊 Figuras Científicas**

#### **Mapas de Habitabilidade Temporal**
- `figures/diagrams/habitability_map_2d.png` - Mapa 2D t₁ vs t₂
- `figures/diagrams/habitability_map_3d.png` - Visualização 3D completa

#### **Análise Estelar**
- `figures/diagrams/stellar_temporal_correlations.png` - Correlação estelar-temporal

### **📈 Dados Processados**
- `data/processed/stellar_temporal_correlations.csv` - Dados da correlação estelar

---

## 🎯 **Como Usar Este Repositório**

### **Para Reproduzir Resultados**
```bash
# 1. Clone o repositório
git clone https://github.com/Infolake/guilherme-ctmck.git

# 2. Execute análises
python scripts/analysis/ctmck_analysis.py
python scripts/analysis/stellar_temporal_correlation.py

# 3. Gere figuras
python scripts/plotting/ctmck_plots.py
python scripts/plotting/generate_habitability_maps.py

# 4. Execute simulações
python scripts/simulations/ctmck_simulations.py
```

### **Para Compilar Manuscrito**
```bash
# Compile LaTeX (requer RevTeX 4.2)
pdflatex ctmck_article_v0.1b.tex
bibtex ctmck_article_v0.1b
pdflatex ctmck_article_v0.1b.tex
pdflatex ctmck_article_v0.1b.tex
```

### **Para Citar Este Trabalho**
Veja `CITATION.cff` para formato acadêmico adequado ou aguarde DOI do Zenodo.

---

## 📋 **Status do Projeto**

- ✅ **Manuscrito**: Pronto para submissão
- ✅ **Código**: Testado e documentado  
- ✅ **Figuras**: Geradas e validadas
- ✅ **Dados**: Processados e disponíveis
- ✅ **Citação**: Configurada para Zenodo
- 🔄 **DOI**: Aguardando Zenodo
- 🔄 **arXiv**: Aguardando DOI

**Total de arquivos essenciais: 12**

---

## 🧬 **Teoria CTMCK - Resumo**

### **Fundamentos**
1. **Tempo Tridimensional**: (t, θ, τ) baseado em Kletetschka
2. **Métrica 6D**: $ds^2 = -c^2dt^2 + d\theta^2 + d\tau^2 + dr^2 + r^2d\Omega^2$
3. **Origem**: Bounce de buraco negro primordial
4. **Unificação**: Quântica + Gravitacional + Cosmológica

### **Previsões Testáveis**
- **Massa de neutrinos**: 0.29 eV
- **Ondas gravitacionais**: LISA ~10⁻² Hz
- **Ressonâncias KK**: 2.3 TeV, 4.1 TeV
- **Anisotropias CMB**: Padrão específico

### **Fenômenos Explicados**
- ✅ Emaranhamento quântico
- ✅ Galáxias JWST precoces
- ✅ Massas de partículas
- ✅ Paradoxos cosmológicos
