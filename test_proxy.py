from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client['data']

with open('data.json',encoding="utf-8") as f:
    data = json.load(f)
i =1
for d in data:
    keys = list(d.keys())
    element = {}
    for k in keys:
        if k != "_id":
            element[k] = d[k]   
        else:
            pass
    db['pvp'].insert_one(element)  
    print("element",i,"inserted")
    i+=1          