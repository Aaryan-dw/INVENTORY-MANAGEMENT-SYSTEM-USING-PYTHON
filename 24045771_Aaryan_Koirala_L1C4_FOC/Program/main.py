from read import read_products
from write import write_products, generate_invoice_sell, generate_invoice_stock
from operation import display_products, sell_product, restock_product

def main():
    while True:
        products = read_products()
        while True:
            print("\nSkin Care Product Sale System")
            print("1. Display Products")
            print("2. Sell Product")
            print("3. Restock Product")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                display_products(products)

            elif choice == "2":
                buyer = input("Enter the buyer's name: ")
                print("\nSelect a product to sell by number:")
                for index, p in enumerate(products, start=1):
                    # Show price with VAT only when displaying products
                    price_with_vat = p["selling_price"] * (1 + 0.13)  # VAT rate: 13%
                    print(f"{index}. {p['name']} - Stock: {p['stock']} - Price: Rs {price_with_vat:.2f}")

                try:
                    product_number = int(input("\nEnter product number: "))
                    if product_number < 1 or product_number > len(products):
                        print("[!] Invalid product number.")
                        continue

                    product = products[product_number - 1]  # Get the selected product

                    # Ask for quantity and ensure it is a valid number
                    while True:
                        try:
                            quantity = int(input(f"Enter the quantity to sell for {product['name']}: "))
                            if quantity <= 0:
                                print("[!] Quantity should be a positive number.")
                                continue
                            break
                        except ValueError:
                            print("[!] Please enter a valid number for quantity.")

                    # Process the sale and generate invoice with VAT
                    if sell_product(products, product["name"], quantity):
                        generate_invoice_sell(product["name"], quantity, product["selling_price"], buyer)
                        write_products(products)
                        print(f"[+] Invoice has been generated with VAT included.")

                except ValueError:
                    print("[!] Invalid input. Please enter a valid product number.")

            elif choice == "3":
                vendor = input("Enter the vendor's name: ")
                print("\nSelect a product to restock by number:")
                for index, p in enumerate(products, start=1):
                    print(f"{index}. {p['name']} - Stock: {p['stock']}")

                try:
                    product_number = int(input("\nEnter product number: "))
                    if product_number < 1 or product_number > len(products):
                        print("[!] Invalid product number.")
                        continue

                    product = products[product_number - 1]  # Get the selected product

                    # Ask for quantity and ensure it is a valid number
                    while True:
                        try:
                            quantity = int(input(f"Enter the quantity to restock for {product['name']}: "))
                            if quantity <= 0:
                                print("[!] Quantity should be a positive number.")
                                continue
                            break
                        except ValueError:
                            print("[!] Please enter a valid number for quantity.")

                    # Process the restocking and generate invoice with VAT
                    if restock_product(products, product["name"], quantity):
                        generate_invoice_stock(product["name"], quantity, vendor)
                        write_products(products)
                        print(f"[+] Invoice has been generated with VAT included.")

                except ValueError:
                    print("[!] Invalid input. Please enter a valid product number.")

            elif choice == "4":
                break

            else:
                print("[!] Invalid choice. Please try again.")

        again = input("Do you want to restart the system? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
