from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, consumption_per_100km: float):
        self.consumption = consumption_per_100km
        self._fuel = 0.0

    def fill_up(self, liters: int):
        self._fuel += liters

    def drive(self, distance: float):
        used_fuel = (distance / 100) * self.consumption
        self._fuel -= used_fuel

    def remaining_fuel(self) -> float:
        return max(0.0, self._fuel)