from fastapi import APIRouter
from app.schemas.payment import PaymentStatus,Payment

router = APIRouter(prefix="/payment")

@router.get("/{id}")
def get_payment_status(id: int):
    return {"payment_id": id, "status": "Success"}

@router.post("/{id}")
def update_payment(payment: Payment):
    payment = {"id":payment.id,"status":payment.status,"amount":payment.amount}
    return payment