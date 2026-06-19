# N-Queen Problem
#
# Place N queens on an N x N chessboard such that:
# 1. No two queens are in the same column.
# 2. No two queens are in the same diagonal.
# 3. One queen is placed in each row.
#
# Backtracking Approach:
# - Place a queen row by row.
# - Try every column in the current row.
# - If the position is safe, place the queen.
# - Recursively solve the next row.
# - If no solution is possible, remove the queen and try another column.


class NQueenSolver:

    def __init__(self, n):
        self.n = n
        self.board = []      # Stores queen column positions
        self.result = []     # Stores all valid solutions

    def is_safe(self, row, col):

        for r in range(len(self.board)):
            c = self.board[r]

            # Same column
            if c == col:
                return False

            # Same diagonal
            if abs(r - row) == abs(c - col):
                return False

        return True

    def solve(self, row):

        # All queens placed successfully
        if row == self.n:
            self.result.append([col + 1 for col in self.board])
            return

        # Try every column in current row
        for col in range(self.n):

            if self.is_safe(row, col):

                # Place queen
                self.board.append(col)

                # Solve next row
                self.solve(row + 1)

                # Backtrack
                self.board.pop()

    def get_solutions(self):

        self.solve(0)
        return self.result


def main():

    n = int(input("Enter N: "))

    solver = NQueenSolver(n)
    solutions = solver.get_solutions()

    print(f"\nTotal Solutions: {len(solutions)}")

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()