import mysql.connector
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


alias_counter = 0
total_aliases = 1
total_queries = 29

# open the test folder and read the files inside
os_name = platform.system()
if os_name == 'Windows':
    print("Windows OS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '\\tempgrades'
    answer = open(f"{directory}\\week11answers.txt", "w")

elif os_name == 'Linux' or os_name == 'Darwin':
    print("Linux/MacOS Detected")
    directory = os.getcwd() + '/v3'
    grading_directory = os.getcwd() + '/v3/tempgrades'
    answer = open(f"{directory}/week11answers.txt", "w")
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
        files = []
        files.append(filename)
        
        file_count += 1 # increment the counter

        # open the file from the list
        files = [f"{grading_directory}/{filename}" for filename in files]
        # print(files)
        for file in files:
            
            edit_file = open(file, "r+")
        # create a list (queue) to loop through the files
        file_contents = edit_file.read()
        # Make changes to file_contents as needed
        if not file_contents.__contains__('-- ~'):
            print("Formatting File...")
            file_contents = file_contents.replace("USE", "-- ~\nUSE")
            file_contents = file_contents.replace("SET", "-- ~\nSET")
            file_contents = file_contents.replace("DROP", "-- ~\nDROP")
            file_contents = file_contents.replace("CREATE", "-- ~\nCREATE")
            file_contents = file_contents.replace("INSERT", "-- ~\nINSERT")
            file_contents = file_contents.replace("DEFAULT CHARACTER -- ~\nSET", "DEFAULT CHARACTER SET")
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
        total_erd_count = 20
        drop_count = 0
        total_drop_count = 10
        create_count = 0
        total_create_count = 10
        insert_count = 0
        total_insert_count = 10
        mydb_count = 0

        # check for the DROP SCHEMA university command
        command_num = 0
        drop_schema_count = 0
        create_schema_count = 0
        
        for command in sqlCommands:
            command_num += 1
            # answer.write(f"COMMAND: {command_num}: \n{command}\n")
            if command_num == 1 and not command.lower().__contains__('drop schema if exists `university`'):
                answer.write("-------DROP SCHEMA UNIVERSITY-------\n")
                answer.write("DROP SCHEMA university not found\n")
                answer.write("Please add DROP SCHEMA university\n")
                answer.write("Executing DROP statement...\n")
                mycursor.execute("DROP SCHEMA IF EXISTS university")
            if command.lower().startswith('drop schema if exists `university`'):
                drop_schema_count += 1
                erd_count += 1
            if command.lower().startswith('create schema if not exists `university`'):
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
                answer.write("`mydb` database name found. Please switch this to be named university\n")
                answer.write("Skipping ERD check...\n")
                mydb_count += 1
                continue
            

        # debug.write(f"COMMAND LIST: {sqlCommands}")
        
        #filter out SET commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('set @OLD_UNIQUE_CHECKS') or not command.lower().startswith('set @OLD_FOREIGN_KEY_CHECKS') or not command.lower().startswith('set @OLD_SQL_MODE') or not command.lower().startswith('set OLD_UNIQUE_CHECKS') or not command.lower().startswith('set OLD_FOREIGN_KEY_CHECKS') or not command.lower().startswith('set OLD_SQL_MODE')]
    
        correct_answer_count = 0
        number = 0
        a_number = 0

        
        
        for command in sqlCommands:
            a_number += 1
            
            # answer.write(f"COMMAND: {a_number}. {command}\n")
        

            try:
                mycursor.execute(command)
                # commit the changes
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
        answer.write("ERD statements can be between 8 and 10\n")
        answer.write(f"{drop_schema_count}/{1} DROP SCHEMA UNIVERSITY Statement Written\n")
        answer.write(f"{create_schema_count}/{1} CREATE SCHEMA UNIVERSITY Statement Written\n")
        answer.write(f"{drop_count}/{total_drop_count} of 10 total possible DROP TABLE Statements Written\n")
        answer.write(f"{create_count}/{total_create_count} of 10 total possible CREATE TABLE Statements Written\n")
        answer.write("-------INSERTS--------\n")
        answer.write("Insert statments can be between 7 and 10\n")
        answer.write(f"{insert_count}/{total_insert_count} of 10 total possible INSERT Statements Written\n")
        answer.write("-----FINAL TOTALS-----\n")
        answer.write(f"{erd_count}/{total_erd_count} of 20 total possible ERD Statements Written\n")
        answer.write(f"{number}/{total_queries} of 29 total possible Statements Written\n")
        answer.write(f"{correct_answer_count}/{total_queries} of 29 total possible Statements Correct\n")

        
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
            os.remove(f"{directory}\\week11answers.txt")
        elif os_name == 'Linux' or os_name == 'Darwin':
            os.remove(f"{directory}/week11answers.txt")
        print("Files Deleted")
    else:
        f.close()
        print("Files Kept")

