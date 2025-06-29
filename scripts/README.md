# 💻 CTMCK Scripts

Scripts para análise, simulação e visualização da teoria **Cosmogênese Temporal Multidimensional Camargo-Kletetschka**.

## 📁 Estrutura

### 📊 `analysis/`
Scripts de análise teórica e cálculos
- **`ctmck_analysis.py`** - Análise principal da teoria CTMCK

### 📈 `plotting/`  
Scripts de visualização e gráficos
- **`ctmck_plots.py`** - Geração de plots e visualizações

### 🔬 `simulations/`
Simulações numéricas
- **`ctmck_simulations.py`** - Simulações numéricas completas

## 🚀 Como Usar

### Análise Principal
```bash
cd scripts/analysis
python ctmck_analysis.py
```

### Gerar Visualizações
```bash
cd scripts/plotting
python ctmck_plots.py
```

### Executar Simulações
```bash
cd scripts/simulations
python ctmck_simulations.py
```

## 📋 Dependências

```bash
pip install numpy matplotlib scipy seaborn pandas
```

## 🎯 Recursos dos Scripts

### `ctmck_analysis.py`
- ✅ Cálculo do parâmetro de Schwarzschild global
- ✅ Métrica 3-temporal
- ✅ Predições de massas de neutrinos (Σmν = 0.29 eV)
- ✅ Frequência de ondas torsionais LISA
- ✅ Ressonâncias Kaluza-Klein TeV
- ✅ Análise de formação galáctica JWST
- ✅ Bias de rotação de Shamir

### `ctmck_plots.py`
- 📊 Visualização da variedade 3-temporal
- 📊 Dinâmica do bounce Einstein-Cartan  
- 📊 Predições para galáxias JWST
- 📊 5 assinaturas observacionais
- 📊 Gráficos de alta qualidade (300 DPI)

### `ctmck_simulations.py`
- 🔬 Simulação do universo bounce
- 🔬 Formação galáctica com sementes herdadas
- 🔬 Oscilações de neutrinos CTMCK
- 🔬 Ondas torsionais banda LISA
- 🔬 Ressonâncias KK em colisores TeV
- 🔬 Salvamento automático de resultados

## 📈 Outputs Gerados

### Figuras (`figures/`)
- `ctmck_theory_overview.png`
- `bounce_dynamics.png`
- `jwst_predictions.png`
- `observable_signatures.png`

### Dados (`data/simulations/`)
- `ctmck_simulation_results.npz`

## 🎯 Predições Testáveis

1. **JWST**: Galáxias ultra-massivas em z > 10
2. **Shamir**: Bias de rotação galáctica preferencial
3. **KATRIN II**: Σmν = 0.29 eV
4. **LISA**: Ondas torsionais f ≈ 10⁻² Hz
5. **Colisores**: Ressonâncias KK 2.3, 4.1 TeV

## 🔧 Personalização

Edite os parâmetros nos scripts para:
- Ajustar constantes físicas
- Modificar intervalos de simulação
- Personalizar visualizações
- Adicionar novas análises

---

*Autor: Guilherme de Camargo*  
*Data: 26/01/2025* 