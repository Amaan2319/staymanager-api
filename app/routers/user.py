from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app.schemas.user import User,users
# import time
# from functools import wraps
from app.core.utils import time_logger
# 1. Import your database session generator
from app.core.database import get_db
# 2. Import the SQLAlchemy Model (The Database Blueprint)
from app.models.user import User as DBUser
# 3. Import the Pydantic Schema (The Data Formatter)
from app.schemas.user import User as UserSchema

# 1. Use APIRouter instead of FastAPI
router = APIRouter(prefix="/user", tags=["Users"])

# def time_logger(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start_time = time.perf_counter()
        
#         func(*args,**kwargs)
#         end_time = time.perf_counter()
        
#         exec_time = end_time-start_time
#         print(f"Function {func.__name__} took {exec_time:.6f} seconds to run")
#     return wrapper


@router.get("/all", response_model=list[UserSchema])
def get_users(db: Session = Depends(get_db)):
    # 1. Query the database: SELECT * FROM users;
    users = db.query(DBUser).all()
    
    # 2. Check if the database is empty
    if not users:
        # Returning an empty list is standard practice for a GET ALL route when no data exists
        return [] 
        
    # 3. Return the database objects
    return users

@router.post("/")
def add_user(new_user: User):
    
    users.append(new_user)
    return {"message": f"User added successfully. User id is {new_user.id}"}
# raise HTTPException(detail="Unable to add user!", status_code=200)


@router.put("/{user_id}")
def update_user(updated_user: User):
    for index, user in enumerate(users):
        if user.id == updated_user.id:
            users[index]=updated_user
            return {"message": "User updated succesfully."}

    raise HTTPException(status_code=404,detail="Unable to update the user. or user does not exists")

@router.delete("/{id}")
def delete_user(id: int):
    for index, user in enumerate(users):
        if user.id == id:
            users.pop(id)
            return {"message": "User deleted sucessfully."}
    raise HTTPException(status_code=404, detail="User does not exist")