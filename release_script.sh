#!/usr/bin/env bash
# CTMCK Release Script – Zenodo + arXiv workflow
# Author: Dr. Guilherme de Camargo – 26 Jan 2025

set -euo pipefail        # falha se qualquer comando falhar
TAG=v0.1                 # versão
BRANCH=main

echo "🚀 CTMCK Release workflow"

# 1. Garante estar no branch correto
git rev-parse --abbrev-ref HEAD | grep -qx "$BRANCH" || {
  echo "❌ Saia do branch $(git rev-parse --abbrev-ref HEAD) e volte ao '$BRANCH'"; exit 1; }

echo "📥 git pull origin $BRANCH"
git pull origin "$BRANCH"

# 2. Testa placeholders pendentes
if grep -R --line-number -E 'zenodo\.PENDING|arXiv:PENDING|\[USERNAME\]' . --exclude-dir=.git --exclude="*.sh"; then
  echo "❌ Ainda existem placeholders PENDING ou [USERNAME]. Corrija antes do release."; exit 1;
fi

# 3. Adiciona arquivos modificados (se houver)
echo "📝 git add ."
git add -A
if git diff --cached --quiet; then
  echo "ℹ️ Nenhuma alteração a commitar."
else
  echo "💾 Commit final…"
  git commit -m "Final preparation for ${TAG} release

• CITATION.cff ready for DOI
• Docs + analyses final  
• Prepared for arXiv upload"
  git push origin "$BRANCH"
fi

# 4. Cria e envia TAG (só se ainda não existir)
if git rev-parse "$TAG" >/dev/null 2>&1; then
  echo "ℹ️ Tag ${TAG} já existe – omitindo criação."; 
else
  echo "🏷️ Criando tag ${TAG}"
  git tag -a "$TAG" -m "CTMCK ${TAG}: First public release

Features:
- Complete CTMCK theory implementation  
- Stellar temporal habitability analysis
- 2D/3D habitability visualizations
- Observable predictions for JWST/LISA
- Comprehensive documentation

This release corresponds to the arXiv preprint submission."
  git push origin "$TAG"
fi

echo "⏳ Aguarde o e-mail do Zenodo com o DOI (5-10 min)."
echo "🔗 Depois edite CITATION.cff e README para incluir 10.5281/zenodo.XXXXXX"
echo "📄 Em seguida faça:"
echo "    git commit -am 'Add Zenodo DOI badge' && git push"
echo ""
echo "📧 PRÓXIMOS PASSOS:"
echo "1. ✅ Tag criada - Zenodo gerará DOI automaticamente"
echo "2. 📧 Aguardar email do Zenodo (5-10 min)"
echo "3. 🔗 Atualizar badges com DOI real"
echo "4. 📄 Submeter ao arXiv usando arxiv_abstract.txt"
echo "5. 📨 Enviar email para Kletetschka"
echo ""
echo "🌟 Zenodo: https://zenodo.org/account/settings/github"
echo "📊 GitHub releases: https://github.com/infolake/guilherme-ctmck/releases"
echo ""
echo "✅ Processo de release concluído!" 