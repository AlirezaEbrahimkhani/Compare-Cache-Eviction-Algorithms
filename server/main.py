from fastapi import FastAPI
from algorithms.lfu import LFUAlgorithm
from algorithms.lru import LRUAlgorithm
from algorithms.arc import ARCAlgorithm

app = FastAPI()
lfu = LFUAlgorithm(11)
lru = LRUAlgorithm(3)
arc = ARCAlgorithm(4)

@app.get("/")
def defaultEndpoint():
    return "Dude... lets move on to /tweet!!"

@app.get("/tweet")
def getTest(id: int):
    tweet = arc.get(id)
    return tweet
