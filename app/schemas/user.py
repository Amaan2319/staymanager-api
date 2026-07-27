from enum import Enum
from pydantic import BaseModel,Field
from typing import Annotated

class UserType(Enum):
    ADMIN = "admin"
    TENANT = "tenant"
    HOSTEL = "hostel"

class User(BaseModel):
    id: Annotated[int, Field(...,gt=0,description="ID should be greater than 0")]
    fName: str
    lName: str
    userType: UserType
    hostelId: Annotated[int, Field(...,gt=0,description="The unique ID must be greater than 0")]

users = list()