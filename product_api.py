from flask import Flask, jsonify, request
app = Flask(__name__)

products = [] #to list store products

@app.route('/products' , methods=['POST', 'GET'])
def handle_products():
    if request.method == 'POST' :
        # to get product data from JSON request
        try:
            data = request.get_json()
            name = data['name']
            description = data['description']
            price = float(data['price'])
        except (KeyError, ValueError):
            return jsonify ({'error': 'Invalid product data'}) , 400

        #for creating new product
        new_product = {'name': name, 'description' : description, 'price': price}
        products.append(new_product)
        return jsonify(new_product), 201

    elif request.method == 'GET':
        #to return a list of all the products
        return jsonify(products)

#for deleting products
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            return jsonify({'message': 'Product deleted successfully'}), 200
        return jsonify({'error': 'Product not found'}), 404

#for updating products
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    for product in products:
        if product['id'] == product_id:
            data = request.get_json()
            product['name'] - data.get('name', product['name'])
            product['description'] = data.get('description', product['description'])
            product['price']
        =data.get('price', product['price'])

            return jsonify(product), 200
    return jsonify({'error': 'Product not found'})
if __name__ == '__main__':
    app.run(debug=True)
