from pydantic import BaseModel


class SqlCredentials(BaseModel):
    username: str
    password: str
    host: str
    database: str
