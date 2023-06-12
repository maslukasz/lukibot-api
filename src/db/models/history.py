from typing import List, Optional
from pydantic import BaseModel

class History_Users(BaseModel):
    guild_id: int | None = None
    user_id: str | None = None
    channel: str | None = None
    data: str | None = None
    messages: int | None = None