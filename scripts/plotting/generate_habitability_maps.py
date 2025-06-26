#!/usr/bin/env python3
"""
Geração dos Mapas de Habitabilidade Temporal CTMCK
Autor: Guilherme de Camargo
Data: 2025-01-26
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os

def create_output_directory():
    """Cria o diretório de saída se não existir"""
    # Usar caminho absoluto
    output_dir = r'C:\Users\Guilh\Downloads\ScientificoDrGuilhermeDeCamargo\guilherme-ctmck\figures\diagrams'
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def generate_3d_habitability_map():
    """Gera o Mapa de Habitabilidade Temporal em 3D"""
    print("Gerando Mapa 3D de Habitabilidade Temporal...")
    
    # Criação dos eixos t1, t2, t3
    t1 = np.linspace(0, 1, 30)
    t2 = np.linspace(0, 1, 30)
    t3 = np.linspace(0, 1, 30)
    t1_grid, t2_grid, t3_grid = np.meshgrid(t1, t2, t3)

    # Função que representa complexidade emergente como uma função das três dimensões temporais
    def complexity(t1, t2, t3):
        return np.exp(-((t1 - 0.4)**2 + (t2 - 0.5)**2 + (t3 - 0.6)**2) * 30)

    # Calcula a complexidade em cada ponto
    complexity_vals = complexity(t1_grid, t2_grid, t3_grid)

    # Seleciona pontos com complexidade acima de um limiar
    threshold = 0.7
    x, y, z = t1_grid[complexity_vals > threshold], t2_grid[complexity_vals > threshold], t3_grid[complexity_vals > threshold]
    colors = complexity_vals[complexity_vals > threshold]

    # Criar o gráfico 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(x, y, z, c=colors, cmap='plasma', s=20)
    ax.set_xlabel('t1 (Tempo Quantico)')
    ax.set_ylabel('t2 (Tempo Relacional)')
    ax.set_zlabel('t3 (Tempo Cosmologico)')
    ax.set_title('Mapa de Habitabilidade Temporal em Tres Dimensoes')
    fig.colorbar(scatter, ax=ax, label='Complexidade Emergente')

    plt.tight_layout()
    
    # Salvar
    output_dir = create_output_directory()
    output_path = os.path.join(output_dir, 'habitability_map_3d.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"[OK] Mapa 3D salvo em: {output_path}")
    
    plt.close()
    return output_path

def generate_2d_habitability_map():
    """Gera o Mapa de Habitabilidade Temporal em 2D"""
    print("Gerando Mapa 2D de Habitabilidade Temporal...")
    
    # Eixos de tempo representando as três dimensões temporais
    t1 = np.linspace(0.01, 1, 100)
    t2 = np.linspace(0.01, 1, 100)
    t3 = np.linspace(0.01, 1, 100)
    T1, T2 = np.meshgrid(t1, t2)

    # Definimos a função de "complexidade emergente" como exemplo didático
    # (máxima quando t2 e t3 são moderados, t1 baixo)
    complexity = np.exp(-10 * (T1 - 0.3)**2) * np.exp(-10 * (T2 - 0.6)**2)

    # Criar o gráfico de contorno
    plt.figure(figsize=(8, 6))
    cp = plt.contourf(T1, T2, complexity, levels=20, cmap='viridis')
    plt.colorbar(cp, label='Indice de Complexidade Emergente')
    plt.xlabel('Tempo Quantico Local (t1)')
    plt.ylabel('Tempo Relacional Sistemico (t2)')
    plt.title('Mapa de Habitabilidade Temporal (t1 vs t2)\ncom t3 implicito como plano estavel')
    plt.scatter([0.1, 0.3, 0.5], [0.9, 0.6, 0.2], color='red')
    plt.text(0.1, 0.9, 'O-B', color='white')
    plt.text(0.3, 0.6, 'G (Sol)', color='white')
    plt.text(0.5, 0.2, 'M', color='white')
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.tight_layout()
    
    # Salvar
    output_dir = create_output_directory()
    output_path = os.path.join(output_dir, 'habitability_map_2d.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"[OK] Mapa 2D salvo em: {output_path}")
    
    plt.close()
    return output_path

def main():
    """Função principal"""
    print("=" * 60)
    print("Gerando Mapas de Habitabilidade Temporal CTMCK")
    print("=" * 60)
    
    try:
        # Gerar ambos os mapas
        path_3d = generate_3d_habitability_map()
        path_2d = generate_2d_habitability_map()
        
        print("=" * 60)
        print("[OK] Ambas as imagens foram geradas com sucesso!")
        print("Localizacao:")
        print(f"   - 3D: {path_3d}")
        print(f"   - 2D: {path_2d}")
        print("=" * 60)
        
        # Verificar se os arquivos existem
        if os.path.exists(path_3d) and os.path.exists(path_2d):
            print("Verificacao: Ambos os arquivos foram criados com sucesso!")
        else:
            print("Aviso: Nem todos os arquivos foram criados corretamente.")
        
    except Exception as e:
        print(f"[ERRO] Erro ao gerar imagens: {e}")

if __name__ == "__main__":
    main()