# ATM Machine Program
# Ask the user to enter a PIN.
# Allow only 3 attempts.
# If the PIN is correct, show the balance.
# Let the user withdraw or deposit money.
# Block the card after 3 wrong attempts.

pin = 1234
balance = 10000
attempts = 3

while attempts > 0:
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == pin:
        print("PIN accepted.")
        print(f"Your current balance is: ₹{balance:.2f}")
        break
    else:
        attempts -= 1
        if attempts == 0:
            exit()
        else:
            print(f"Incorrect PIN. Attempts remaining: {attempts}")

while True:
    print("\n------Welcome to PyBank ATM------")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        amount = float(input("Enter amount: ₹"))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Withdrawn ₹{amount:.2f}")
            print(f"New Balance: ₹{balance:.2f}")

    elif choice == '2':
        amount = float(input("Enter amount: ₹"))
        balance += amount
        print(f"Deposited ₹{amount:.2f}")
        print(f"New Balance: ₹{balance:.2f}")

    elif choice == '3':
        print("Thank you for using PyBank ATM!")
        break
    else:
        print("Invalid choice.")

