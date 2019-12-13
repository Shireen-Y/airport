import pyodbc
from db_connect import *

class Air_passengers(MSDBConnect):

    def __sql_query(self, sql_query): # Encapsulation makes it private, meaning it can only be called by other methods
        return self.cursor.execute(sql_query)

    def create_passenger(self,first_name, last_name, passport_number):
        query = f"INSERT INTO Passengers (first_name, last_name, passport_number VALUES ('{first_name}', '{last_name}', '{passport_number}'')"
        result = self.__sql_query(query)
        self.docker_Northwind.commit()
        return result

