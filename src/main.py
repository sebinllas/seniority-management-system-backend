from fastapi import FastAPI
from src.controllers import employee
from src.controllers import role

app = FastAPI()

app.include_router(employee.router, prefix="/employee", tags=["employee"])
app.include_router(role.router, prefix="/role", tags=["role"])