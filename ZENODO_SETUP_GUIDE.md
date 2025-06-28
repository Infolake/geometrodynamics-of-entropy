# Zenodo Setup Guide - CTMCK Theory

## 🎯 Objetivo
Obter DOI permanente para o repositório CTMCK via Zenodo, permitindo citação acadêmica adequada.

## ✅ Pré-requisitos (já atendidos)
- [x] Repositório público no GitHub: `https://github.com/Infolake/guilherme-ctmck`
- [x] Release v1.0.0 criada
- [x] Conteúdo científico organizado

## 📋 Passo-a-Passo

### 1. Acesse o Zenodo
- URL: https://zenodo.org/
- Clique em **"Log in"** (canto superior direito)
- Escolha **"Log in with GitHub"**
- Use suas credenciais do GitHub (`infolake`)

### 2. Conecte o Repositório
- Após login, vá para: https://zenodo.org/account/settings/github/
- Procure por `guilherme-ctmck` na lista
- **Toggle ON** o switch ao lado do repositório
- O repositório agora está conectado ao Zenodo

### 3. Crie um Release no GitHub (já feito)
- ✅ Tag v1.0.0 já criada e enviada
- O Zenodo detectará automaticamente novos releases

### 4. Configure Metadados no Zenodo
Quando o release for detectado, configure:

**Basic Information:**
- **Title**: "CTMCK Theory - Three-Temporal Bounce Cosmology"
- **Authors**: "Guilherme de Camargo"
- **Description**: "Comprehensive framework integrating three-dimensional time theory with black hole bounce cosmology"

**License:**
- **License**: MIT License

**Categories:**
- **Upload Type**: Software/Dataset
- **Access Right**: Open Access

**Additional Metadata:**
- **Keywords**: "cosmology, quantum gravity, three-dimensional time, JWST, neutrino mass"
- **Subject**: Physics and Astronomy
- **Language**: English

### 5. Obter o DOI
- Após configuração, clique **"Publish"**
- Zenodo gerará DOI no formato: `10.5281/zenodo.XXXXXX`
- Anote o DOI para atualizar README e citações

### 6. Atualizar Repositório
Após obter o DOI, atualize:
- `README.md`: Substituir `PENDING_ARXIV_ID` pelo DOI Zenodo
- `CITATION.cff`: Adicionar DOI
- `references.bib`: Incluir entrada Zenodo

## 🔄 Processo Automático
Uma vez configurado:
- Novos releases → Novos DOIs automaticamente
- Versionamento preservado
- Citações sempre atualizadas

## 📧 Notificações
O Zenodo enviará e-mail confirmando:
1. Repositório conectado
2. Release detectado
3. DOI gerado
4. Publicação confirmada

## 🎯 Resultado Final
- **DOI permanente** para citação acadêmica
- **Arquivo preservado** no Zenodo
- **Integração automática** com GitHub
- **Credibilidade científica** aumentada

## ⚠️ Importante
- Uma vez publicado no Zenodo, **não pode ser deletado**
- Apenas **metadados** podem ser editados posteriormente
- **Versionamento** permite atualizações futuras

---

**Status**: ✅ Repositório público e release v1.0.0 prontos
**Próximo passo**: Configurar conta Zenodo e conectar repositório 