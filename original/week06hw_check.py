try: 
    import mysql.connector
except ImportError:
    print("MYSQL module not found. Installing...")
    os.system("pip install mysql-connector-python")
    import mysql.connector
    print("MYSQL module installed")
import os
import platform


# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="student",
    password="student",
)

# Create a cursor
mycursor = mydb.cursor()


# open the test folder and read the files inside
os_name = platform.system()
if os_name == 'Windows':
    print("Windows OS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '\\tempgrades'
    answer = open(f"{directory}\\week06answers.txt", "w")

elif os_name == 'Linux' or os_name == 'Darwin':
    print("Linux/MacOS Detected")
    directory = '/home/student/Desktop/itm111grading/original'
    grading_directory = '/home/student/Desktop/itm111grading/original/tempgrades'
    answer = open(f"{directory}/week06answers.txt", "w")
    
# if directory doesn't exist, write no files to grade
if not os.path.exists(grading_directory):
    print("No Directory\n")
    os.makedirs(grading_directory)
    print("Directory Created\n")

# if the directory is empty, write no files to grade
if not os.listdir(grading_directory):
    
    print("No Files to Grade\n")

# loop through the files in the directory
else:

    print("Grading in progress...")
    
    file_count = 0
   
    for filename in os.listdir(grading_directory):

        file_count += 1 # increment the counter
        edit_file = open(f"{grading_directory}/{filename}", "r+")
        file_contents = edit_file.read()
        # Make changes to file_contents as needed
        if not file_contents.__contains__('-- ~'):
            print("Formatting File...")
            file_contents = file_contents.replace("USE", "-- ~\nUSE")
            file_contents = file_contents.replace("SET", "-- ~\nSET")
            file_contents = file_contents.replace("-- ~\nSET", "SET")
            file_contents = file_contents.replace("DROP", "-- ~\nDROP")
            file_contents = file_contents.replace("CREATE", "-- ~\nCREATE")
            file_contents = file_contents.replace("INSERT", "-- ~\nINSERT")
            file_contents = file_contents.replace(";", ";\n-- ~")
            edit_file.seek(0)
            edit_file.write(file_contents)
            edit_file.truncate()
            edit_file.close()
        else:
            edit_file.close()
            print("File already formatted")
            
        f = open(f"{grading_directory}/{filename}", "r")
        print(f"Grading {filename}...")
        answer.write("***********************************\n")
        answer.write(f"File: {filename}\n")
        
        

        sqlFile = f.read()
        sqlCommands = sqlFile.split('-- ~')
        # strip the \n from the commands
        sqlCommands = [command.strip() for command in sqlCommands]
        # Filter out SELECT and USE commands
        sqlCommands = [command for command in sqlCommands if command.lower().startswith('use') or command.lower().startswith('drop') or command.lower().startswith('create') or command.lower().startswith('insert') or command.lower().startswith('update') or command.lower().startswith('delete')]
        
        erd_count = 0
        
        drop_count = 0
        
        create_count = 0
        
        insert_count = 0
        
        mydb_count = 0
        drop_schema_count = 0
        create_schema_count = 0

        
        for command in sqlCommands:
            if command.lower().startswith('drop schema if exists'):
                drop_schema_count += 1
                erd_count += 1
            if command.lower().startswith('create schema if not exists'):
                create_schema_count += 1
                erd_count += 1
            if command.lower().startswith('drop table'):
                drop_count += 1
                erd_count += 1
            if command.lower().startswith('create table'):
                create_count += 1
                erd_count += 1
            if command.lower().__contains__('insert'):
                insert_count += 1
            if mydb_count > 0:
                break
            if command.lower().__contains__('mydb'):
                answer.write("`mydb` database name found. Please switch this to be named `film`\n")
                answer.write("Skipping ERD check...\n")
                mydb_count += 1
                continue
            

        # debug.write(f"COMMAND LIST: {sqlCommands}")
        
        #filter out SET commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('set')]
    
        correct_answer_count = 0
        number = 0
        a_number = 0

    
        
        for command in sqlCommands:
            a_number += 1
            
            # debug.write(f"Query {a_number}. {command}\n")
        

            try:
                mycursor.execute(command)
                mydb.commit()
                number += 1
                correct_answer_count += 1
            except mysql.connector.Error as e:
                # number the queries run and print the error
                answer.write("Error found. Skipping to the next file...\n")
                answer.write("-------ERROR DETAILS-------\n")
                answer.write(f"Query {number + 1}. Error: {e}\n")
                
                answer.write("------QUERY------\n")
                answer.write(f"{command}\n")
                answer.write("-------RESULTS-------\n")
                break
            
            
        # answer.write("--------RESULTS-------\n")
        answer.write("---------ERD----------\n")
        answer.write(f"{drop_schema_count}/{1} DROP SCHEMA UNIVERSITY Statement Written\n")
        answer.write(f"{create_schema_count}/{1} CREATE SCHEMA UNIVERSITY Statement Written\n")
        answer.write(f"{drop_count} DROP TABLE Statements Written\n")
        answer.write(f"{create_count} CREATE TABLE Statements Written\n")
        answer.write("-------INSERTS--------\n")
        answer.write(f"{insert_count} INSERT Statements Written\n")
        answer.write("-----FINAL TOTALS-----\n")
        answer.write(f"{erd_count} ERD Statements Written\n")
        answer.write(f"{number} Statements Written\n")
        answer.write(f"{correct_answer_count} Statements Correct\n")

        
        alias_counter = 0
        answer.write("***********************************\n\n")
    answer.write("***********************************\n")
    answer.write(f"Total Files Graded: {file_count}\n")
    answer.write("***********************************\n")

    print("Grading Complete")

    answer.close()
    # ask if user wants to delete files in the tempgrades folder
    # if yes, delete the files

    # if no, keep the files
    f.close()
    mydb.close()
    delete_files = input("Would you like to delete the files in the tempgrades folder? (yes/no): ")
    if delete_files.lower() == "yes":
        f.close()
        for filename in os.listdir(grading_directory):
            os.remove(f"{grading_directory}/{filename}")
        if os_name == 'Windows':
            os.remove(f"{directory}\\week06answers.txt")
        elif os_name == 'Linux' or os_name == 'Darwin':
            os.remove(f"{directory}/week06answers.txt")
        print("Files Deleted")
    else:
        f.close()
        print("Files Kept")

