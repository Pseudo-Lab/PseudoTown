from odmantic import Model
from utils.db import engine


class UserId(Model):
    user_id: int

    @classmethod
    async def issue_id(cls) -> int:
        find_id = await engine.find_one(cls)
        new_id = {}
        if not find_id:
            new_id.setdefault("user_id", 0)
        else:
            new_id = {"id": find_id.id, "user_id": find_id.user_id + 1}

        result = await engine.save(cls(**new_id))
        return result.user_id


class UserModel(Model):
    user_id: int
    name: str
    phone: str
    bingo: list

    @classmethod
    async def add_or_get_user(cls, name: str, phone: str, bingo: list) -> dict:
        find_user = await engine.find(cls, cls.name == name and cls.phone == phone)
        if find_user:
            return {"ok": True, "user_id": find_user.user_id, "bingo": find_user.bingo}

        user_id = await UserId.issue_id()
        new_user_info = {
            "user_id": user_id,
            "name": name,
            "phone": phone,
            "bingo": bingo,
        }
        new_user = cls(**new_user_info)
        result = await engine.save(new_user)
        return {"ok": True, "user_id": result.user_id, "bingo": result.bingo}


if __name__ == "__main__":
    import asyncio

    cur_id = asyncio.run(UserId.issue_id())
    print(cur_id)
