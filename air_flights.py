import pyodbc
from db_connect import *

class Air_flights(MSDBConnect):

    def __sql_query(self, sql_query): # Encapsulation makes it private, meaning it can only be called by other methods
        return self.cursor.execute(sql_query)

    def list_flights(self):
        query = 'SELECT * FROM Flights'
        result = self.__sql_query(query)
        return result

