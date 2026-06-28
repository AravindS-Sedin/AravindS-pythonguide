# ==================================================
# Context Managers & Resource Handling
#
# Tasks:
# 1. Build a FileHandler context manager using
#    __enter__() and __exit__()
# 2. Build a MySQL database connection context
#    manager using @contextmanager
# 3. Ensure cleanup happens even on exceptions
# 4. Suppress exceptions in FileHandler using
#    return True
# 5. Bonus: Timer context manager
#
# Concepts:
# Context Manager, Resource Cleanup,
# __enter__, __exit__, contextlib,
# Generator-Based Context Managers
# ==================================================

import time
import mysql.connector

from contextlib import contextmanager


class FileHandler:

    def __init__(self, filename, mode):

        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):

        print(f"Opening file: {self.filename}")

        self.file = open(self.filename, self.mode)

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):

        print("Executing cleanup...")

        if self.file:
            self.file.close()
            print("File closed")

        if exc_type:
            print(f"Error handled: {exc_val}")

        return True


@contextmanager
def db_connection():

    conn = None

    try:

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="expense_tracker"
        )

        print("Database Connected")

        yield conn

    finally:

        if conn and conn.is_connected():

            conn.close()

            print("Connection Closed")


class Timer:

    def __enter__(self):

        self.start_time = time.perf_counter()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        end_time = time.perf_counter()

        print(
            f"Execution Time: "
            f"{end_time - self.start_time:.6f} seconds"
        )

        return False


def test_file_handler():

    print("\n========== File Handler Demo ==========")
    print("-" * 40)

    with FileHandler("sample.txt", "w") as file:

        file.write("Hello Context Manager")

        raise ValueError(
            "Deliberate file processing error"
        )

    print("-" * 40)


def test_db_connection():

    print("\n======= Database Connection Demo =======")
    print("-" * 40)

    try:

        with db_connection() as conn:

            cursor = conn.cursor()

            cursor.execute("SHOW TABLES")

            tables = cursor.fetchall()

            print("\nTables in Database:")

            for table in tables:
                print(table[0])

            print()

            raise RuntimeError(
                "Database query failed"
            )

    except Exception as error:

        print(f"Error: {error}")

    print("-" * 40)


def test_timer():

    print("\n============== Timer Demo ==============")
    print("-" * 40)

    with Timer():

        total = sum(
            x * x
            for x in range(1_000_000)
        )

        print("Calculation completed")


def main():

    test_file_handler()

    test_db_connection()

    test_timer()


if __name__ == "__main__":
    main()