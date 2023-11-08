from odmantic import Model
from utils.db import engine
from typing import List

BOARD_XY = 5


class BingoBoard(Model):
    user_id: int
    board: List[List[int]]

    @classmethod
    async def get_board(cls, user_id: int) -> dict:
        find_board = await engine.find_one(cls, cls.user_id == user_id)
        if not find_board:
            return {"ok": False, "message": "빙고보드 없음, 갱신 필요"}
        return {"ok": True, "board": find_board.board}

    @classmethod
    async def new_board(cls, user_id: int, board: List[List[int]]) -> dict:
        find_board = await engine.find_one(cls, cls.user_id == user_id)
        if find_board:
            return {"ok": False, "message": "빙고보드가 이미 존재합니다"}

        new_board_data = {"user_id": user_id, "board": board}
        new_board = cls(**new_board_data)
        result = await engine.save(new_board)
        if not result:
            return {"ok": False, "message": "빙고보드가 추가 실패"}
        return {"ok": True, "message": "빙고보드가 추가 완료"}

    @classmethod
    async def add_bingo_to_board(cls, user_id: int, board: List[int]) -> dict:
        find_board = await engine.find_one(cls, cls.user_id == user_id)
        if find_board:
            return {"ok": False, "message": "해당 유저의 빙고보드를 찾을 수 없습니다"}

        for num in board:
            x = num / BOARD_XY
            y = num % BOARD_XY
            find_board.board[y][x] = 0

        result = await engine.save(find_board)
        if not result:
            return {"ok": False, "message": "빙고보드가 갱신 실패"}
        return {"ok": True, "message": "빙고보드가 갱신 완료"}
