class FuelTank:
    def __init__(self, capacity: float) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.__capacity = capacity
        self.__level = 0.0

    def get_level(self) -> float:
        return round(self.__level, 2)

    def get_capacity(self) -> float:
        return self.__capacity

    def fill(self, litres: float) -> None:
        """Add fuel to the tank without exceeding capacity."""
        if litres <= 0:
            raise ValueError("Litres must be positive")

        if self.__level + litres > self.__capacity:
            raise ValueError("Tank overflow")

        self.__level += litres

    def consume(self, litres: float) -> None:
        """Remove fuel from the tank if enough fuel is available."""
        if litres <= 0:
            raise ValueError("Litres must be positive")

        if litres > self.__level:
            raise ValueError("Not enough fuel")

        self.__level -= litres

    def fill_to_full(self) -> float:
        """Fill the tank to full capacity and return litres added."""
        litres_added = self.__capacity - self.__level
        self.__level = self.__capacity
        return litres_added

    def percent_full(self) -> float:
        return round((self.__level / self.__capacity) * 100, 1)


if __name__ == "__main__":
    t = FuelTank(50.0)

    print(t.get_level())
    print(t.get_capacity())

    t.fill(20)
    print(t.get_level())

    t.fill(10.5)
    print(t.get_level())

    t.consume(10)
    print(t.get_level())

    print(t.percent_full())

    added = t.fill_to_full()
    print(added)
    print(t.get_level())