from flask import Flask, request, jsonify

app = Flask(__name__)

# Danh sách các sản phẩm
products = [
    {"id": 1, "name": "Product 1", "price": 10.0},
    {"id": 2, "name": "Product 2", "price": 20.0},
    {"id": 3, "name": "Product 3", "price": 30.0},
]

# Lấy danh sách sản phẩm
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Tạo một sản phẩm mới
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Lấy thông tin chi tiết của một sản phẩm
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return "Product not found", 404

# Cập nhật thông tin của một sản phẩm
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        product["name"] = data["name"]
        product["price"] = data["price"]
        return jsonify(product)
    return "Product not found", 404

# Xóa một sản phẩm
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    before_len = len(products)
    products = [p for p in products if p["id"] != product_id]
    if len(products) < before_len:
        return "", 204
    return "Product not found", 404

if __name__ == '__main__':
    app.run(debug=True)
