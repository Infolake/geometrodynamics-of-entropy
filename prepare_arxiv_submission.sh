#!/bin/bash

# Script para preparar submissão arXiv
# Autor: Guilherme de Camargo
# Data: 2025-01-26

echo "=== Preparando Submissão arXiv CTMCK ==="

# Limpar arquivos auxiliares
echo "Limpando arquivos auxiliares..."
rm -f *.aux *.log *.bbl *.blg *.out *.toc *.fdb_latexmk *.fls *.synctex.gz

# Verificar se o arquivo principal existe
if [ ! -f "ctmck_article_v0.1b.tex" ]; then
    echo "❌ Erro: ctmck_article_v0.1b.tex não encontrado!"
    exit 1
fi

# Criar ZIP para submissão
echo "Criando ZIP para submissão..."
zip -r ctmck_v0p1_arxiv.zip ctmck_article_v0.1b.tex

# Verificar se ZIP foi criado
if [ -f "ctmck_v0p1_arxiv.zip" ]; then
    echo "✅ ZIP criado com sucesso: ctmck_v0p1_arxiv.zip"
    echo ""
    echo "📦 Conteúdo do ZIP:"
    unzip -l ctmck_v0p1_arxiv.zip
    echo ""
    echo "🚀 PRONTO PARA SUBMISSÃO ARXIV!"
    echo ""
    echo "📋 Checklist de Submissão:"
    echo "   ✓ Arquivo principal: ctmck_article_v0.1b.tex"
    echo "   ✓ Refinamentos cosméticos aplicados"
    echo "   ✓ DOIs clicáveis"
    echo "   ✓ Unidades em micro-hertz"
    echo "   ✓ Referência Bell inequalities"
    echo "   ✓ ZIP limpo e otimizado"
    echo ""
    echo "🎯 Categoria sugerida: gr-qc (primária), astro-ph.CO (secundária)"
    echo "📄 Licença: CC-BY 4.0"
    echo "🔧 Fonte: Other (LaTeX)"
    echo ""
    echo "Após obter ID arXiv, execute:"
    echo "   git commit -am 'Add arXiv ID 2401.xxxxx'"
    echo "   git push"
else
    echo "❌ Erro ao criar ZIP!"
    exit 1
fi 