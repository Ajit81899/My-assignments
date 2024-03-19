import requests
from pymongo import MongoClient


response = requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")
data = response.json()


client = MongoClient('mongodb://localhost:27017/')
db = client['CityPopulation']
collection = db['Citymycollection']


collection.insert_one(data)