from datetime import datetime
from sqlmodel import Field, SQLModel


class EmployeeSkill(SQLModel, table=True):
    __tablename__ = 'employee_skill'  # type: ignore
    employee_id: int = Field(foreign_key='employee.id', primary_key=True)
    skill_id: int = Field(foreign_key='skill.id', primary_key=True)
    attainment_date: datetime = Field(default_factory=datetime.now)
