
from pydantic import BaseModel

from typing import TypeVar, Generic

T = TypeVar('T')

class TweetLike(BaseModel):
    name: str
    email: str
    text: str
    id: int

class Response(Generic[T]):
    data: T
    hit: bool

class LruTweet(Generic[T]):
    data: T
    timestamp: str