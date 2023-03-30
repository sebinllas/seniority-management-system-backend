from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
from src.models import EmployeeProject

if TYPE_CHECKING:
    from src.models import Employee

class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    employees: List["Employee"] = Relationship(
        back_populates='projects', link_model=EmployeeProject)