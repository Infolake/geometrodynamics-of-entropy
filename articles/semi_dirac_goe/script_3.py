# Compilar o PDF usando LaTeX
import subprocess
import os

# Verificar se os arquivos necessários existem
files_needed = ['semi_dirac_goe.tex', 'goe_dispersion.png', 'goe_arpes_compare.png', 'goe_fit_parameters.png']
for file in files_needed:
    if os.path.exists(file):
        print(f"✓ {file} encontrado")
    else:
        print(f"✗ {file} não encontrado")

# Tentar compilar o LaTeX
print("\nTentando compilar o LaTeX...")

try:
    # Primeiro passo de compilação
    result1 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'semi_dirac_goe.tex'], 
                           capture_output=True, text=True, timeout=30)
    print("Primeira compilação concluída.")
    
    # Segunda compilação (para resolver referências)
    result2 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'semi_dirac_goe.tex'], 
                           capture_output=True, text=True, timeout=30)
    print("Segunda compilação concluída.")
    
    # Verificar se o PDF foi criado
    if os.path.exists('semi_dirac_goe.pdf'):
        print("\n✓ PDF gerado com sucesso: semi_dirac_goe.pdf")
        
        # Mostrar tamanho do arquivo
        size = os.path.getsize('semi_dirac_goe.pdf')
        print(f"Tamanho do arquivo: {size/1024:.1f} KB")
        
    else:
        print("\n✗ Erro: PDF não foi gerado")
        if result2.stderr:
            print("Erros de compilação:")
            print(result2.stderr)
            
except subprocess.TimeoutExpired:
    print("Timeout na compilação do LaTeX")
except subprocess.CalledProcessError as e:
    print(f"Erro na compilação: {e}")
except FileNotFoundError:
    print("pdflatex não encontrado. Tentando método alternativo...")
    
    # Método alternativo usando Python
    try:
        import subprocess
        import sys
        
        # Verificar se temos latexmk
        result = subprocess.run(['latexmk', '--version'], capture_output=True)
        if result.returncode == 0:
            print("Usando latexmk...")
            subprocess.run(['latexmk', '-pdf', 'semi_dirac_goe.tex'], check=True)
            print("PDF gerado com latexmk!")
        else:
            print("LaTeX não disponível neste ambiente.")
            print("Arquivo .tex criado com sucesso. Para gerar o PDF:")
            print("1. Baixe o arquivo semi_dirac_goe.tex")
            print("2. Execute: pdflatex semi_dirac_goe.tex")
            print("3. Execute novamente: pdflatex semi_dirac_goe.tex")
            
    except Exception as e:
        print(f"Erro no método alternativo: {e}")
        print("\nArquivos criados:")
        print("- semi_dirac_goe.tex (arquivo LaTeX)")
        print("- goe_dispersion.png")
        print("- goe_arpes_compare.png")  
        print("- goe_fit_parameters.png")
        print("\nPara gerar o PDF, execute:")
        print("pdflatex semi_dirac_goe.tex")
        print("pdflatex semi_dirac_goe.tex")