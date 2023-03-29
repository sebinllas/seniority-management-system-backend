from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship, create_engine
from datetime import datetime


class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: Optional[int] = Field(foreign_key='employee.id')
    employee: Optional["Employee"] = Relationship(back_populates='account')
    creation_date: Optional[datetime] = Field(default_factory=datetime.now)
    username: str
    password: str
    is_admin_account: bool = False


class EmployeeSkills(SQLModel, table=True):
    employee_id: int = Field(foreign_key='employee.id', primary_key=True)
    skill_id: int = Field(foreign_key='skill.id', primary_key=True)
    attainment_date: datetime = Field(default_factory=datetime.now)


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    biography: str
    photo: str
    account_id: int = Field(foreign_key='account.id')
    account: Account = Relationship(back_populates='employee')
    skills: List["Skill"] = Relationship(link_model=EmployeeSkills)
    requests: List["SkillValidationRequest"] = Relationship(
        back_populates='employee')


class SeniorityLevelSkills(SQLModel, table=True):
    seniority_level_id: Optional[int] = Field(
        foreign_key="senioritylevel.id", primary_key=True)
    skill_id: Optional[int] = Field(foreign_key='skill.id', primary_key=True)
    requests: List["SkillValidationRequest"] = Relationship(
        back_populates='seniority_level')


class Skill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    seniority_levels: List["SeniorityLevel"] = Relationship(
        back_populates='skills', link_model=SeniorityLevelSkills
    )


class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    seniority_levels: Optional["SeniorityLevel"] = Relationship(
        back_populates='role')


class SeniorityLevel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    role_id: int = Field(default=None, foreign_key="role.id")
    skills: List["Skill"] = Relationship(
        back_populates="seniority_levels", link_model=SeniorityLevelSkills)
    role: Optional[Role] = Relationship(back_populates="seniority_levels")


class SkillValidationRequest(SQLModel, table=True):
    employee_id: Optional[int] = Field(
        foreign_key='employee.id', primary_key=True)
    employee: Employee = Relationship(back_populates='employee')
    seniority_level_id: Optional[int] = Field(foreign_key='senioritylevel.id')
    seniority_level: "SeniorityLevel" = Relationship(back_populates='requests')
    request_date: datetime = Field(default_factory=datetime.now)
    support_file: Optional[str]
    approved: bool = False
    validated: bool = False


class Interaction(SQLModel, table=True):
    employee_from_id: int = Field(foreign_key='employee.id', primary_key=True)
    employee_to_id: int = Field(foreign_key='employee.id', primary_key=True)
    date: datetime = Field(default_factory=datetime.now)


engine = create_engine(
    "postgresql://postgres:root@localhost:5432/seniority-management", echo=True)


SQLModel.metadata.create_all(engine)
