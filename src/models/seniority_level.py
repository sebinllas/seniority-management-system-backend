from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
from src.models import SeniorityLevelSkill

if TYPE_CHECKING:
    from src.models import Skill, Role


class SeniorityLevel(SQLModel, table=True):
    __tablename__ = 'seniority_level'  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    role_id: Optional[int] = Field(foreign_key='role.id')
    skills: List["Skill"] = Relationship(
        back_populates="seniority_levels", link_model=SeniorityLevelSkill)
    role: Optional["Role"] = Relationship(back_populates="seniority_levels")
