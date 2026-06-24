from c1_vehicle import Vehicle
from c3_types import Car, Truck, Motorcycle
from c4_electric import ElectricCar


class Fleet:
    def __init__(self, name: str) -> None:
        self.name = name
        self._vehicles = []

    def add(self, vehicle: Vehicle) -> None:
        """Add a vehicle if another vehicle with the same plate is not already present."""
        if vehicle.plate in self:
            raise ValueError("Vehicle with this plate already exists")

        self._vehicles.append(vehicle)

    def remove(self, plate: str) -> None:
        """Remove a vehicle by plate or raise KeyError if not found."""
        vehicle = self.find(plate)

        if vehicle is None:
            raise KeyError("Plate not found")

        self._vehicles.remove(vehicle)

    def find(self, plate: str) -> Vehicle | None:
        for vehicle in self._vehicles:
            if vehicle.plate == plate:
                return vehicle

        return None

    def total_kilometres(self) -> int:
        total = 0

        for vehicle in self._vehicles:
            total += vehicle.kilometres

        return total

    def drive_all(self, km: int) -> tuple[list, list]:
        """Try to drive every vehicle and collect successful and failed attempts."""
        successes = []
        failures = []

        for vehicle in self._vehicles:
            try:
                vehicle.drive(km)
                successes.append(vehicle.plate)
            except ValueError as error:
                failures.append((vehicle.plate, str(error)))

        return successes, failures

    def __len__(self) -> int:
        return len(self._vehicles)

    def __iter__(self):
        return iter(self._vehicles)

    def __contains__(self, plate: str) -> bool:
        return self.find(plate) is not None

    def __str__(self) -> str:
        return f"Fleet '{self.name}': {len(self)} vehicle(s)"


def print_summary(fleet: Fleet) -> None:
    print("=== FLEET REPORT ===")
    print(fleet)
    print("Total kilometres:", fleet.total_kilometres())
    print("--------------------")

    for vehicle in fleet:
        print(vehicle)

    print("====================")


if __name__ == "__main__":
    fleet = Fleet("Main")

    car = Car("B-1", "Toyota", "Yaris", 2023, seats=5)
    truck = Truck("B-2", "MAN", "TGX", 2021, payload_kg=18000)
    motorcycle = Motorcycle("B-3", "Yamaha", "MT-07", 2024)
    electric = ElectricCar(
        "B-4",
        "Tesla",
        "Model 3",
        2024,
        battery_kwh=60.0,
        range_km=400
    )

    fleet.add(car)
    fleet.add(truck)
    fleet.add(motorcycle)
    fleet.add(electric)

    print(len(fleet))
    print("B-2" in fleet)
    print("B-99" in fleet)

    print(fleet.find("B-3").make)
    print(fleet.find("B-99"))

    try:
        fleet.add(Car("B-1", "Foo", "Bar", 2000))
    except ValueError as error:
        print("Error caught:", error)

    successes, failures = fleet.drive_all(10)
    print(successes)
    print(failures)

    car.refuel(5)
    truck.refuel(5)
    motorcycle.refuel(5)
    electric.charge(20)

    successes, failures = fleet.drive_all(10)
    print(successes)
    print(failures)

    print(fleet.total_kilometres())

    fleet.remove("B-3")
    print(len(fleet))
    print("B-3" in fleet)

    try:
        fleet.remove("B-99")
    except KeyError as error:
        print("Error caught:", error)

    print_summary(fleet)