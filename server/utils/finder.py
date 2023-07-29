import json
import os

class Finder:

    def __init__(self) -> None:
        self.tweets = self.readTweets()

    def readTweets(self):
        dirname = os.path.dirname(__file__)
        f = open(os.path.join(dirname, "tweets.json"))
        data = json.load(f)
        return data
    
    def find(self, tweetId: int):
        return self.tweets[tweetId - 1]