TotalPrice = 0
items = []

def print_invoice(items, total):
    print("\nInvoice:")
    for item, price in items:
        print(f"{item}: ₹{price}")
    print(f"Total Price: ₹{TotalPrice}")

while True:
    product = input("Enter the product (or type 'done' to finish): ")
    if product.lower() == "done":
        break
    try:
        price = int(input("Enter price: ₹"))
        items.append((product, price))
        TotalPrice += price
    except ValueError:
        print("Please enter a valid number.")

print_invoice(items, TotalPrice)
