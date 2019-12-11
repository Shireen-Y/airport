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

while True:
    print('1- Create a Passenger')
    print('2- Add passenger to the flight')
    print('3- List of passengers')
    print('4- List all flights')
    user_input = input('Choose one of the above options or enter exit: ')
    if user_input == '1':
        print('You have chosen option 1 - Create a Passenger')
        name = input('What is your full name? ')
        pass_num = input('Please enter your passport number: ')
        print('Thank you, please wait a moment..')
        new_passenger = Passengers(name.title(), pass_num)
        passenger_list.extend([new_passenger])
        print(new_passenger.name + ' has been added successfully, thank you.')

    elif user_input == '2':
        print('You have chosen option 2 - Add passenger to the flight')
        chosen_passenger = input('What is the passport number of the passenger? ')
        chosen_flight = input('Where is the passenger flying to? ')
        for passenger in passenger_list:
            if chosen_passenger == passenger.passport_number:
                for flight in flight_list:
                    if chosen_flight == flight.destination:
                        flight.add_passenger(passenger)
                        print(passenger.name.title() + ' has been added to the flight terminating at: ' + flight.destination)

    elif user_input == '3':
        print('You have chosen option 3- List all passengers')
        for passenger in passenger_list:
            print('Name: ' + passenger.name + ', Passport number: ' + passenger.passport_number)

    elif user_input == '4':
        print('You have chosen option 4- List all flights')
        for flight in flight_list:
            print('Plane: ' + flight.plane + ', Flight origin: ' + flight.origin + ', Flight destination: ' + flight.destination)

    elif user_input == 'exit':
        break