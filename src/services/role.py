from sqlmodel import Session, select

from src.config.db import engine
from src.models import Role


def get_all():
    with Session(engine) as session:
        statement = select(Role)
        result = session.exec(statement)
        return result.all()


def create(role: Role):
    with Session(engine) as session:
        session.add(role)
        session.commit()
        session.refresh(role)
        return role
