import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user =  'root',
	passwd = 'W7301@jqir#'

	)


cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE crmdjango")

print("All Done!")