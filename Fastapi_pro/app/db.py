import os
from sqlmodel import SQLModel
from sqlmodel import create_engine


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 上一级目录
sqlite_file_name = os.path.join(BASE_DIR, "database.db")
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_engine():
    return engine
