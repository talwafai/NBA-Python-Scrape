import pyodbc

cnxn = pyodbc.connect(driver='ODBC Driver 17 for SQL Server', server='LAPTOP-PG2ESL4M', database='test', Trusted_Connection='yes')

cursor = cnxn.cursor()

cursor.execute("insert into test(id, name) values ('10', 'crap')")
#commit the transaction
cnxn.commit()

#192.168.0.81,1433