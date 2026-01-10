# Contributing to Shorty 🔗

Thanks for checking out **Shorty**, a simple URL shortener built with Python. This guide is written for beginners who are learning **Git, GitHub, and Python**, so don’t worry, I've kept things clear and practical.

---

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** to your local machine

   ```bash
   git clone https://github.com/mrjxtr/shorty.git
   # or
   git clone git@github.com:mrjxtr/shorty.git

   cd shorty
   ```

3. **Switch to the dev branch**

   ```bash
   git checkout dev
   ```

4. **Create a new branch from dev**

   ```bash
   git checkout -b <type>/<shortDescription>
   ```

You should always start your work from `dev`, **never from `main`**.

---

## Branch Naming

Branch names should be **short, clear, and consistent**. Use one of the allowed types as a prefix.

### Allowed Types

- `feat`
- `style`
- `update`
- `refactor`
- `perf`
- `fix`
- `chore`
- `docs`

### Format

```
<type>/<shortDescription>
```

✅ Preferred style (short & readable):

- `feat/addCustomAlias`
- `fix/redirectBug`
- `docs/updateReadme`

CamelCase is fine after the slash. Keep it **as short as possible**.

✅ Alternative style (if you preffer):

- `feat/add-custom-alias`
- `fix/redirect-bug`
- `docs/update-readme`

---

## Virtual Environment & Dependencies

Before running or changing the project, always use a **virtual environment**.

### Create & Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
# or
.venv\Scripts\activate     # Windows
```

Make sure your virtual environment is activated before installing or running anything.

### Dependencies (requirements.txt)

- Install dependencies using:

  ```bash
  pip install -r requirements.txt
  ```

- **If you add a new dependency**, you MUST update `requirements.txt`:

  ```bash
  pip freeze > requirements.txt
  ```

Keeping `requirements.txt` up to date ensures others can run the project without issues.

---

## Commit Messages

Commit messages should follow the **same types as branch naming** and be **short**.

### Format

```
<type>: short description
```

### Examples

- `feat: add url validation`
- `fix: redirect logic`
- `docs: update readme`
- `refactor: simplify handler`

Rules:

- Use lowercase for the description
- No punctuation at the end
- Say _what_ changed, not _how_ you felt

---

## Pull Request (PR) Titles ✅ (Important)

Pull Request titles follow the **same idea**, but the type must be **UPPERCASE**.

### Format

```
<TYPE>: short, clear description
```

### Examples

- `FEAT: add custom alias`
- `FIX: redirect logic`
- `DOCS: update setup guide`
- `REFACTOR: clean up redirect handler`

Rules:

- TYPE must be capitalized
- Keep it one line
- If it feels long, it _is_ long

---

## Pull Request Description

Every PR must include a **short description**.

Answer these in 1–3 bullet points:

- What is this PR about?
- What was changed?
- Anything reviewers should know?

Keep it simple. No essays.

---

## Pre-Pull Request Checklist ✅

This checklist exists to help you **avoid common beginner mistakes**. Complete everything before opening a PR.

Before opening a PR to `dev`, make sure all of these are true:

- [ ] I did **not** work directly on `main`
- [ ] My branch was created from `dev`
- [ ] Code runs **without errors**
- [ ] App starts and works as expected
- [ ] New dependencies (if any) are added to `requirements.txt`
- [ ] Commit messages follow the correct format
- [ ] PR title follows the correct format
- [ ] PR has a short, clear description

If any box is unchecked, fix it **before** requesting review.

---

## Branching Rules

These rules are **non-negotiable**:

- ❌ **Never push directly to `main`**
- ❌ Never open a PR directly into `main`
- ✅ Always branch from `dev`
- ✅ Always open Pull Requests **into `dev`**

`main` is reserved for stable, reviewed code only.

---

## Pull Request Description

In the PR description, answer any or all of these:

- **What did you change?**
- **Why did you change it?**
- **How can it be tested?** (if applicable)

Keep it short. Bullet points are fine.

---

## Code Guidelines

- Keep functions **small and readable**
- Use **clear variable names**
- Prefer **simple Python** over clever Python
- If you’re unsure, add a comment

This is a learning project, clarity beats cleverness.

---

## Asking for Help

If you’re stuck:

- Ask questions
- Explain what you tried

That’s part of learning. Totally fine 👍

---

## Final Notes

- One PR = one focused change
- Small PRs are better than big ones
- Don’t be afraid to make mistakes, that’s how you learn

Happy coding ✨
