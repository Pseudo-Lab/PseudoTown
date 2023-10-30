from odmantic import Model
from utils.db import engine


class UserModel(Model):
    name: str
    phone: str

    @classmethod
    async def add_or_update_user(cls, name: str, phone: str) -> bool:
        find_user = await engine.find(cls, cls.name == name)
        new_user_info = {"name": name, "phone": phone}
        if find_user:
            new_user_info.setdefault("id", find_user[0].id)

        new_user = cls(**new_user_info)
        result = await engine.save(new_user)
        return True if result else False
