from fastapi import APIRouter
from app.schemas.payment import PaymentStatus

router = APIRouter(prefix="/payment")

@router.get("/{id}")
def get_payment_status(id: int):
    return {"payment_id": id, "status": "Success"}

@router.post("/{id}")
def update_payment(id: int,status: PaymentStatus,amount: float):
    payment = {"id":id,"status":status,"amount":amount}
    return payment