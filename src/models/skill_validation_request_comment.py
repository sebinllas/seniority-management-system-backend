from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from src.models import SkillValidationRequest

class SkillValidationRequestComment(SQLModel, table=True):
    __tablename__ = 'skill_validation_request_comment'  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    request_id: int = Field(foreign_key='skill_validation_request.id')
    request: "SkillValidationRequest" = Relationship(back_populates='comments')
    comment: str
    date: datetime = Field(default_factory=datetime.now)