from odmantic import Model
from utils.db import engine


class UserModel(Model):
    name: str
    phone: str

    @classmethod
    async def add_or_update_user(cls, name: str, phone: str) -> bool:
        new_user = cls(name=name, phone=phone)
        result = await engine.save(new_user)
        return True if result else False
