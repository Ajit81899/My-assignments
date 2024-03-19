import requests
from pymongo import MongoClient


response = requests.get("https://api.weatherbit.io/v2.0/alerts?lat=39.75895&lon=-84.19161&key=3a01582fbcd64166afcfbfa51f3f6555")
data = response.json()


client = MongoClient('mongodb://localhost:27017/')
db = client['Weather']
collection = db['Weathermycollection']


collection.insert_one(data)