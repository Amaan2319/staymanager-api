from pydantic import BaseModel,Field
from typing import Annotated
from enum import Enum


class PaymentStatus(Enum):
    PENDING= "pending"
    SUCCESS="success"
    FAILED="failed"

class Payment(BaseModel):
    id: Annotated[int, Field(...,gt=0,description="The unique ID must be greater than 0")]
    state: PaymentStatus
    amount: Annotated[float,Field(...,gt=0.0,description="Payment cannot be negative or zero")]
