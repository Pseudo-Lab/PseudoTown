from pydantic import BaseModel
from pydantic.schema import List


class Board(BaseModel):
    board: List[List[int]]


class Bingo(BaseModel):
    bingo: List[int]
