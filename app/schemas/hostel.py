from enum import Enum
from pydantic import BaseModel,Field
from typing import Annotated

class HostelType(Enum):
    GIRLS="girls"
    BOYS="boys"
    GENERAL="general"

class Hostel(BaseModel):
    id: Annotated[int,Field(gt=0,description="ID should be greater than 0")]
    name: str
    hostelType: HostelType