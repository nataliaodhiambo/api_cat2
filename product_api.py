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

if __name__ == '__main__':
    app.run(debug=True)
