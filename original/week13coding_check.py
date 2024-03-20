import mysql.connector
import decimal
import datetime
import os


def format_list(list):
    list = [str(item) for item in list]
    new_list = '\n'.join(list)
    new_list = new_list.replace('[', '')
    new_list = new_list.replace(']', '')
    new_list = new_list.replace("'", "")
    return new_list
# with open('week10hw.sql', 'r') as f:
#     print(f.read())

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="student",
    password="student",
)

# print("Connected to the database")

answer = open(f"week13answers.txt", "w")

# print("***********************************")

# Create a cursor
mycursor = mydb.cursor()


correct_answer_list = [[[['Togo']], # 1
                        [['Georgia', 4968000], 
                         ['Sierra Leone', 4854000], 
                         ['Papua New Guinea', 4807000], 
                         ['Kyrgyzstan', 4699000], 
                         ['Togo', 4629000]],
                        ],
                       [[['Africaans']], # 2
                        [['Abhyasi'], 
                         ['Acholi'], 
                         ['Adja'], 
                         ['Afar'], 
                         ['Afrikaans']]],
                       [[[37]], # 3
                        [['37']],
                        [['North America', 37]]],
                       [[[808119]],  # 4
                        [[808119.0000]], 
                        [[808119.00]], 
                        [['808,119']],
                        [['808,119.00']],
                        [['808,119.0000']],
                        [['Australia', '808119.0000']],
                        [['Australia', '80,8119.0000']],
                        [['Australia', '808119.00']],
                        [['Australia', '80,8119.00']]]
                       ]


alias_counter = 0
total_aliases = 2
total_queries = 4

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
            file_contents = file_contents.replace("USE", "-- ~\nUSE")
            file_contents = file_contents.replace("use", "-- ~\nUSE")
            file_contents = file_contents.replace("SELECT", "-- ~\nSELECT")
            file_contents = file_contents.replace("select", "-- ~\nSELECT")
            file_contents = file_contents.replace("(-- ~\nSELECT", "(SELECT")
            file_contents = file_contents.replace("(-- ~\nselect", "(SELECT")
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
        # print("---------------------")

        sqlFile = f.read()
        sqlCommands = sqlFile.split('-- ~')
        # strip the \n from the commands
        sqlCommands = [command.strip() for command in sqlCommands]
        # print(sqlCommands)
        # Filter out SELECT and USE commands
        sqlCommands = [command for command in sqlCommands if (not command.lower().startswith('select *') and command.lower().startswith('select')) or command.lower().startswith('use')]
        use_world_count = 0
        for command in sqlCommands:
            if command.lower().startswith('use world'):
                use_world_count += 1
        if use_world_count > 1:
            answer.write(f"USE bike; command used {use_world_count} times. Only use it once\n")
            answer.write("Skipping to the next file...\n")
            answer.write("***********************************\n\n")
            continue
        
        
        # print(sqlCommands)
        # filter out SELECT @ and SELECT @@ commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('select @') and not command.lower().startswith('select @@')]

        #filter out SET commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('set')]
    
        correct_answer_count = 0
        number = 0
        a_number = 0
        format_counter = 0
        concat_counter = 0
        query4_alias_count = 0
        
        query1_clause_list = []
        query1_function_list = []
        query2_clause_list = []
        query2_function_list = []
        query3_clause_list = []
        query3_function_list = []
        query4_clause_list = []
        query4_function_list = []
    
        
        for command in sqlCommands:
            a_number += 1
            
            # print(f"{a_number}. {command}")
            if a_number == 1 and not command.lower().__contains__('use'):
                answer.write(f"USE world; Statement NOT FOUND\n")


            if a_number == 2: # Query 1
                if command.lower().__contains__('select'):
                    if not command.lower().__contains__('from'):
                        query1_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query1_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query1_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('limit'):
                        query1_clause_list.append(f"LIMIT Clause NOT used")

            if a_number == 3: # Query 2
                if command.lower().__contains__('select'):
                    if not command.lower().__contains__('distinct'):
                        query2_clause_list.append(f"DISTINCT keyword NOT used")
                    if not command.lower().__contains__('from'):
                        query2_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query2_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('limit'):
                        query2_clause_list.append(f"LIMIT Clause NOT used")
                    

            if a_number == 4: # Query 3
                if command.lower().__contains__('select'):
                    
                    if not command.lower().__contains__('from'):
                        query3_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query3_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('group by'):
                        query3_clause_list.append(f"GROUP BY Clause NOT used")
                    if not command.lower().__contains__('count'):
                        query3_function_list.append(f"COUNT Function NOT used")

            if a_number == 5: # Query 4
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        for word in command.split():
                            if word.lower() == 'as':
                                alias_counter += 1
                                query4_alias_count += 1
                    if query4_alias_count < 2:
                        answer.write(f"2 Aliases needed. {2 - query4_alias_count} missing\n")
                    if not command.lower().__contains__(' as '):
                        query4_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query4_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query4_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query4_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('group by'):
                        query4_clause_list.append(f"GROUP BY Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query4_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('avg'):
                        query4_function_list.append(f"AVG Function NOT used")
                    
                        

            

            # pass each list to a function
            # the function will do all the replacing and formatting
            # then return the list
            # print(f"[{command}]")
            new_query1c_list = format_list(query1_clause_list)
            new_query1f_list = format_list(query1_function_list)
            new_query2c_list = format_list(query2_clause_list)
            new_query2f_list = format_list(query2_function_list)
            new_query3c_list = format_list(query3_clause_list)
            new_query3f_list = format_list(query3_function_list)
            new_query4c_list = format_list(query4_clause_list)
            new_query4f_list = format_list(query4_function_list)
            

            try:
                mycursor.execute(command)
            except mysql.connector.Error as e:
                # number the queries run and print the error
                answer.write("Error found. Skipping to the next file...\n")
                answer.write("-------ERROR DETAILS-------\n")
                answer.write(f"Query {number + 1}. Error: {e}\n")
                
                answer.write("------QUERY------\n")
                answer.write(f"{command}\n")
                answer.write("---------------------\n")
                
                break
            output = mycursor.fetchall()
            if len(output) == 0 and command.lower().__contains__('select'):
                answer.write(f"Query {number + 1}. No results returned\n")
                number += 1
                continue

            
            output_list = [list(row) for row in output if row is not None]
            # print(f"[{command}]")

            # change all decimal values to strings
            for row in output_list:
                for i in range(len(row)):
                    if type(row[i]) == decimal.Decimal:
                        row[i] = str(row[i])

            # change all date values to strings
            for row in output_list:
                for i in range(len(row)):
                    if type(row[i]) == datetime.date:
                        row[i] = str(row[i])
                        
            
            # filter out empty commands
            # only output the result if information is returned
            if len(output_list) > 0:
                student_answers = [list(row) for row in output_list if row is not None]
                # final_student_answers.append(student_answers)
                

                # Compare the student answers to the correct answers
                if (student_answers in correct_answer_list or student_answers in correct_answer_list[number]):
                    number += 1
                    correct_answer_count += 1
                    # answer.write(f"Command: {command}\n")
                    # answer.write(f"Student Answer: {student_answers}\n")
                
                else:
                    number += 1

                    answer.write("---------------------\n")
                    answer.write(f"{number}. Incorrect!\n")
                    # 1, and 5 are the USE statments
                    # check for certain clauses and print that they were used
                    answer.write("------QUERY------\n")
                    answer.write(f"{command}\n")
                    answer.write("-----CLAUSES-----\n")
                    if a_number == 2:
                        # print(new_query1_list)
                        if len(new_query1c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query1c_list}\n")
                    elif a_number == 3:
                        # print(new_query2_list)
                        if len(new_query2c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query2c_list}\n")
                    elif a_number == 4:
                        # print(new_query3_list)
                        if len(new_query3c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query3c_list}\n")
                    elif a_number == 5:
                        # print(new_query4_list)
                        if len(new_query4c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query4c_list}\n")

                    answer.write("----FUNCTIONS----\n")
                    if a_number == 2:
                        # print(new_query1_list)
                        if len(new_query1f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query1f_list}\n")
                    if a_number == 3:
                        # print(new_query2_list)
                        if len(new_query2f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query2f_list}\n")
                    if a_number == 4:
                        # print(new_query3_list)
                        if len(new_query3f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query3f_list}\n")
                    if a_number == 5:
                        # print(new_query4_list)
                        if len(new_query4f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query4f_list}\n")
                   
                    answer.write("-----ANSWERS-----\n")
                    
                    answer.write(f"Student Answer: {student_answers}\n")
                    answer.write(f"Correct Answer: {correct_answer_list[number-1]}\n")
                    answer.write("---------------------\n")
        answer.write("--------RESULTS-------\n") 
        answer.write(f"{alias_counter}/{total_aliases} Aliases Used\n")
        answer.write(f"{number}/{total_queries} Queries Written\n")
        answer.write(f"{correct_answer_count}/{total_queries} Queries Correct\n")

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
        answer = open(f"week08answers.txt", "w")
        answer.close()
    else:
        print("Files Kept")
    # print("***********************************")
        
    # print("***********************************\n")
    # print("***********************************")
