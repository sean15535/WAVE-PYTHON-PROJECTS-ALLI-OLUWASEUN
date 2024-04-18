#importing sqlite 3
import sqlite3
#creating a connection to the database
connection = sqlite3.connect('database.db')
# a cursor can be considered as the walking stick 
# that we use to navigate through the database
cursor = connection.cursor()
#creating a table
cursor.execute("CREATE TABLE user(id INTEGER NOT NULL PRIMARY KEY, username TEXT varchar(12));")
#inserting data

connection.close()


