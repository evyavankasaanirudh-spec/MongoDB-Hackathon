from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["mongodb_hackathon_db"]

orders = db["orders"]


# -----------------------------------
# 1. Join orders with customers
# -----------------------------------
print("\n1. Orders with customer information:")

pipeline = [
    {
        "$lookup": {
            "from": "customers",
            "localField": "customer_id",
            "foreignField": "customer_id",
            "as": "customer"
        }
    },
    {
        "$unwind": "$customer"
    },
    {
        "$project": {
            "_id": 0,
            "order_id": 1,
            "amount": 1,
            "status": 1,
            "customer_name": "$customer.name",
            "customer_city": "$customer.city"
        }
    }
]

for result in orders.aggregate(pipeline):
    print(result)


# -----------------------------------
# 2. Join orders with products
# -----------------------------------
print("\n2. Orders with product information:")

pipeline = [
    {
        "$lookup": {
            "from": "products",
            "localField": "product_id",
            "foreignField": "product_id",
            "as": "product"
        }
    },
    {
        "$unwind": "$product"
    },
    {
        "$project": {
            "_id": 0,
            "order_id": 1,
            "quantity": 1,
            "amount": 1,
            "product_name": "$product.name",
            "category": "$product.category"
        }
    }
]

for result in orders.aggregate(pipeline):
    print(result)


# -----------------------------------
# 3. Join customers + products
# -----------------------------------
print("\n3. Complete order information:")

pipeline = [
    {
        "$lookup": {
            "from": "customers",
            "localField": "customer_id",
            "foreignField": "customer_id",
            "as": "customer"
        }
    },
    {
        "$unwind": "$customer"
    },
    {
        "$lookup": {
            "from": "products",
            "localField": "product_id",
            "foreignField": "product_id",
            "as": "product"
        }
    },
    {
        "$unwind": "$product"
    },
    {
        "$project": {
            "_id": 0,
            "order_id": 1,
            "customer": "$customer.name",
            "product": "$product.name",
            "category": "$product.category",
            "quantity": 1,
            "amount": 1,
            "status": 1
        }
    }
]

for result in orders.aggregate(pipeline):
    print(result)


client.close()