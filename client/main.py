import requests
from time import sleep

class Main:
    
    def getTweet(self, id: int):
        r = requests.get('http://localhost:8000/tweet', params={'id': id})
        return r.text
    
main = Main()

for i in range(0, 11):
    print(i)
    print(main.getTweet(i))
