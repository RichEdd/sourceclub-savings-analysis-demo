# GitHub Setup

Run these commands from the project folder after [Git](https://git-scm.com/download/win) and [GitHub CLI](https://cli.github.com/) are installed.

```powershell
cd C:\Users\rkedd\Projects\sourceclub-savings-analysis-demo

git init
git add .
git commit -m "Add Source Club savings analysis demo prototype"

# Create public repo (change visibility or name as needed)
gh repo create sourceclub-savings-analysis-demo --public --source=. --remote=origin --push --description "Lightweight AI-assisted savings analysis prototype for dental procurement workflows using fuzzy product matching and automated savings calculations."
```

If the repo name is taken, pick another name:

```powershell
gh repo create YOUR-USERNAME/sourceclub-savings-demo --public --source=. --remote=origin --push
```

Then update the repo URL in `EXECUTIVE_SUMMARY.md` if needed.
