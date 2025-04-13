# Worksheet 1: Using Version Control with GitHub

## ✅ Initial Setup

- Repository cloned with:
  ```bash
  git clone https://github.com/SuhasThapa/osd-cw1.git
  ```

## 🌿 Branching and Development

- New branch created for scoring features:
  ```bash
  git checkout -b feature/scoring
  ```

- Added changes:
  ```bash
  git add yatzy.py
  git commit -m "Added Ones and Twos scoring methods"
  ```

- Pushed to GitHub:
  ```bash
  git push origin feature/scoring
  ```

## 🔄 Syncing and Merging

- Pulled latest changes:
  ```bash
  git pull origin main
  ```

- Merged feature branch:
  ```bash
  git checkout main
  git merge feature/scoring
  ```

> 📸 Screenshots attached in `/screenshots/`
