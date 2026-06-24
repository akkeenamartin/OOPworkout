class Vehicle:
    fleet_size = 0

    def __init__(self, plate: str, make: str, model: str, year: int) -> None:
        self.plate = plate
        self.make = make
        self.model = model
        self.year = year
        self.kilometres = 0

        Vehicle.fleet_size += 1

    def drive(self, km: int) -> None:
        if km <= 0:
            raise ValueError("Kilometres must be positive")

        self.kilometres += km

    def describe(self) -> str:
        return f"{self.year} {self.make} {self.model} ({self.plate})"

    def service_due(self) -> bool:
        return self.kilometres > 15000

    def __str__(self) -> str:
        return self.describe()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.plate!r}, {self.make!r}, {self.model!r}, {self.year!r})"

    def __eq__(self, other) -> bool:
        if not hasattr(other, "plate"):
            return False

        return self.plate == other.plate

    def __hash__(self) -> int:
        return hash(self.plate)


if __name__ == "__main__":
    v = Vehicle("B-AB-1234", "Volkswagen", "Golf", 2022)

    print(v.plate)
    print(v.kilometres)

    v.drive(50)
    print(v.kilometres)

    v.drive(120)
    print(v.kilometres)

    print(v.describe())
    print(v.service_due())
    print(Vehicle.fleet_size)