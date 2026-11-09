# TaskFlow API

A small Flask REST API for practicing GitHub Actions and Docker CI/CD.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -r requirements-dev.txt
python run.py
```

API base URL: `http://localhost:5000`

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/tasks` | List tasks |
| POST | `/tasks` | Create a task; JSON: `{"title":"Example"}` |
| PATCH | `/tasks/<id>` | Update title and/or done |
| DELETE | `/tasks/<id>` | Delete a task |

## Run tests and lint

```bash
pytest -q
ruff check .
```

## Build and run with Docker

```bash
docker build -t taskflow-api:local .
docker run --rm -p 5000:5000 taskflow-api:local
```

The task list is stored in memory and resets when the application restarts. This is intentional for this CI/CD training project.
