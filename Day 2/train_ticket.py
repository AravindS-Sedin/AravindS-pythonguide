# Train Ticket Fare Calculator
# Ask for passenger name, age, class, and distance.
# Calculate fare based on travel class.
# Apply discount if eligible.
# Add 5% GST and show the final ticket amount.
# Display a booking confirmation message.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
class_type = input("Class (Sleeper/3AC/2AC): ")
distance = int(input("Distance (km): "))

fare_rates = {
    "Sleeper": 1.00,
    "3AC": 1.50,
    "2AC": 1.80
}

if class_type not in fare_rates:
    print("Invalid class.")
    exit()

rate = fare_rates[class_type]

base_fare = distance * rate

discount = 0

if age < 12 or age >= 60:
    discount = base_fare * 0.10

fare_after_discount = base_fare - discount
gst = fare_after_discount * 0.05
total_fare = fare_after_discount + gst

print("\n--- Train Ticket Summary ---")
print(f"Passenger Name : {name}")
print(f"Age            : {age}")
print(f"Class          : {class_type}")
print(f"Distance       : {distance} km")
print(f"Base Fare      : ₹{base_fare:.2f}")
if discount > 0:
    print(f"Discount       : -₹{discount:.2f}")
print(f"GST (5%)       : +₹{gst:.2f}")
print(f"Total Fare     : ₹{total_fare:.2f}")
print(f"\nBooking confirmed for {name} — Bon voyage!")