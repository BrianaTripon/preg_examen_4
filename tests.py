import unittest

from Controller.controller import Controller
from Repository.bus_repository import BusRepo
from Repository.route_repository import RouteRepo


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.__route_repo = RouteRepo("routes")
        self.__bus_repo = BusRepo("buses")
        self.__controller = Controller(self.__route_repo, self.__bus_repo)

    def test_get_bus_on_route(self):
        buses = self.__controller.get_bus_on_route(5)
        self.assertEqual(buses[0].get_times_used_on_route(), 7)
        self.assertEqual(buses[1].get_times_used_on_route(), 1)
        self.assertNotEqual(buses[1].get_model(), "dacia")

    def test_increase_usage(self):
        usage = self.__controller.increase_usage(1, 1)
        self.assertEqual(usage, 4)
        usage = self.__controller.increase_usage(2, 1)
        self.assertNotEqual(usage, 15)

    def test_compute_travel_distance(self):
        total = self.__controller.compute_travel_distance(1)
        self.assertEqual(total, 30)
        total = self.__controller.compute_travel_distance(3)
        self.assertNotEqual(total, 90)

if __name__ == "__main__":
    unittest.main()

