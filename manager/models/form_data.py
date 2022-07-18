import enum
from pydantic import BaseModel

class FormTeamCreate(BaseModel):
    user_id: str
    team_name: str
    
class FormTeamDisplay(BaseModel):
    team_id: str
        
class FormTeamEdit(BaseModel):
    team_id: int
    player_name: str
    player_elo: int   
    

class FormUser(BaseModel):
    user_email: str
    user_password: str


class FormScrimSearch(BaseModel):
    team_name: str
    team_id: int
    team_elo: int
    order_elo: int
    scrim_date: int
    
class FormScrimHistory(BaseModel):
    team_id: int
    
class FormScrimScore(BaseModel):
    scrim_id: int
    team_id: int
    scrim_score: int
