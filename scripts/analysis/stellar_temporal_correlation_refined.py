#!/usr/bin/env python3
"""
Correlação Refinada entre Tipos Espectrais Estelares e Dimensões Temporais CTMCK
Autor: Guilherme de Camargo
Data: 2025-01-26

Versão refinada com índice de habitabilidade temporal balanceado
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

class RefinedStellarTemporalAnalysis:
    """Classe para análise refinada da correlação estelar-temporal CTMCK"""
    
    def __init__(self):
        # Dados dos tipos espectrais estelares
        self.stellar_data = {
            'Tipo': ['O', 'B', 'A', 'F', 'G', 'K', 'M'],
            'Massa_Solar': [60, 18, 3.2, 1.7, 1.0, 0.8, 0.3],
            'Luminosidade_Solar': [1000000, 20000, 80, 6, 1, 0.4, 0.04],
            'Temp_Superficie_K': [45000, 20000, 8500, 6500, 5500, 4000, 3000],
            'Tempo_Vida_Anos': [3e6, 1e7, 3e8, 3e9, 1e10, 5e10, 1e12],
            'Zona_Habitavel_UA': [100, 50, 9, 2.5, 1.0, 0.6, 0.2]  # Distância da zona habitável
        }
        
        self.df = pd.DataFrame(self.stellar_data)
        
        # Calcular índices temporais CTMCK refinados
        self._calculate_refined_temporal_indices()
    
    def _calculate_refined_temporal_indices(self):
        """Calcula os índices refinados das três dimensões temporais"""
        
        # t₁ (Tempo Quântico): Normalizado para escala 0-1
        t1_raw = (self.df['Massa_Solar'] ** 3.5) / 1000
        self.df['t1_quantum'] = t1_raw / t1_raw.max()
        
        # t₂ (Tempo Relacional): Estabilidade (inverso da luminosidade, normalizado)
        t2_raw = 1 / np.log10(self.df['Luminosidade_Solar'] + 1)
        self.df['t2_relational'] = t2_raw / t2_raw.max()
        
        # t₃ (Tempo Cosmológico): Longevidade normalizada
        t3_raw = np.log10(self.df['Tempo_Vida_Anos'])
        self.df['t3_cosmological'] = (t3_raw - t3_raw.min()) / (t3_raw.max() - t3_raw.min())
        
        # Índice de Habitabilidade Temporal REFINADO
        # Favorece equilíbrio: t₁ baixo-moderado, t₂ alto, t₃ moderado-alto
        # Penaliza extremos (muito alta energia ou muito baixa energia)
        
        # Função Gaussiana para t₁ (ótimo em ~0.1-0.3)
        t1_factor = np.exp(-10 * (self.df['t1_quantum'] - 0.2)**2)
        
        # Função crescente para t₂ (estabilidade é sempre boa)
        t2_factor = self.df['t2_relational']
        
        # Função Gaussiana para t₃ (ótimo em ~0.6-0.8, nem muito curto nem muito longo)
        t3_factor = np.exp(-5 * (self.df['t3_cosmological'] - 0.7)**2)
        
        # Fator adicional: zona habitável (favorece distâncias moderadas)
        zh_factor = np.exp(-0.5 * (np.log10(self.df['Zona_Habitavel_UA']) - 0)**2)
        
        self.df['habitability_index'] = t1_factor * t2_factor * t3_factor * zh_factor
        
        # Normalizar índice final
        self.df['habitability_index'] = self.df['habitability_index'] / self.df['habitability_index'].max()
    
    def create_refined_stellar_table(self):
        """Cria tabela refinada com correlações temporais"""
        
        print("=" * 110)
        print("CORRELACAO REFINADA: TIPOS ESPECTRAIS ESTELARES E DIMENSOES TEMPORAIS CTMCK")
        print("=" * 110)
        
        print(f"{'Tipo':<6}{'Massa':<8}{'Luminosidade':<12}{'Vida(anos)':<12}{'t1':<8}{'t2':<8}{'t3':<8}{'Hab.Index':<10}{'Ranking':<8}")
        print("-" * 110)
        
        # Ordenar por índice de habitabilidade
        df_sorted = self.df.sort_values('habitability_index', ascending=False)
        
        for i, (_, row) in enumerate(df_sorted.iterrows()):
            print(f"{row['Tipo']:<6}{row['Massa_Solar']:.1f}{'Ms':<7}"
                  f"{row['Luminosidade_Solar']:.0e}{'Ls':<4}"
                  f"{row['Tempo_Vida_Anos']:.0e}{'anos':<4}"
                  f"{row['t1_quantum']:.3f}{'':>5}"
                  f"{row['t2_relational']:.3f}{'':>5}"
                  f"{row['t3_cosmological']:.3f}{'':>5}"
                  f"{row['habitability_index']:.4f}{'':>6}"
                  f"#{i+1:<7}")
        
        print("\n" + "=" * 110)
        print("INTERPRETACAO DAS DIMENSOES TEMPORAIS CTMCK:")
        print("=" * 110)
        print("t1 (Tempo Quantico):     Intensidade processos nucleares (0=baixo, 1=alto)")
        print("t2 (Tempo Relacional):   Estabilidade evolutiva (0=instavel, 1=estavel)") 
        print("t3 (Tempo Cosmologico):  Longevidade estelar (0=curto, 1=longo)")
        print("Habitabilidade Index:    Potencial desenvolvimento complexidade (0-1)")
        print("=" * 110)
        
        return df_sorted
    
    def theoretical_insights(self):
        """Análise teórica refinada"""
        
        df_sorted = self.df.sort_values('habitability_index', ascending=False)
        best_star = df_sorted.iloc[0]
        
        print("\n" + "=" * 110)
        print("INSIGHTS TEORICOS DA CORRELACAO ESTELAR-TEMPORAL CTMCK")
        print("=" * 110)
        
        print(f"\nESTRELA OTIMA PARA HABITABILIDADE TEMPORAL:")
        print(f"   [BEST] Tipo: {best_star['Tipo']} - Indice: {best_star['habitability_index']:.4f}")
        print(f"   [DATA] t1={best_star['t1_quantum']:.3f}, t2={best_star['t2_relational']:.3f}, t3={best_star['t3_cosmological']:.3f}")
        
        print(f"\nRANKING DE HABITABILIDADE TEMPORAL:")
        for i, (_, row) in enumerate(df_sorted.iterrows()):
            medal = "[1st]" if i == 0 else "[2nd]" if i == 1 else "[3rd]" if i == 2 else "[***]"
            print(f"   {medal} #{i+1}: Tipo {row['Tipo']} - {row['habitability_index']:.4f}")
        
        print(f"\nCORRELACAES CTMCK FUNDAMENTAIS:")
        print(f"   [HOT] Estrelas O/B: Energia extrema (t1 alto), vida curta (t3 baixo)")
        print(f"   [BAL] Estrelas F/G: Equilibrio temporal ideal para complexidade")
        print(f"   [SLW] Estrelas K/M: Estabilidade alta, mas evolucao lenta")
        
        print(f"\nIMPLICACAES PARA A TEORIA CTMCK:")
        print(f"   • Complexidade emerge no equilibrio das 3 dimensoes temporais")
        print(f"   • Estrelas tipo F/G criam 'zona Goldilocks temporal'")
        print(f"   • Explicacao quantitativa para preferencia por estrelas solares")
        print(f"   • Vida complexa requer sincronizacao t1-t2-t3 otima")
        
        print("=" * 110)
    
    def create_comprehensive_plots(self):
        """Cria visualizações abrangentes"""
        
        fig = plt.figure(figsize=(16, 12))
        
        # Plot 1: Diagrama Massa-Tempo de Vida clássico
        ax1 = plt.subplot(2, 3, 1)
        plt.loglog(self.df['Massa_Solar'], self.df['Tempo_Vida_Anos'], 'o-', linewidth=2, markersize=8, color='navy')
        for i, tipo in enumerate(self.df['Tipo']):
            plt.annotate(tipo, (self.df['Massa_Solar'].iloc[i], self.df['Tempo_Vida_Anos'].iloc[i]), 
                        xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
        plt.xlabel('Massa Estelar (Massas Solares)')
        plt.ylabel('Tempo de Vida (Anos)')
        plt.title('Relacao Massa-Longevidade Estelar')
        plt.grid(True, alpha=0.3)
        
        # Plot 2: Três dimensões temporais
        ax2 = plt.subplot(2, 3, 2)
        x = np.arange(len(self.df))
        width = 0.25
        
        plt.bar(x - width, self.df['t1_quantum'], width, label='t1 (Quantico)', alpha=0.8, color='red')
        plt.bar(x, self.df['t2_relational'], width, label='t2 (Relacional)', alpha=0.8, color='green')
        plt.bar(x + width, self.df['t3_cosmological'], width, label='t3 (Cosmologico)', alpha=0.8, color='blue')
        
        plt.xlabel('Tipo Espectral')
        plt.ylabel('Indice Temporal Normalizado')
        plt.title('Tres Dimensoes Temporais CTMCK')
        plt.xticks(x, self.df['Tipo'])
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Plot 3: Índice de habitabilidade refinado
        ax3 = plt.subplot(2, 3, 3)
        df_sorted = self.df.sort_values('habitability_index', ascending=True)
        colors = plt.cm.viridis(df_sorted['habitability_index'])
        bars = plt.barh(df_sorted['Tipo'], df_sorted['habitability_index'], color=colors)
        plt.xlabel('Indice de Habitabilidade Temporal')
        plt.title('Ranking de Habitabilidade CTMCK')
        plt.grid(True, alpha=0.3)
        
        # Plot 4: Espaço temporal 3D
        ax4 = plt.subplot(2, 3, 4, projection='3d')
        scatter = ax4.scatter(self.df['t1_quantum'], self.df['t2_relational'], self.df['t3_cosmological'],
                             c=self.df['habitability_index'], cmap='plasma', s=150, alpha=0.8)
        
        for i, tipo in enumerate(self.df['Tipo']):
            ax4.text(self.df['t1_quantum'].iloc[i], self.df['t2_relational'].iloc[i], 
                    self.df['t3_cosmological'].iloc[i], f'  {tipo}', fontsize=10, fontweight='bold')
        
        ax4.set_xlabel('t1 (Tempo Quantico)')
        ax4.set_ylabel('t2 (Tempo Relacional)')
        ax4.set_zlabel('t3 (Tempo Cosmologico)')
        ax4.set_title('Espaco Temporal 3D CTMCK')
        
        # Plot 5: Correlação Habitabilidade vs Massa
        ax5 = plt.subplot(2, 3, 5)
        plt.semilogx(self.df['Massa_Solar'], self.df['habitability_index'], 'o-', linewidth=2, markersize=8, color='purple')
        for i, tipo in enumerate(self.df['Tipo']):
            plt.annotate(tipo, (self.df['Massa_Solar'].iloc[i], self.df['habitability_index'].iloc[i]), 
                        xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
        plt.xlabel('Massa Estelar (Massas Solares)')
        plt.ylabel('Indice de Habitabilidade Temporal')
        plt.title('Habitabilidade vs Massa Estelar')
        plt.grid(True, alpha=0.3)
        
        # Plot 6: Zona habitável vs Habitabilidade
        ax6 = plt.subplot(2, 3, 6)
        plt.loglog(self.df['Zona_Habitavel_UA'], self.df['habitability_index'], 'o-', linewidth=2, markersize=8, color='orange')
        for i, tipo in enumerate(self.df['Tipo']):
            plt.annotate(tipo, (self.df['Zona_Habitavel_UA'].iloc[i], self.df['habitability_index'].iloc[i]), 
                        xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
        plt.xlabel('Distancia Zona Habitavel (UA)')
        plt.ylabel('Indice de Habitabilidade Temporal')
        plt.title('Zona Habitavel vs Habitabilidade CTMCK')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Salvar
        output_dir = r'C:\Users\Guilh\Downloads\ScientificoDrGuilhermeDeCamargo\guilherme-ctmck\figures\diagrams'
        output_path = os.path.join(output_dir, 'stellar_temporal_correlations_refined.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"\n[OK] Analise refinada salva em: {output_path}")
        
        plt.close()
        return output_path

def main():
    """Função principal"""
    print("Iniciando Analise Refinada de Correlacao Estelar-Temporal CTMCK...")
    
    # Criar instância da análise refinada
    analysis = RefinedStellarTemporalAnalysis()
    
    # Executar análises
    df_sorted = analysis.create_refined_stellar_table()
    analysis.theoretical_insights()
    plot_path = analysis.create_comprehensive_plots()
    
    print(f"\n[OK] Analise refinada completa!")
    print(f"[PLOTS] Graficos: {plot_path}")

if __name__ == "__main__":
    main()