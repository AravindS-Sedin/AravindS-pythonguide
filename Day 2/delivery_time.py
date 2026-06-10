# Delivery Time Estimator
# Calculate estimated delivery time based on:
# - Distance to destination
# - Weather conditions
# - Traffic conditions (peak/normal)
# Add delays if there is rain, storm, or peak-hour traffic.
# Display the estimated delivery time and delivery status.


distance = float(input("Distance (km): "))
weather = input("Weather (clear/rain/storm): ")
time_of_day = input("Time (peak/normal): ")

delivery_time = distance * 3 

if weather == "rain":
    delivery_time += 10
elif weather == "storm":
    delivery_time += 20


if time_of_day == "peak":
    delivery_time += 15

if weather == "storm":
    status = "Delivery delayed due to severe weather"
elif weather == "rain":
    status = "Running slightly late due to rain"
elif time_of_day == "peak":
    status = "Heavy traffic in your area"
else:
    status = "On time"

print("\n--- Delivery Summary ---")
print(f"Estimated Delivery Time: {delivery_time:.2f} minutes")
print(f"Status: {status}")

