from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["mongodb_hackathon_db"]

products = db["products"]


# -----------------------------------
# 1. Unique index
# -----------------------------------
unique_index = products.create_index(
    [("product_id", 1)],
    unique=True
)

print("1. Unique index created:")
print(unique_index)


# -----------------------------------
# 2. Single-field indexes
# -----------------------------------
category_index = products.create_index(
    [("category", 1)]
)

price_index = products.create_index(
    [("price", 1)]
)

print("\n2. Single-field indexes created:")
print(category_index)
print(price_index)


# -----------------------------------
# 3. Compound index
# -----------------------------------
compound_index = products.create_index(
    [
        ("category", 1),
        ("price", -1)
    ]
)

print("\n3. Compound index created:")
print(compound_index)


# -----------------------------------
# 4. Display all indexes
# -----------------------------------
print("\n4. Current indexes:")

for index in products.list_indexes():
    print(index)


# -----------------------------------
# 5. Query using indexed field
# -----------------------------------
print("\n5. Query using product_id:")

product = products.find_one(
    {"product_id": 101}
)

print(product)


# -----------------------------------
# 6. Explain query execution
# -----------------------------------
print("\n6. Query execution plan:")

explain_result = products.find(
    {"product_id": 101}
).explain()

print("Winning Plan:")
print(
    explain_result["queryPlanner"]["winningPlan"]
)


client.close()