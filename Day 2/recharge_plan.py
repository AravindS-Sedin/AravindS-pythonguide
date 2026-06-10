# Mobile Recharge Plan Selector
# Recommends the best plan based on budget and preference.
# Shows:
# 1. Best affordable plan
# 2. Savings compared to the next higher plan
# 3. Extra data benefit compared to the lower plan
# 4. Message if no plan fits the budget

budget = int(input("Enter your budget (₹): "))
preference = input("Preference (calls/data/both): ").lower()

plans = {
    "calls": [
        {"price": 199, "calls": "Unlimited", "data": "100MB/day", "validity": 28},
        {"price": 239, "calls": "Unlimited", "data": "300MB/day", "validity": 28},
        {"price": 299, "calls": "Unlimited", "data": "500MB/day", "validity": 56}
    ],

    "data": [
        {"price": 199, "data": 1.0, "calls": "100 mins/day", "validity": 28},
        {"price": 239, "data": 1.5, "calls": "Unlimited", "validity": 28},
        {"price": 299, "data": 2.0, "calls": "Unlimited", "validity": 56}
    ],

    "both": [
        {"price": 199, "data": 1.0, "calls": "Unlimited", "sms": "100/day", "validity": 28},
        {"price": 239, "data": 1.5, "calls": "Unlimited", "sms": "100/day", "validity": 28},
        {"price": 299, "data": 2.0, "calls": "Unlimited", "sms": "100/day", "validity": 56}
    ]
}

if budget < 199:
    print(f"Sorry, no plans available for ₹{budget}.")
    print("Minimum budget needed: ₹199")

elif preference not in plans:
    print("Invalid preference entered.")

else:
    category_plans = plans[preference]

    if preference == "calls":
        best_index = 0
    else:
        best_index = -1

        for i in range(len(category_plans)):
            if category_plans[i]["price"] <= budget:
                best_index = i

    best_plan = category_plans[best_index]

    print("\n---")

    if preference == "calls":
        print(
            f"Best Plan: ₹{best_plan['price']} — "
            f"{best_plan['calls']}, "
            f"{best_plan['data']}, "
            f"{best_plan['validity']} days"
        )
    else:
        print(
            f"Best Plan: ₹{best_plan['price']} — "
            f"{best_plan['data']}GB/day, "
            f"{best_plan['validity']} days, "
            f"{best_plan['calls']}"
        )

    if best_index == len(category_plans) - 1:
        print("You save ₹0 (this is the top plan!)")
    else:
        next_plan = category_plans[best_index + 1]
        savings = next_plan["price"] - best_plan["price"]

        print(
            f"You save ₹{savings} vs the ₹{next_plan['price']} plan."
        )

    if best_index == 0:
        print("No lower plan to compare against.")

    elif preference != "calls":
        lower_plan = category_plans[best_index - 1]

        extra_data = best_plan["data"] - lower_plan["data"]

        print(
            f"Extra data vs ₹{lower_plan['price']} plan: "
            f"+{extra_data}GB/day"
        )