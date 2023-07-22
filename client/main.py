import json
  
# Opening JSON file
f = open('tweets.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
for i in range(0, 100):
    print(data[i])
  
# Closing file 
f.close()