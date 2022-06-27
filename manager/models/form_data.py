import datetime

from pydantic import BaseModel


class FormData(BaseModel):
    team_name: str
    team_elo: str
    order_elo: str
    scrim_date: datetime
