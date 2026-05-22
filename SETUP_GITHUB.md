# GitHub Setup (Complete)

Your machine is configured and this project is published.

| Item | Value |
|------|-------|
| **GitHub account** | [RichEdd](https://github.com/RichEdd) |
| **Repository** | https://github.com/RichEdd/sourceclub-savings-analysis-demo |
| **Default branch** | `master` |
| **Protocol** | HTTPS (credentials via GitHub CLI) |

## Installed tools

- **Git** 2.54+ — `C:\Program Files\Git\cmd\git.exe`
- **GitHub CLI** 2.92+ — `gh`

## Push future changes

```powershell
cd C:\Users\rkedd\Projects\sourceclub-savings-analysis-demo
git add .
git commit -m "Describe your change"
git push
```

## If you sign out or switch machines

```powershell
gh auth login -h github.com -p https -w
gh auth setup-git
```

## Optional: rename default branch to `main`

```powershell
git branch -m master main
git push -u origin main
gh repo edit --default-branch main
```
