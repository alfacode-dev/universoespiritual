from fastapi import APIRouter

from .schemas import Item

router = APIRouter()


@router.get("/", tags=["root"])
async def read_root():
    return {"message": "Bienvenido a UniversoEspiritual API"}


@router.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}


@router.get("/items/{item_id}", response_model=Item, tags=["items"])
async def get_item(item_id: int):
    return Item(id=item_id, name=f"Item {item_id}", description="Ejemplo")
