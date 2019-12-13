import pyodbc
from db_connect import *

class Air_passengers(MSDBConnect):

    def __sql_query(self, sql_query): # Encapsulation makes it private, meaning it can only be called by other methods
        return self.cursor.execute(sql_query)

    def create_passenger(self, first_name, last_name, pass_num):
        query = f"INSERT INTO Passengers (first_name, last_name, passport_number) VALUES ('{first_name}','{last_name}','{pass_num}')"
        result = self.__sql_query(query)
        self.docker_Airport_DB.commit()
        return result

    def all_passengers(self):
        query = 'SELECT * FROM Passengers'
        result = self.__sql_query(query)
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(f"Passenger ID: {record.passenger_ID}, Name: {record.first_name} {record.last_name}, Passport Number: {record.passport_number}")

    def add_passenger_to_flight(self, ask_flight, pass_num):
        query = f"UPDATE Passengers SET flight_ID = '{ask_flight}' WHERE passport_number = '{pass_num}'"
        result = self.__sql_query(query)
        self.docker_Northwind.commit()
        return result
