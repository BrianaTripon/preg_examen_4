
class UI:
    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def print_menu():
        print("1. Display all buses from a given route.")
        print("2. Increase usage.")
        print("3. Total distance of a bus.")
        print("0. Exit.")

    def start(self):
        while True:
            self.print_menu()
            option = input("Enter option: ").strip()
            if option == '1':
                route_code = int(input("Enter the route code for which you want to see all the buses: "))
                buses = self.__controller.get_bus_on_route(route_code)
                if buses == []:
                    print("No buses on this route!")
                for bus in buses:
                    print(bus)
            elif option == '2':
                bus_id = int(input("Enter a bus id: "))
                route_code = int(input("Enter a route code: "))
                if not isinstance(bus_id, int):
                    print("The bus id must be an integer number!")
                if not isinstance(route_code, int):
                    print("The route code must be an integer number!")
                usage = self.__controller.increase_usage(bus_id, route_code)
                print(usage)
            elif option == '3':
                bus_id = int(input("Enter a bus id: "))
                total_distance = self.__controller.compute_travel_distance(bus_id)
                print(total_distance)
            elif option == '0':
                return
