products = {
    "Speaker": 3000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Headphones": 2000,
    "Monitor": 7000
}
cart = []
total = 0
print("Available Products:")
for name, price in products.items():
    print(f"{name} - {price}")
while True:
    item = input("\nEnter product name (or 'done' to finish): ")

    if item.lower() == "done":
        break

    if item in products:
        cart.append(item)
        total += products[item]
        print(f"{item} added to cart.")
    else:
        print("Product not found!")
discount = 0
if total > 1000:
    discount = total * 0.10
final_amount = total - discount

print("\n--- Bill Summary ---")
print(f"Total: ₹{total}")
print(f"Discount: ₹{discount}")
print(f"Final Amount: ₹{final_amount}")