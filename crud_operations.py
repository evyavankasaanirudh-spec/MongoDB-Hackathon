from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["mongodb_hackathon_db"]

products = db["products"]


# -------------------------
# CREATE
# -------------------------
new_product = {
    "product_id": 107,
    "name": "Gaming Mouse",
    "category": "Accessories",
    "price": 2500,
    "stock": 40,
    "tags": ["mouse", "gaming", "computer"]
}

result = products.insert_one(new_product)

print("CREATE:")
print("Inserted ID:", result.inserted_id)


# -------------------------
# READ
# -------------------------
print("\nREAD - All Products:")

for product in products.find():
    print(
        product["product_id"],
        "-",
        product["name"],
        "- ₹",
        product["price"]
    )


print("\nREAD - Single Product:")

product = products.find_one({"product_id": 101})

print(product)


# -------------------------
# UPDATE
# -------------------------
print("\nUPDATE:")

result = products.update_one(
    {"product_id": 107},
    {
        "$set": {
            "price": 2800,
            "stock": 35
        }
    }
)

print("Documents modified:", result.modified_count)


# -------------------------
# DELETE
# -------------------------
print("\nDELETE:")

result = products.delete_one({"product_id": 107})

print("Documents deleted:", result.deleted_count)


client.close()