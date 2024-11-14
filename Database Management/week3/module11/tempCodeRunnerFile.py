import mysql.connector

db_name = "python_test_db"

mydbconnection = mysql.connector.connect(
host ="localhost",
user ="root",
password= "strange!",
database = db_name
)


mycursor = mydbconnection.cursor()

sqlquery ="""
             UPDATE Student SET Name ='miz'
             WHERE Name = 'marouful islam zishan'
           """

mycursor.execute(sqlquery)
mydbconnection.commit()
print("update TABLE SUCCESSFUL")