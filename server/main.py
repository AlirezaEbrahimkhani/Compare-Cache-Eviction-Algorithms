import redis
from fastapi import FastAPI
from models.tweet import Tweet


app = FastAPI()


# Read from standalone REDIS
rd = redis.Redis(host='localhost', 
                 port=6379, 
                 db=0)

# write a key
rd.set("Key1", "nima maloche")
# read a key
print(rd.get("Key1"))

@app.get("/")
def defaultEndpoint():
    print("pedar Saaaaag")
    return "Dude... lets move on to /tweet!!"

@app.get("/tweet")
def getTest():
    return {"name": "Hello Baby"}

@app.post("/tweet/")
async def create_tweet(tweet:Tweet):
    print(tweet)
    return tweet




