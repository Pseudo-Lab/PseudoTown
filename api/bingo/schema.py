from pydantic import BaseModel
from pydantic.schema import List


class Board(BaseModel):
    board: List[List[int]]


class UserID(BaseModel):
    user_id: int


class Attr(BaseModel):
    attribute: List[int]
