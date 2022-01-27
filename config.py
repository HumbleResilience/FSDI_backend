import pymongo
import certifi

mongo_url = "mongodb+srv://etech:rawr1542@cluster0.3s8er.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

#get specific database
db = client.get_database("PcPlus")