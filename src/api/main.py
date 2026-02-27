from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel

from .routes import router
from src.db import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables on startup
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(title="UniversoEspiritual API", version="0.1.0", lifespan=lifespan)

app.include_router(router, prefix="/api")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8000, reload=True)
