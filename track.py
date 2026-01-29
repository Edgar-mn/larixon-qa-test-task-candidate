from vehicle import Vehicle

class Track(Vehicle):
    def __init__(self, consumption_per_trailer: float, trailers_count: int):
        # По условию: расход прямо пропорционален количеству прицепов
        self.total_consumption = consumption_per_trailer * trailers_count
        self._fuel = 0.0

    def fill_up(self, liters: int):
        self._fuel += liters

    def drive(self, distance: float):
        used_fuel = (distance / 100) * self.total_consumption
        self._fuel -= used_fuel

    def remaining_fuel(self) -> float:
        return max(0.0, self._fuel)