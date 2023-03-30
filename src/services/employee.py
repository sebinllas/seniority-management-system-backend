from sqlmodel import Session, select

from src.config.db import engine
from src.models import Employee


def get_all():
    with Session(engine) as session:
        statement = select(Employee)
        result = session.exec(statement)
        return result.all()


def create(employee: Employee):
    with Session(engine) as session:
        session.add(employee)
        session.commit()
        session.refresh(employee)
        return employee