from sqlmodel import SQLModel, Field
from datetime import datetime


class Interaction(SQLModel, table=True):
    employee_from_id: int = Field(foreign_key='employee.id', primary_key=True)
    employee_to_id: int = Field(foreign_key='employee.id', primary_key=True)
    date: datetime = Field(default_factory=datetime.now)
