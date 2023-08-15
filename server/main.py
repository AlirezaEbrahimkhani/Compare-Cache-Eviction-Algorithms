from fastapi import FastAPI
from utils.redis import Redis
from algorithms.lfu import LFUAlgorithm
from algorithms.lru import LRUAlgorithm
from algorithms.arc import ARCAlgorithm

cache_capacity: int = 100

redis = Redis()
app = FastAPI()
lfu = LFUAlgorithm(cache_capacity)
lru = LRUAlgorithm(cache_capacity)
arc = ARCAlgorithm(cache_capacity)

@app.get("/")
def defaultEndpoint():
    return "Dude... lets move on to /tweet!!"

@app.get("/tweet/lru")
def getTest(id: int):
    tweet = lru.get(id)
    return tweet

@app.get("/tweet/lfu")
def getTest(id: int):
    tweet = lfu.get(id)
    return tweet

@app.get("/tweet/arc")
def getTest(id: int):
    tweet = arc.get(id)
    return tweet

@app.get("/tweet/clear")
def getTest():
    redis.clearDB()
