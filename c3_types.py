from c1_vehicle import Vehicle
from c2_tank import FuelTank


class FuelledVehicle(Vehicle):
    def __init__(
        self,
        plate: str,
        make: str,
        model: str,
        year: int,
        capacity: float,
        consumption: float
    ) -> None:
        super().__init__(plate, make, model, year)

        self.tank = FuelTank(capacity)
        self.consumption = consumption

    def refuel(self, litres: float) -> None:
        self.tank.fill(litres)

    def drive(self, km: int) -> float:
        """Consume fuel first, then increase kilometres if fuel is enough."""
        fuel_needed = self.consumption * km / 100

        self.tank.consume(fuel_needed)
        super().drive(km)

        return fuel_needed

    def range_remaining(self) -> float:
        return self.tank.get_level() / self.consumption * 100


class Car(FuelledVehicle):
    def __init__(
        self,
        plate: str,
        make: str,
        model: str,
        year: int,
        seats: int = 5
    ) -> None:
        super().__init__(plate, make, model, year, 50.0, 6.0)
        self.seats = seats

    def describe(self) -> str:
        return f"{super().describe()}, car, {self.seats} seats"


class Truck(FuelledVehicle):
    def __init__(
        self,
        plate: str,
        make: str,
        model: str,
        year: int,
        payload_kg: int
    ) -> None:
        super().__init__(plate, make, model, year, 200.0, 18.0)
        self.payload_kg = payload_kg

    def describe(self) -> str:
        return f"{super().describe()}, truck, {self.payload_kg} kg payload"


class Motorcycle(FuelledVehicle):
    def __init__(self, plate: str, make: str, model: str, year: int) -> None:
        super().__init__(plate, make, model, year, 15.0, 3.5)

    def describe(self) -> str:
        return f"{super().describe()}, motorcycle"


if __name__ == "__main__":
    c = Car("B-CD-5678", "Toyota", "Yaris", 2023, seats=5)
    print(c.describe())

    c.refuel(20)
    print(c.tank.get_level())

    print(c.drive(100))
    print(c.tank.get_level())
    print(c.kilometres)

    tr = Truck("B-EF-9012", "MAN", "TGX", 2021, payload_kg=18000)
    print(tr.describe())

    tr.refuel(150)
    print(tr.drive(100))
    print(tr.tank.get_level())

    m = Motorcycle("B-GH-3456", "Yamaha", "MT-07", 2024)
    print(m.describe())

    m.refuel(10)
    print(m.drive(100))
    print(m.tank.get_level())

    try:
        tr.drive(2000)
    except ValueError as error:
        print("Error caught:", error)

    print(tr.tank.get_level())
    print(tr.kilometres)