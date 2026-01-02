🧴 Skin Care Product Sale System
📌 Overview:
The Skin Care Product Sale System is a Python-based console application designed to manage the sale and restocking of skin care products. It supports product display, selling with promotional offers, restocking, invoice generation, and file-based data persistence.
This project uses a modular approach with separate files for reading data, writing data, business operations, and the main program flow.

🗂️ Project Structure:
├── main.py
├── operation.py
├── read.py
├── write.py
├── products.txt
├── invoice.txt   (auto-generated)

⚙️ Features:
📦 Display all available skin care products
🛒 Sell products with Buy 3 Get 1 Free offer
💰 VAT calculation (13%) for display purposes
🧾 Automatic invoice generation for sales and restocking
🔄 Restock products from vendors
💾 Persistent storage using text files
🔁 Option to restart the system after exit

🧠 Business Rules
  1. VAT rate is fixed at 13%
  2. VAT is shown only during display, not added to invoice total
  3. Promotional offer: Buy 3 Get 1 Free
  4. Stock must be sufficient to apply the offer
  5. All changes are saved back to products.txt

📄 File Descriptions
1️⃣ main.py
  1. Entry point of the system
  2. Displays menu options
  3. Handles user input
  4. Coordinates all operations (display, sell, restock, exit)
2️⃣ operation.py
  1. Contains core business logic
  2. Functions:
     a. display_products()
     b. sell_product()
     c. restock_product()
  3. Applies VAT and promotional rules
3️⃣ read.py
  1. Reads product data from products.txt
  2. Converts data into Python dictionaries
4️⃣ write.py
  1. Writes updated product data back to file
  2. Generates:
    a. Sale invoices
    b. Restock invoices
  3. Uses timestamp for record tracking
5️⃣ products.txt
  1. Stores product information in CSV format: "ProductName,Brand,Stock,SellingPrice,Origin"
  2. Example: "Vitamin C Serum,Garnier,179,2000,France"

🧾 Invoice Details:
Invoices are stored in invoice.txt and include:
  1. Date and time
  2. Buyer/Vendor name
  3. Product name
  4. Quantity sold or restocked
  5. Free items (if applicable)
  6. Total price (excluding VAT)

▶️ How to Run the Program:
  1. Make sure Python 3 is installed
  2. Keep all files in the same directory
  3. Run the program: python main.py

🧪 Sample Menu
Skin Care Product Sale System
1. Display Products
2. Sell Product
3. Restock Product
4. Exit

📌 Notes:
invoice.txt is automatically created if it does not exist
Ensure products.txt is present before running the program
Input validation is applied for quantity and product selection

👨‍💻 Author:
Aaryan Koirala
BSc (Hons) Computing
Itahari International College
