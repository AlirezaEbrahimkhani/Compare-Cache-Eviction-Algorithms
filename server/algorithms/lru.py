import json
from utils.redis import Redis
from datetime import datetime
from models.types import LruTweet , Response
from utils.finder import Finder

class LRUAlgorithm:
    def __init__(self, capacity) -> None:
        self.redis = Redis().get_instance()
        self.finder = Finder()
        self.capacity = capacity
        
    def get(self, key) -> Response[LruTweet]:
        value = self.redis.get(key)
        if value != None:
            value = json.loads(value)
            response: Response[LruTweet] = {
                "data": value,
                "hit": True
            }
            value["timestamp"] = str(datetime.now())
            self.set(key, value)
        else:
            tweet: LruTweet ={
                "data": self.finder.find(key),
                "timestamp": str(datetime.now())
            }
            response = self.set(key,tweet)
        return response
    
    def set(self, key, value) -> Response[LruTweet]:
        keys = self.redis.keys()
        redisData =[]
        for k in keys:
            redisData.append(json.loads(self.redis.get(k)))
        redisData.sort(key=lambda x:x['timestamp'])
        if self.capacity <= len(self.redis.keys()):
            last_item = redisData.pop(0)
            self.redis.delete(last_item["data"]["id"])
        self.redis.set(key, json.dumps(value))
        response: Response[LruTweet] = {
            "data": value,
            "hit": False
        }
        return response