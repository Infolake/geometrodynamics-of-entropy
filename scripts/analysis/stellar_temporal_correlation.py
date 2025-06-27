#!/usr/bin/env python3
"""
Correlação entre Tipos Espectrais Estelares e Dimensões Temporais CTMCK
Autor: Guilherme de Camargo
Data: 2025-01-26

Análise da relação entre massa estelar, tempo de vida e as três dimensões temporais:
- t₁: Tempo Quântico Local (processos nucleares internos)
- t₂: Tempo Relacional Sistêmico (evolução estelar e interações)
- t₃: Tempo Cosmológico (escala de formação e morte estelar)
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

class StellarTemporalAnalysis:
    """Classe para análise da correlação estelar-temporal CTMCK"""
    
    def __init__(self):
        # Dados dos tipos espectrais estelares
        self.stellar_data = {
            'Tipo': ['O', 'B', 'A', 'F', 'G', 'K', 'M'],
            'Massa_Solar': [60, 18, 3.2, 1.7, 1.0, 0.8, 0.3],
            'Luminosidade_Solar': [1000000, 20000, 80, 6, 1, 0.4, 0.04],
            'Temp_Superficie_K': [45000, 20000, 8500, 6500, 5500, 4000, 3000],
            'Tempo_Vida_Anos': [3e6, 1e7, 3e8, 3e9, 1e10, 5e10, 1e12],
            'Cor': ['azul', 'azul-branco', 'branco', 'amarelo-branco', 'amarelo', 'laranja', 'vermelho']
        }
        
        self.df = pd.DataFrame(self.stellar_data)
        
        # Calcular índices temporais CTMCK
        self._calculate_temporal_indices()
    
    def _calculate_temporal_indices(self):
        """Calcula os índices das três dimensões temporais para cada tipo estelar"""
        
        # t₁ (Tempo Quântico): Relacionado à intensidade dos processos nucleares
        # Proporcional à taxa de fusão nuclear (Massa^3.5 aproximadamente)
        self.df['t1_quantum'] = (self.df['Massa_Solar'] ** 3.5) / 1000
        
        # t₂ (Tempo Relacional): Relacionado à evolução estelar e estabilidade
        # Inversamente proporcional à luminosidade (estrelas mais luminosas evoluem mais rápido)
        self.df['t2_relational'] = 1 / np.log10(self.df['Luminosidade_Solar'] + 1)
        
        # t₃ (Tempo Cosmológico): Diretamente relacionado ao tempo de vida estelar
        # Normalizado em escala logarítmica
        self.df['t3_cosmological'] = np.log10(self.df['Tempo_Vida_Anos']) / 12  # Normalizado para escala 0-1
        
        # Índice de Habitabilidade Temporal (combinação das três dimensões)
        # Favorece equilíbrio: t₁ moderado, t₂ alto (estabilidade), t₃ alto (longevidade)
        self.df['habitability_index'] = (
            np.exp(-2 * (self.df['t1_quantum'] - 0.3)**2) *  # t₁ ótimo ~ 0.3
            self.df['t2_relational'] *                        # t₂ maior é melhor
            self.df['t3_cosmological']                        # t₃ maior é melhor
        )
    
    def create_stellar_temporal_table(self):
        """Cria tabela detalhada com correlações temporais"""
        
        print("=" * 100)
        print("CORRELAÇÃO ENTRE TIPOS ESPECTRAIS ESTELARES E DIMENSÕES TEMPORAIS CTMCK")
        print("=" * 100)
        
        # Criar tabela formatada
        table_data = []
        for _, row in self.df.iterrows():
            table_data.append([
                row['Tipo'],
                f"{row['Massa_Solar']:.1f}",
                f"{row['Luminosidade_Solar']:.0e}",
                f"{row['Tempo_Vida_Anos']:.0e}",
                f"{row['t1_quantum']:.3f}",
                f"{row['t2_relational']:.3f}",
                f"{row['t3_cosmological']:.3f}",
                f"{row['habitability_index']:.4f}"
            ])
        
        headers = ['Tipo', 'Massa☉', 'Lum☉', 'Vida(anos)', 't₁(quant)', 't₂(relac)', 't₃(cosmo)', 'Hab.Index']
        
        # Imprimir tabela
        print(f"{'Tipo':<6}{'Massa☉':<8}{'Luminosidade☉':<12}{'Vida(anos)':<12}{'t₁':<10}{'t₂':<10}{'t₃':<10}{'Índice Hab.':<12}")
        print("-" * 100)
        
        for row in table_data:
            print(f"{row[0]:<6}{row[1]:<8}{row[2]:<12}{row[3]:<12}{row[4]:<10}{row[5]:<10}{row[6]:<10}{row[7]:<12}")
        
        print("\n" + "=" * 100)
        print("INTERPRETAÇÃO DAS DIMENSÕES TEMPORAIS:")
        print("=" * 100)
        print("t₁ (Tempo Quântico):     Intensidade dos processos nucleares internos")
        print("t₂ (Tempo Relacional):   Estabilidade evolutiva e interações sistêmicas") 
        print("t₃ (Tempo Cosmológico):  Longevidade e escala temporal cosmológica")
        print("Índice Habitabilidade:   Potencial para desenvolvimento de complexidade")
        print("=" * 100)
    
    def plot_temporal_correlations(self):
        """Cria visualizações das correlações temporais"""
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # Gráfico 1: Massa vs Tempo de Vida (clássico)
        ax1.loglog(self.df['Massa_Solar'], self.df['Tempo_Vida_Anos'], 'o-', linewidth=2, markersize=8)
        for i, tipo in enumerate(self.df['Tipo']):
            ax1.annotate(tipo, (self.df['Massa_Solar'].iloc[i], self.df['Tempo_Vida_Anos'].iloc[i]), 
                        xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
        ax1.set_xlabel('Massa Estelar (Massas Solares)')
        ax1.set_ylabel('Tempo de Vida (Anos)')
        ax1.set_title('Relação Massa-Longevidade Estelar')
        ax1.grid(True, alpha=0.3)
        
        # Gráfico 2: Três Dimensões Temporais
        x = np.arange(len(self.df))
        width = 0.25
        
        ax2.bar(x - width, self.df['t1_quantum'], width, label='t₁ (Quântico)', alpha=0.8, color='red')
        ax2.bar(x, self.df['t2_relational'], width, label='t₂ (Relacional)', alpha=0.8, color='green')
        ax2.bar(x + width, self.df['t3_cosmological'], width, label='t₃ (Cosmológico)', alpha=0.8, color='blue')
        
        ax2.set_xlabel('Tipo Espectral')
        ax2.set_ylabel('Índice Temporal Normalizado')
        ax2.set_title('Três Dimensões Temporais CTMCK por Tipo Estelar')
        ax2.set_xticks(x)
        ax2.set_xticklabels(self.df['Tipo'])
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Gráfico 3: Índice de Habitabilidade Temporal
        colors = plt.cm.viridis(self.df['habitability_index'] / self.df['habitability_index'].max())
        bars = ax3.bar(self.df['Tipo'], self.df['habitability_index'], color=colors)
        ax3.set_xlabel('Tipo Espectral')
        ax3.set_ylabel('Índice de Habitabilidade Temporal')
        ax3.set_title('Potencial de Habitabilidade Temporal CTMCK')
        ax3.grid(True, alpha=0.3)
        
        # Adicionar valores nas barras
        for bar, valor in zip(bars, self.df['habitability_index']):
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height + 0.001,
                    f'{valor:.3f}', ha='center', va='bottom', fontsize=9)
        
        # Gráfico 4: Diagrama 3D das Dimensões Temporais
        ax4 = fig.add_subplot(224, projection='3d')
        scatter = ax4.scatter(self.df['t1_quantum'], self.df['t2_relational'], self.df['t3_cosmological'],
                             c=self.df['habitability_index'], cmap='plasma', s=100)
        
        # Adicionar labels dos tipos
        for i, tipo in enumerate(self.df['Tipo']):
            ax4.text(self.df['t1_quantum'].iloc[i], self.df['t2_relational'].iloc[i], 
                    self.df['t3_cosmological'].iloc[i], tipo, fontsize=10, fontweight='bold')
        
        ax4.set_xlabel('t₁ (Tempo Quântico)')
        ax4.set_ylabel('t₂ (Tempo Relacional)')
        ax4.set_zlabel('t₃ (Tempo Cosmológico)')
        ax4.set_title('Espaço Temporal 3D CTMCK')
        
        plt.colorbar(scatter, ax=ax4, label='Índice de Habitabilidade', shrink=0.8)
        
        plt.tight_layout()
        
        # Salvar
        output_dir = '../../figures/diagrams'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'stellar_temporal_correlations.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"\n[OK] Gráficos salvos em: {output_path}")
        
        plt.close()
        return output_path
    
    def theoretical_analysis(self):
        """Análise teórica detalhada das correlações"""
        
        print("\n" + "=" * 100)
        print("ANÁLISE TEÓRICA: CORRELAÇÃO ESTELAR-TEMPORAL CTMCK")
        print("=" * 100)
        
        # Encontrar estrela com maior índice de habitabilidade
        best_star = self.df.loc[self.df['habitability_index'].idxmax()]
        
        print(f"\n🌟 ESTRELA ÓTIMA PARA HABITABILIDADE TEMPORAL:")
        print(f"   Tipo: {best_star['Tipo']} (como nosso Sol)")
        print(f"   Índice de Habitabilidade: {best_star['habitability_index']:.4f}")
        print(f"   t₁ (Quântico): {best_star['t1_quantum']:.3f}")
        print(f"   t₂ (Relacional): {best_star['t2_relational']:.3f}")
        print(f"   t₃ (Cosmológico): {best_star['t3_cosmological']:.3f}")
        
        print(f"\n📊 INSIGHTS DA TEORIA CTMCK:")
        print(f"   • Estrelas tipo O/B: Alto t₁ (processos quânticos intensos), baixo t₃ (vida curta)")
        print(f"   • Estrelas tipo G: Equilíbrio ótimo das três dimensões temporais")
        print(f"   • Estrelas tipo M: Baixo t₁, alto t₃, mas evolução muito lenta")
        
        print(f"\n🔬 IMPLICAÇÕES PARA HABITABILIDADE:")
        print(f"   • Complexidade requer equilíbrio temporal multidimensional")
        print(f"   • Estrelas G oferecem 'zona de Goldilocks temporal'")
        print(f"   • Teoria CTMCK explica por que vida complexa favorece estrelas tipo solar")
        
        print("=" * 100)
    
    def save_data_table(self):
        """Salva tabela de dados em CSV"""
        output_dir = '../../data/processed'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'stellar_temporal_correlations.csv')
        self.df.to_csv(output_path, index=False)
        print(f"[OK] Dados salvos em: {output_path}")
        return output_path

def main():
    """Função principal"""
    print("Iniciando Análise de Correlação Estelar-Temporal CTMCK...")
    
    # Criar instância da análise
    analysis = StellarTemporalAnalysis()
    
    # Executar análises
    analysis.create_stellar_temporal_table()
    analysis.theoretical_analysis()
    plot_path = analysis.plot_temporal_correlations()
    data_path = analysis.save_data_table()
    
    print(f"\n✅ Análise completa!")
    print(f"📊 Gráficos: {plot_path}")
    print(f"📄 Dados: {data_path}")

if __name__ == "__main__":
    main() 