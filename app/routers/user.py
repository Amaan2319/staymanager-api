from fastapi import APIRouter
from app.schemas.user import User

# 1. Use APIRouter instead of FastAPI
router = APIRouter()

# 2. Change @app to @router
@router.get("/users")
def get_users():
    return "no users currently"

@router.post("/users/")
def add_user(user: User):
    # Use user.id directly from the validated Pydantic model
    return {"message": f"User added successfully. User id is {user.id}"}