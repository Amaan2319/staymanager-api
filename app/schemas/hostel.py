from enum import Enum
from pydantic import BaseModel

class HostelType(Enum):
    GIRLS="girls"
    BOYS="boys"
    GENERAL="general"

class Hostel(BaseModel):
    id: int
    name: str
    hostelType: HostelType