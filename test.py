# 1. Fresh clone
git clone https://dev.azure.com/YOUR_ORG/YOUR_PROJECT/_git/YOUR_REPO repo-clean
cd repo-clean

# 2. Rewrite only LuisBranch
git filter-repo --replace-text <(echo 'regex:password:"123"==>password:"<Brian_sandbox_password>"') --refs refs/heads/LuisBranch

# 3. Verify — should return nothing
git log LuisBranch -p | grep 'password:"123"'

# 4. Re-add remote and force push just that branch
git remote add origin https://dev.azure.com/YOUR_ORG/YOUR_PROJECT/_git/YOUR_REPO
git push origin LuisBranch --force