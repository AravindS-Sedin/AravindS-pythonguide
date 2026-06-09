marks = []
grades = []

print("Enter marks for 5 subjects:")

for i in range (1,6):
    mark = float(input(f"Subject {i}: "))
    marks.append(mark)

total = 0
for mark in marks:
    total += mark

percentage = (total / 500) * 100

for mark in marks:
    if mark <= 100 and mark >= 91:
        grade = 'A'
    elif mark <= 90 and mark >= 81:
        grade = 'B'
    elif mark <= 80 and mark >= 71:
        grade = 'C'
    elif mark <= 70 and mark >= 61:
        grade = 'D'
    else:
        grade = 'F'
    grades.append(grade)

print("\n--- Grade Report ---")
print(f"Total: {total}")
print(f"Percentage: {percentage:.2f}%")

for i in range (1,6):
    if grades[i-1] != 'F':
        print(f"Subject {i}: {marks[i-1]}  {grades[i-1]}")
    else:
        print(f"Subject {i}: {marks[i-1]}  {grades[i-1]}  - Fail")
