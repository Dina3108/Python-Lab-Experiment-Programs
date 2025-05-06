from product_Details.entry_display import products

def update_product():
    display_products()
    prod_name = input("Enter the product name to update: ")
    for product in products:
        if product["name"].lower() == prod_name.lower():
            product["name"] = input("Enter new name: ") or product["name"]
            product["price"] = float(input("Enter new price: ") or product["price"])
            product["quantity"] = int(input("Enter new quantity: ") or product["quantity"])
            print("Product updated successfully!")
            return
    print("Product not found.")

def delete_product():
    display_products()
    prod_name = input("Enter the product name to delete: ")
    for product in products:
        if product["name"].lower() == prod_name.lower():
            products.remove(product)
            print("Product deleted successfully!")
            return
    print("Product not found.")

def display_products():
    if not products:
        print("No products available.")
    else:
        print("\nAvailable Products:")
        for idx, product in enumerate(products, 1):
            print(f"{idx}. {product['name']} - ₹{product['price']} - Qty: {product['quantity']}")