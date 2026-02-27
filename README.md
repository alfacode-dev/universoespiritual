# UniversoEspiritual

[![CI](https://github.com/alfacode-dev/universoespiritual/actions/workflows/ci.yml/badge.svg)](https://github.com/alfacode-dev/universoespiritual/actions/workflows/ci.yml)

Scaffold for the UniversoEspiritual project.

This is an initial project created by GitHub Copilot. It contains a minimal Python CLI in `src/main.py`.

Author
------

Roberto Navarro

Quick start

1. Create a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies (if any):

```bash
pip install -r requirements.txt
```

3. Run the CLI:

```bash
python -m src.main
# show version
python -m src.main --version
```

License
-------

This project is available under the MIT License — see the `LICENSE` file.

What's next

- Choose a framework (FastAPI/Flask for backend, React/Vue for frontend), or I can add tests and CI.

Tell me which direction you'd like to take and I'll continue scaffolding.
 
Run the FastAPI app

After installing dependencies (`pip install -r requirements.txt`) you can start the development server with:

```bash
uvicorn src.api.main:app --reload --host 127.0.0.1 --port 8000
```
API endpoints (high level):

- `POST /api/users` — create a user (body: `username`, `full_name`).
- `GET /api/users` — list users.
- `GET /api/items` — list items. Supports query params: `q` (search name), `limit`, `offset`.
- `POST /api/items` — create item (protected by token when `UNIVERSO_API_TOKEN` is set). Body: `name`, `description`, `owner_id`.
- `PUT /api/items/{id}` — update item (protected).
- `DELETE /api/items/{id}` — delete item (protected).

Token usage:

Set environment variable `UNIVERSO_API_TOKEN` to enable token-based protection. Provide header `Authorization: Bearer <token>` when making write requests.

Example (bash):

```bash
export UNIVERSO_API_TOKEN=secrettoken
curl -H "Authorization: Bearer $UNIVERSO_API_TOKEN" -X POST http://127.0.0.1:8000/api/items -d '{"name":"X"}' -H 'Content-Type: application/json'
```

Frontend (React) preview
-------------------------

I've scaffolded a small React + Vite frontend in the `frontend/` folder. To run it locally you need Node.js (>=16) and npm or yarn installed.

Install and run dev server:

```bash
cd frontend
npm install
npm run dev
```

By default the frontend proxies to `/api` on the same host (use the backend running at http://127.0.0.1:8000). You can set `VITE_API_BASE` in `.env` to point to a different API base URL.

Using SQL Server in production
-----------------------------

This project can use any SQL database supported by SQLAlchemy/SQLModel. To use Microsoft SQL Server in production, set the `DATABASE_URL` environment variable to a SQLAlchemy URL. Example format (ODBC driver 17):

```
DATABASE_URL="mssql+pyodbc://USER:PASSWORD@HOST:1433/DATABASE?driver=ODBC+Driver+17+for+SQL+Server"
```

Notes:
- You must install the `pyodbc` Python package (already in `requirements.txt`).
- The target host must have a suitable ODBC driver installed (e.g., `ODBC Driver 17 for SQL Server`). On Linux you may need `unixodbc` and the Microsoft ODBC driver; on macOS install the Microsoft ODBC driver via Homebrew. See https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
- When deploying with Docker or on your host, set `DATABASE_URL` in the environment (see `docker-compose.prod.yml` and `Procfile`).
- Alembic migrations will use `DATABASE_URL` when provided.

If you don't set `DATABASE_URL`, the app will use a local sqlite file `universo.db` for development.

Setting `DATABASE_URL` locally (example)
---------------------------------------

Create a `.env` file from the provided example and set your connection string (do NOT commit `.env`):

```bash
cp .env.example .env
# edit .env and set the real password (or paste the full URL-encoded string)
```

Or export directly in your shell (example using URL-encoded password):

```bash
export DATABASE_URL='mssql+pyodbc://sa:%24ys112177%23@alfacode.com.mx:1432/alfacodeuniversoactivo?driver=ODBC+Driver+17+for+SQL+Server'
export UNIVERSO_API_TOKEN='your_token_here'
.venv/bin/uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

Warning: the password in the example is URL-encoded; if you paste a password containing special characters (e.g., `#`, `$`, `?`, `@`) you must URL-encode them (e.g. `#` -> `%23`, `$` -> `%24`). Rotate credentials if they were shared inadvertently.


Then open http://127.0.0.1:8000/docs for the interactive API docs.

Run with Docker
---------------

Build and start the app with Docker Compose:

```bash
docker compose build
docker compose up
```

The API will be available at http://127.0.0.1:8000 and the docs at /docs.

Production with Docker
----------------------

Build the production image and run with Docker Compose (no volume mounts):

```bash
docker compose -f docker-compose.prod.yml build
docker compose -f docker-compose.prod.yml up -d
```

Check logs with:

```bash
docker compose -f docker-compose.prod.yml logs -f
```

To stop and remove containers:

```bash
docker compose -f docker-compose.prod.yml down
```