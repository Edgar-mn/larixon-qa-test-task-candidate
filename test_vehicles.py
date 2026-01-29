import unittest
from car import Car
from track import Track

class TestVehicles(unittest.TestCase):
    
    def test_car_consumption(self):
        # 7L per 100km, 500km distance = 35L used
        car = Car(7)
        car.fill_up(80)
        car.drive(500)
        self.assertEqual(car.remaining_fuel(), 45.0)

    def test_track_consumption(self):
        # 15L * 2 trailers = 30L per 100km. 500km distance = 150L used
        track = Track(15, 2)
        track.fill_up(250)
        track.drive(500)
        self.assertEqual(track.remaining_fuel(), 100.0)

    def test_zero_fuel_remaining(self):
        # Testing if fuel doesn't go negative if we drive too far
        car = Car(10)
        car.fill_up(5)
        car.drive(100) # Should use 10L, but only has 5L
        self.assertEqual(car.remaining_fuel(), 0.0)

if __name__ == "__main__":
    unittest.main()