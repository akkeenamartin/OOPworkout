from c3_types import Car, Truck
from c4_electric import ElectricCar


if __name__ == "__main__":
    c = Car("B-CD-5678", "Toyota", "Yaris", 2023, seats=5)

    print(str(c))
    print(repr(c))

    c2 = Car("B-CD-5678", "Toyota", "Corolla", 2020)
    print(c == c2)

    c3 = Car("B-XX-0000", "Toyota", "Yaris", 2023)
    print(c == c3)

    tr = Truck("B-CD-5678", "MAN", "Other", 2000, payload_kg=1)
    print(c == tr)

    tr2 = Truck("B-EF-9012", "MAN", "TGX", 2021, payload_kg=18000)
    print(repr(tr2))

    e = ElectricCar(
        "B-EV-0001",
        "Tesla",
        "Model 3",
        2024,
        battery_kwh=60.0,
        range_km=400
    )

    print(repr(e))

    vehicles = set()
    vehicles.add(c)
    vehicles.add(c2)

    print(len(vehicles))