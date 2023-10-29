from fastapi import APIRouter, Body
from auth.models import UserModel

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/user/{name}")
async def add_or_update_user(name: str, body: dict):
    await UserModel.add_or_update_user(name, body.get("phone"))
