import mysql.connector

nama_db = {
    'user' : 'root',
    'password' : 'password',
    'host' : 'localhost',
    'database' : 'aset',
}

connection = mysql.connector.connect(**nama_db)
cursor =  connection.cursor()

