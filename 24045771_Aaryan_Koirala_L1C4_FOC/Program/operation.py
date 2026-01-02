# operation.py

# VAT rate
VAT_RATE = 0.13  # 13% VAT

def display_products(products):
    print("\n{:<20} {:<15} {:<10} {:<15} {:<10}".format("Product", "Brand", "Stock", "Price (Rs)", "Origin"))
    print("-"*75)
    for p in products:
        # Calculate the price with VAT for display purpose only
        price_with_vat = p["selling_price"] * (1 + VAT_RATE)
        print("{:<20} {:<15} {:<10} {:<15} {:<10}".format(p["name"], p["brand"], p["stock"], f"Rs {price_with_vat:.2f}", p["origin"]))


def sell_product(products, product_name, quantity):
    for p in products:
        if p["name"].lower() == product_name.lower():
            if p["stock"] < quantity:
                print("[!] Not enough stock available.")
                return False

            free_items = quantity // 3  # Buy 3 Get 1 Free
            total_quantity = quantity + free_items

            if p["stock"] < total_quantity:
                print(f"[!] Not enough stock to apply offer. You can only buy up to {p['stock'] - (p['stock'] // 4)} units.")
                return False

            p["stock"] -= total_quantity
            print(f"[+] Sold {quantity} units of {p['name']}.")
            if free_items > 0:
                print(f"[🎁] You received {free_items} unit(s) FREE under the Buy 3 Get 1 offer!")
            return True
    print("[!] Product not found.")
    return False


def restock_product(products, product_name, quantity):
    for p in products:
        if p["name"].lower() == product_name.lower():
            p["stock"] += quantity
            return True
    print("[!] Product not found.")
    return False
