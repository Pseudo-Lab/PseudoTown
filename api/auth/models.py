from odmantic import Model
from utils.db import engine


class UserId(Model):
    user_id: int

    @classmethod
    async def issue_id(cls) -> int:
        find_id = await engine.find_one(cls)
        new_id = {}
        if not find_id:
            new_id.setdefault("user_id", 1)
        else:
            new_id = {"id": find_id.id, "user_id": find_id.user_id + 1}

        result = await engine.save(cls(**new_id))
        return result.user_id


class UserModel(Model):
    user_id: int
    name: str
    discord: str

    @classmethod
    async def add_or_get_user(cls, name: str, discord: str) -> dict:
        find_user = await engine.find_one(cls, cls.name == name and cls.discord == discord)
        if find_user:
            return {
                "ok": True,
                "user_id": find_user.user_id,
            }

        user_id = await UserId.issue_id()
        new_user_info = {
            "user_id": user_id,
            "name": name,
            "discord": discord,
        }
        new_user = cls(**new_user_info)
        result = await engine.save(new_user)
        return {"ok": True, "user_id": result.user_id}


if __name__ == "__main__":
    import asyncio

    cur_id = asyncio.run(UserId.issue_id())
    print(cur_id)
