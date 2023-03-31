import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Dj@1234'
    
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE djco")

print("All Done!")