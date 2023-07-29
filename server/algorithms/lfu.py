import json
from utils.finder import Finder
from utils.redis import Redis
from models.types import Response, TweetLike

# [b'10', b'8', b'3', b'2', b'4', b'6', b'9', b'5', b'1', b'lfu_cache', b'7']
class LFUAlgorithm:

    def __init__(self, capacity) -> None:
        self.redis = Redis().get_instance()
        self.finder = Finder()
        self.capacity = capacity

    def get(self, key) -> Response[TweetLike]:
        self.redis.zincrby('lfu_cache', 1, key)
        value = self.redis.get(key)
        if value != None:
            response: Response[TweetLike] = {
                "data": json.loads(value),
                "hit": True
            }
        else:
            response = self.set(key, self.finder.find(key))
        return response

    def set(self, key, value) -> Response[TweetLike]:
        if self.redis.zcard('lfu_cache') >= self.capacity:
            lfu_key = self.redis.zrange('lfu_cache', 0, 0)[0]
            self.redis.delete(lfu_key)
            self.redis.zrem('lfu_cache', lfu_key)

        self.redis.set(key, json.dumps(value))
        self.redis.zadd('lfu_cache', {key: 0})
        response: Response[TweetLike] = {
            "data": value,
            "hit": False
        }
        return response
