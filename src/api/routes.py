from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select

from src.db import get_session
from src.models import Item as ItemModel, User as UserModel
from .schemas import ItemCreate, ItemRead, UserCreate, UserRead
from .deps import get_api_token

router = APIRouter()


@router.get("/", tags=["root"])
async def read_root():
    return {"message": "Bienvenido a UniversoEspiritual API"}


@router.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}


@router.post("/users", response_model=UserRead, tags=["users"])
def create_user(user: UserCreate, session=Depends(get_session)):
    # naive uniqueness check
    existing = session.exec(select(UserModel).where(UserModel.username == user.username)).first()
    if existing:
        raise HTTPException(status_code=400, detail="username already exists")
    db_user = UserModel(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get("/users", response_model=List[UserRead], tags=["users"])
def list_users(session=Depends(get_session)):
    users = session.exec(select(UserModel)).all()
    return users


@router.post("/items", response_model=ItemRead, tags=["items"])
def create_item(item: ItemCreate, session=Depends(get_session), authorized=Depends(get_api_token)):
    # name uniqueness
    existing = session.exec(select(ItemModel).where(ItemModel.name == item.name)).first()
    if existing:
        raise HTTPException(status_code=400, detail="item with this name already exists")
    db_item = ItemModel(**item.model_dump())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.get("/items", response_model=List[ItemRead], tags=["items"])
def list_items(q: Optional[str] = Query(None), limit: int = Query(100, ge=1, le=1000), offset: int = 0, session=Depends(get_session)):
    stmt = select(ItemModel)
    if q:
        stmt = stmt.where(ItemModel.name.contains(q))
    stmt = stmt.limit(limit).offset(offset)
    items = session.exec(stmt).all()
    return items


@router.get("/items/{item_id}", response_model=ItemRead, tags=["items"])
def get_item(item_id: int, session=Depends(get_session)):
    item = session.get(ItemModel, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/items/{item_id}", response_model=ItemRead, tags=["items"])
def update_item(item_id: int, item: ItemCreate, session=Depends(get_session), authorized=Depends(get_api_token)):
    db_item = session.get(ItemModel, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description
    db_item.owner_id = item.owner_id
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.delete("/items/{item_id}", status_code=204, tags=["items"])
def delete_item(item_id: int, session=Depends(get_session), authorized=Depends(get_api_token)):
    item = session.get(ItemModel, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return None
