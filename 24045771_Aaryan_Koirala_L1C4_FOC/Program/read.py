def read_products():
    products = []
    try:
        with open("products.txt", "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                name, brand, stock, price, origin = line.strip().split(",")
                products.append({
                    "name": name,
                    "brand": brand,
                    "stock": int(stock),
                    "selling_price": int(price),
                    "origin": origin
                })
    except FileNotFoundError:
        print("[!] products.txt not found.")
    return products