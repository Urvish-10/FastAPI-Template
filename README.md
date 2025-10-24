# 🚀 FastAPI Template (with SQLModel + uv)

This repository serves as a **production-ready FastAPI template** built with:

* ⚡ **FastAPI** — a modern, high-performance web framework.
* 🧱 **SQLModel** — an elegant ORM powered by SQLAlchemy and Pydantic.
* ⚙️ **uv** — an ultra-fast package manager and virtual environment manager.
* 🧬 **Alembic** — for database migrations.
* 🔒 **JWT Authentication** scaffolding ready.
* 🧩 Clean and scalable folder structure for real-world APIs.

This template is designed for developers who want to **start FastAPI projects quickly** with best practices and modern tooling.

---

## 📂 Project Structure

```
FastAPI-Template/
├── app/
│   ├── api/               # API endpoints (routes)
│   ├── core/              # Config, environment, database, security, logging, etc.
│   ├── models/            # SQLModel database models
│   ├── schemas/           # Pydantic schemas for request/response validation
│   ├── utilities/          # CRUD operations and utils function logics
│   ├── main.py            # FastAPI app entry point
│   └── __init__.py
├── alembic/               # Alembic migration files
├── tests/                 # Unit and integration tests
├── .env                   # Environment variables
├── pyproject.toml          # Project dependencies (managed by uv)
└── README.md
```

---

## ⚙️ Prerequisites

Make sure you have:

* [Python 3.13+](https://www.python.org/downloads/)
* [uv](https://github.com/astral-sh/uv)
* PostgreSQL (or SQLite for local development)

---

## 🧰 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Urvish-10/FastAPI-Template.git
cd FastAPI-Template
```

### 2️⃣ Create and Activate Virtual Environment

```bash
uv venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
uv sync
```

---

## 🧾 Environment Variables

Create a `.env` file in the project root:

```
PROJECT_NAME=FastAPI Template
API_PREFIX=/api
DEBUG=True
DATABASE_URL=sqlite:///./test.db
ACCESS_TOKEN_EXPIRE_MINUTES=60
SECRET_KEY=your-secret-key
ALGORITHM=HS256
```

---

## 🧠 Quick Start (Run the Server)

```bash
uvicorn app.main:app --reload
```

Now visit: 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)
You should see:

```json
{"message": "Welcome to FastAPI Template!"}
```

Interactive API Docs:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🗄️ Database Setup (SQLModel + Alembic)

### Initialize Alembic

```bash
alembic init alembic
```

### Configure Alembic

In `alembic.ini`, update:

```
sqlalchemy.url = sqlite:///./test.db
```

### Create and Apply Migration

```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

---

## 🧩 Example: Basic Model + API

**app/models/user.py**

```python
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
```

**app/api/routes/user.py**

```python
from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

@router.get("/")
def get_users():
    return [{"id": 1, "name": "John Doe"}]
```

**app/main.py**

```python
from fastapi import FastAPI
from app.api.routes import user

app = FastAPI(title="FastAPI Template")
app.include_router(user.router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Template!"}
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📦 Dependency Management (via uv)

| Command             | Description                   |
| ------------------- | ----------------------------- |
| `uv add fastapi`    | Add a new dependency          |
| `uv remove fastapi` | Remove a dependency           |
| `uv sync`           | Sync venv with pyproject.toml |
| `uv run <cmd>`      | Run a command inside venv     |

---

## 🧱 Common Commands

| Task               | Command                                     |
| ------------------ | ------------------------------------------- |
| Run API            | `uvicorn app.main:app --reload`             |
| Format code        | `uv run black .`                            |
| Run tests          | `uv run pytest`                             |
| Generate migration | `alembic revision --autogenerate -m "desc"` |
| Apply migration    | `alembic upgrade head`                      |

---

## 🚀 Deployment Notes

Use **Gunicorn + Uvicorn workers** for production:

```bash
gunicorn app.main:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

### Recommended Setup

* Use `.env` or environment variables for configuration.
* Set `DEBUG=False` in production.
* Use **Nginx** or **Caddy** as a reverse proxy.

---

## 📘 Documentation

* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [SQLModel Docs](https://sqlmodel.tiangolo.com/)
* [uv Docs](https://docs.astral.sh/uv/)
* [Alembic Docs](https://alembic.sqlalchemy.org/)

---

## 🤝 Contribution

We welcome contributions from the community! Whether it's bug fixes, new features, documentation improvements, or suggesting enhancements, please feel free to contribute.

Please read our [Contribution Guidelines](CONTRIBUTION.md) before submitting pull requests or opening issues.


---


## 🧑‍💻 Author

**Urvish Bhatt**
Software Engineer — Python | FastAPI | Django | DRF | AI | Agents | R&D Robotics

---

## 🏁 License

This project is licensed under the **MIT License** — feel free to use, fork, and modify it.
