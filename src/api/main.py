from fastapi import FastAPI

from .routes import router

app = FastAPI(title="UniversoEspiritual API", version="0.1.0")

app.include_router(router, prefix="/api")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8000, reload=True)
