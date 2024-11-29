import requests

url = "http://localhost:5000/products"

#to add a new product
new_product = {'name': 'T-shirt', 'description': 'Cool T-shirt', 'price': 500.00}
response = requests.post(url, json=new_product)

if response.status_code == 201:
    print("Product created successfully!")
    print(response.json())
else:
    print("Error adding product: {response.text}")

#to get all products
response = requests.get(url)

if response.status_code == 200:
    print("Products:")
    for product in response.json():
        print(product)
    else:
        print("Error getting products: {response.text}")
