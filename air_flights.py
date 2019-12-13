import pyodbc
from db_connect import *

class Air_flights(MSDBConnect):

    def __sql_query(self, sql_query): # Encapsulation makes it private, meaning it can only be called by other methods
        return self.cursor.execute(sql_query)

    def all_flights(self):
        query = 'SELECT * FROM Flights'
        result = self.__sql_query(query)
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(f"Flight ID: {record.flight_ID}, Passenger ID: {record.passenger_ID}, Plane ID: {record.plane_ID}, Origin of flight: {record.origin}, Destination of flight: {record.destination}")

