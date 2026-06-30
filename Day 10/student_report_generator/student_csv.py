import csv
import glob
from pathlib import Path


class StudentReportGenerator:

    GRADES = {
        90: "A",
        80: "B",
        70: "C",
        60: "D",
        50: "E"
    }

    def read_students(self, filepath):
        students = []

        with open(filepath, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:

                marks = [
                    int(row["maths"]),
                    int(row["science"]),
                    int(row["english"]),
                    int(row["history"]),
                    int(row["pe"])
                ]

                total = sum(marks)
                percentage = total / len(marks)

                row["total"] = total
                row["percentage"] = round(percentage, 2)
                row["grade"] = self.calculate_grade(percentage)

                students.append(row)

        return students


    def calculate_grade(self, percentage):
        for cutoff, grade in self.GRADES.items():
            if percentage >= cutoff:
                return grade
        return "F"


    def write_results(self, students, output_file):

        Path("results").mkdir(exist_ok=True)

        fields = [
            "name",
            "roll_no",
            "total",
            "percentage",
            "grade"
        ]

        with open(output_file, "w", newline="") as file:

            writer = csv.DictWriter(file, fieldnames=fields)

            writer.writeheader()

            for student in students:

                writer.writerow({
                    "name": student["name"],
                    "roll_no": student["roll_no"],
                    "total": student["total"],
                    "percentage": student["percentage"],
                    "grade": student["grade"]
                })


    def process_files(self):

        for filepath in glob.glob("data/*.csv"):

            print(f"Processing {filepath}")

            students = self.read_students(filepath)

            output = f"results/{Path(filepath).stem}_results.csv"

            self.write_results(students, output)

        print("\nAll files processed successfully.")


def main():

    report_generator = StudentReportGenerator()
    report_generator.process_files()


if __name__ == "__main__":
    main()