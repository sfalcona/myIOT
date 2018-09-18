import sqlite3
import os

print(os.path.realpath(os.path.dirname(
    os.path.abspath(__file__)) + "/myDB/myUsers.db"))
connection = sqlite3.connect(os.path.realpath(
    os.path.dirname(os.path.abspath(__file__)) + "/myDB/myUsers.db"))
cursor = connection.cursor()


cursor.execute("""DROP TABLE users;""")
cursor.execute("""DROP TABLE credentials;""")

sql_command = """
CREATE TABLE users (  
family VARCHAR(30),
fname VARCHAR(20), 
lname VARCHAR(30));"""
cursor.execute(sql_command)
print('Creating table')

sql_command = """
CREATE TABLE credentials ( 
family VARCHAR(30),
password VARCHAR(20));"""
cursor.execute(sql_command)
print('Creating table')


myUsers = [ ("Falconaro", "Sebastian", "Falconaro"),
			("Falconaro","Bernardo", "Michel"),
			("Milhas", "Sebastian", "Milhas")]


sql_command = """INSERT INTO users VALUES (?,?,?)"""
cursor.executemany(sql_command, myUsers)
connection.commit()

myCred = [	('Falconaro', 'Milhastrolo'),
			('Milhas', 'FalconaroCapo')]


sql_command = """INSERT INTO credentials VALUES (?,?)"""
cursor.executemany(sql_command, myCred)
connection.commit()



sql_command = """
SELECT lname 
FROM users
INNER JOIN credentials ON users.family = credentials.family
WHERE fname = ? 
"""

cursor.execute(sql_command,('Sebastian',) )

print(cursor.fetchall())


connection.close()
