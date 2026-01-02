# write.py
import datetime

def write_products(products):
    with open("products.txt", "w") as f:
        for p in products:
            line = f"{p['name']},{p['brand']},{p['stock']},{p['selling_price']},{p['origin']}\n"
            f.write(line)

def generate_invoice_sell(product_name, quantity, price, buyer_name):
    free_items = quantity // 3
    total_quantity = quantity + free_items
    total_price = quantity * price  # Use the original price, not VAT-inclusive price

    with open("invoice.txt", "a") as f:
        f.write("===== SALE INVOICE =====\n")
        f.write("Date/Time: " + str(datetime.datetime.now()) + "\n")
        f.write(f"Buyer: {buyer_name}\n")
        f.write(f"Product: {product_name}\n")
        f.write(f"Purchased Quantity: {quantity}\n")
        f.write(f"Free Items (Buy 3 Get 1): {free_items}\n")
        f.write(f"Total Items Given: {total_quantity}\n")
        f.write(f"Unit Price: Rs {price}\n")  # Original price, not VAT-inclusive
        f.write(f"Total Paid: Rs {total_price}\n")
        f.write("-"*40 + "\n")

def generate_invoice_stock(product_name, quantity, vendor_name):
    with open("invoice.txt", "a") as f:
        f.write("===== RESTOCK INVOICE =====\n")
        f.write("Date/Time: " + str(datetime.datetime.now()) + "\n")
        f.write(f"Vendor: {vendor_name}\n")
        f.write(f"Product: {product_name}\n")
        f.write(f"Quantity Restocked: {quantity}\n")
        f.write("-"*40 + "\n")
