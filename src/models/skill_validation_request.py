from sqlmodel import Field, Relationship, SQLModel
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from src.models import Employee, Skill, SkillValidationRequestComment

class SkillValidationRequest(SQLModel, table=True):
    __tablename__ = 'skill_validation_request'  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: Optional[int] = Field(foreign_key='employee.id')
    employee: "Employee" = Relationship(back_populates='requests')
    skill_id: Optional[int] = Field(foreign_key='skill.id')
    skill: "Skill" = Relationship(back_populates='requests')
    request_date: datetime = Field(default_factory=datetime.now)
    support_file: Optional[str]
    validator: Optional[int] = Field(foreign_key='account.id')
    approved: bool = False
    validated: bool = False
    comments: List["SkillValidationRequestComment"] = Relationship(
        back_populates='request')