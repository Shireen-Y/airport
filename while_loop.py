from passengers_class import *
from planes_class import *
from flight_trip_class import *

passenger1 = Passengers('Joana Thompson', 'B343123')
passenger2 = Passengers('Birt Kuman', 'B13927')
passenger_list = []
passenger_list.extend([passenger1, passenger2])

plane1 = Planes('1234')
plane2 = Planes('5678')
plane3 = Planes('9012')
plane_list = []
plane_list.extend([plane1, plane2, plane3])

while True:
    print('1- Create a Passenger')
    print('2- Create a Plane')
    print('3- Add a plane to a flight')
    print('4- Add a destination to a flight')
    print('5- Add the origin of the flight')
    print('6- Add passenger to the flight')
    print('7- List of passengers')
    user_input = input('Choose one of the above options or enter exit: ')
    if user_input == '1':
        print('You have chosen option 1 - Create a Passenger')
        name = input('What is your full name? ')
        pass_num = input('Please enter your passport number: ')
        print('Thank you, please wait a moment..')
        new_passenger = Passengers(name.title(), pass_num)
        passenger_list.extend([new_passenger])
        print(new_passenger.name + ' has been added successfully, thank you.')