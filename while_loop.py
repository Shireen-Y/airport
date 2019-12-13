import pyodbc
from air_passengers import *
from air_flights import *

# passenger1 = Passengers('Joana Thompson', 'B343123')
# passenger2 = Passengers('Birt Kuman', 'B13927')
# passenger_list = []
# passenger_list.extend([passenger1, passenger2])
#
# flight1 = Flight_trip('LA', 'London', 'BA707')
# flight2 = Flight_trip('Amsterdam', 'London', 'EJ246')
# flight_list = []
# flight_list.extend([flight1, flight2])

passenger_table = Air_passengers()
flights_table = Air_flights()

import time

while True:
    print('1- Create a Passenger')
    print('2- List of passengers')
    print('3- List all flights')
    print('4- Add passenger to the flight')
    user_input = input('Choose one of the above options or enter exit: ')

    if user_input == '1':
        print('You have chosen option 1 - Create a Passenger')
        first_name = input('What is your first name? ')
        last_name = input('What is your last name? ')
        pass_num = input('Please enter your passport number: ')
        print('Thank you, please wait a moment..')
        passenger_table.create_passenger(first_name, last_name, pass_num)
        time.sleep(0.7)
        print('New passenger added, thank you')
        # new_passenger = Passengers(name.title(), pass_num.capitalize())
        # passenger_list.extend([new_passenger])
        time.sleep(0.7)

    elif user_input == '2':
        print('You have chosen option 2- List all passengers')
        passenger_table.all_passengers()
        time.sleep(0.7)

    elif user_input == '3':
        print('You have chosen option 3- List all flights')
        flights_table.all_flights()
        time.sleep(0.7)

    elif user_input == '4':
        print('You have chosen option 4- Add passenger to the flight')
        ask_flight = input('Where is the passenger flying to? (Insert Flight ID of the flight) ')
        pass_num = input('What is the passport number of the passenger? ')
        print('Thank you, please wait a moment..')
        passenger_table.add_passenger_to_flight(ask_flight, pass_num)
        time.sleep(0.7)
        print('Passenger has successfully been added to the flight')
        time.sleep(0.7)

    elif user_input == 'exit':
        break