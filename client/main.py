import json
import requests
  
# Opening JSON file
f = open('tweets.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
for i in range(0, 100):
    pload = data[i]
    r = requests.post('http://localhost:8000/tweet/', json=pload)
    print(r.text)
  
# Closing file 
f.close()