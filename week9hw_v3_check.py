import mysql.connector
import decimal
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

answer = open(f"week09answers.txt", "w")

# print("***********************************")

# Create a cursor
mycursor = mydb.cursor()


correct_answer_list = [[[['van Rijn', 'Rembrandt', 'Night Watch'], # 1
                        ['van Rijn', 'Rembrandt', 'Storm on the Sea of Galilee']],
                        [['van Rijn', 'Rembrandt', 'nightwatch.jpg'],
                         ['van Rijn', 'Rembrandt', 'stormgalilee.jpg']],
                        [['Rembrandt', 'van Rijn', 'Night Watch'],
                         ['Rembrandt', 'van Rijn', 'Storm on the Sea of Galilee']],
                        [['Rembrandt', 'van Rijn', 'nightwatch.jpg'],
                         ['Rembrandt', 'van Rijn', 'stormgalilee.jpg']],
                         [['Night Watch', 'van Rijn', 'Rembrandt'],
                         ['Storm on the Sea of Galilee', 'van Rijn', 'Rembrandt']],
                         [['nightwatch.jpg', 'van Rijn', 'Rembrandt'],
                         ['stormgalilee.jpg', 'van Rijn', 'Rembrandt']],
                         [['Rembrandt','Night Watch'],
                          ['Rembrandt','Storm on the Sea of Galilee']],
                         [['van Rijn','nightwatch.jpg'],
                          ['van Rijn','stormgalilee.jpg']],
                          [['Night Watch', 'Storm on the Sea of Galilee']],
                          [['nightwatch.jpg'], ['stormgalilee.jpg']]],
                        [['nightwatch.jpg']], # 2
                       [['Leonardo', 'da Vinci', 'Head of a Woman'], # 3
                        ['Leonardo', 'da Vinci', 'Last Supper'], 
                        ['Leonardo', 'da Vinci', 'Mona Lisa'], 
                        ['Michelangelo', 'Simoni', None]],
                       [[[None, 'Wong', 'Walter']], # 4
                        [[None, 'Walter', 'Wong']],
                        [['Walter', 'Wong', None]],
                        [['Wong', 'Walter', None]],
                        [['Walter', 'Wong']],
                        [['Wong', 'Walter']]],
                       [['Beautiful Birds'], # 5
                        ['Corn Shucking for Fun and Profit']],
                       [['Ebru', 'Alpin'], # 6
                        ['Isamu', 'Legleitner']],
                       [[['Hisao', # 7 
                         'Lipner', 
                         'Human Resources', 
                         '$53,315']],
                         [['Hisao', 'Lipner', 'Human Resources', '$53,315.00']]]]


alias_counter = 0
total_aliases = 1
total_queries = 7

# open the test folder and read the files inside
directory = 'tempgrades'
# if directory doesn't exist, write no files to grade
if not os.path.exists(directory):
    print("\nNo Directory\n")
    os.makedirs(directory)
    print("Directory Created\n")

# if the directory is empty, write no files to grade
if not os.listdir(directory):
    # answer.write("No Files to Grade\n")
    print("\nNo Files to Grade\n")

# loop through the files in the directory
else:
    print("Grading in progress...")
    # creating a counter to keep track of how
    # many files are being graded
    file_count = 0

    for filename in os.listdir(directory):
        file_count += 1 # increment the counter
        f = open(f"{directory}/{filename}", "r")
            
        answer.write("***********************************\n")
        answer.write(f"File: {filename}\n")
        # print("---------------------")

        sqlFile = f.read()
        sqlCommands = sqlFile.split('-- ~')
        # strip the \n from the commands
        sqlCommands = [command.strip() for command in sqlCommands]
        # print(sqlCommands)
        # Filter out SELECT commands
        sqlCommands = [command for command in sqlCommands if (not command.lower().startswith('select *') and command.lower().startswith('select')) or command.lower().startswith('use')]
        # print(sqlCommands)
    
        # final_student_answers = []
        number = 0
        for command in sqlCommands:
            # print(f"[{command}]") 
            mycursor.execute(command)
            output = mycursor.fetchall()
            

            
            output_list = [list(row) for row in output if row is not None]
            # print(f"[{command}]")
            # replace the word Decimal with nothing
            #surround the decimal values with "" to match the expected output
            for row in output_list:
                for i in range(len(row)):
                    if type(row[i]) == decimal.Decimal:
                        row[i] = str(row[i])
            # filter out empty commands
            # only output the result if information is returned
            if len(output_list) > 0:
                student_answers = [list(row) for row in output_list if row is not None]
                # final_student_answers.append(student_answers)
                

                # Compare the student answers to the correct answers
                # print(f"Correct Answers: {correct_answers}")
                # print(f"Student Answers: {student_answers}") 
                if student_answers in correct_answer_list or student_answers in correct_answer_list[number]:
                    number += 1
                    # answer.write(f"Command: {command}\n")
                    # answer.write(f"Student Answer: {student_answers}\n")

                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(')  as'):
                        alias_counter += 1
                    elif (not command.lower().__contains__(') as ') and not command.lower().__contains__(' as ')) or alias_counter == total_aliases :
                        answer.write(f"Alias NOT used in query {number}\n")
                        # answer.write(f"All Aliases accounted for\n")
                
                else:
                    number += 1
                    # print("---------------------------------")
                    answer.write("---------------------\n")
                    answer.write(f"{number}. Incorrect!\n")
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as '):
                        alias_counter += 1
                        answer.write(f"Alias used\n")
                    else:
                        answer.write(f"No Alias Found\n")
                    # check for certain clauses and print that they were used
                    answer.write("-----COMMAND-----\n")
                    answer.write(f"{command}\n")
                    answer.write("-----CLAUSES-----\n")
                    if not command.lower().__contains__('select'):
                        answer.write(f"SELECT Clause used\n")
                    if not command.lower().__contains__('from'):
                        answer.write(f"FROM Clause used\n")
                    if not command.lower().__contains__('join'):
                        answer.write(f"JOIN Clause NOT used\n")
                    if not command.lower().__contains__('on'):
                        answer.write(f"ON Clause NOT used\n")
                    if not command.lower().__contains__('where'):
                        answer.write(f"WHERE Clause NOT used\n")
                    if not command.lower().__contains__('order by'):
                        answer.write(f"ORDER BY Clause NOT used\n")
                    if not command.lower().__contains__('limit'):
                        answer.write(f"LIMIT Clause NOT used\n")
                    answer.write("----FUNCTIONS----\n")
                    if not command.lower().__contains__('format'):
                        answer.write(f"FORMAT Function NOT used\n")
                    if not command.lower().__contains__('concat'):
                        answer.write(f"CONCAT Function NOT used\n")
                    answer.write("-----ANSWERS-----\n")
                    
                    answer.write(f"Student Answer: {student_answers}\n")
                    answer.write(f"Correct Answer: {correct_answer_list[number-1]}\n")
                    answer.write("---------------------\n")
                    # print("---------------------")
                    # print(f"{number}. Incorrect!")
                    # print("---------------------")
                    # print("---------------------------------")


        answer.write(f"{alias_counter}/{total_aliases} Aliases used\n")
        answer.write(f"Total Queries: {number}/{total_queries}\n")
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
    delete_files = input("Would you like to delete the files in the tempgrades folder? (yes/no): ")
    if delete_files.lower() == "yes":
        f.close()
        for filename in os.listdir(directory):
            os.remove(f"{directory}/{filename}")
        print("Files Deleted")
    else:
        print("Files Kept")
    # print("***********************************")
        
    # print("***********************************\n")
    # print("***********************************")
