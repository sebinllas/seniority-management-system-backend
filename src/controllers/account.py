from fastapi import APIRouter

import src.services.employee as employee_service
import src.services.account as account_service
from src.models import Employee
from src.models import Account

router = APIRouter()


@router.get("/", response_model=Account)
def get_all():
    return account_service.get_all()


@router.post("/", response_model=Account)
def create(account: Account):
    return account_service.create(account)
