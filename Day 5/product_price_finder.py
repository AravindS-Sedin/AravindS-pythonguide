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



# iterative binary search to find closest price

def find_closest_iterative(prices, target):
    left = 0
    right = len(prices) - 1

    while left <= right:
        mid = (left + right) // 2

        if prices[mid] == target:
            return prices[mid]

        elif prices[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    # Target is larger than all elements
    if left >= len(prices):
        return prices[right]

    # Target is smaller than all elements
    if right < 0:
        return prices[left]

    # Compare neighbors
    if abs(prices[left] - target) < abs(prices[right] - target):
        return prices[left]

    return prices[right]



# recursive binary search to find closest price

def find_closest_recursive(prices, target, left, right):

    # Target not found
    if left > right:

        # Target is larger than all elements
        if left >= len(prices):
            return prices[right]

        # Target is smaller than all elements
        if right < 0:
            return prices[left]

        # Compare the two neighbors
        if abs(prices[left] - target) < abs(prices[right] - target):
            return prices[left]

        return prices[right]

    mid = (left + right) // 2

    if prices[mid] == target:
        return prices[mid]

    elif prices[mid] < target:
        return find_closest_recursive(
            prices,
            target,
            mid + 1,
            right
        )

    else:
        return find_closest_recursive(
            prices,
            target,
            left,
            mid - 1
        )

# Linear Search (for comparison)

def linear_search(prices, target):
    for i, price in enumerate(prices):
        if price == target:
            return price
    return -1

# def main():
#     prices = [100, 200, 300, 400]
#     target = 250

#     #iterative search
#     print("Closest price:", find_closest_iterative(prices, target))

#     #recursive search
#     closest = find_closest_recursive(
#         prices,
#         target,
#         0,
#         len(prices) - 1
#     )
#     print("Closest price:", closest)


# if __name__ == "__main__":
#     main()


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
import timeit

prices = list(range(1, 1_000_001))
target = 999_999

# Measure Linear Search
linear_time = timeit.timeit(
    lambda: linear_search(prices, target),
    number=100
)

# Measure Binary Search
binary_time = timeit.timeit(
    lambda: find_closest_recursive(prices, target, 0, len(prices) - 1),
    number=100
)

print(f"Linear Search (100 runs): {linear_time:.6f} seconds")
print(f"Binary Search (100 runs): {binary_time:.6f} seconds")