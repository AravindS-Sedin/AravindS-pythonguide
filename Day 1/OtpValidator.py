import random
otp = random.randint(100000, 999999)
print("Generated OTP:", otp)
count = 3

while count > 0:
    user_otp = int(input("Enter the OTP: "))
    if user_otp == otp:
        print("OTP is valid.")
        break
    else:
        count -= 1
        print(f"Invalid OTP. Attempts Remaining: {count}")

