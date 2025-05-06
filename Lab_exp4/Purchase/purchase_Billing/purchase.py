from product_Details.entry_display import products

def purchase_products():
    cart = []
    total = 0
    if not products:
        print("No products available for purchase.")
        return

    print("\nAvailable Products:")
    for idx, product in enumerate(products, 1):
        print(f"{idx}. {product['name']} - ₹{product['price']} - Qty: {product['quantity']}")

    while True:
        choice = input("Enter product name to buy (or 'done' to checkout): ")
        if choice.lower() == "done":
            break

        for product in products:
            if product["name"].lower() == choice.lower():
                qty = int(input(f"Enter quantity of {choice}: "))
                if qty <= product["quantity"]:
                    cart.append({"name": choice, "price": product["price"], "quantity": qty})
                    total += product["price"] * qty
                    product["quantity"] -= qty
                    print(f"Added {qty} {choice}(s) to cart.")
                else:
                    print(f"Only {product['quantity']} {choice}(s) available.")
                break
        else:
            print("Product not found!")

    # Billing
    print("\n--- Bill ---")
    for item in cart:
        print(f"{item['name']} x {item['quantity']} = ₹{item['price'] * item['quantity']}")

    print(f"\nSubtotal: ₹{total}")

    discount = 0
    if total > 1000:
        discount = 0.10 * total
        print(f"Discount (10%): -₹{discount}")

    taxed_total = total - discount
    tax = 0.18 * taxed_total
    final_total = taxed_total + tax

    print(f"Tax (18%): +₹{tax:.2f}")
    print(f"Final Amount: ₹{final_total:.2f}")