import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()
#creating a table
cursor.execute("CREATE TABLE user(id INTEGER NOT NULL PRIMARY KEY, username TEXT varchar(12));")
#inserting data

