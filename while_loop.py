import pyodbc
import time

from air_passengers import *
from air_flights import *
from air_planes import *

passenger_table = Air_passengers()
flights_table = Air_flights()
planes_table = Air_planes()

while True:
    print('1- Create a Passenger')
    print('2- Search a passenger')
    print('3- List all flights')
    print('4- Create a flight')
    print('5- Add passenger to the flight')
    print('6- List all planes')
    print('7- Add a plane')
    print('_______________________________')
    user_input = input('Choose one of the above options or enter exit: ')

    if user_input == '1':
        print('You have chosen option 1 - Create a Passenger')
        passenger_table.create_passenger()
        time.sleep(0.7)
        print('New passenger added, thank you')
        time.sleep(0.7)

    elif user_input == '2':
        print('You have chosen option 2 - Search a passenger')
        passenger_table.all_passengers()
        time.sleep(0.7)

    elif user_input == '3':
        print('You have chosen option 3 - List all flights')
        flights_table.all_flights()
        print('All flights listed')
        time.sleep(0.7)

    elif user_input == '4':
        print('You have selected option 4 - Create a flight')
        flights_table.create_flight()
        print('You have successfully created a flight!')
        time.sleep(0.7)

    elif user_input == '5':
        print('You have chosen option 5 - Add passenger to the flight')
        passenger_table.add_passenger_to_flight()
        time.sleep(0.7)
        print('Passenger has successfully been added to the flight!')
        time.sleep(0.7)

    elif user_input == '6':
        print('You have chosen option 6 - List all planes')
        plane = planes_table.list_all_planes()
        print(plane)

    elif user_input == '7':
        print('You have chosen option 7 - Add a plane')
        planes_table.add_plane()
        print('Plane successfully added!')


    elif user_input == 'exit':
        break

