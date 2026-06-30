"""
Cab Fare Calculator

This module provides utility functions to calculate cab fares,
apply discounts, and generate trip summaries.

The module demonstrates:
- Google-style docstrings
- Type hints
- help()
- doctest examples
- pydoc documentation
"""


def calculate_fare(distance: float, vehicle: str) -> float:
    """
    Calculate cab fare based on distance and vehicle type.

    Args:
        distance (float): Trip distance in kilometers.
        vehicle (str): Vehicle type ("car", "bike", or "auto").

    Returns:
        float: Total fare in Indian Rupees.

    Raises:
        ValueError: If the distance is negative.
        ValueError: If the vehicle type is invalid.

    Example:
        >>> calculate_fare(10, "car")
        200.0
        >>> calculate_fare(5, "bike")
        50.0
    """

    if distance < 0:
        raise ValueError("Distance cannot be negative.")

    rates = {
        "car": 20,
        "bike": 10,
        "auto": 15
    }

    if vehicle not in rates:
        raise ValueError("Invalid vehicle type.")

    return distance * rates[vehicle]


def apply_discount(fare: float, discount: float) -> float:
    """
    Apply percentage discount to the fare.

    Args:
        fare (float): Original fare.
        discount (float): Discount percentage.

    Returns:
        float: Discounted fare.

    Raises:
        ValueError: If discount is not between 0 and 100.

    Example:
        >>> apply_discount(200, 10)
        180.0
        >>> apply_discount(500, 20)
        400.0
    """

    if not (0 <= discount <= 100):
        raise ValueError("Discount must be between 0 and 100.")

    return fare - (fare * discount / 100)


def trip_summary(distance: float, vehicle: str, discount: float = 0) -> str:
    """
    Generate a formatted trip summary.

    Args:
        distance (float): Distance traveled.
        vehicle (str): Vehicle type.
        discount (float): Discount percentage.

    Returns:
        str: Multi-line trip summary.

    Raises:
        ValueError: If any invalid value is supplied.

    Example:
        >>> print(trip_summary(10, "car", 10))
        Vehicle : car
        Distance: 10 km
        Fare    : Rs.180.0
    """

    fare = calculate_fare(distance, vehicle)
    fare = apply_discount(fare, discount)

    return (
        f"Vehicle : {vehicle}\n"
        f"Distance: {distance} km\n"
        f"Fare    : Rs.{fare}"
    )


def main():
    """
    Demonstrate the fare calculator.

    Returns:
        None
        
    """

    print(trip_summary(15, "car", 10))


if __name__ == "__main__":
    main()