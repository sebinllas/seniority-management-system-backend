from sqlmodel import create_engine, SQLModel, Session, select

from src.account.models import Account
from src.employee.models import Employee
from src.role.models import Role
from src.seniority_level.models import SeniorityLevelSkill, SeniorityLevel
from src.skill.models import Skill
from src.skill_validation_request.models import SkillValidationRequest

db_url = 'postgresql://postgres:root@localhost:5432/seniority-management'
engine = create_engine(db_url)

SQLModel.metadata.create_all(engine)
