from fastapi import FastAPI
from utils.redis import Redis
from algorithms.lfu import LFUAlgorithm

app = FastAPI()
redis = Redis()
lfu = LFUAlgorithm(11)

@app.get("/")
def defaultEndpoint():
    return "Dude... lets move on to /tweet!!"

@app.get("/tweet")
def getTest(id: int):
    tweet = lfu.get(id)
    print(redis.getKeys())
    return tweet
