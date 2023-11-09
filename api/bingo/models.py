from odmantic import Model
from utils.db import engine
from typing import List

BOARD_XY = 5
MAGIC_NUM = 1000


class Attribute(Model):
    user_id: int
    attribute: List[int]

    @classmethod
    async def get_attr(cls, user_id: int) -> dict:
        find_attr = await engine.find_one(cls, cls.user_id == user_id)
        if not find_attr:
            return {"ok": False, "message": "특성 없음. 추가 필요."}
        return {"ok": True, "attribute": find_attr.attribute}

    @classmethod
    async def set_attr(cls, user_id: int, attribute: List[int]):
        find_attr = await engine.find_one(cls, cls.user_id == user_id)
        if find_attr:
            return {"ok": False, "message": "특성이 이미 있습니다."}

        new_attr_data = {"user_id": user_id, "attribute": attribute}
        new_attr = cls(**new_attr_data)
        result = await engine.save(new_attr)
        if not result:
            return {"ok": False, "message": "특성 추가 실패"}
        return {"ok": True, "message": "특성 추가 완료"}


class BingoBoard(Model):
    user_id: int
    gave_ids: List[int]
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

        new_board_data = {"user_id": user_id, "gave_ids": [], "board": board}
        new_board = cls(**new_board_data)
        result = await engine.save(new_board)
        if not result:
            return {"ok": False, "message": "빙고보드가 추가 실패"}
        return {"ok": True, "message": "빙고보드가 추가 완료"}

    @classmethod
    async def add_bingo_to_board(cls, user_id: int, gave_user_id: int) -> dict:
        find_board = await engine.find_one(cls, cls.user_id == user_id)
        if not find_board:
            return {"ok": False, "message": "해당 유저의 빙고보드를 찾을 수 없습니다"}

        attr = await Attribute.get_attr(gave_user_id)
        for num in attr.get("attribute", []):
            x = num % BOARD_XY
            y = int(num / BOARD_XY)
            if find_board.board[y][x] < MAGIC_NUM:
                find_board.board[y][x] -= MAGIC_NUM

        find_board.gave_ids.append(user_id)

        result = await engine.save(find_board)
        if not result:
            return {"ok": False, "message": "빙고보드가 갱신 실패"}
        return {"ok": True, "message": "빙고보드가 갱신 완료"}
