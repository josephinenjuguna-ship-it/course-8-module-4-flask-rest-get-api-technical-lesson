# app.py

from flask import Flask, jsonify, request  

app = Flask(__name__)

# TODO: Define mock data for a list of products
# Example: Each product should have id, name, price, and category
data = [
    {"id":1, "name": "Laptop", "price":899.99, "category": "electronics"},
    {"id":2, "name": "Book", "price":14.99, "category": "books"},
    {"id":3, "name": "Desk", "price":199.99, "category": "furniture"},
]
# TODO: Implement a homepage route that returns a JSON welcome message

@app.route("/")
def index():
    return({"message":"Welcome to the product API!","resource_endpoint":"/products"}), 200


# TODO: Implement GET /products to return all products or filter by category

@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    filtered = data
    if category:
        filtered = [item for item in data if item["category"] == category]
    return jsonify(filtered), 200


# TODO: Implement G@app.route("/")

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    for p in data:
        if p["id"] == id:
            return jsonify(p), 200
    return jsonify({"message":"Product not found"}), 404
if __name__ == "__main__":
    app.run(debug=True)
