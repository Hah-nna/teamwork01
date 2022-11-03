from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://admin:adminshow@cluster0.3luh09a.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.db

doc = {
    "name":"string",
    "text":"dsadsa"
}

db.comments.insert_one(doc)



