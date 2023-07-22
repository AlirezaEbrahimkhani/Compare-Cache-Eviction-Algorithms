from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def defaultEndpoint():
    return "Dude... lets move on to /tweet!!"

@app.get("/tweet")
def getTest():
    return {"name": "Hello Baby"}
