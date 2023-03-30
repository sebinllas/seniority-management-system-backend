from sqlmodel import create_engine, SQLModel, Session, select

from src.models import *

db_url = 'postgresql://postgres:root@localhost:5432/seniority-management'
engine = create_engine(db_url)

SQLModel.metadata.create_all(engine)
