# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2026-02-27

- Add `User` model and ownership relation for `Item` (`owner_id`).
- Add token-based write protection via `UNIVERSO_API_TOKEN` and dependency `src/api/deps.py`.
- Add pagination and name search to `GET /api/items` (`q`, `limit`, `offset`).
- Replace FastAPI startup event with `lifespan` handler.
- Add tests for users and auth (`tests/test_users.py`).
- Add Alembic scaffolding and `alembic.ini` / `alembic/env.py`.
- Add simple logging config and initialize from app startup.
- Update README with new endpoints and token usage.

## [0.1.0] - initial

- Initial scaffold with FastAPI, SQLModel, CRUD for `Item`, basic tests and CI.
