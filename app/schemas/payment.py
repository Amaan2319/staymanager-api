from pydantic import BaseModel,Field
from enum import Enum


class PaymentStatus(Enum):
    PENDING= "pending"
    SUCCESS="success"
    FAILED="failed"

class Payment(BaseModel):
    id: int
    state: PaymentStatus
    amount: float=Field(...,gt=0.0,description="Payment cannot be negative or zero")
