from pydantic import BaseModel
from pydantic.schema import List


class UserInfo(BaseModel):
    phone: str
    bingo: List[int]
