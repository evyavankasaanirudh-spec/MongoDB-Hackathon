from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["mongodb_hackathon_db"]

orders = db["orders"]


# -----------------------------------
# 1. Total sales by customer
# -----------------------------------
print("\n1. Total sales by customer:")

pipeline = [
    {
        "$group": {
            "_id": "$customer_id",
            "total_spent": {"$sum": "$amount"}
        }
    },
    {
        "$sort": {
            "total_spent": -1
        }
    }
]

for result in orders.aggregate(pipeline):
    print(result)


# -----------------------------------
# 2. Average order amount
# -----------------------------------
print("\n2. Average order amount:")

pipeline = [
    {
        "$group": {
            "_id": None,
            "average_order": {"$avg": "$amount"}
        }
    }
]

for result in orders.aggregate(pipeline):
    print(result)


# -----------------------------------
# 3. Total revenue from completed orders
# -----------------------------------
print("\n3. Total revenue from completed orders:")

pipeline = [
    {
        "$match": {
            "status": "Completed"
        }
    },
    {
        "$group": {
            "_id": None,
            "total_revenue": {"$sum": "$amount"}
        }
    }
]

for result in orders.aggregate(pipeline):
    print(result)


# -----------------------------------
# 4. Orders grouped by status
# -----------------------------------
print("\n4. Number of orders by status:")

pipeline = [
    {
        "$group": {
            "_id": "$status",
            "order_count": {"$sum": 1}
        }
    },
    {
        "$sort": {
            "order_count": -1
        }
    }
]

for result in orders.aggregate(pipeline):
    print(result)


# -----------------------------------
# 5. Average order amount by status
# -----------------------------------
print("\n5. Average order amount by status:")

pipeline = [
    {
        "$group": {
            "_id": "$status",
            "average_amount": {"$avg": "$amount"}
        }
    },
    {
        "$sort": {
            "average_amount": -1
        }
    }
]

for result in orders.aggregate(pipeline):
    print(result)


client.close()