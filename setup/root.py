import mysql.connector
import os
import platform

# connect to root user
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="C4nGet1n!",
)

# print(mydb)


# execute the root commands to grant access to the new user
directory = os.getcwd()
# check to see what system I'm using
name = platform.system()
if name == 'Linux' or name == 'Darwin':
    filename = f"{directory}/root.sql"
elif name == 'Windows':
    filename = f"{directory}\\root.sql"

mycursor = mydb.cursor()
mycursor.execute('SHOW DATABASES')
test_output = mycursor.fetchall()

for x in test_output:
# test for the bike database
    if x[0] == 'bike':
        break
    else:
        print('Required databases missing. Creating...')
        mycursor.execute('source itm111_databases.sql')
        mydb.commit()
        print('Database creation successful.')

with open(filename, 'r+') as file:
    sqlFile = file.read()
    commands = sqlFile.split('-- ~')
    commands = [command.strip() for command in commands]
    for command in commands:
        # print(command)

        try:
            mycursor = mydb.cursor()
            mycursor.execute(command)
            mydb.commit()
        except Exception as e:
            print(e)
            continue

# close the connection
mydb.close()

# connect to the new user
student = mysql.connector.connect(
    host="localhost",
    user="student",
    password="student",
)

studentcursor = student.cursor()
studentcursor.execute("SHOW DATABASES")
output = studentcursor.fetchall()
# print the databases
count = 0
for x in output:
    count += 1
    print(x)

print(f"{count} databases found")