# Worksheet 2: GitHub Actions for Automation

## ⚙️ CI/CD Setup

- GitHub Actions enabled via:
  `.github/workflows/python-app.yml`

- This runs on pushes and PRs to `main`
- It checks out code, sets up Python, and runs:
  ```bash
  python -m unittest discover
  ```

## ✅ Benefits

- Ensures tests pass before merging
- Prevents broken code in `main`
- Encourages clean, modular development

## 📸 Evidence

- Action run screenshot showing success
- PR screenshot showing automatic checks
