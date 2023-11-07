from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
import os

db_key = os.environ.get("DB_KEY")
client = AsyncIOMotorClient(db_key)
engine = AIOEngine(client=client, database="pseudo_town_db")
