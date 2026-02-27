from fastapi import FastAPI
from sqlmodel import SQLModel

from .routes import router
from src.db import engine


app = FastAPI(title="UniversoEspiritual API", version="0.1.0")

app.include_router(router, prefix="/api")


@app.on_event("startup")
def on_startup():
    # Create database tables
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8000, reload=True)
