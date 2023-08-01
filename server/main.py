import redis
from fastapi import FastAPI
from utils.redis import Redis
from algorithms.lfu import LFUAlgorithm
from algorithms.lru import LRUAlgorithm

app = FastAPI()
redis = Redis()
lfu = LFUAlgorithm(11)
lru = LRUAlgorithm(3)

@app.get("/")
def defaultEndpoint():
    return "Dude... lets move on to /tweet!!"

@app.get("/tweet")
def getTest(id: int):
    tweet = lru.get(id)
    return tweet
