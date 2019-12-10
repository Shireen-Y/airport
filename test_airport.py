from passengers_class import *
from planes_class import *
from flight_trip_class import *

# passenger1 = Passengers('Joana Thompson', 'B343123')
# passenger2 = Passengers('Birt Kuman', 'B13927')
# name = input('What is your full name? ')
# passport_number = input('What is your passport number? ')
# passenger1 = Passengers(name, passport_number)
# print('You have successfully added: ')
# print(passenger1.create_passenger(name, passport_number))

def test_passenger():
    assert Passengers('Joana Thompson', 'B343123').name == 'Joana Thompson'
    assert Passengers('Birt Kuman', 'B13927').passport_number == 'B13927'

def test_planes():
    assert Planes('1234').plane_number == '1234'
    assert Planes('5678').plane_number == '5678'