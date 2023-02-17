from Domain.route import Route


class RouteRepo:
    def __init__(self, file_name):
        self.__routes = []
        file = open(file_name, "r")
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(',')
            self.__routes.append(Route(int(line[0]), int(line[1])))
        file.close()

    def get_all_routes(self):
        return self.__routes[:]

    def get_route_by_code(self, route_code):
        for route in self.get_all_routes():
            if route.get_code() == route_code:
                return route
