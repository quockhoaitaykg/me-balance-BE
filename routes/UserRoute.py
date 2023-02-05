from fastapi import HTTPException, APIRouter
from models.Users import UsersBaseModel
from services.UserService import fetch_all_users, create_user

router = APIRouter()

@router.get("/test")
async def read_root():
    return {"Hello": "World"}

@router.get("/all")
async def get_todo():
    response = await fetch_all_users()
    return response

# @router.get("/{title}", response_model=list[Users])
# async def get_user_name(name):
#     response = await fetch_one_user(name)
#     if response:
#         return response
#     raise HTTPException(404, f"There is no todo with the title {name}")
#
@router.post("/create", response_description="Add new user", response_model=UsersBaseModel)
async def post_todo(user: UsersBaseModel):
    response = create_user(user.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")
