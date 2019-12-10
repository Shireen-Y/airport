from humans_class import *

class Passengers_class(Humans):
    def __init__(self, name, passport_number):
        super().__init__(name)
        self.__passport_number = passport_number

    def get_passport_number(self):
        return self.__passport_number
