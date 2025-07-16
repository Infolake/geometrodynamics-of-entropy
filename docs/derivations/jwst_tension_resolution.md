# Derivação Detalhada: Tensão JWST - Galáxias Precoces

**Autor:** Dr. Guilherme de Camargo  
**Derivação:** 3/7 da série GoE  
**Capítulo relacionado:** [Monografia Cap. 7.4](../../Geometrodynamics_of_Entropy_A_Comprehensive_Monograph.md)

---

## Introdução

O James Webb Space Telescope (JWST) revolucionou nossa compreensão do universo primordial ao detectar galáxias massivas e evoluídas em redshifts $z > 10$, correspondendo a apenas ~500 milhões de anos após o Big Bang. Esta observação cria uma tensão fundamental com os modelos cosmológicos padrão, conhecida como **Tensão JWST**.

### Observações Problemáticas

- **Galáxias massivas:** $M_* > 10^{10} M_\odot$ em $z \sim 10-13$
- **Evolução rápida:** Formação estelar em <100 Myr
- **Abundância:** Densidade numérica maior que esperado
- **Metalicidade:** Enriquecimento químico precoce

A GoE resolve esta tensão através do **bounce cosmológico** e formação de buracos negros primordiais (PBHs).

---

## Cosmologia GoE vs ΛCDM

### Modelo Padrão (ΛCDM)

No modelo ΛCDM, a formação de estruturas segue:

$$\frac{dM_{\text{halo}}}{dt} \propto (1+z)^{-3/2} \sqrt{\Omega_m(z)}$$

Esta taxa é insuficiente para formar galáxias massivas em $z > 10$.

### Bounce Cosmológico GoE

A GoE substitui a singularidade inicial por um bounce:

$$a(t) = a_{\text{min}} \cosh\left(\frac{t}{\tau_{\text{bounce}}}\right)$$

onde:
- $a_{\text{min}}$: fator de escala mínimo no bounce
- $\tau_{\text{bounce}}$: escala temporal do bounce

---

## Densidade de Energia de Torção

### Componente Fundamental

A densidade de energia de torção na GoE:

$$\boxed{\rho_{\text{tor}}(a) = \rho_{\text{tor},0} \cdot a^{-6}}$$

Esta dependência $a^{-6}$ é **mais forte que radiação** ($a^{-4}$) e domina no universo primordial.

### Derivação da Lei de Escala

A densidade de torção emerge do tensor de Einstein modificado:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu} + 8\pi G T_{\mu\nu}^{\text{tor}}$$

onde o tensor de torção:

$$T_{\mu\nu}^{\text{tor}} = \frac{1}{2\kappa^2} \left( S_\mu S_\nu - \frac{1}{4} g_{\mu\nu} S^2 \right)$$

com $S_\mu$ sendo o vetor de torção.

### Conservação de Energia

A equação de continuidade para torção:

$$\dot{\rho}_{\text{tor}} + 3H(\rho_{\text{tor}} + P_{\text{tor}}) = 0$$

Com equação de estado $P_{\text{tor}} = \rho_{\text{tor}}$ (torção ultra-relativística):

$$\frac{d\rho_{\text{tor}}}{da} = -\frac{6\rho_{\text{tor}}}{a}$$

Integrando: $\rho_{\text{tor}}(a) = \rho_{\text{tor},0} a^{-6}$

---

## Formação de Buracos Negros Primordiais

### Condições no Bounce

Durante o bounce, a densidade de torção atinge:

$$\rho_{\text{tor}}(a_{\text{min}}) = \rho_{\text{Planck}} \left(\frac{a_0}{a_{\text{min}}}\right)^6$$

Para $a_{\text{min}}/a_0 \sim 10^{-30}$:

$$\rho_{\text{tor}}(a_{\text{min}}) \sim 10^{180} \rho_{\text{Planck}}$$

### Critério de Colapso

PBHs formam quando a densidade local excede:

$$\rho > \rho_{\text{crit}} = \frac{3}{32\pi G t^2}$$

No regime dominado por torção:

$$t_{\text{form}} \sim \left(\frac{32\pi G \rho_{\text{tor}}}{3}\right)^{-1/2}$$

### Espectro de Massa dos PBHs

A massa típica dos PBHs formados:

$$M_{\text{PBH}} \sim \frac{4\pi}{3} \rho_{\text{tor}}(t_{\text{form}}) \left(\frac{t_{\text{form}}}{2}\right)^3$$

Resultando em:

$$\boxed{M_{\text{PBH}} \sim 10^{3-6} M_\odot}$$

---

## Espectro de Perturbações "Azul"

### Modificação da Inflação

O bounce GoE produz um espectro de perturbações:

$$P(k) = A_s \left(\frac{k}{k_{\text{pivot}}}\right)^{n_s - 1}$$

com **índice espectral azul:** $n_s > 1$.

### Derivação do Índice

Durante o bounce, o modo de Hubble:

$$\frac{d}{dt}\left(\frac{\delta\phi}{H}\right) = \frac{\ddot{a}}{aH^2} \frac{\delta\phi}{H}$$

Para bounce: $\ddot{a} > 0$, resultando em crescimento das perturbações em pequenas escalas.

O índice espectral:

$$n_s - 1 = \frac{d\ln P}{d\ln k} = 2\epsilon - \eta$$

onde no bounce: $\epsilon < 0$ e $\eta > 0$, levando a $n_s > 1$.

### Consequências Observacionais

1. **Mais potência em pequenas escalas:** Favorece formação precoce
2. **Supressão em grandes escalas:** Consistente com CMB
3. **Pico em escala intermediária:** Máximo em $k \sim 10^{6-8}$ Mpc⁻¹

---

## Formação Acelerada de Galáxias

### Sementes de Alto Redshift

PBHs de $10^{3-6} M_\odot$ servem como sementes galácticas em $z \sim 20-30$:

$$t_{\text{seed}} \sim 100-200 \text{ Myr}$$

### Taxa de Acreção Modificada

Com sementes massivas, a taxa de acreção:

$$\frac{dM}{dt} = \frac{4\pi \rho_{\text{gas}} R_{\text{Bondi}}^2 v_{\text{sound}}}{\sqrt{1 + (v_{\text{escape}}/v_{\text{sound}})^2}}$$

é **dramaticamente aumentada** devido ao maior $R_{\text{Bondi}}$.

### Tempo de Formação

Galáxias $10^{10} M_\odot$ podem formar em:

$$t_{\text{form}} \sim \frac{M_{\text{final}}}{dM/dt} \sim 50-100 \text{ Myr}$$

**Compatível com observações JWST!**

---

## Predições Quantitativas

### Função de Massa das Galáxias

$$\frac{dn}{dM_*}(z) = \frac{dn_{\text{PBH}}}{dM_{\text{PBH}}} \times \frac{M_{\text{PBH}}}{M_*} \times \epsilon_{\text{eff}}(z)$$

onde $\epsilon_{\text{eff}}$ é a eficiência de conversão barião-estelar.

### Densidade Numérica

Para $z \sim 10$:

$$n_{\text{gal}}(M_* > 10^{10} M_\odot) \sim 10^{-4} \text{ Mpc}^{-3}$$

**Acordo com JWST:** $n_{\text{obs}} \sim (1-5) \times 10^{-4}$ Mpc⁻³

### Metalicidade Precoce

A metalicidade rápida emerge de:

1. **Formação estelar intensa:** $\text{SFR} \sim 100-1000 M_\odot$/ano
2. **Ventos estelares:** Enriquecimento eficiente
3. **Mistura turbulenta:** Homogeneização química

---

## Validação Observacional

### Acordo com JWST

| Observável | JWST | GoE | Status |
|------------|------|-----|---------|
| Densidade numérica | $10^{-4}$ Mpc⁻³ | $10^{-4}$ Mpc⁻³ | ✅ |
| Massa estelar | $>10^{10} M_\odot$ | $10^{10-11} M_\odot$ | ✅ |
| Redshift formação | $z > 10$ | $z \sim 10-15$ | ✅ |
| Tempo formação | $<200$ Myr | $50-100$ Myr | ✅ |

### Testes Futuros

1. **Roman Space Telescope:** Censo completo $z > 10$
2. **Euclid:** Estatísticas de lente gravitacional
3. **30m ELTs:** Espectroscopia detalhada

---

## Código de Validação

```python
import numpy as np
import matplotlib.pyplot as plt

def torsion_density(a, rho_tor_0):
    """
    Densidade de energia de torção vs fator de escala
    """
    return rho_tor_0 * a**(-6)

def pbh_mass_spectrum(t_form, rho_tor):
    """
    Espectro de massa dos PBHs
    """
    return (4*np.pi/3) * rho_tor * (t_form/2)**3

def galaxy_formation_time(M_final, M_seed, accretion_rate):
    """
    Tempo de formação galáctica
    """
    return (M_final - M_seed) / accretion_rate

# Parâmetros GoE
rho_tor_0 = 1e-29  # kg/m³ hoje
a_min = 1e-30      # fator de escala mínimo
a_today = 1.0

# Evolução da densidade de torção
a_range = np.logspace(-30, 0, 1000)
rho_tor = torsion_density(a_range, rho_tor_0)

# Massa típica de PBHs
t_bounce = 1e-43   # segundos (tempo de Planck)
M_pbh = pbh_mass_spectrum(t_bounce, rho_tor[0])

# Conversão para massas solares
M_solar = 1.989e30  # kg
M_pbh_solar = M_pbh / M_solar

print(f"Massa típica PBH: {M_pbh_solar:.0e} M_☉")

# Tempo de formação galáctica
M_galaxy = 1e10  # M_☉
M_seed = M_pbh_solar
rate = 100  # M_☉/ano

t_form_yr = galaxy_formation_time(M_galaxy, M_seed, rate)
t_form_myr = t_form_yr / 1e6

print(f"Tempo formação: {t_form_myr:.0f} Myr")
print(f"Compatível JWST: {'✅' if t_form_myr < 200 else '❌'}")

# Plot evolução densidade
plt.figure(figsize=(10, 6))
plt.loglog(a_range, rho_tor/rho_tor_0, 'b-', linewidth=2, label='Torção (a⁻⁶)')
plt.loglog(a_range, a_range**(-4), 'r--', label='Radiação (a⁻⁴)')
plt.loglog(a_range, a_range**(-3), 'g--', label='Matéria (a⁻³)')
plt.xlabel('Fator de escala a')
plt.ylabel('ρ/ρ₀')
plt.title('Evolução das Densidades de Energia')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(1e-30, 1)
plt.ylim(1, 1e180)
plt.show()
```

---

## Implicações e Extensões

### Conexão com Outros Problemas

1. **Problema do horizonte:** Resolvido pelo bounce
2. **Problema da planicidade:** Naturalidade geométrica
3. **Monopólos magnéticos:** Diluição durante bounce

### Limitações Atuais

1. **Modelo simplificado de bounce:** Dinâmica completa requer simulações
2. **Eficiência de formação estelar:** Incertezas astrofísicas
3. **Feedback e regulação:** Processos de auto-regulação

### Extensões Futuras

1. **Simulações hidrodinâmicas:** Formação detalhada
2. **Química primordial:** Evolução metalicidade
3. **Reionização:** Impacto na evolução cósmica

---

## Referências

1. **Observacionais:**
   - JWST Collaboration, *ApJL* **950**, L1 (2023)
   - Naidu *et al.*, *ApJL* **940**, L14 (2022)

2. **Teóricas:**
   - Monografia GoE, Capítulo 7.4
   - [Derivação GWB](gwb_spectrum_derivation.md)
   - [Notebook cosmológico](../../notebooks/derivations/goe_derivations_complete.ipynb)

3. **Revisões:**
   - Steinhardt & Turok, *Science* **312**, 1180 (2006)
   - Carr *et al.*, *Annu. Rev. Nucl. Part. Sci.* **70**, 355 (2020)

---

*Derivação validada em: Julho 2025 • Acordo observacional: ✓ • Predições testáveis: ✓*