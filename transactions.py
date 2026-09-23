from pymongo import MongoClient
from datetime import datetime
from pymongo.errors import PyMongoError

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["mongodb_hackathon_db"]

products = db["products"]
orders = db["orders"]


def place_order(customer_id, product_id, quantity):
    with client.start_session() as session:

        try:
            with session.start_transaction():

                # 1. Find product
                product = products.find_one(
                    {"product_id": product_id},
                    session=session
                )

                if product is None:
                    raise Exception("Product not found.")

                # 2. Check stock
                if product["stock"] < quantity:
                    raise Exception("Insufficient stock.")

                # 3. Decrease stock
                products.update_one(
                    {"product_id": product_id},
                    {
                        "$inc": {
                            "stock": -quantity
                        }
                    },
                    session=session
                )

                # 4. Calculate amount
                amount = product["price"] * quantity

                # 5. Create order
                new_order = {
                    "order_id": 2001,
                    "customer_id": customer_id,
                    "product_id": product_id,
                    "quantity": quantity,
                    "amount": amount,
                    "status": "Completed",
                    "order_date": datetime.now()
                }

                orders.insert_one(
                    new_order,
                    session=session
                )

                print("Order created successfully.")

            print("Transaction committed successfully!")

        except (PyMongoError, Exception) as error:
            print("Transaction failed:", error)


# Place an order
place_order(
    customer_id=1,
    product_id=101,
    quantity=1
)


# Display updated product
print("\nUpdated product:")

product = products.find_one(
    {"product_id": 101},
    {"_id": 0}
)

print(product)


client.close()