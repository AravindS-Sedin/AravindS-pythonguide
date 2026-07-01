"""Example module demonstrating PEP 8 coding standards."""


class Employee:
    """Represents an employee."""

    def __init__(self, name: str) -> None:
        """Initialize an employee with a name."""
        self.name = name

    def print_name(self) -> None:
        """Print the employee's name."""
        print(self.name)


def calculate_salary(hours: int, rate: int) -> int:
    """Calculate salary based on hours worked and hourly rate."""
    salary = hours * rate

    if salary > 0:
        print("Salary calculated successfully.")

    return salary


LONG_MESSAGE = (
    "This is an extremely long string that has been "
    "split across multiple lines to satisfy the "
    "maximum line length recommended by PEP 8."
)


employee = Employee("Aravind")
employee.print_name()

print(calculate_salary(40, 100))
print(LONG_MESSAGE)
