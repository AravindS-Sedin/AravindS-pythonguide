# Currency Converter
# Convert an amount from one currency to another.
# Validate that both currencies are supported.
# Use USD as the base currency for conversion.
# Display the exchange rate and converted amount.
# Also show the equivalent value in all supported currencies.


rates = {
    "USD": 1.0,
    "INR": 84.50,
    "EUR": 0.87,
    "GBP": 0.75,
    "JPY": 154.00,
    "AED": 3.67,
    "CAD": 1.36
}

symbols = {
    "USD": "$",
    "INR": "₹",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "AED": "AED ",
    "CAD": "C$"
}

amount = float(input("Enter amount: "))
from_currency = input("From Currency (USD,INR,EUR,GBP,JPY,AED,CAD): ").upper()
to_currency = input("To Currency (USD,INR,EUR,GBP,JPY,AED,CAD): ").upper()


if from_currency not in rates:
    print(f"Error: '{from_currency}' is not a supported currency.")

elif to_currency not in rates:
    print(f"Error: '{to_currency}' is not a supported currency.")

elif from_currency == to_currency:
    print(
        f"{symbols[from_currency]}{amount:,.2f} {from_currency} → "
        f"{symbols[to_currency]}{amount:,.2f} {to_currency}"
    )
    print("Both currencies are the same.")

else:
    # Convert source currency to USD
    amount_in_usd = amount / rates[from_currency]

    # Convert USD to target currency
    converted_amount = amount_in_usd * rates[to_currency]

    # Exchange rate
    exchange_rate = rates[to_currency] / rates[from_currency]

    print("\n--- Conversion Result ---")
    print(
        f"{symbols[from_currency]}{amount:,.2f} {from_currency} → "
        f"{symbols[to_currency]}{converted_amount:,.2f} {to_currency}"
    )

    print(
        f"Rate: 1 {from_currency} = "
        f"{exchange_rate:.4f} {to_currency}"
    )

    print("\nEquivalent in all currencies:")

    for currency, rate in rates.items():
        value = amount_in_usd * rate

        print(
            f"{symbols[currency]}{value:,.2f} "
            f"{currency}"
        )