# UniversoEspiritual

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
-------------------

After installing dependencies (`pip install -r requirements.txt`) you can start the development server with:

```bash
uvicorn src.api.main:app --reload --host 127.0.0.1 --port 8000
```

Then open http://127.0.0.1:8000/docs for the interactive API docs.

Run with Docker
---------------

Build and start the app with Docker Compose:

```bash
docker compose build
docker compose up
```

The API will be available at http://127.0.0.1:8000 and the docs at /docs.