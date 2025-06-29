# Zenodo Setup Guide - CTMCK Theory

## 🎯 Objective
Obtain permanent DOI for the CTMCK repository via Zenodo, enabling proper academic citation.

## ✅ Prerequisites (already met)
- [x] Public GitHub repository: `https://github.com/Infolake/guilherme-ctmck`
- [x] Release v1.0.0 created
- [x] Scientific content organized

## 📋 Step-by-Step

### 1. Access Zenodo
- URL: https://zenodo.org/
- Click **"Log in"** (upper right corner)
- Choose **"Log in with GitHub"**
- Use your GitHub credentials (`infolake`)

### 2. Connect Repository
- After login, go to: https://zenodo.org/account/settings/github/
- Search for `guilherme-ctmck` in the list
- **Toggle ON** the switch next to the repository
- Repository is now connected to Zenodo

### 3. Create GitHub Release (already done)
- ✅ Tag v1.0.0 already created and pushed
- Zenodo will automatically detect new releases

### 4. Configure Metadata in Zenodo
When the release is detected, configure:

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