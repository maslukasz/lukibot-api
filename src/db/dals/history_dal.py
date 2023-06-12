from typing import List, Optional

from src.db.database import database
from src.db.models.history import History_Users

import json

class HistoryDAL():
    async def get_guild_user(self, user_id: int):
        return await database.fetch_all('SELECT guild_id, data messages FROM history_users WHERE user_id = :user_id', values={'user_id': user_id})
    
    #await c.execute(f"SELECT DISTINCT sum(messages), data FROM history_users WHERE data BETWEEN DATE_ADD(now(), INTERVAL -14 day) AND date(now()) AND guild_id = {ctx.get_guild().id} GROUP BY data LIMIT 14")

    async def get_date_messages(self, guild_id: str, day: int):
        return await database.fetch_all('SELECT DISTINCT sum(messages) as messages, data as date FROM history_users WHERE data BETWEEN DATE_ADD(now(), INTERVAL -:day day) AND date(now()) AND guild_id = :guild_id GROUP BY data LIMIT :day ', values={'guild_id': guild_id, 'day': day})
        