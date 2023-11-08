from fastapi import APIRouter
from bingo.models import BingoBoard
from bingo.schema import Board, Bingo

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
async def add_bingo(user_id: int, bingo: Bingo) -> dict:
    return await BingoBoard.add_bingo_to_board(user_id, bingo.bingo)
