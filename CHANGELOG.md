# CHANGELOG

## [v0.1.1-en] - 2025-06-28

### 🌍 Full English Internationalization
- **BREAKING**: Complete repository conversion to English
- All code, documentation, and plot labels now in English
- Portuguese content removed from all files

### 📝 Documentation
- `README.md`: Updated repository structure, fixed LICENSE link
- `PROJECT_INDEX.md`: Complete English translation
- `ZENODO_SETUP_GUIDE.md`: Internationalized setup instructions
- `scripts/README.md`: Full English conversion

### 💻 Code Changes
- `scripts/analysis/stellar_temporal_correlation.py`: Complete rewrite in English
  - Professional English docstrings and comments
  - Fixed absolute paths using relative project root
  - Enhanced analysis output with clear English descriptions
- `scripts/plotting/generate_habitability_maps.py`: Full English conversion
  - All plot labels and print messages in English
  - Fixed comment "Sol" → "Sun"
- `scripts/plotting/habitability_map_plot.py`: Complete internationalization
  - Function comments and plot labels in English
  - "Anã Vermelha" → "Red Dwarf", "Sol" → "Sun"

### 🎨 Figures
- Regenerated all temporal habitability maps with English labels
- `habitability_map_2d.png`: English axes and titles
- `habitability_map_3d.png`: English dimensional labels
- `stellar_temporal_correlations.png`: Complete English visualization

### 🧪 Testing
- Added `tests/english_lint.py` for automated language compliance
- Repository now passes English-only content validation

### 🛠️ Infrastructure
- Created `LICENSE` file (MIT License)
- Updated `.gitignore` with English comments
- Fixed all file references in documentation

### 📊 Data
- Updated `stellar_temporal_correlations.csv` with English headers
- All processed datasets now use English column names

---

## [v0.1.1] - 2025-06-26

### 🧹 Repository Cleanup
- Removed 22 unnecessary files
- Streamlined structure to 12 essential files
- Updated project documentation

### 📄 Core Files
- Maintained scientific manuscript `ctmck_article_v0.1b.tex`
- Preserved essential analysis scripts and figures
- Kept complete bibliography `references.bib`

---

## [v1.0.0] - 2025-01-26

### 🎉 Initial Release
- Complete CTMCK theoretical framework
- Stellar-temporal correlation analysis
- Scientific manuscript ready for submission
- Full documentation and reproducible results
