from pydantic import BaseModel
from pydantic.schema import List


class UserInfo(BaseModel):
    discord: str
