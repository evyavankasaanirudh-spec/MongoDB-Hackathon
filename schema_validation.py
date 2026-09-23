from pymongo import MongoClient
from pymongo.errors import WriteError

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["mongodb_hackathon_db"]

# Remove old demo collection if it exists
if "validated_products" in db.list_collection_names():
    db["validated_products"].drop()


# -----------------------------------
# Create collection with validation
# -----------------------------------
validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [
            "product_id",
            "name",
            "category",
            "price",
            "stock"
        ],
        "properties": {
            "product_id": {
                "bsonType": "int"
            },
            "name": {
                "bsonType": "string"
            },
            "category": {
                "bsonType": "string"
            },
            "price": {
                "bsonType": ["int", "double"],
                "minimum": 0
            },
            "stock": {
                "bsonType": "int",
                "minimum": 0
            }
        }
    }
}

db.create_collection(
    "validated_products",
    validator=validator,
    validationLevel="strict",
    validationAction="error"
)

validated_products = db["validated_products"]

print("Schema validation collection created successfully!")


# -----------------------------------
# Valid document
# -----------------------------------
valid_product = {
    "product_id": 201,
    "name": "Monitor",
    "category": "Electronics",
    "price": 18000,
    "stock": 10
}

try:
    validated_products.insert_one(valid_product)
    print("\nValid document inserted successfully!")

except WriteError as error:
    print("Valid document rejected:", error)


# -----------------------------------
# Invalid document
# -----------------------------------
invalid_product = {
    "product_id": "202",
    "name": "Keyboard",
    "category": "Accessories",
    "price": -500,
    "stock": 10
}

try:
    validated_products.insert_one(invalid_product)
    print("Invalid document inserted.")

except WriteError:
    print("\nInvalid document rejected by schema validation!")


# -----------------------------------
# Display valid documents
# -----------------------------------
print("\nValid documents in collection:")

for product in validated_products.find({}, {"_id": 0}):
    print(product)


client.close()