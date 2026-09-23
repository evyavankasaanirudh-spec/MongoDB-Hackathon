from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["mongodb_hackathon_db"]

products = db["products"]


# 1. $gt - Greater Than
print("\n1. Products with price greater than ₹30,000:")

for product in products.find({"price": {"$gt": 30000}}):
    print(product["name"], "-", product["price"])


# 2. $lt - Less Than
print("\n2. Products with price less than ₹10,000:")

for product in products.find({"price": {"$lt": 10000}}):
    print(product["name"], "-", product["price"])


# 3. $gte - Greater Than or Equal To
print("\n3. Products with stock >= 20:")

for product in products.find({"stock": {"$gte": 20}}):
    print(product["name"], "-", product["stock"])


# 4. $in - Match any value from a list
print("\n4. Electronics or Wearables:")

for product in products.find(
    {"category": {"$in": ["Electronics", "Wearables"]}}
):
    print(product["name"], "-", product["category"])


# 5. $and - Multiple conditions
print("\n5. Electronics costing more than ₹40,000:")

query = {
    "$and": [
        {"category": "Electronics"},
        {"price": {"$gt": 40000}}
    ]
}

for product in products.find(query):
    print(product["name"], "-", product["price"])


# 6. $or - Either condition
print("\n6. Products costing less than ₹10,000 OR stock greater than 25:")

query = {
    "$or": [
        {"price": {"$lt": 10000}},
        {"stock": {"$gt": 25}}
    ]
}

for product in products.find(query):
    print(product["name"], "-", product["price"], "-", product["stock"])


# 7. $exists - Check whether a field exists
print("\n7. Products containing tags field:")

for product in products.find({"tags": {"$exists": True}}):
    print(product["name"])


# 8. Sorting
print("\n8. Products sorted by price (highest first):")

for product in products.find().sort("price", -1):
    print(product["name"], "-", product["price"])


# 9. Projection
print("\n9. Product names and prices only:")

for product in products.find(
    {},
    {"_id": 0, "name": 1, "price": 1}
):
    print(product)


client.close()
