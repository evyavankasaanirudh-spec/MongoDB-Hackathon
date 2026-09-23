from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")

db = client["mongodb_hackathon_db"]

print("Connected to MongoDB successfully!")
print("Database:", db.name)

client.close()
