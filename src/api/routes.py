from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from src.db import get_session
from src.models import Item as ItemModel
from .schemas import ItemCreate, ItemRead

router = APIRouter()


@router.get("/", tags=["root"])
async def read_root():
    return {"message": "Bienvenido a UniversoEspiritual API"}


@router.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}


@router.post("/items", response_model=ItemRead, tags=["items"])
def create_item(item: ItemCreate, session=Depends(get_session)):
    db_item = ItemModel(**item.dict())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.get("/items", response_model=List[ItemRead], tags=["items"])
def list_items(session=Depends(get_session)):
    items = session.exec(select(ItemModel)).all()
    return items


@router.get("/items/{item_id}", response_model=ItemRead, tags=["items"])
def get_item(item_id: int, session=Depends(get_session)):
    item = session.get(ItemModel, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/items/{item_id}", response_model=ItemRead, tags=["items"])
def update_item(item_id: int, item: ItemCreate, session=Depends(get_session)):
    db_item = session.get(ItemModel, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.delete("/items/{item_id}", status_code=204, tags=["items"])
def delete_item(item_id: int, session=Depends(get_session)):
    item = session.get(ItemModel, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return None
