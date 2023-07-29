import redis
import json

class Redis:
    __instance = None
    def __init__(self) -> None:
        if Redis.__instance == None:
            Redis.__instance = redis.Redis(host='localhost', 
                        port=6379, 
                        db=0)
            print("Connected to redis...")
            Redis.clearDB(self)

    @staticmethod
    def get_instance():
        if Redis.__instance == None:
            Redis()
        return Redis.__instance
        
    def getInstance(self):
        return self
    
    def get(self, key):
        return Redis.__instance.get(str(key))
    
    def set(self, key, value):
        Redis.__instance.set(str(key), json.dumps(value))

    def getKeys(self):
        return Redis.__instance.keys()
    
    def clearDB(self):
        Redis.__instance.flushdb()
