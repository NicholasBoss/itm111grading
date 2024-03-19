import mysql.connector
import os


# with open('week10hw.sql', 'r') as f:
#     print(f.read())

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="student",
    password="student",
)

# print("Connected to the database")

answer = open(f"week06answers.txt", "w")

# print("***********************************")

# Create a cursor
mycursor = mydb.cursor()


total_queries = 41

# open the test folder and read the files inside
directory = 'tempgrades'
# if directory doesn't exist, write no files to grade
if not os.path.exists(directory):
    print("No Directory\n")
    os.makedirs(directory)
    print("Directory Created\n")

# if the directory is empty, write no files to grade
if not os.listdir(directory):
    # answer.write("No Files to Grade\n")
    print("No Files to Grade\n")

# loop through the files in the directory
else:

    print("Grading in progress...")
    
    file_count = 0
   
    for filename in os.listdir(directory):

        file_count += 1 # increment the counter
        edit_file = open(f"{directory}/{filename}", "r+")
        file_contents = edit_file.read()
        # Make changes to file_contents as needed
        if not file_contents.__contains__('-- ~'):
            file_contents = file_contents.lower().replace("use", "-- ~\nUSE")
            file_contents = file_contents.lower().replace("set", "-- ~\nSET")
            file_contents = file_contents.lower().replace("drop", "-- ~\nDROP")
            file_contents = file_contents.lower().replace("create", "-- ~\nCREATE")
            file_contents = file_contents.lower().replace("insert", "-- ~\nINSERT")
            file_contents = file_contents.replace(";", ";\n-- ~")
            edit_file.seek(0)
            edit_file.write(file_contents)
            edit_file.truncate()
            edit_file.close()
        else:
            edit_file.close()
            
        f = open(f"{directory}/{filename}", "r")
            
        answer.write("***********************************\n")
        answer.write(f"File: {filename}\n")
        
        # answer.write("---------------------\n")

        sqlFile = f.read()
        sqlCommands = sqlFile.split('-- ~')
        # strip the \n from the commands
        sqlCommands = [command.strip() for command in sqlCommands]
        # print(sqlCommands)
        # Filter out SELECT and USE commands
        sqlCommands = [command for command in sqlCommands if command.lower().startswith('use') or command.lower().startswith('drop') or command.lower().startswith('create') or command.lower().startswith('insert') or command.lower().startswith('update') or command.lower().startswith('delete')]
        
        erd_count = 0
        total_erd_count = 28
        drop_count = 0
        total_drop_count = 14
        create_count = 0
        total_create_count = 14
        insert_count = 0
        total_insert_count = 13
        mydb_count = 0

        
        for command in sqlCommands:
            if command.lower().startswith('drop'):
                drop_count += 1
                erd_count += 1
            if command.lower().startswith('create'):
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
            

        # print(sqlCommands)
        
        #filter out SET commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('set')]
    
        correct_answer_count = 0
        number = 0
        a_number = 0

    
        
        for command in sqlCommands:
            a_number += 1
            
            # answer.write(f"{a_number}. {command}\n")
        

            try:
                mycursor.execute(command)
            except mysql.connector.Error as e:
                # number the queries run and print the error
                answer.write("Error found. Skipping to the next file...\n")
                answer.write("-------ERROR DETAILS-------\n")
                answer.write(f"Query {number + 1}. Error: {e}\n")
                
                answer.write("------QUERY------\n")
                answer.write(f"{command}\n")
                answer.write("-------RESULTS-------\n")
                break
            output = mycursor.fetchall()
            # print(output)

            # if the output is empty, no error was found and 
            # the command was an insert, update, or delete statement
            # print that the command was successful
            if len(output) == 0 and (command.lower().__contains__('drop')):
                # answer.write(f"Query {number + 1}. DROP Successful\n")
                number += 1
                correct_answer_count += 1
                continue
            if len(output) == 0 and (command.lower().__contains__('create')):
                # answer.write(f"Query {number + 1}. CREATE Successful\n")
                number += 1
                correct_answer_count += 1
                continue
            if len(output) == 0 and (command.lower().__contains__('insert')):
                # answer.write(f"Query {number + 1}. INSERT Successful\n")
                number += 1
                correct_answer_count += 1
                continue
        
            
            
            
            # print(f"[{command}]")
        # answer.write("--------RESULTS-------\n")
        answer.write("---------ERD----------\n")
        answer.write(f"{drop_count}/{total_drop_count} of 14 total possible DROP Statements Written\n")
        answer.write(f"{create_count}/{total_create_count} of 10 total possible CREATE Statements Written\n")
        answer.write("-------INSERTS--------\n")
        answer.write(f"{insert_count}/{total_insert_count} of 13 total possible INSERT Statements Written\n")
        answer.write("-----FINAL TOTALS-----\n")
        answer.write(f"{erd_count}/{total_erd_count} of 28 total possible ERD Statements Written\n")
        answer.write(f"{number}/{total_queries} of 41 total possible Statements Written\n")
        answer.write(f"{correct_answer_count}/{total_queries} of 41 total possible Statements Correct\n")

        # print(f"{alias_counter}/{total_aliases} Aliases used")
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
    delete_files = input("Would you like to delete the files in the tempgrades folder? (yes/no): ")
    if delete_files.lower() == "yes":
        for filename in os.listdir(directory):
            os.remove(f"{directory}/{filename}")
        print("Files Deleted")
        answer = open(f"week06answers.txt", "w")
        answer.close()
    else:
        print("Files Kept")
    # print("***********************************")
        
    # print("***********************************\n")
    # print("***********************************")
