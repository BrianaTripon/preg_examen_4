
class Route:
    def __init__(self, code, length):
        self.__code = code
        self.__length = length

    def get_code(self):
        return self.__code

    def get_length(self):
        return self.__length

    def __str__(self):
        s = ''
        s += str(self.__code)
        s += ' '
        s += str(self.__length)
        return s