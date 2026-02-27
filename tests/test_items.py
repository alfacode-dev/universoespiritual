from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session

from src.api.main import app
from src.db import get_session
from src.models import Item as ItemModel


TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})


def override_get_session():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_session] = override_get_session
client = TestClient(app)


def test_crud_item():
    # create
    resp = client.post("/api/items", json={"name": "Prueba", "description": "desc"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] is not None
    item_id = data["id"]

    # get
    resp = client.get(f"/api/items/{item_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "Prueba"

    # list
    resp = client.get("/api/items")
    assert resp.status_code == 200
    items = resp.json()
    assert isinstance(items, list) and len(items) >= 1

    # update
    resp = client.put(f"/api/items/{item_id}", json={"id": item_id, "name": "Mod", "description": "nuevo"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "Mod"

    # delete
    resp = client.delete(f"/api/items/{item_id}")
    assert resp.status_code == 204

    # not found
    resp = client.get(f"/api/items/{item_id}")
    assert resp.status_code == 404
