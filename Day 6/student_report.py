# Student Report Card

# Real-World App: CBSE / Extramarks

# Concepts:
# - Encapsulation
# - Private Attributes (__)
# - @property
# - Validation
# - Operator Overloading (__gt__)

# Features:
# - Student details stored privately
# - Add marks subject-wise
# - Reject invalid marks (<0 or >100)
# - Reject duplicate subjects
# - Read-only percentage and grade
# - Compare students using percentage

class Student:

    def __init__(self, name, roll_no):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = {}

    @property
    def name(self):
        return self.__name

    @property
    def roll_no(self):
        return self.__roll_no

    def add_marks(self, subject, marks):

        if subject in self.__marks:
            print(f"{subject} marks already entered.")
            return

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        self.__marks[subject] = marks

    @property
    def percentage(self):

        if not self.__marks:
            return 0

        total = sum(self.__marks.values())
        return total / len(self.__marks)

    @property
    def grade(self):

        pct = self.percentage

        grades = {
            90: "A+",
            80: "A",
            70: "B",
            60: "C",
            50: "D"
        }

        for cutoff, grade in grades.items():
            if pct >= cutoff:
             return grade

        return "F"

    def display_report(self):

        print("\n----- REPORT CARD -----")
        print(f"Name       : {self.__name}")
        print(f"Roll No    : {self.__roll_no}")

        print("\nMarks:")
        for subject, marks in self.__marks.items():
            print(f"{subject:<10}: {marks}")

        print(f"\nPercentage : {self.percentage:.2f}%")
        print(f"Grade      : {self.grade}")
        print("-----------------------")

    # Compare students using percentage
    def __gt__(self, other):
        return self.percentage > other.percentage


def main():

    s1 = Student("Aravind", 101)

    s1.add_marks("Maths", 95)
    s1.add_marks("Science", 88)
    s1.add_marks("English", 92)

    s1.display_report()


    s2 = Student("Chaitali", 102)

    s2.add_marks("Maths", 80)
    s2.add_marks("Science", 75)
    s2.add_marks("English", 82)

    s2.display_report()

    print()

    if s1 > s2:
        print(f"{s1.name} scored higher.")
    else:
        print(f"{s2.name} scored higher.")


if __name__ == "__main__":
    main()
