class Controller:
    def __init__(self, route_repo, bus_repo):
        self.__route_repo = route_repo
        self.__bus_repo = bus_repo

    def get_bus_on_route(self, route_code):
        buses_on_route = []
        buses = self.__bus_repo.get_all_buses()
        for bus in buses:
            if bus.get_route_code() == route_code:
                buses_on_route.append(bus)
        return buses_on_route[:]

    def increase_usage(self, bus_id, route_code):
        buses = self.__bus_repo.get_all_buses()
        usage = 0
        for bus in buses:
            if bus.get_bus_id() == bus_id and bus.get_route_code() == route_code:
                usage = bus.get_times_used_on_route()
                usage += 1
        return usage

    def compute_travel_distance(self, bus_id):
        total = 0
        bus = self.__bus_repo.get_bus_by_id(bus_id)
        route_code = bus.get_route_code()
        route = self.__route_repo.get_route_by_code(route_code)
        length = route.get_length()
        times_used = bus.get_times_used_on_route()
        total = total + length * times_used
        return total


