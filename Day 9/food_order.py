# ============================================================
# Pydantic Food Order Validator
# ============================================================
#
# Objective:
# Validate food orders using Pydantic models.
#
# Concepts Covered:
# - BaseModel
# - Field Constraints
# - Enum
# - Optional Fields
# - Custom Validators
# - ValidationError
#
# Features:
# - Validate customer details
# - Validate order items
# - Restrict payment methods
# - Validate tip amount
# - Ensure order total > 0
# - Display structured validation errors
#
# Real World Usage:
# Similar validation is used in:
# - Swiggy
# - Zomato
# - Uber Eats
# ============================================================


from pydantic import BaseModel, Field, validator, ValidationError
from typing import List, Optional
from enum import Enum


# Restricts payment method to predefined values
class PaymentMethod(str, Enum):
    UPI = "upi"
    CARD = "card"
    CASH = "cash"


# Represents a single food item in an order
class OrderItem(BaseModel):

    name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    quantity: int = Field(
        ...,
        ge=1,
        le=20
    )

    price: float = Field(
        ...,
        gt=0
    )


# Represents complete food order
class Order(BaseModel):

    customer_name: str = Field(
        ...,
        min_length=2
    )

    items: List[OrderItem] = Field(
        ...,
        min_items=1
    )

    delivery_address: str = Field(
        ...,
        min_length=10
    )

    payment_method: PaymentMethod

    tip: Optional[float] = Field(
        default=None,
        ge=0,
        le=500
    )

    @validator("items")
    def total_must_be_positive(
        cls,
        items: List[OrderItem]
    ) -> List[OrderItem]:

        total = sum(
            item.price * item.quantity
            for item in items
        )

        if total <= 0:
            raise ValueError(
                "Order total must be greater than 0"
            )

        return items

    def total_amount(self) -> float:

        total = sum(
            item.price * item.quantity
            for item in self.items
        )

        if self.tip:
            total += self.tip

        return total
    
    def display_order(self) -> None:

        print("\n----- ORDER SUMMARY -----")

        print(f"Customer : {self.customer_name}")
        print(f"Address  : {self.delivery_address}")
        print(f"Payment  : {self.payment_method.value}")

        print("\nItems:")

        subtotal = 0.0

        for item in self.items:

            item_total = item.quantity * item.price
            subtotal += item_total

            print(
                f"{item.name:}"
                f"{item.quantity:} x "
                f"Rs.{item.price:.2f} "
                f"= Rs.{item_total:.2f}"
            )

        print("-" * 40)

        print(f"Subtotal : Rs.{subtotal:.2f}")

        if self.tip:
            print(f"Tip      : Rs.{self.tip:.2f}")

        print(f"Total    : Rs.{self.total_amount():.2f}")


def main() -> None:

    print("VALID ORDER")
    print("-" * 50)

    try:

        order = Order(
            customer_name="Aravind",
            items=[
                OrderItem(
                    name="Pizza",
                    quantity=2,
                    price=250
                ),
                OrderItem(
                    name="Burger",
                    quantity=1,
                    price=150
                )
            ],
            delivery_address="12 Gandhi Street Chennai",
            payment_method=PaymentMethod.UPI,
            tip=50
        )

        order.display_order()

    except ValidationError as e:
        print(e.json(indent=2))

    print("\nINVALID ORDER")
    print("-" * 50)

    try:

        bad_order = Order(
            customer_name="A",
            items=[
                OrderItem(
                    name="",
                    quantity=0,
                    price=-100
                )
            ],
            delivery_address="Short",
            payment_method="bitcoin",
            tip=1000
        )

        bad_order.display_order()

    except ValidationError as e:
        print(e.json(indent=2))


if __name__ == "__main__":
    main()