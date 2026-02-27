from typing import Generator
import os

from sqlmodel import create_engine, Session

# Allow configuring the DB via DATABASE_URL environment variable. If not set,
# fall back to a local sqlite file for development.
sqlite_file = "universo.db"
sqlite_url = f"sqlite:///{sqlite_file}"

database_url = os.getenv("DATABASE_URL", sqlite_url)

# Use SQLite-specific connect args when appropriate
connect_args = {}
if database_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(database_url, echo=False, connect_args=connect_args)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
