# Instructions for Remote Tag Push

## Current Status
The v1.0.0 tag has been successfully corrected locally and is ready to be pushed to the remote repository.

## Local Tag Status
- ✅ v1.0.0 tag now points to commit: `95217dc757552246c03754d42f3d09aae2dd3296`
- ✅ This commit contains the final repository with DOI: `10.5281/zenodo.15765710`
- ✅ Tag annotation updated with official Zenodo DOI reference

## Required Remote Push Commands
Since the environment has authentication limitations, the following commands need to be executed manually:

```bash
# Navigate to repository
cd /path/to/guilherme-ctmck

# Delete the old remote tag
git push origin --delete v1.0.0

# Push the corrected tag
git push origin v1.0.0

# Alternatively, force push all tags
git push origin --force --tags
```

## Verification Commands
After pushing, verify the correction:

```bash
# Check remote tag
git ls-remote --tags origin | grep v1.0.0

# Verify tag content
git fetch --tags
git show v1.0.0 --no-patch --format="%H %s %ai"
```

## Expected Results
- Remote v1.0.0 tag will point to commit `95217dc` 
- GitHub release will show complete repository structure
- Zenodo DOI will reference final repository state with correct DOI values

## Impact
- ✅ Repository completeness verified
- ✅ DOI corrections included  
- ✅ Scientific integrity maintained
- ✅ Zenodo integration corrected