# Worksheet 3: Using GitHub Issues

## 👥 Collaboration

- Rupesh dulal identified a bug with the `FullHourse()`
- Issue created: **"FullHourse() fails with reverse order inputs"**

## 🔧 Fix Process

- Created fix branch:
  ```bash
  git checkout -b fix/fullhouse-bug
  ```

- Applied fix, committed, and linked issue:
  ```bash
  git commit -m "Fix: FullHourse handles all valid combos. Fixes #3"
  ```

- Opened PR → GitHub Actions passed → Merged


## 🤔 Reflections

- Important to write clear issues and link them
- Peer code review is powerful for catching logic bugs
