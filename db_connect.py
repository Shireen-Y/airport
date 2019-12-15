import pyodbc

class MSDBConnect():
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Airport_DB'
        self.username = 'SA'
        self.password = 'Passw0rd2018'

        self.docker_Airport_DB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        self.cursor = self.docker_Airport_DB.cursor()

    def __sql_query(self, sql_query): # Encapsulation makes it private, meaning it can only be called by other methods
        return self.cursor.execute(sql_query)
