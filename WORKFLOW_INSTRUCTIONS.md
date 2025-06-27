# 🚀 CTMCK Release Workflow Instructions

## 📋 **Complete Release Process**

### **✅ Prerequisites Checklist**

Before running the release script, ensure:

- [ ] ✅ All placeholders `[USERNAME]` replaced with your GitHub username
- [ ] ✅ All `PENDING` placeholders ready for replacement  
- [ ] ✅ Zenodo account created and connected to GitHub
- [ ] ✅ Repository toggle activated in Zenodo settings
- [ ] ✅ Repository is PUBLIC (Zenodo only works with public repos)
- [ ] ✅ You are on the `main` branch
- [ ] ✅ All files committed and pushed

---

## 🖥️ **Platform-Specific Instructions**

### **Windows (PowerShell)**
```powershell
# Make scripts executable (if needed)
# Scripts should work directly in PowerShell

# Run release script
bash ./release_script.sh

# After getting Zenodo DOI and arXiv ID:
bash ./update_doi.sh 10.5281/zenodo.1234567 2501.00001
```

### **Linux/Mac (Bash)**
```bash
# Make scripts executable
chmod +x release_script.sh update_doi.sh

# Run release script
./release_script.sh

# After getting Zenodo DOI and arXiv ID:
./update_doi.sh 10.5281/zenodo.1234567 2501.00001
```

---

## 🔄 **Step-by-Step Release Process**

### **Step 1: Pre-Release Verification**
The `release_script.sh` will automatically check:
- ✅ You're on the `main` branch
- ✅ No PENDING or [USERNAME] placeholders remain
- ✅ All changes are committed
- ✅ Tag doesn't already exist

### **Step 2: Execute Release**
```bash
# Windows
bash ./release_script.sh

# Linux/Mac  
./release_script.sh
```

**What the script does:**
1. 📥 Pulls latest changes from GitHub
2. 🔍 Checks for placeholder strings that need updating
3. 📝 Commits any final changes (if needed)
4. 🏷️ Creates and pushes v0.1 tag
5. ⏳ Triggers Zenodo DOI generation

### **Step 3: Wait for Zenodo Email (5-10 minutes)**
You'll receive an email like:
```
Subject: DOI 10.5281/zenodo.1234567 has been registered for ...
Your upload has been published with DOI: 10.5281/zenodo.1234567
```

### **Step 4: Update DOI Badges**
```bash
# Replace with your actual DOI and arXiv ID
./update_doi.sh 10.5281/zenodo.1234567 2501.00001
```

**What this script does:**
1. 💾 Creates backup of files
2. 🔄 Replaces all PENDING placeholders with real values
3. ✅ Shows you the changes made
4. 📝 Optionally commits and pushes changes

### **Step 5: Submit to arXiv**
1. Go to: https://arxiv.org/submit
2. Use content from `arxiv_abstract.txt` (exactly 150 words)
3. Primary category: `gr-qc` 
4. Secondary category: `astro-ph.CO`
5. Upload your LaTeX/PDF files

### **Step 6: Communicate Results**
1. 📧 Send email to Kletetschka using `email_kletetschka_template.txt`
2. 📱 Post on social media using `press_release_template.txt`
3. 🔗 Update your profiles with the new links

---

## 🛠️ **Script Details**

### **release_script.sh Features**
- ✅ **Branch protection**: Only runs on `main` branch
- ✅ **Placeholder detection**: Fails if PENDING/[USERNAME] found
- ✅ **Idempotent**: Safe to run multiple times
- ✅ **Smart commits**: Only commits if changes exist
- ✅ **Tag protection**: Won't overwrite existing tags

### **update_doi.sh Features**  
- ✅ **Automatic backup**: Creates .bak files before changes
- ✅ **Multi-file update**: Updates README, CITATION.cff, profile
- ✅ **Change verification**: Shows what was modified
- ✅ **Interactive commit**: Asks before pushing changes

---

## 🚨 **Troubleshooting**

### **"Branch check failed"**
```bash
git checkout main
git pull origin main
./release_script.sh
```

### **"Placeholders still exist"**
Search and replace manually:
```bash
# Find all instances
grep -r "PENDING\|USERNAME" . --exclude-dir=.git

# Replace in specific files
sed -i 's/\[USERNAME\]/yourusername/g' README.md
```

### **"Tag already exists"**
If you need to recreate:
```bash
git tag -d v0.1              # Delete local tag
git push origin :refs/tags/v0.1  # Delete remote tag
./release_script.sh          # Run again
```

### **"Zenodo not triggering"**
Check:
1. Repository is PUBLIC
2. Zenodo toggle is ON at: https://zenodo.org/account/settings/github
3. Tag was actually pushed: `git ls-remote --tags origin`

---

## 📋 **Files Modified by Scripts**

### **release_script.sh modifies:**
- Git repository (creates tag, commits)
- GitHub (pushes tag and commits)

### **update_doi.sh modifies:**
- `README.md` - Updates DOI and arXiv badges
- `CITATION.cff` - Uncomments and fills DOI fields
- `github_profile_README.md` - Updates profile links

---

## 🎯 **Final Verification**

After completing all steps, verify:
- [ ] ✅ GitHub shows v0.1 release with correct date
- [ ] ✅ Zenodo page displays your repository snapshot  
- [ ] ✅ README badges show real DOI/arXiv numbers (not PENDING)
- [ ] ✅ arXiv preprint is live and accessible
- [ ] ✅ All links in documentation work correctly

---

## 🏆 **Success Metrics**

You'll know everything worked when:
- 🌟 **GitHub**: Repository has official v0.1 release
- 📊 **Zenodo**: DOI resolves to your project page
- 📄 **arXiv**: Preprint is searchable and citable  
- 🔗 **Badges**: All show green/working status
- 📧 **Email**: Kletetschka receives your message with working links

**Congratulations! Your CTMCK theory is now officially published and citable! 🎉** 