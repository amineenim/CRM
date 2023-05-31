# import requirements
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root123'
)

# prepare a cursor object 
cursor = dataBase.cursor()

# create the database

cursor.execute("CREATE DATABASE crm")

print(' database created successefully !')
