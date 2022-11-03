from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://admin:adminshow@cluster0.3luh09a.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.db

# db.commentsSanghyun.delete_many({})
# db.commentsJeongik.delete_many({})
# db.commentsYujin.delete_many({})
# db.commentsHana.delete_many({})