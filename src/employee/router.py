from typing import List

from fastapi import APIRouter

import src.employee.service as employee_service
from src.employee.models import Employee

router = APIRouter()


@router.get("/", response_model=List[Employee])
def get_all():
    return employee_service.get_all()


@router.post("/", response_model=Employee)
def create(employee: Employee):
    return employee_service.create(employee)
