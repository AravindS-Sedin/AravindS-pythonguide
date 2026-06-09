bill_amount = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))
tip_percent = float(input("Enter the tip percentage (0 if no tip): "))

tip_amount = bill_amount * (tip_percent / 100)
total_amount = bill_amount + tip_amount
share_per_person = total_amount / num_people

print("\n--- Bill Summary ---")
print(f"Total bill amount (including tip): {total_amount:.2f}")
print(f"Tip amount: {tip_amount:.2f}")
print(f"Per person share: {share_per_person:.2f}")