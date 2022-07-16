import datetime

from pydantic import BaseModel


class FormData(BaseModel):
    team_name: str
    team_id: int
    team_elo: int
    order_elo: int
    scrim_date: datetime
