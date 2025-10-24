
---
# Contributing to FastAPI Template

Thank you for your interest in contributing! 🙏
This document outlines the workflow and best practices for contributing to the FastAPI Template repository.

---

## 1️⃣ Branching & Workflow

We follow a **feature-branch + pull request** workflow to keep the `main` branch stable.

1. **Create a feature branch** from `main`:

```bash
git checkout main
git pull origin main
git checkout -b feature/my-new-feature
```

* Use descriptive names like `feature/add-auth` or `bugfix/fix-login`.

2. **Make your changes** on the feature branch.

3. **Run tests locally**:

```bash
uv run pytest
```

4. **Format your code** and check style:

```bash
uv run black .
uv run isort .
uv run flake8 .
```

5. **Push your branch** to GitHub:

```bash
git push origin feature/my-new-feature
```

6. **Open a Pull Request (PR)**

   * Target branch: `main`
   * Include a clear title and description
   * Link any related issues if applicable

7. **PR Review**

   * A maintainer (you) will review the changes before merging
   * Ensure tests pass locally and code is formatted correctly

8. **Merge PR**

   * Only maintainers can merge into `main`
   * Avoid direct commits to `main`

---

## 2️⃣ Code Standards

* **Python version**: 3.13+
* **Code style**: [Black](https://black.readthedocs.io/), [isort](https://pycqa.github.io/isort/)
* **Type checking**: [mypy](http://mypy-lang.org/)
* **Database models**: Use SQLModel
* **Password hashing**: Use **Argon2** (via Passlib) instead of bcrypt

---

## 3️⃣ Testing

* Unit tests should be in the `tests/` directory
* Run all tests before opening a PR:

```bash
uv run pytest
```

* Add new tests for new features or bug fixes

---

## 4️⃣ Commit Messages

Use **clear, concise messages**:

```
feat(auth): add JWT authentication
fix(user): validate email format
chore(deps): update FastAPI to latest version
```

* Optional: follow [Conventional Commits](https://www.conventionalcommits.org/)

---

## 5️⃣ Pull Request Guidelines

* Keep PRs **focused and small**
* Provide **context and description**
* Reference issues with `#<issue_number>`

---

## 6️⃣ Security & Secrets

* **Never commit secrets or credentials**
* Use `.env.example` for environment variables

---

## 7️⃣ Optional: Future CI Integration

* CI/GitHub Actions are **not yet configured**
* When added in the future, all PRs should pass automated checks (tests, linting, type checks) before merging

---

## 8️⃣ Additional Notes

* Keep the **main branch stable** — it should always be deployable
* Use `feature/` or `bugfix/` branches for any work
* Rebase your branch on `main` if needed before opening a PR:

```bash
git fetch origin
git rebase origin/main
```

---
