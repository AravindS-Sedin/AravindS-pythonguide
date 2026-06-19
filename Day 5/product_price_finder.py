# Product Price Finder
# Compare Linear Search and Binary Search on a sorted price list.
# Measures execution time for finding a target price using
# time.perf_counter().
#
# Linear Search  -> O(n)
# Binary Search  -> O(log n)
#
# Demonstrates why Binary Search is preferred for searching
# large sorted datasets such as product prices in e-commerce
# applications.



import timeit


class ProductPriceFinder:

    def __init__(self, prices):
        self.prices = sorted(prices)

    # Linear Search (Exact Match)
    def linear_search(self, target):

        for price in self.prices:
            if price == target:
                return price

        return -1

    # Iterative Binary Search (Closest Price)
    def find_closest_iterative(self, target):

        left = 0
        right = len(self.prices) - 1

        while left <= right:

            mid = (left + right) // 2

            if self.prices[mid] == target:
                return self.prices[mid]

            elif self.prices[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        # Target is larger than all elements
        if left >= len(self.prices):
            return self.prices[right]

        # Target is smaller than all elements
        if right < 0:
            return self.prices[left]

        # Compare neighbors
        if abs(self.prices[left] - target) < abs(self.prices[right] - target):
            return self.prices[left]

        return self.prices[right]

    # Recursive Binary Search (Closest Price)
    def find_closest_recursive(self, target, left, right):

        # Target not found
        if left > right:

            # Target is larger than all elements
            if left >= len(self.prices):
                return self.prices[right]

            # Target is smaller than all elements
            if right < 0:
                return self.prices[left]

            # Compare neighbors
            if abs(self.prices[left] - target) < abs(self.prices[right] - target):
                return self.prices[left]

            return self.prices[right]

        mid = (left + right) // 2

        if self.prices[mid] == target:
            return self.prices[mid]

        elif self.prices[mid] < target:
            return self.find_closest_recursive(
                target,
                mid + 1,
                right
            )

        else:
            return self.find_closest_recursive(
                target,
                left,
                mid - 1
            )

    # Benchmark Comparison
    def benchmark(self, target):

        linear_time = timeit.timeit(
            lambda: self.linear_search(target),
            number=100
        )

        iterative_time = timeit.timeit(
            lambda: self.find_closest_iterative(target),
            number=100
        )

        recursive_time = timeit.timeit(
            lambda: self.find_closest_recursive(
                target,
                0,
                len(self.prices) - 1
            ),
            number=100
        )

        print("\n--- Benchmark Results ---")
        print(f"Linear Search      : {linear_time:.6f} seconds")
        print(f"Iterative Binary Search      : {iterative_time:.6f} seconds")
        print(f"Recursive Binary Search      : {recursive_time:.6f} seconds")


def main():

    prices = [100, 200, 300, 400]
    finder = ProductPriceFinder(prices)

    target = 250

    print("Price List:", prices)
    print("Target:", target)

    print(
        "\nClosest Price (Iterative):",
        finder.find_closest_iterative(target)
    )

    print(
        "Closest Price (Recursive):",
        finder.find_closest_recursive(
            target,
            0,
            len(finder.prices) - 1
        )
    )

    # Large dataset for benchmarking
    large_dataset = ProductPriceFinder(
        list(range(1, 1_000_001))
    )

    large_dataset.benchmark(999_999)


if __name__ == "__main__":
    main()


# benchmark linear vs binary search
# import time
# prices = list(range(1, 1_000_001))
# target = 999_999

# # Linear Search
# start = time.perf_counter()
# linear_search(prices, target)
# linear_time = time.perf_counter() - start

# # Binary Search
# start = time.perf_counter()
# find_closest_recursive(prices, target, 0, len(prices) - 1)
# binary_time = time.perf_counter() - start

# print(f"Linear Search : {linear_time:.6f}s")
# print(f"Binary Search : {binary_time:.6f}s")

# benchmark linear vs binary search
# import timeit

# prices = list(range(1, 1_000_001))
# target = 999_999

# # Measure Linear Search
# linear_time = timeit.timeit(
#     lambda: linear_search(prices, target),
#     number=100
# )

# # Measure Binary Search
# binary_time = timeit.timeit(
#     lambda: find_closest_recursive(prices, target, 0, len(prices) - 1),
#     number=100
# )

# print(f"Linear Search (100 runs): {linear_time:.6f} seconds")
# print(f"Binary Search (100 runs): {binary_time:.6f} seconds")


# benchmark linear vs binary search
# import time
# prices = list(range(1, 1_000_001))
# target = 999_999

# # Linear Search
# start = time.perf_counter()
# linear_search(prices, target)
# linear_time = time.perf_counter() - start

# # Binary Search
# start = time.perf_counter()
# find_closest_recursive(prices, target, 0, len(prices) - 1)
# binary_time = time.perf_counter() - start

# print(f"Linear Search : {linear_time:.6f}s")
# print(f"Binary Search : {binary_time:.6f}s")