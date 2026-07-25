from enum import Enum
from pydantic import BaseModel

class UserType(Enum):
    ADMIN = "admin"
    TENANT = "tenant"
    HOSTEL = "hostel"

class User(BaseModel):
    id: int
    fName: str
    lName: str
    userType: UserType
    hostelId: int

users = list()