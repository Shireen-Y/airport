import pyodbc

class MSDBConnect():
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'

        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        self.cursor = self.docker_Northwind.cursor()

    def __sql_query(self, sql_query): # Encapsulation makes it private, meaning it can only be called by other methods
        return self.cursor.execute(sql_query)


# These are our variables to connect
server = 'localhost,1433'
database = 'Airport_DB'
username = 'SA'
password = 'Passw0rd2018'

# Making the connection
docker_Airport_DB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Making the cursor
cursor = docker_Airport_DB.cursor()

# Executing some SQL commands
cursor.execute("SELECT * FROM Passengers")

# Accessing specific data or column
row = cursor.fetchone()
# print(row)
# print(row.first_name, row.last_name)