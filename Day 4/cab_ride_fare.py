# Cab Ride Fare Cache
#
# Features:
# 1. Cache fare calculations using a dictionary.
# 2. Return HIT if route already exists.
# 3. Return MISS if fare needs to be calculated.
# 4. Track search frequency.
# 5. Display top searched routes.
# 6. Clear cache while preserving frequency data.


class FareCache:

    RATE_PER_KM = 12

    def __init__(self):

        self.cache = {}

        self.frequency = {}

        self.distances = {
            "Pune->Mumbai": 148,
            "Pune->Nashik": 210,
            "Mumbai->Nashik": 165,
            "Pune->Nagpur": 720,
            "Mumbai->Goa": 590,
            "Pune->Kolhapur": 230
        }

    def search(self, route):

        if route not in self.distances:
            print("Route not found")
            return

        self.frequency[route] = (
            self.frequency.get(route, 0) + 1
        )

        if route in self.cache:

            fare = self.cache[route]

            print(
                f"HIT  — {self.format_fare(fare)} "
                f"(instant)"
            )

            return fare

        distance = self.distances[route]

        fare = distance * self.RATE_PER_KM

        self.cache[route] = fare

        print(
            f"MISS — {self.format_fare(fare)} "
            f"[saved to cache]"
        )

        return fare

    def top_routes(self, n):

        print(f"\n------Top {n} Routes------")

        sorted_routes = sorted(
            self.frequency.items(),
            key=lambda item: item[1],
            reverse=True
        )

        for rank, (route, count) in enumerate(
                sorted_routes[:n], start=1):

            print(
                f"{rank}. {route} "
                f"(searched {count}x)"
            )

    def clear_cache(self):

        self.cache.clear()

        print("Cache cleared")

    @staticmethod
    def format_fare(amount):

        return f"Rs.{amount:,}"
    

farecache = FareCache()

farecache.search("Pune->Mumbai")
farecache.search("Pune->Mumbai")
farecache.search("Pune->Nashik")
farecache.search("Pune->Mumbai")

farecache.top_routes(3)