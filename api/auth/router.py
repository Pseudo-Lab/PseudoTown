from fastapi import APIRouter
from auth.models import UserModel

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/user/{name}")
async def add_or_update_user(name: str, body: dict):
    result = await UserModel.add_or_update_user(name, body.get("phone"))
    return {"ok": result}
