from typing import List

from fastapi import APIRouter

import src.role.service as role_service
from src.role.models import Role

router = APIRouter()


@router.get("/employee", response_model=List[Role])
def get_all():
    return role_service.get_all()


@router.post("/employee", response_model=Role)
def create(role: Role):
    return role_service.create(role)
