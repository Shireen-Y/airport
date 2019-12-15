import pyodbc
from db_connect import *

class Air_planes(MSDBConnect):

    def __sql_query(self, sql_query): # Encapsulation makes it private, meaning it can only be called by other methods
        return self.cursor.execute(sql_query)

    def add_plane(self):
        ask_plane = input('What is the plane number? ')
        query = f"INSERT INTO Planes (plane_number) VALUES ('{ask_plane}')"
        result = self.__sql_query(query)
        self.docker_Airport_DB.commit()
        return result

    def list_all_planes(self):
        query = 'SELECT * FROM Planes'
        result = self.__sql_query(query)
        print('Listing all the planes..')
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(record)
        return 'Complete'