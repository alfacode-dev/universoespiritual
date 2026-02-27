from typing import Generator

from sqlmodel import create_engine, Session

sqlite_file = "universo.db"
sqlite_url = f"sqlite:///{sqlite_file}"

# `check_same_thread` is required for SQLite when using threads
engine = create_engine(sqlite_url, echo=False, connect_args={"check_same_thread": False})


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
