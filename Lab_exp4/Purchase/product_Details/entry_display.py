products = []

def add_product():
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Product Quantity: "))
    products.append({"name": name, "price": price, "quantity": quantity})
    print(f"{name} added successfully!")

def display_products():
    if not products:
        print("No products available.")
    else:
        print("\nAvailable Products:")
        for idx, product in enumerate(products, 1):
            print(f"{idx}. {product['name']} - ₹{product['price']} - Qty: {product['quantity']}")