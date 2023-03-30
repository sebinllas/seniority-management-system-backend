from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
from src.models import SeniorityLevelSkill

if TYPE_CHECKING:
    from src.models import SeniorityLevel, SkillValidationRequest

class Skill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    seniority_levels: List["SeniorityLevel"] = Relationship(
        back_populates='skills', link_model=SeniorityLevelSkill)
    requests: List["SkillValidationRequest"] = Relationship()
