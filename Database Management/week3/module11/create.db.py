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
            CREATE TABLE STUDENT (
            Roll VARCHAR(4),
            NAME VARCHAR(50)
            )
           """

mycursor.execute(sqlquery)
print("CREATE TABLE SUCCESSFUL")