import pyodbc

print(pyodbc.drivers())

server = 'LAPTOP-PG2ESL4M' 
database = 'NBA_PLAYER_DB' 
username = 'talwafai' 
password = 'charmane' 
#cnxn = pyodbc.connect(r'Driver=ODBC Driver 17 for SQL Server;Server=LAPTOP-PG2ESL4M;DATABASE=NBA_PLAYER_DB;Trusted_Connection=yes;')
cnxn = pyodbc.connect(r'Driver=ODBC Driver 17 for SQL Server;Server=LAPTOP-PG2ESL4M;Trusted_Connection=yes;')

cursor = cnxn.cursor()