from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

# Емуляція бази даних
fake_users_db = {}
current_id = 1

# GET: Отримати всіх юзерів
@router.get("/", response_model=List[UserResponse])
def get_users():
    return list(fake_users_db.values())

# GET: Отримати юзера за ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_users_db[user_id]

# POST: Створити нового юзера
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    global current_id
    new_user = {"id": current_id, **user.model_dump()}
    fake_users_db[current_id] = new_user
    current_id += 1
    return new_user

# PUT: Оновити дані юзера
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    stored_user_data = fake_users_db[user_id]
    update_data = user_update.model_dump(exclude_unset=True)
    updated_user = {**stored_user_data, **update_data}
    
    fake_users_db[user_id] = updated_user
    return updated_user

# DELETE: Видалити юзера
@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_users_db[user_id]
    return {"message": "User deleted successfully"}