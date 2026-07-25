from pydantic import BaseModel
from enum import Enum


class PaymentStatus(Enum):
    PENDING= "pending"
    SUCCESS="success"
    FAILED="failed"

class Payment(BaseModel):
    id: int
    state: PaymentStatus
    amount: float
