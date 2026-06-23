# ==================================================
# List Comprehensions & Generator Expressions
#
# Problem:
# Perform common data-processing tasks using
# comprehensions instead of traditional for-loops.
#
# Tasks:
# 1. Squares of even numbers (1-100)
# 2. Flatten a 2D list
# 3. Filter valid emails
# 4. Use a generator for large-scale summation
# 5. Apply discounts using dict comprehension
# 6. Compare list vs generator memory usage
#
# Concepts:
# List Comprehension, Dict Comprehension,
# Generator Expression, Memory Optimization
# ==================================================

import sys


class DataPipeline:

    def __init__(self):

        self.data = [
            "aravind@gmail.com",
            "invalid_email",
            "alice@yahoo.com",
            "missingdot@gmail",
            "sedin@company.org"
        ]

        self.prices = {
            "Laptop": 80000,
            "Mouse": 1200,
            "Keyboard": 2500,
            "Monitor": 15000
        }

        self.matrix = [
            [1, 2],
            [3, 4]
        ]

    def even_squares(self):

        squares = [x ** 2 for x in range(1, 101) if x % 2 == 0]

        print("\n1. Squares of Even Numbers")
        print(squares[:10], "...")

        return squares

    def flatten_2d(self):

        flat = [num for row in self.matrix for num in row]

        print("\n2. Flattened List")
        print(flat)

        return flat

    def filter_emails(self):

        emails = [
            email
            for email in self.data
            if "@" in email and "." in email
        ]

        print("\n3. Valid Emails")
        print(emails)

        return emails

    def generator_sum(self):

        gen = (x ** 2 for x in range(1, 1_000_001))

        total = sum(gen)

        print("\n4. Generator Sum")
        print(f"Sum = {total}")

        return total

    def apply_discount(self):

        discounted = {
            product: round(price * 0.90, 2)
            for product, price in self.prices.items()
        }

        print("\n5. Discounted Prices")
        print(discounted)

        return discounted

    def compare_memory(self):

        lst = [x ** 2 for x in range(100000)]

        gen = (x ** 2 for x in range(100000))

        list_memory = sys.getsizeof(lst)
        generator_memory = sys.getsizeof(gen)

        print("\nMemory Comparison")
        print("-" * 40)

        print(f"List Memory      : {list_memory} bytes")
        print(f"Generator Memory : {generator_memory} bytes")

        ratio = round(list_memory / generator_memory)

        print(f"Generator uses ~{ratio}x less memory")

    def run(self):

        self.even_squares()

        self.flatten_2d()

        self.filter_emails()

        self.generator_sum()

        self.apply_discount()

        self.compare_memory()


def main():

    pipeline = DataPipeline()

    pipeline.run()


if __name__ == "__main__":
    main()