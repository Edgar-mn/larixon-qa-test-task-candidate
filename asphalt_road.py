from typing import List
from vehicle import Vehicle

class AsphaltRoad:
    def __init__(self):
        self.vehicles: List[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def fill_up(self, vehicle: Vehicle, liters: int):
        vehicle.fill_up(liters)

    def drive(self, vehicle: Vehicle, distance: float):
        vehicle.drive(distance)

    def print_vehicle_remaining_fuels(self):
        for vehicle in self.vehicles:
            # This line gets the name of the class (e.g., 'Car' or 'Track')
            class_name = vehicle.__class__.__name__
            print(f"{class_name} remaining fuel: {vehicle.remaining_fuel()}")