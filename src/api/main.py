from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from sqlmodel import SQLModel

from .routes import router
from src.db import engine
from src.logging_config import configure_logging
from fastapi.staticfiles import StaticFiles


configure_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables on startup
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(title="UniversoEspiritual API", version="0.2.0", lifespan=lifespan)

app.include_router(router, prefix="/api")

# Prefer serving a production build if present at `frontend/dist`, otherwise fall back to the simple preview in `src/frontend`.
frontend_prod = Path("frontend/dist")
if frontend_prod.exists():
    app.mount("/", StaticFiles(directory=str(frontend_prod), html=True), name="frontend")
else:
    app.mount("/app", StaticFiles(directory="src/frontend", html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8000, reload=True)
