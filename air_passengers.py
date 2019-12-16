import pyodbc
from db_connect import *

class Air_passengers(MSDBConnect):

    def __sql_query(self, sql_query): # Encapsulation makes it private, meaning it can only be called by other methods
        return self.cursor.execute(sql_query)

    def create_passenger(self):
        first_name = input('What is the passengers first name? ')
        last_name = input('What is the passengers last name? ')
        passport_number = input('What is the passengers passport number? ')
        query = f"INSERT INTO Passengers (first_name, last_name, passport_number) VALUES ('{first_name}','{last_name}','{passport_number}')"
        print('Please wait a moment...')
        result = self.__sql_query(query)
        self.cursor.commit()
        return result

    def all_passengers(self):
        ask_passenger = input('What is the name of the passenger? ')
        query = f"SELECT * FROM Passengers WHERE first_name LIKE '%{ask_passenger}%' OR last_name LIKE '%{ask_passenger}%'"
        result = self.__sql_query(query)
        print('Here is what we found.. ')
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(f"Passenger ID: {record.passenger_ID}, Full name: {record.first_name} {record.last_name}, Passport Number: {record.passport_number}, Flight ID: {record.flight_ID}")
        return 'All results completed'

    def add_passenger_to_flight(self):
        ask_flight = input('What is the flight ID you would like to add the passenger to? ')
        passport_number = input('What is the passengers passport number? ')
        query = f"UPDATE Passengers SET flight_ID = '{ask_flight}' WHERE passport_number = '{passport_number}'"
        print('Thank you please wait a moment..')
        result = self.__sql_query(query)
        self.docker_Airport_DB.commit()
        return result
