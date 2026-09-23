from pymongo import MongoClient
from datetime import datetime, timedelta

# Connect to MongoDB
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["mongodb_hackathon_db"]

# Collections
products = db["products"]
customers = db["customers"]
orders = db["orders"]

# Clear previous demo data
products.delete_many({})
customers.delete_many({})
orders.delete_many({})


# -------------------------
# PRODUCTS
# -------------------------
product_data = [
    {
        "product_id": 101,
        "name": "Laptop",
        "category": "Electronics",
        "price": 75000,
        "stock": 15,
        "tags": ["computer", "portable", "work"]
    },
    {
        "product_id": 102,
        "name": "Smartphone",
        "category": "Electronics",
        "price": 45000,
        "stock": 30,
        "tags": ["mobile", "android", "communication"]
    },
    {
        "product_id": 103,
        "name": "Headphones",
        "category": "Accessories",
        "price": 5000,
        "stock": 50,
        "tags": ["audio", "wireless", "music"]
    },
    {
        "product_id": 104,
        "name": "Mechanical Keyboard",
        "category": "Accessories",
        "price": 7000,
        "stock": 25,
        "tags": ["keyboard", "gaming", "computer"]
    },
    {
        "product_id": 105,
        "name": "Smart Watch",
        "category": "Wearables",
        "price": 12000,
        "stock": 20,
        "tags": ["watch", "fitness", "smart"]
    },
    {
        "product_id": 106,
        "name": "Tablet",
        "category": "Electronics",
        "price": 30000,
        "stock": 18,
        "tags": ["tablet", "portable", "work"]
    }
]

products.insert_many(product_data)


# -------------------------
# CUSTOMERS
# -------------------------
customer_data = [
    {
        "customer_id": 1,
        "name": "Arjun Kumar",
        "email": "arjun@example.com",
        "city": "Hyderabad",
        "membership": "Premium"
    },
    {
        "customer_id": 2,
        "name": "Priya Sharma",
        "email": "priya@example.com",
        "city": "Bangalore",
        "membership": "Standard"
    },
    {
        "customer_id": 3,
        "name": "Rahul Verma",
        "email": "rahul@example.com",
        "city": "Chennai",
        "membership": "Premium"
    },
    {
        "customer_id": 4,
        "name": "Sneha Reddy",
        "email": "sneha@example.com",
        "city": "Hyderabad",
        "membership": "Standard"
    }
]

customers.insert_many(customer_data)


# -------------------------
# ORDERS
# -------------------------
now = datetime.now()

order_data = [
    {
        "order_id": 1001,
        "customer_id": 1,
        "product_id": 101,
        "quantity": 1,
        "amount": 75000,
        "status": "Completed",
        "order_date": now - timedelta(days=5)
    },
    {
        "order_id": 1002,
        "customer_id": 2,
        "product_id": 102,
        "quantity": 2,
        "amount": 90000,
        "status": "Completed",
        "order_date": now - timedelta(days=4)
    },
    {
        "order_id": 1003,
        "customer_id": 3,
        "product_id": 103,
        "quantity": 3,
        "amount": 15000,
        "status": "Pending",
        "order_date": now - timedelta(days=3)
    },
    {
        "order_id": 1004,
        "customer_id": 1,
        "product_id": 104,
        "quantity": 2,
        "amount": 14000,
        "status": "Completed",
        "order_date": now - timedelta(days=2)
    },
    {
        "order_id": 1005,
        "customer_id": 4,
        "product_id": 105,
        "quantity": 1,
        "amount": 12000,
        "status": "Cancelled",
        "order_date": now - timedelta(days=1)
    },
    {
        "order_id": 1006,
        "customer_id": 3,
        "product_id": 106,
        "quantity": 2,
        "amount": 60000,
        "status": "Completed",
        "order_date": now
    }
]

orders.insert_many(order_data)


# -------------------------
# DISPLAY RESULTS
# -------------------------
print("Sample data inserted successfully!")
print("Products:", products.count_documents({}))
print("Customers:", customers.count_documents({}))
print("Orders:", orders.count_documents({}))

client.close()