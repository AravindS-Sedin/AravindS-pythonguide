# Vehicle Fleet System

# Build a fare calculator using inheritance and polymorphism.

# Vehicle -> Base Class
# Car, Bike, Auto -> Child Classes
# fare() -> Overridden in each child
# trip_summary() -> Defined once in Vehicle
# super() -> Reuse parent constructor
# SurgePricedCar -> Applies 1.5x surge pricing


class Vehicle:

    def __init__(self, vehicle_no):
        self.vehicle_no = vehicle_no

    def fare(self, distance):
        raise NotImplementedError(
            "Child class must implement fare()"
        )

    def trip_summary(self, distance):
        total_fare = self.fare(distance)

        print("\n----- TRIP SUMMARY -----")
        print(f"Vehicle Type : {self.__class__.__name__}")
        print(f"Vehicle No   : {self.vehicle_no}")
        print(f"Distance     : {distance} km")
        print(f"Total Fare   : Rs.{total_fare:.2f}")


class Car(Vehicle):

    BASE_FARE = 50
    RATE_PER_KM = 15

    def __init__(self, vehicle_no):
        super().__init__(vehicle_no)

    def fare(self, distance):
        return self.BASE_FARE + (distance * self.RATE_PER_KM)


class Bike(Vehicle):

    BASE_FARE = 20
    RATE_PER_KM = 8

    def __init__(self, vehicle_no):
        super().__init__(vehicle_no)

    def fare(self, distance):
        return self.BASE_FARE + (distance * self.RATE_PER_KM)


class Auto(Vehicle):

    BASE_FARE = 30
    RATE_PER_KM = 10

    def __init__(self, vehicle_no):
        super().__init__(vehicle_no)

    def fare(self, distance):
        return self.BASE_FARE + (distance * self.RATE_PER_KM)


class SurgePricedCar(Car):

    SURGE_MULTIPLIER = 1.5

    def fare(self, distance):
        normal_fare = super().fare(distance)
        return normal_fare * self.SURGE_MULTIPLIER


def main():

    vehicles = [
        Car("TN01AB1234"),
        Bike("TN02CD5678"),
        Auto("TN03EF9876"),
        SurgePricedCar("TN04GH1111")
    ]

    distance = 10

    for vehicle in vehicles:
        vehicle.trip_summary(distance)


if __name__ == "__main__":
    main()