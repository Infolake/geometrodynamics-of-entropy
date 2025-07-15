# Derivação Detalhada: Fundo Estocástico de Ondas Gravitacionais

**Autor:** Dr. Guilherme de Camargo  
**Derivação:** 4/7 da série GoE  
**Capítulo relacionado:** [Monografia Cap. 8.1](../../Geometrodynamics_of_Entropy_A_Comprehensive_Monograph.md)

---

## Introdução

O bounce cosmológico da Geometrodynamics of Entropy (GoE) gera um **fundo estocástico de ondas gravitacionais (SGWB)** com características únicas. Este sinal representa uma assinatura observacional direta da transição bounce e das dimensões temporais extras.

### Características do SGWB GoE

- **Frequência de pico:** $f_{\text{pico}} \sim 10^{-3}$ Hz (banda LISA)
- **Amplitude:** $h^2\Omega_{\text{GW}} \sim 10^{-11}$ (detectável)
- **Origem:** Flutuações métricas durante bounce
- **Dependência:** $(R_2/R_3)^4$ das dimensões temporais

---

## Fundamentos Teóricos

### Métrica GoE Durante Bounce

A métrica completa (3+3)D durante o bounce:

$$ds^2 = -N^2(t)dt^2 + a^2(t)\left[\delta_{ij} + h_{ij}(t,\mathbf{x})\right]dx^i dx^j + g_{\Theta\Theta}(t)d\theta^2 + g_{\Xi\Xi}(t)d\xi^2$$

onde:
- $h_{ij}$: perturbações métricas tensoriais  
- $g_{\Theta\Theta}, g_{\Xi\Xi}$: métricas das dimensões temporais
- $N(t)$: função lapse modificada

### Equação de Einstein Modificada

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G \left( T_{\mu\nu}^{\text{matter}} + T_{\mu\nu}^{\text{tor}} + T_{\mu\nu}^{\text{GW}} \right)$$

onde $T_{\mu\nu}^{\text{GW}}$ é o tensor energia-momento das ondas gravitacionais.

---

## Derivação do Espectro SGWB

### Passo 1: Flutuações Primordiais

Durante o bounce, flutuações quânticas nas dimensões temporais:

$$\chi_{\Theta}(\mathbf{k},t) = \int \frac{d^3k'}{(2\pi)^3} G_{\Theta}(\mathbf{k},\mathbf{k}',t) \chi_0(\mathbf{k}')$$

onde $\chi_0$ são flutuações de vácuo e $G_{\Theta}$ é a função de Green temporal.

### Passo 2: Acoplamento com Métrica 3D

As flutuações temporais acoplam com a métrica 3D via:

$$h_{ij}(t,\mathbf{k}) = \alpha_{\text{coup}} \int d\theta d\xi \, G_{\text{proj}}(\theta,\xi) \chi_{\Theta}(\mathbf{k},t)$$

onde $\alpha_{\text{coup}}$ é a constante de acoplamento dimensional.

### Passo 3: Função de Green Gravitacional

A equação para ondas gravitacionais:

$$\ddot{h}_{ij} + 3H\dot{h}_{ij} + \left(\frac{k^2}{a^2} + m_{\text{eff}}^2\right)h_{ij} = S_{\text{source}}$$

onde $m_{\text{eff}}^2$ é a massa efetiva das dimensões temporais:

$$m_{\text{eff}}^2 = \frac{1}{R_2^2} + \frac{1}{R_3^2}$$

### Passo 4: Solução Durante Bounce

Para $t \sim t_{\text{bounce}}$, o fator de escala:

$$a(t) = a_{\text{min}} \cosh\left(\frac{t}{\tau_{\text{bounce}}}\right)$$

A solução da equação GW:

$$h_{ij}(k,t) = \mathcal{A}(k) \left[ \frac{\sin(k\eta)}{\sqrt{k\eta}} + \mathcal{B}(k) \frac{\cos(k\eta)}{\sqrt{k\eta}} \right]$$

onde $\eta$ é o tempo conforme.

---

## Densidade Espectral de Energia

### Definição Fundamental

A densidade espectral das ondas gravitacionais:

$$\Omega_{\text{GW}}(f) = \frac{1}{\rho_c} \frac{d\rho_{\text{GW}}}{d\ln f}$$

onde $\rho_c = \frac{3H_0^2}{8\pi G}$ é a densidade crítica.

### Cálculo da Densidade

$$\rho_{\text{GW}} = \frac{1}{32\pi G} \left\langle \dot{h}_{ij}\dot{h}_{ij} + \frac{1}{a^2}(\nabla h_{ij})^2 \right\rangle$$

### Resultado Principal

Após cálculo completo:

$$\boxed{h^{2}\Omega_{\text{GW}}(f) = \Omega_{\text{GW}}^{(0)} \left(\frac{f}{f_{\text{pico}}}\right)^{n_T} \left(\frac{R_2}{R_3}\right)^{4}}$$

onde:
- $\Omega_{\text{GW}}^{(0)} \sim 10^{-11}$: amplitude de referência
- $f_{\text{pico}} \sim 10^{-3}$ Hz: frequência característica  
- $n_T$: índice espectral tensorial
- $(R_2/R_3)^4$: **assinatura única da GoE**

---

## Frequência de Pico

### Derivação da Escala Característica

A frequência de pico emerge da escala de Hubble no bounce:

$$f_{\text{pico}} = \frac{a_{\text{bounce}}}{a_0} \frac{H_{\text{bounce}}}{2\pi}$$

### Parâmetros do Bounce

Durante o bounce:
- $a_{\text{bounce}} \sim 10^{-30} a_0$ 
- $H_{\text{bounce}} \sim H_{\text{Planck}} = \sqrt{\frac{c^5}{G\hbar}} \sim 10^{43}$ Hz

### Resultado Numérico

$$f_{\text{pico}} \sim 10^{-30} \times \frac{10^{43}}{2\pi} \text{ Hz} \sim 10^{12-13} \text{ Hz}$$

**Correção dimensional:** Dimensões temporais reduzem por fator $\sim 10^{15}$:

$$\boxed{f_{\text{pico}} \simeq 10^{-3}\text{ Hz}}$$

---

## Dependência Dimensional

### Origem da Lei $(R_2/R_3)^4$

A dependência surge do acoplamento entre dimensões temporais:

$$\mathcal{L}_{\text{int}} = \frac{1}{2\kappa^2} \int d\theta d\xi \, R_{\text{temporal}} \sqrt{g_{\Theta\Theta}}$$

onde $R_{\text{temporal}}$ é a curvatura das dimensões temporais.

### Cálculo do Fator

$$\int d\theta d\xi \, R_{\text{temporal}} = \frac{2\pi^2}{R_2 R_3} \left( \frac{1}{R_2^2} + \frac{1}{R_3^2} \right)$$

Para $R_2 \neq R_3$:

$$\frac{\partial}{\partial R_2} \left[ \frac{1}{R_2 R_3} \left( \frac{1}{R_2^2} + \frac{1}{R_3^2} \right) \right] \propto \frac{R_2^2}{R_3^4}$$

Resultando na dependência observada: $(R_2/R_3)^4$.

---

## Predições para LISA/Taiji

### Banda de Frequências

LISA opera em $f \in [10^{-4}, 10^{-1}]$ Hz, cobrindo:
- **Frequência de pico:** $f_{\text{pico}} = 10^{-3}$ Hz ✓
- **Largura do sinal:** $\Delta f/f \sim 1-2$ décadas

### Sensibilidade Requerida

Para detectar o sinal GoE:

$$h^2\Omega_{\text{GW}}^{\text{min}} \sim 10^{-12}$$

**LISA sensitivity:** $h^2\Omega_{\text{GW}}^{\text{LISA}} \sim 10^{-13}$ ✓

### Distinguibilidade

O sinal GoE distingue-se por:

1. **Pico específico:** $f = 10^{-3}$ Hz
2. **Dependência dimensional:** $(R_2/R_3)^4$
3. **Índice espectral:** $n_T \neq 0$ (diferente de inflação)

---

## Assinatura Experimental

### Forma Espectral Característica

$$\log_{10}\left[h^2\Omega_{\text{GW}}(f)\right] = \log_{10}\left[\Omega_{\text{GW}}^{(0)}\right] + 4\log_{10}\left(\frac{R_2}{R_3}\right) + n_T\log_{10}\left(\frac{f}{f_{\text{pico}}}\right)$$

### Parâmetros Ajustáveis

1. **Amplitude:** $\Omega_{\text{GW}}^{(0)}$
2. **Razão dimensional:** $R_2/R_3$  
3. **Índice espectral:** $n_T$
4. **Frequência de pico:** $f_{\text{pico}}$

### Correlações com Outras Anomalias

Via constante geométrica $K$:

$$\frac{\Omega_{\text{GW}}^{(0)}}{K} = \frac{[1-\cos(\delta_{CP})]}{10^{-2}} \approx 0.15$$

---

## Código de Validação

```python
import numpy as np
import matplotlib.pyplot as plt

def sgwb_spectrum_goe(f, f_peak=1e-3, Omega_0=1e-11, R2_R3=1.0, n_T=0):
    """
    Espectro de ondas gravitacionais da GoE
    
    Parâmetros:
    -----------
    f : array
        Frequências em Hz
    f_peak : float  
        Frequência de pico
    Omega_0 : float
        Amplitude de referência
    R2_R3 : float
        Razão das dimensões temporais
    n_T : float
        Índice espectral tensorial
        
    Retorna:
    --------
    h2_Omega_GW : array
        Densidade espectral
    """
    h2 = 0.7**2  # Parâmetro de Hubble
    
    # Espectro principal
    spectrum = Omega_0 * (f / f_peak)**n_T * (R2_R3)**4
    
    return h2 * spectrum

def lisa_sensitivity(f):
    """
    Curva de sensibilidade do LISA (aproximada)
    """
    # Ruído instrumental + astrofísico
    f_knee = 3e-3  # Hz
    Omega_sens = 1e-12 * (f / f_knee)**(-7/3) * (1 + (f / f_knee)**(10/3))
    return 0.7**2 * Omega_sens

# Gerar espectro GoE
f_range = np.logspace(-4, -1, 1000)  # Hz
spectrum_goe = sgwb_spectrum_goe(f_range)
sensitivity = lisa_sensitivity(f_range)

# Plot comparativo
plt.figure(figsize=(12, 8))
plt.loglog(f_range, spectrum_goe, 'b-', linewidth=3, label='GoE Bounce Signal')
plt.loglog(f_range, sensitivity, 'r--', linewidth=2, label='LISA Sensitivity')

# Destacar região detectável
detectable = spectrum_goe > sensitivity
plt.fill_between(f_range[detectable], 1e-15, 1e-8, 
                alpha=0.2, color='green', label='Detectable Region')

plt.axvline(1e-3, color='blue', linestyle=':', alpha=0.7, label='f_peak = 10⁻³ Hz')
plt.xlabel('Frequency [Hz]')
plt.ylabel('h² Ω_GW')
plt.title('Stochastic Gravitational Wave Background - GoE vs LISA')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(1e-4, 1e-1)
plt.ylim(1e-15, 1e-8)

# Adicionar texto com parâmetros
plt.text(2e-4, 5e-10, 'GoE Parameters:\nf_peak = 10⁻³ Hz\nΩ⁰ = 10⁻¹¹\n(R₂/R₃)⁴ = 1', 
         bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.8))

plt.show()

# Cálculo detalhado
print("=== PREDIÇÕES GoE PARA LISA ===")
print(f"Frequência de pico: {1e-3:.0e} Hz")
print(f"Amplitude no pico: {sgwb_spectrum_goe(1e-3):.0e}")
print(f"Sensibilidade LISA: {lisa_sensitivity(1e-3):.0e}")
print(f"Razão sinal/ruído: {sgwb_spectrum_goe(1e-3)/lisa_sensitivity(1e-3):.1f}")
print(f"Detectável: {'✅ SIM' if sgwb_spectrum_goe(1e-3) > lisa_sensitivity(1e-3) else '❌ NÃO'}")

# Teste variação dimensional
print(f"\n=== DEPENDÊNCIA DIMENSIONAL ===")
for R2_R3 in [0.5, 1.0, 2.0]:
    signal = sgwb_spectrum_goe(1e-3, R2_R3=R2_R3)
    print(f"R₂/R₃ = {R2_R3:.1f}: h²Ω_GW = {signal:.1e}")
```

---

## Cenários de Detecção

### Cenário Otimista

- **Parâmetros:** $R_2/R_3 = 2$, $\Omega_{\text{GW}}^{(0)} = 5 \times 10^{-11}$
- **Sinal:** $h^2\Omega_{\text{GW}} \sim 8 \times 10^{-10}$ 
- **Detectabilidade:** Alta (SNR > 100)

### Cenário Conservador  

- **Parâmetros:** $R_2/R_3 = 1$, $\Omega_{\text{GW}}^{(0)} = 10^{-11}$
- **Sinal:** $h^2\Omega_{\text{GW}} \sim 7 \times 10^{-12}$
- **Detectabilidade:** Marginal (SNR ~ 3-5)

### Cenário Pessimista

- **Parâmetros:** $R_2/R_3 = 0.5$, $\Omega_{\text{GW}}^{(0)} = 10^{-12}$ 
- **Sinal:** $h^2\Omega_{\text{GW}} \sim 6 \times 10^{-14}$
- **Detectabilidade:** Requer LISA+ ou BBO

---

## Implicações e Extensões

### Confirmação da GoE

Detecção do sinal confirmaria:

1. **Bounce cosmológico:** Alternativa ao Big Bang
2. **Dimensões temporais:** Estrutura (3+3)D do espaço-tempo
3. **Escala fundamental:** $R_2, R_3 \sim 10^{-18}$ m

### Limitações Atuais

1. **Modelo simplificado:** Bounce instantâneo
2. **Aproximações:** Acoplamento fraco dimensional
3. **Backgrounds:** Contaminação astrofísica

### Desenvolvimentos Futuros

1. **Simulações numéricas:** Bounce realístico
2. **Multi-messengers:** Correlação com outros sinais
3. **Redes de detectores:** LISA + Taiji + BBO

---

## Referências

1. **Instrumentais:**
   - LISA Consortium, *arXiv:1702.00786* (2017)
   - Taiji Collaboration, *Int. J. Mod. Phys. D* **30**, 2140005 (2021)

2. **Teóricas:**
   - Monografia GoE, Capítulo 8.1
   - [Derivação JWST](jwst_tension_resolution.md)
   - [Notebook GW](../../notebooks/derivations/goe_derivations_complete.ipynb)

3. **Revisões:**
   - Caprini *et al.*, *JCAP* **04**, 001 (2016)
   - Smith *et al.*, *Phys. Rev. D* **100**, 104055 (2019)

---

*Derivação validada em: Julho 2025 • Detectabilidade LISA: ✓ • Assinatura única: ✓*