from passengers_class import *
from planes_class import *
from flight_trip_class import *

passenger1 = Passengers('Joana Thompson', 'B343123')
passenger2 = Passengers('Birt Kuman', 'B13927')
passenger_list = []
passenger_list.extend([passenger1, passenger2])

flight1 = Flight_trip('LA', 'London', 'BA707')
flight2 = Flight_trip('Amsterdam', 'London', 'EJ246')
flight_list = []
flight_list.extend([flight1, flight2])

import time

while True:
    print('1- Create a Passenger')
    print('2- List of passengers')
    print('3- List all flights')
    print('4- Add passenger to the flight')
    user_input = input('Choose one of the above options or enter exit: ')

    if user_input == '1':
        print('You have chosen option 1 - Create a Passenger')
        name = input('What is your full name? ')
        pass_num = input('Please enter your passport number: ')
        print('Thank you, please wait a moment..')
        new_passenger = Passengers(name.title(), pass_num.capitalize())
        passenger_list.extend([new_passenger])
        time.sleep(0.7)
        print(new_passenger.name + ' has been added successfully, thank you.')
        time.sleep(0.7)

    elif user_input == '2':
        print('You have chosen option 3- List all passengers')
        for passenger in passenger_list:
            print('Name: ' + passenger.name.title() + ', Passport number: ' + passenger.passport_number.capitalize())
            time.sleep(0.7)

    elif user_input == '3':
        print('You have chosen option 4- List all flights')
        for flight in flight_list:
            print('Plane: ' + flight.plane + ', Flight origin: ' + flight.origin.title() + ', Flight destination: ' + flight.destination.capitalize())
            time.sleep(0.7)

    elif user_input == '4':
        print('You have chosen option 2 - Add passenger to the flight')
        chosen_passenger = input('What is the passport number of the passenger? ')
        chosen_flight = input('Where is the passenger flying to? ')
        for passenger in passenger_list:
            if chosen_passenger == passenger.passport_number.capitalize():
                for flight in flight_list:
                    if chosen_flight == flight.destination.title():
                        flight.add_passenger(passenger)
                        print(passenger.name.title() + ' has been added to the flight terminating at: ' + flight.destination.title())
                        time.sleep(0.7)


    elif user_input == 'exit':
        break