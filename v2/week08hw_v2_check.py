import mysql.connector
import decimal
import datetime
import os
import platform


def format_list(list):
    list = [str(item) for item in list]
    new_list = '\n'.join(list)
    new_list = new_list.replace('[', '')
    new_list = new_list.replace(']', '')
    new_list = new_list.replace("'", "")
    return new_list

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="student",
    password="student",
)

# Create a cursor
mycursor = mydb.cursor()


correct_answer_list = [[['Fishing in the Mojave', '12.97'], # 1
                        ['Car Racing Made Easy', '14.37'], 
                        ['Pine Cone Computing', '16.28'], 
                        ['Cooking Like Mad', '16.74'], 
                        ['If Only I Could Sing', '11.58'], 
                        ['Beautiful Birds', '11.58'], 
                        ['Corn Shucking for Fun and Profit', '14.00'], 
                        ['MySQL Magic', '10.18']],
                       [[1, '12'], # 2
                        [2, '12'], 
                        [3, '11'], 
                        [5, '11'], 
                        [3, '12'], 
                        [5, '11'], 
                        [4, '11'], 
                        [3, '12'], 
                        [4, '12'], 
                        [3, '12'], 
                        [3, '12']],
                       [['March 1st, 2011', 12, 'March 1st, 2012'], # 3
                        ['March 1st, 2011', 14, 'May 1st, 2012'], 
                        ['February 1st, 2012', 12, 'February 1st, 2013'], 
                        ['February 1st, 2012', 12, 'February 1st, 2013'], 
                        ['September 1st, 2011', 12, 'September 1st, 2012'], 
                        ['July 1st, 2012', 24, 'July 1st, 2014'], 
                        ['August 1st, 2012', 12, 'August 1st, 2013'], 
                        ['May 1st, 2011', 12, 'May 1st, 2012'], 
                        ['September 1st, 2011', 12, 'September 1st, 2012'], 
                        ['December 1st, 2011', 12, 'December 1st, 2012'], 
                        ['May 1st, 2011', 18, 'November 1st, 2012']],
                       [['Trek Checkpoint ALR Frameset'], # 4
                        ['Trek Checkpoint SL 6'], 
                        ["Trek Checkpoint SL 5 Women's"], 
                        ["Trek Checkpoint ALR 5 Women's"], 
                        ['Trek Checkpoint ALR 5'], 
                        ["Trek Checkpoint ALR 4 Women's"], 
                        ["Electra Townie Original 21D Ladies'"], 
                        ["Electra Townie Original 21D EQ Ladies'"], 
                        ["Electra Townie Original 1 Ladies'"], 
                        ["Electra Townie Commute 8D Ladies'"], 
                        ['Electra Townie Commute 8D'], 
                        ['Electra Townie Commute 27D Ladies'], 
                        ['Electra Townie Commute 27D'], 
                        ["Electra Townie Balloon 8D EQ Ladies'"]],
                       [["Trek Checkpoint ALR 4 Women's - 2019", '$1,699.99', '$85.00', '$161.50'], # 5
                        ['Trek Checkpoint ALR 5 - 2019', '$1,999.99', '$100.00', '$190.00'], 
                        ["Trek Checkpoint ALR 5 Women's - 2019", '$1,999.99', '$100.00', '$190.00'], 
                        ["Trek Checkpoint SL 5 Women's - 2019", '$2,799.99', '$140.00', '$266.00'], 
                        ['Trek Checkpoint SL 6 - 2019', '$3,799.99', '$190.00', '$361.00'], 
                        ['Trek Checkpoint ALR Frameset - 2019', '$3,199.99', '$160.00', '$304.00']]
                      ]

alias_counter = 0
total_aliases = 8
total_queries = 5

# open the test folder and read the files inside
os_name = platform.system()
if os_name == 'Windows':
    print("Windows OS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '\\tempgrades'
    answer = open(f"{directory}\\week08answers.txt", "w")

elif os_name == 'Linux' or os_name == 'Darwin':
    print("Linux/MacOS Detected")
    directory = os.getcwd() + '/v3'
    grading_directory = os.getcwd() + '/v3/tempgrades'
    answer = open(f"{directory}/week08answers.txt", "w")
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
            file_contents = file_contents.replace("SELECT", "-- ~\nSELECT")
            file_contents = file_contents.replace("(-- ~\nSELECT", "(SELECT")
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
        # print("---------------------")

        sqlFile = f.read()
        sqlCommands = sqlFile.split('-- ~')
        # strip the \n from the commands
        sqlCommands = [command.strip() for command in sqlCommands]
                # Filter out SELECT and USE commands
        sqlCommands = [command for command in sqlCommands if (not command.lower().startswith('select *') and command.lower().startswith('select')) or command.lower().startswith('use')]
        use_bike_count = 0
        use_magazine_count = 0
        for command in sqlCommands:
            if command.lower().startswith('use bike'):
                use_bike_count += 1
            if command.lower().startswith('use magazine'):
                use_magazine_count += 1
        if use_bike_count > 1:
            answer.write(f"USE bike; command used {use_bike_count} times. Only use it once\n")
            answer.write("Skipping to the next file...\n")
            answer.write("***********************************\n\n")
            continue
        if use_magazine_count > 1:
            answer.write(f"USE magazine; command used {use_magazine_count} times. Only use it once\n")
            answer.write("Skipping to the next file...\n")
            answer.write("***********************************\n\n")
            continue
        
        
        # debug.write(f"COMMAND LIST: {sqlCommands}")
        # filter out SELECT @ and SELECT @@ commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('select @') and not command.lower().startswith('select @@')]

        #filter out SET commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('set')]
    
        correct_answer_count = 0
        number = 0
        a_number = 0
        date_format_counter = 0
        format_counter = 0
        concat_counter = 0
        query3_alias_counter = 0
        query5_alias_counter = 0
        
        query1_clause_list = []
        query1_function_list = []
        query2_clause_list = []
        query2_function_list = []
        query3_clause_list = []
        query3_function_list = []
        query4_clause_list = []
        query4_function_list = []
        query5_clause_list = []
        query5_function_list = []
    
        
        for command in sqlCommands:
            a_number += 1
            
            # debug.write(f"Query {a_number}. {command}\n")            
            if a_number == 1 and not command.lower().__contains__('use'):
                answer.write(f"USE magazine; Statement NOT FOUND\n")


            if a_number == 2: # Query 1
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                    if not command.lower().__contains__(' as '):
                        query1_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query1_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('round'):
                        query1_function_list.append(f"ROUND Function NOT used")

            if a_number == 3: # Query 2
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                    if not command.lower().__contains__(' as '):
                        query2_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query2_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('round'):
                        query2_function_list.append(f"ROUND Function NOT used")
                    if not command.lower().__contains__('datediff'):
                        query2_function_list.append(f"DATEDIFF Function NOT used")
                    if not command.lower().__contains__('(\'2020-12-20\', subscriptionStartDate)'):
                        query2_function_list.append(f"DATEDIFF parameters out of order")
                    

            if a_number == 4: # Query 3
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        for word in command.split():
                            if word.lower() == 'as':
                                alias_counter += 1
                                query3_alias_counter += 1
                    if query3_alias_counter < 2:
                        query3_clause_list.append(f"2 Aliases are needed. {2 - query3_alias_counter} missing")
                    if not command.lower().__contains__(' as '):
                        query3_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query3_clause_list.append(f"FROM Clause NOT used")
                    if not command.__contains__('DATE_FORMAT(subscriptionStartDate,\'%m %d, %y\')'):
                        query3_function_list.append(f"DATE_FORMAT Function NOT used on first column")
                    if not command.lower().__contains__('date_format'):
                        query3_function_list.append(f"DATE_FORMAT Function NOT used")
                    if not command.lower().__contains__('date_add'):
                        query3_function_list.append(f"DATE_ADD Function NOT used")
                    if not command.__contains__("'%M %D, %Y'"):
                        query3_function_list.append(f"Date format NOT correct")
                    if not command.__contains__('subscriptionLength MONTH'):
                        query3_function_list.append(f"MONTH timeunit NOT used")
            
            if a_number == 5 and not command.lower().__contains__('use'):
                if not command.lower().__contains__('use'):
                    answer.write(f"USE bike; Statement NOT FOUND\n")

            if a_number == 6: # Query 4
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                    if not command.lower().__contains__(' as '):
                        query4_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query4_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query4_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('limit'):
                        query4_clause_list.append(f"LIMIT Clause NOT used")
                    if not command.lower().__contains__('substring'):
                        query4_function_list.append(f"SUBSTRING Function NOT used")
                    
            if a_number == 7: # Query 5
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        for word in command.split():
                            if word.lower() == 'as':
                                alias_counter += 1
                                query5_alias_counter += 1
                    if query5_alias_counter < 3:
                        query5_clause_list.append(f"3 Aliases are needed. {3 - query5_alias_counter} missing")
                    if not command.lower().__contains__(' as '):
                        query5_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query5_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query5_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('concat'):
                        query5_function_list.append(f"CONCAT Function NOT used")
                    if not command.lower().__contains__('format('):
                        query5_function_list.append(f"FORMAT Function NOT used")
                        
                        

            

            # pass each list to a function
            # the function will do all the replacing and formatting
            # then return the list
            
            new_query1c_list = format_list(query1_clause_list)
            new_query1f_list = format_list(query1_function_list)
            new_query2c_list = format_list(query2_clause_list)
            new_query2f_list = format_list(query2_function_list)
            new_query3c_list = format_list(query3_clause_list)
            new_query3f_list = format_list(query3_function_list)
            new_query4c_list = format_list(query4_clause_list)
            new_query4f_list = format_list(query4_function_list)
            new_query5c_list = format_list(query5_clause_list)
            new_query5f_list = format_list(query5_function_list)
            
            output = ''
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
            if a_number not in(1,5):
                output = mycursor.fetchall()
            if len(output) == 0 and command.lower().__contains__('select'):
                answer.write(f"Query {number + 1}. No results returned\n")
                number += 1
                continue

            
            output_list = [list(row) for row in output if row is not None]
            

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
                        # debug.write(new_query1_list)
                        if len(new_query1c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query1c_list}\n")
                    elif a_number == 3:
                        # debug.write(new_query2_list)
                        if len(new_query2c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query2c_list}\n")
                    elif a_number == 4:
                        # debug.write(new_query3_list)
                        if len(new_query3c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query3c_list}\n")
                    elif a_number == 6:
                        # debug.write(new_query4_list)
                        if len(new_query4c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query4c_list}\n")
                    elif a_number == 7:
                        # debug.write(new_query5_list)
                        if len(new_query5c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query5c_list}\n")

                    answer.write("----FUNCTIONS----\n")
                    if a_number == 2:
                        # debug.write(new_query1f_list)
                        if len(new_query1f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query1f_list}\n")
                    if a_number == 3:
                        # debug.write(new_query2f_list)
                        if len(new_query2f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query2f_list}\n")
                    if a_number == 4:
                        # debug.write(new_query3f_list)
                        if len(new_query3f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query3f_list}\n")
                    if a_number == 6:
                        # debug.write(new_query4f_list)
                        if len(new_query4f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query4f_list}\n")
                    if a_number == 7:
                        # debug.write(new_query5f_list)
                        if len(new_query5f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query5f_list}\n")
                   
                    answer.write("-----ANSWERS-----\n")
                    
                    answer.write(f"Student Answer: {student_answers}\n")
                    answer.write(f"Correct Answer: {correct_answer_list[number-1]}\n")
                    answer.write("---------------------\n")
        answer.write("--------RESULTS-------\n") 
        answer.write(f"{alias_counter}/{total_aliases} Aliases Used\n")
        answer.write(f"{number}/{total_queries} Queries Written\n")
        answer.write(f"{correct_answer_count}/{total_queries} Queries Correct\n")

        
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
        f.close()
        for filename in os.listdir(grading_directory):
            os.remove(f"{grading_directory}/{filename}")
        if os_name == 'Windows':
            os.remove(f"{directory}\\week08answers.txt")
        elif os_name == 'Linux' or os_name == 'Darwin':
            os.remove(f"{directory}/week08answers.txt")
        print("Files Deleted")
    else:
        f.close()
        print("Files Kept")

