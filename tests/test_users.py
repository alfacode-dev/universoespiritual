from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import StaticPool
import os

from src.api.main import app
from src.db import get_session


TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


def override_get_session():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_session] = override_get_session
client = TestClient(app)


def test_user_and_item_auth(monkeypatch):
    # set API token for this test
    monkeypatch.setenv("UNIVERSO_API_TOKEN", "test-token")

    # create user
    resp = client.post("/api/users", json={"username": "alice", "full_name": "Alice"})
    assert resp.status_code == 200
    user = resp.json()
    assert user["username"] == "alice"

    # attempt to create item without auth -> should be 401
    resp = client.post("/api/items", json={"name": "Item1", "description": "desc"})
    assert resp.status_code == 401

    # create item with auth
    headers = {"Authorization": "Bearer test-token"}
    resp = client.post("/api/items", json={"name": "Item1", "description": "desc", "owner_id": user["id"]}, headers=headers)
    assert resp.status_code == 200
    item = resp.json()
    assert item["name"] == "Item1"
