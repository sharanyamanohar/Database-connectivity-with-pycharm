import mysql.connector as connection

mydb = connection.connect(host = "Localhost", user = "root", passwd = "mysql", use_pure = True)
#Check if the connection is established
cursor = mydb.cursor(buffered = True) #Create a cusrsor to execute queries
cursor.execute("Create database sara321")
cursor.execute("SHOW DATABASES")

cursor.execute("Create table sara321.ineuron(age int ,job varchar(30),marital varchar(30) ,education varchar(30) ")
cursor.execute("insert into sara321.ineuron values(44,'technician','single','secondary'),(33,'entrepreneur','married','secondary')")
cursor.execute("select * from sara321.ineuron")
