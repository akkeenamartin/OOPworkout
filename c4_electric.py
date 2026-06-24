from c1_vehicle import Vehicle


class ElectricCar(Vehicle):
    def __init__(
        self,
        plate: str,
        make: str,
        model: str,
        year: int,
        battery_kwh: float,
        range_km: int
    ) -> None:
        super().__init__(plate, make, model, year)

        if battery_kwh <= 0:
            raise ValueError("Battery capacity must be positive")

        if range_km <= 0:
            raise ValueError("Range must be positive")

        self.battery_kwh = battery_kwh
        self.range_km = range_km
        self.__charge = 0.0

    def get_charge(self) -> float:
        return round(self.__charge, 2)

    def charge(self, kwh: float) -> None:
        """Add charge to the battery without exceeding capacity."""
        if kwh <= 0:
            raise ValueError("Charge amount must be positive")

        if self.__charge + kwh > self.battery_kwh:
            raise ValueError("Battery overflow")

        self.__charge += kwh

    def drive(self, km: int) -> float:
        """Use battery charge first, then increase kilometres if charge is enough."""
        if km <= 0:
            raise ValueError("Kilometres must be positive")

        energy_needed = self.battery_kwh * km / self.range_km

        if energy_needed > self.__charge:
            raise ValueError("Not enough charge")

        self.__charge -= energy_needed
        super().drive(km)

        return energy_needed

    def describe(self) -> str:
        return f"{super().describe()}, electric car"


if __name__ == "__main__":
    e = ElectricCar(
        "B-EV-0001",
        "Tesla",
        "Model 3",
        2024,
        battery_kwh=60.0,
        range_km=400
    )

    print(e.describe())

    e.charge(30)
    print(e.get_charge())

    print(e.drive(100))
    print(e.get_charge())
    print(e.kilometres)

    try:
        e.drive(1000)
    except ValueError as error:
        print("Error caught:", error)

    print(e.get_charge())
    print(e.kilometres)