from sqlmodel import Field, SQLModel

class EmployeeProject(SQLModel, table=True):
    __tablename__ = 'employee_project'  # type: ignore
    employee_id: int = Field(foreign_key='employee.id', primary_key=True)
    project_id: int = Field(foreign_key='project.id', primary_key=True)