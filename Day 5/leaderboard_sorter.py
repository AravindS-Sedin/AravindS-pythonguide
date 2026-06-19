"""
Leaderboard Sorter

Sort a leaderboard by score (highest score first)
using Bubble Sort, Merge Sort, and Quick Sort.

Also compares execution times of each algorithm.

Real-world examples:
- BGMI Leaderboards
- MPL Rankings
- Kahoot Quiz Scores
"""

import random
import time


class LeaderboardSorter:

    def __init__(self, players):
        self.players = players

    # ---------------------------------------------
    # Bubble Sort
    # ---------------------------------------------
    def bubble_sort(self):

        arr = self.players.copy()
        n = len(arr)

        for i in range(n):

            swapped = False

            for j in range(n - i - 1):

                if arr[j]["score"] < arr[j + 1]["score"]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if not swapped:
                break

        return arr

    # ---------------------------------------------
    # Merge Sort
    # ---------------------------------------------
    def merge_sort(self, data=None):

        if data is None:
            data = self.players

        if len(data) <= 1:
            return data

        mid = len(data) // 2

        left = self.merge_sort(data[:mid])
        right = self.merge_sort(data[mid:])

        return self.merge(left, right)

    def merge(self, left, right):

        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if left[i]["score"] >= right[j]["score"]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    # ---------------------------------------------
    # Quick Sort
    # ---------------------------------------------
    def quick_sort(self, data=None):

        if data is None:
            data = self.players

        if len(data) <= 1:
            return data

        pivot = data[len(data) // 2]["score"]

        greater = []
        equal = []
        less = []

        for player in data:

            if player["score"] > pivot:
                greater.append(player)

            elif player["score"] < pivot:
                less.append(player)

            else:
                equal.append(player)

        return (
            self.quick_sort(greater)
            + equal
            + self.quick_sort(less)
        )

    # ---------------------------------------------
    # Benchmark Utility
    # ---------------------------------------------
    def benchmark(self, sort_function):

        start = time.perf_counter()

        sort_function()

        end = time.perf_counter()

        return end - start

    # ---------------------------------------------
    # Compare Algorithms
    # ---------------------------------------------
    def compare_sorts(self):

        algorithms = [
            ("Bubble Sort", self.bubble_sort),
            ("Merge Sort", self.merge_sort),
            ("Quick Sort", self.quick_sort)
        ]

        print("\nExecution Times")
        print("-" * 35)

        for name, func in algorithms:

            duration = self.benchmark(func)

            print(f"{name:<15}: {duration:.6f} seconds")

    # ---------------------------------------------
    # Display Leaderboard
    # ---------------------------------------------
    def display_top_players(self, sorted_players, top_n=10):

        print("\nTop Players")
        print("-" * 25)

        for player in sorted_players[:top_n]:

            print(
                f"{player['name']:<12}"
                f"{player['score']}"
            )


def main():

    players = [
        {
            "name": f"Player{i}",
            "score": random.randint(100, 10000)
        }
        for i in range(1000)
    ]

    sorter = LeaderboardSorter(players)

    leaderboard = sorter.merge_sort()

    sorter.display_top_players(leaderboard)

    sorter.compare_sorts()


if __name__ == "__main__":
    main()