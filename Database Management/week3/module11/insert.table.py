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
             INSERT INTO STUDENT(ROLL,NAME)
             VALUES('101','marouful islam zishan')
           """

mycursor.execute(sqlquery)
mydbconnection.commit()
print("INSERT TABLE SUCCESSFUL")