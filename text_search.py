from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["mongodb_hackathon_db"]

products = db["products"]


# -----------------------------------
# 1. Create text index
# -----------------------------------
text_index = products.create_index(
    [
        ("name", "text"),
        ("tags", "text")
    ]
)

print("Text index created:")
print(text_index)


# -----------------------------------
# 2. Search for "computer"
# -----------------------------------
print("\n1. Search results for 'computer':")

results = products.find(
    {
        "$text": {
            "$search": "computer"
        }
    },
    {
        "_id": 0,
        "name": 1,
        "category": 1,
        "tags": 1
    }
)

for product in results:
    print(product)


# -----------------------------------
# 3. Search for "gaming"
# -----------------------------------
print("\n2. Search results for 'gaming':")

results = products.find(
    {
        "$text": {
            "$search": "gaming"
        }
    },
    {
        "_id": 0,
        "name": 1,
        "category": 1,
        "tags": 1
    }
)

for product in results:
    print(product)


# -----------------------------------
# 4. Search with relevance score
# -----------------------------------
print("\n3. Search with relevance score:")

results = products.find(
    {
        "$text": {
            "$search": "computer"
        }
    },
    {
        "_id": 0,
        "name": 1,
        "category": 1,
        "score": {
            "$meta": "textScore"
        }
    }
).sort(
    [
        ("score", {"$meta": "textScore"})
    ]
)

for product in results:
    print(product)


client.close()