from fastapi import APIRouter
from bingo.models import BingoBoard, Attribute
from bingo.schema import Board, UserID, Attr

router = APIRouter(
    prefix="/bingo",
    tags=["bingo"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{user_id}")
async def get_bingo_board(user_id: int) -> dict:
    return await BingoBoard.get_board(user_id)


@router.post("/{user_id}")
async def new_bingo_board(user_id: int, board: Board) -> dict:
    return await BingoBoard.new_board(user_id, board.board)


@router.post("/{user_id}/add")
async def add_bingo(user_id: int, gave_id: UserID) -> dict:
    return await BingoBoard.add_bingo_to_board(user_id, gave_id.user_id)


@router.get("/attr/{user_id}")
async def get_attr(user_id: int) -> dict:
    return await Attribute.get_attr(user_id)


@router.post("/attr/{user_id}")
async def set_attr(user_id: int, attr: Attr) -> dict:
    return await Attribute.set_attr(user_id, attr.attribute)
