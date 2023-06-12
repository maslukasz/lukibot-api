from fastapi import FastAPI, Path

from src.db.database import database
from src.db.dals.history_dal import HistoryDAL

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.get("/user/{user_id}")
async def user_all_guilds(user_id: int):
    return await HistoryDAL().get_guild_user(user_id=user_id)

@app.get("/guilds/{guild_id}/{day}")
async def date_guild(guild_id: int, day: int=Path(gt=1, le=30)):
    return await HistoryDAL().get_date_messages(guild_id=guild_id, day=day)
