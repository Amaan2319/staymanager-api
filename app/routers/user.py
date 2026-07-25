from fastapi import APIRouter,HTTPException
from app.schemas.user import User,users

# 1. Use APIRouter instead of FastAPI
router = APIRouter(prefix="/user")

# 2. Change @app to @router
@router.get("/all")
def get_users():
    if users:
        return users

    else:
        return {"Message": "No users"}

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