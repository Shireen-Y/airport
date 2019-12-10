from humans_class import *

class Passengers(Humans):
    def __init__(self, name, passport_number):
        super().__init__(name)
        self.passport_number = passport_number


    # def create_passenger(self, name, passport_number):
    #     return 'Name: ' + name + ', Passport Number: ' + passport_number


