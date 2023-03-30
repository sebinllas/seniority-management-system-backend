from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
from src.models import EmployeeSkill, EmployeeProject

if TYPE_CHECKING:
    from src.models import Project, SkillValidationRequest, Account, Skill, Role, SkillValidationRequest


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str]
    email: Optional[str]
    biography: Optional[str]
    role_id: Optional[int] = Field(default=None, foreign_key='role.id')
    role: Optional["Role"] = Relationship(back_populates='employees')
    account: "Account" = Relationship(back_populates='employee')
    skills: List["Skill"] = Relationship(link_model=EmployeeSkill)
    requests: List["SkillValidationRequest"] = Relationship(
        back_populates='employee')
    projects: List["Project"] = Relationship(
        back_populates='employees', link_model=EmployeeProject)
