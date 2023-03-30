from sqlmodel import Field, SQLModel
from typing import Optional

class SeniorityLevelSkill(SQLModel, table=True):
    __tablename__ = 'seniority_level_skill'  # type: ignore
    seniority_level_id: Optional[int] = Field(
        foreign_key="seniority_level.id", primary_key=True)
    skill_id: Optional[int] = Field(foreign_key='skill.id', primary_key=True)