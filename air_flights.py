import pyodbc
from db_connect import *

class Air_flights(MSDBConnect):

    def __sql_query(self, sql_query): # Encapsulation makes it private, meaning it can only be called by other methods
        return self.cursor.execute(sql_query)

    def all_flights(self):
        print('Listing all the flights we have available, please wait a moment..')
        query = 'SELECT * FROM Flights'
        result = self.__sql_query(query)
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(record)

    def create_flight(self):
        ask_plane = input('What is the plane ID? ')
        ask_origin = input('Where is the flight departing from? ')
        ask_destination = input('Where is the flight terminating? ')
        query = f"INSERT INTO Flights (plane_ID, origin, destination) VALUES ('{ask_plane}', '{ask_origin}', '{ask_destination}')"
        result = self.__sql_query(query)
        self.docker_Airport_DB.commit()
        return result
