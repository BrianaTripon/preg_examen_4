from Domain.bus import Bus


class BusRepo:
    def __init__(self, file_name):
        self.__buses = []
        file = open(file_name, "r")
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(',')
            self.__buses.append(Bus(int(line[0]), int(line[1]), line[2], int(line[3])))
        file.close()

    def get_all_buses(self):
        return self.__buses[:]

    def get_bus_by_id(self, bus_id):
        for bus in self.get_all_buses():
            if bus.get_bus_id() == bus_id:
                return bus
