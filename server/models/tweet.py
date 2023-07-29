
from pydantic import BaseModel

class Tweet(BaseModel):
    name: str
    email: str
    text:str
    id: int