#!/usr/bin/env bash
# CTMCK Update DOI Script - Atualiza badges após receber DOI do Zenodo
# Usage: ./update_doi.sh 10.5281/zenodo.1234567 2501.00001
# Author: Dr. Guilherme de Camargo – 26 Jan 2025

set -euo pipefail

# Verifica argumentos
if [ $# -ne 2 ]; then
    echo "❌ Uso: $0 <zenodo_doi> <arxiv_id>"
    echo "   Exemplo: $0 10.5281/zenodo.1234567 2501.00001"
    exit 1
fi

ZENODO_DOI="$1"
ARXIV_ID="$2"

echo "🔄 Atualizando badges com:"
echo "   📊 Zenodo DOI: $ZENODO_DOI"
echo "   📄 arXiv ID: $ARXIV_ID"

# Backup dos arquivos
echo "💾 Criando backup..."
cp README.md README.md.bak
cp CITATION.cff CITATION.cff.bak

# Atualizar README.md
echo "📝 Atualizando README.md..."
sed -i "s|zenodo\.PENDING|$ZENODO_DOI|g" README.md
sed -i "s|arXiv-PENDING|arXiv-$ARXIV_ID|g" README.md
sed -i "s|arXiv:PENDING|arXiv:$ARXIV_ID|g" README.md
sed -i "s|https://arxiv.org/abs/PENDING|https://arxiv.org/abs/$ARXIV_ID|g" README.md

# Atualizar CITATION.cff
echo "📝 Atualizando CITATION.cff..."
sed -i "s|# doi: 10.5281/zenodo.PENDING|doi: $ZENODO_DOI|g" CITATION.cff
sed -i "s|# doi: \"10.48550/arXiv.XXXX.XXXXX\"|doi: \"10.48550/arXiv.$ARXIV_ID\"|g" CITATION.cff

# Atualizar outros arquivos se necessário
if [ -f "github_profile_README.md" ]; then
    echo "📝 Atualizando github_profile_README.md..."
    sed -i "s|zenodo\.PENDING|$ZENODO_DOI|g" github_profile_README.md
    sed -i "s|arXiv:PENDING|arXiv:$ARXIV_ID|g" github_profile_README.md
fi

# Verificar mudanças
echo "🔍 Verificando mudanças..."
if git diff --quiet README.md CITATION.cff; then
    echo "⚠️ Nenhuma mudança detectada. Verifique se os placeholders estavam corretos."
else
    echo "✅ Mudanças detectadas:"
    git diff --name-only README.md CITATION.cff
fi

# Confirmar commit
echo ""
echo "📋 PRÓXIMO PASSO:"
echo "   Revise as mudanças e execute:"
echo "   git add README.md CITATION.cff github_profile_README.md"
echo "   git commit -m 'Add Zenodo DOI and arXiv ID badges'"
echo "   git push"
echo ""
echo "🎯 Ou execute automaticamente:"
read -p "   Fazer commit automaticamente? (s/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    git add README.md CITATION.cff github_profile_README.md 2>/dev/null || true
    git commit -m "Add Zenodo DOI ($ZENODO_DOI) and arXiv ID ($ARXIV_ID) badges"
    git push
    echo "✅ Badges atualizados e commitados!"
else
    echo "ℹ️ Commit manual necessário."
fi

echo ""
echo "🎉 DOIs atualizados com sucesso!"
echo "🔗 Zenodo: https://doi.org/$ZENODO_DOI"
echo "📄 arXiv: https://arxiv.org/abs/$ARXIV_ID" 