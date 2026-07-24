from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class PaymentStatus(Enum):
    PENDING= "pending"
    SUCCESS="success"
    FAILED="failed"

class Payment(BaseModel):
    id: int
    state: PaymentStatus
    amount: float

class HostelType(Enum):
    GIRLS="girls"
    BOYS="boys"
    HYBRID="hybrid"

class Hostel(BaseModel):
    id: int
    hostel_type: HostelType
    name: str

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

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/payment/{id}")
def get_payment_status(id: int):
    return {"payment_id": id, "status": "Success"}

@app.post("/payment/{id}")
def update_payment(id: int,status: PaymentStatus,amount: float):
    payment = {"id":id,"status":status,"amount":amount}
    return payment

@app.get("/users")
def get_users():
    return "no users currently"

@app.post("/users/")
def add_user(user: User):
    user_dict = user.model_dump()
    users.append(user_dict)
    return {"message": f"User added sucessfully. User id is {user.id}"}