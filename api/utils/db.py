from utils.db_auth import db_key
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

client = AsyncIOMotorClient(db_key)
engine = AIOEngine(client=client, database="pseudo_town_db")
