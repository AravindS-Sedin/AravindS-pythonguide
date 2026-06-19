"""
File System Size Calculator using Recursion

Features:
1. Calculate total folder size recursively.
2. Print folder structure like the tree command.
3. Display sizes in KB / MB / GB.
4. Demonstrate recursion using Factorial.
5. Demonstrate recursion using Fibonacci.
6. Fibonacci uses memoization (dictionary cache).

Real-world Applications:
- Windows Folder Properties
- macOS Storage Analyzer
- Linux tree/du commands
- File explorers and backup tools
"""


import os


class RecursionDemo:

    # Convert bytes into readable form
    @staticmethod
    def format_size(size):

        units = ["B", "KB", "MB", "GB", "TB"]

        for unit in units:
            if size < 1024:
                return f"{size:.2f} {unit}"

            size /= 1024

        return f"{size:.2f} PB"

   
    # Recursive Folder Size
    def folder_size(self, path):

        total = 0

        for entry in os.scandir(path):

            if entry.is_file():

                total += entry.stat().st_size

            elif entry.is_dir():

                total += self.folder_size(entry.path)

        return total


    # Print Folder Tree
    def print_tree(self, path, indent=0):

        print("  " * indent + os.path.basename(path))

        try:

            for entry in os.scandir(path):

                if entry.is_file():

                    size = self.format_size(
                        entry.stat().st_size
                    )

                    print(
                        "  " * (indent + 1)
                        + f"{entry.name} ({size})"
                    )

                elif entry.is_dir():

                    self.print_tree(
                        entry.path,
                        indent + 1
                    )

        except PermissionError:

            print(
                "  " * (indent + 1)
                + "[Permission Denied]"
            )


    # Factorial Recursion
    def factorial(self, n):

        # Base Case
        if n <= 1:
            return 1

        # Recursive Case
        return n * self.factorial(n - 1)


    # Fibonacci with Memoization
    def fibonacci(self, n, cache=None):

        if cache is None:
            cache = {0: 0, 1: 1}

        # Already computed
        if n in cache:
            return cache[n]

        cache[n] = (
            self.fibonacci(n - 1, cache)
            + self.fibonacci(n - 2, cache)
        )

        return cache[n]


def main():

    demo = RecursionDemo()

    print("=" * 50)
    print("RECURSION - FILE SYSTEM SIZE CALCULATOR")
    print("=" * 50)

    folder_path = input(
        "Enter folder path: "
    )

    if not os.path.exists(folder_path):

        print("Path does not exist.")
        return

    print("\nFolder Structure:")
    print("-" * 50)

    demo.print_tree(folder_path)

    total_size = demo.folder_size(folder_path)

    print("\nTotal Folder Size:")
    print(
        demo.format_size(total_size)
    )

    print("\nFactorial Example")
    print("5! =", demo.factorial(5))

    print("\nFibonacci Example")
    print("Fib(10) =", demo.fibonacci(10))


if __name__ == "__main__":
    main()