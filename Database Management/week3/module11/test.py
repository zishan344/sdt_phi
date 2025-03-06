import mysql.connector

mydb = mysql.connector.connect(
host ="localhost",
user ="root",
password= "strange!"
)



print(mydb)