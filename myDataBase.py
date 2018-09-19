import sqlite3
from Crypto.Cipher import AES
from Crypto import Random
import os


key = b'0123456789ABCDEF'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)


class myDB():
	'''Base de datos para guardar usuarios'''
	def __init__(self, name = "/myDB/myUsers.db"):
		'''Inicializo la base de datos con dos tablas, una de usuarios y otra de credenciales'''
		self.connection = sqlite3.connect(os.path.realpath(os.path.dirname(os.path.abspath(__file__)) + name ))
		self.cursor = self.connection.cursor()

		self.sql_command = """
		CREATE TABLE users (  
		family VARCHAR(30),
		fname VARCHAR(20), 
		lname VARCHAR(30));"""
		self.cursor.execute(self.sql_command)

		self.sql_command = """
		CREATE TABLE credentials ( 
		family VARCHAR(30),
		password VARCHAR(20));"""
		self.cursor.execute(self.sql_command)
		self.connection.commit()

	def addItem(self, table, items):
		'''Agrego a la tabla "table" un tuple con los items'''
		if table == "users":
			self.sql_command = """INSERT INTO users VALUES (?,?,?)"""
			self.cursor.executemany(self.sql_command, items)
			self.connection.commit()
		if table == "credentials":
			for element in items:
				## ARREGLAR ESTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
			self.sql_command = """INSERT INTO credentials VALUES (?,?)"""
			self.a = items[0]
			self.b = cipher.encrypt(items[1])
			self.cursor.executemany(self.sql_command, items)
			self.connection.commit()


	def check(self, query, items):
		self.sql_command = query
		self.cursor.executemany(self.sql_command, items)
		self.connection.commit()
		return self.cursor.fetchall()	

	def close(self):
		self.connection.close()




sql_command = """
SELECT lname 
FROM users
INNER JOIN credentials ON users.family = credentials.family
WHERE fname = ? 
"""




myUsers = [ ("Falconaro", "Sebastian", "Falconaro"),
			("Falconaro","Bernardo", "Michel"),
			("Milhas", "Sebastian", "Milhas")]




myCred = [	('Falconaro', 'Milhastrolo'),
			('Milhas', 'FalconaroCapo')]
