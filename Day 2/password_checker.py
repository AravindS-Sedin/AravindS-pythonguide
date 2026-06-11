# Password Strength Checker
# Check whether a password contains:
# - At least 8 characters
# - Uppercase letter
# - Lowercase letter
# - Digit
# - Special character
# Calculate a strength score and classify it as
# Weak, Medium, or Strong.
# Show suggestions to improve the password if needed.


password = input("Enter password: ")

length_ok = len(password) >= 8
upper_ok = False
lower_ok = False
digit_ok = False
special_ok = False

for ch in password:
    if ch.isupper():
        upper_ok = True
    elif ch.islower():
        lower_ok = True
    elif ch.isdigit():
        digit_ok = True
    else:
        special_ok = True

score = sum([length_ok, upper_ok, lower_ok, digit_ok, special_ok])

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("\n--- Password Report ---")
print(f"Length : {'OK' if length_ok else 'Missing'}")
print(f"Upper  : {'OK' if upper_ok else 'Missing'}")
print(f"Lower  : {'OK' if lower_ok else 'Missing'}")
print(f"Digit  : {'OK' if digit_ok else 'Missing'}")
print(f"Special: {'OK' if special_ok else 'Missing'}")
print(f"\nStrength: {strength} ({score}/5)")

if strength == "Strong":
    print("Your password is secure!")
else:
    print("\nTips to improve:")

    if not length_ok:
        print("- Use at least 8 characters")
    if not upper_ok:
        print("- Add an uppercase letter")
    if not lower_ok:
        print("- Add a lowercase letter")
    if not digit_ok:
        print("- Add a digit")
    if not special_ok:
        print("- Add a special character")