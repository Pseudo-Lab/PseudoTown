from fastapi import APIRouter
from auth.models import UserModel
from auth.schema import UserInfo

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/user/{name}")
async def add_or_get_user(name: str, body: UserInfo) -> dict:
    return await UserModel.add_or_get_user(name, body.discord)
