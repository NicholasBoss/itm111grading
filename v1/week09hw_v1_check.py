import os
import platform
os_name = platform.system()
try: 
    import mysql.connector
except ImportError or ModuleNotFoundError:
    print("MYSQL module not found. Installing...")
    if os_name == 'Windows':
        os.system("pip install mysql-connector-python")
    elif os_name == 'Linux' or os_name == 'Darwin':
        os.system("pip3 install mysql-connector-python")
    import mysql.connector
    print("MYSQL module installed")
import decimal
import time

# start timer
start_time = time.time()

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


correct_answer_list = [[[['irises.jpg'], # 1
                        ['womengarden.jpg']],
                        [['Irises', 'irises.jpg'], ['Woman in the Garden', 'womengarden.jpg']],
                        [['Irises'], ['Woman in the Garden']]],
                       [[['irises.jpg'], # 2
                        ['sunflowers.jpg'], 
                        ['womengarden.jpg']],
                        [['irises.jpg', 'flowers'], ['sunflowers.jpg', 'flowers'], ['womengarden.jpg', 'flowers']],
                        [['Irises'], ['Sunflowers'], ['Woman in the Garden']],
                        [['Irises', 'flowers'], ['Sunflowers', 'flowers'], ['Woman in the Garden', 'flowers']]],
                       [['Vincent', 'van Gogh', 'Irises'], # 3
                        ['Vincent', 'van Gogh', 'Starry Night'], 
                        ['Vincent', 'van Gogh', 'Sunflowers'], 
                        ['Rembrandt', 'van Rijn', 'Night Watch'], 
                        ['Rembrandt', 'van Rijn', 'Storm on the Sea of Galilee'], 
                        ['Leonardo', 'da Vinci', 'Head of a Woman'], 
                        ['Leonardo', 'da Vinci', 'Last Supper'], 
                        ['Leonardo', 'da Vinci', 'Mona Lisa'], 
                        ['Venture', 'Coy', 'Hillside Stream'], 
                        ['Venture', 'Coy', 'Old Barn'], 
                        ['Deborah', 'Gill', 'Beach Baby'], 
                        ['Claude', 'Monet', 'Woman in the Garden'], 
                        ['Pablo', 'Picasso', 'Old Guitartist'], 
                        ['Michelangelo', 'Simoni', None]],
                       [[['Beautiful Birds', 'Sanders', 'Samantha'], # 4
                        ['Beautiful Birds', 'Lamont', 'Lucy'], 
                        ['Car Racing Made Easy', 'Anderson', 'Albert'], 
                        ['Cooking Like Mad', 'Sanders', 'Samantha'], 
                        ['Corn Shucking for Fun and Profit', 'Lamont', 'Lucy'], 
                        ['Corn Shucking for Fun and Profit', 'Jimenez', 'Jose'], 
                        ['Fishing in the Mojave', 'Johnston', 'Julie'], 
                        ['Fishing in the Mojave', 'Sanders', 'Samantha'], 
                        ['Fishing in the Mojave', 'Jimenez', 'Jose'], 
                        ['If Only I Could Sing', 'Sanders', 'Samantha'], 
                        ['Pine Cone Computing', 'Sanders', 'Samantha']],
                        [['Beautiful Birds', 'Samantha', 'Sanders'], ['Beautiful Birds', 'Lucy', 'Lamont'], ['Car Racing Made Easy', 'Albert', 'Anderson'], ['Cooking Like Mad', 'Samantha', 'Sanders'], ['Corn Shucking for Fun and Profit', 'Lucy', 'Lamont'], ['Corn Shucking for Fun and Profit', 'Jose', 'Jimenez'], ['Fishing in the Mojave', 'Julie', 'Johnston'], ['Fishing in the Mojave', 'Samantha', 'Sanders'], ['Fishing in the Mojave', 'Jose', 'Jimenez'], ['If Only I Could Sing', 'Samantha', 'Sanders'], ['Pine Cone Computing', 'Samantha', 'Sanders']],
                        [['Sanders', 'Samantha', 'Beautiful Birds'], ['Lamont', 'Lucy', 'Beautiful Birds'], ['Anderson', 'Albert', 'Car Racing Made Easy'], ['Sanders', 'Samantha', 'Cooking Like Mad'], ['Lamont', 'Lucy', 'Corn Shucking for Fun and Profit'], ['Jimenez', 'Jose', 'Corn Shucking for Fun and Profit'], ['Johnston', 'Julie', 'Fishing in the Mojave'], ['Sanders', 'Samantha', 'Fishing in the Mojave'], ['Jimenez', 'Jose', 'Fishing in the Mojave'], ['Sanders', 'Samantha', 'If Only I Could Sing'], ['Sanders', 'Samantha', 'Pine Cone Computing']]],
                       [[['Beautiful Birds'], # 5
                        ['Cooking Like Mad'], 
                        ['Fishing in the Mojave'], 
                        ['If Only I Could Sing'], 
                        ['Pine Cone Computing']],
                        [['Beautiful Birds', 'Sanders', 'Samantha'], ['Cooking Like Mad', 'Sanders', 'Samantha'], ['Fishing in the Mojave', 'Sanders', 'Samantha'], ['If Only I Could Sing', 'Sanders', 'Samantha'], ['Pine Cone Computing', 'Sanders', 'Samantha']]],
                       [[['Youpyo', 'Aamodt'], # 6
                        ['Basim', 'Aamodt'], 
                        ['Rajmohan', 'Aamodt'], 
                        ['Marla', 'Aamodt'], 
                        ['Arumugam', 'Aamodt']],
                        [['Youpyo', 'Aamodt', 'Customer Service'], ['Basim', 'Aamodt', 'Customer Service'], ['Rajmohan', 'Aamodt', 'Customer Service'], ['Marla', 'Aamodt', 'Customer Service'], ['Arumugam', 'Aamodt', 'Customer Service']],
                        [['Aamodt', 'Youpyo'], ['Aamodt', 'Basim'], ['Aamodt', 'Rajmohan'], ['Aamodt', 'Marla'], ['Aamodt', 'Arumugam']]],
                       [[['Mayuko', 'Warwick', 'Production', '$47,017.00']], # 7
                        [['Mayuko', 'Warwick', 'Production', '$47,017']],
                        [['Mayuko', 'Warwick', '$47,017', 'Production']]] 
                      ]

alias_counter = 0
total_aliases = 1
total_queries = 7

# open the test folder and read the files inside
if os_name == 'Windows':
    print("Windows OS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '\\tempgrades'
    answer = open(f"{directory}\\week09answers.txt", "w")

elif os_name == 'Linux':
    print("Linux Detected")
    directory = '/home/student/Desktop/itm111grading/v1'
    grading_directory = '/home/student/Desktop/itm111grading/v1/tempgrades'
    answer = open(f"{directory}/week09answers.txt", "w")

elif os_name == 'Darwin':
    print("MacOS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '/tempgrades'
    answer = open(f"{directory}/week09answers.txt", "w")
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
        use_v_art_count = 0
        use_employees_count = 0
        use_magazine_count = 0
        for command in sqlCommands:
            if command.lower().startswith('use v_art'):
                use_v_art_count += 1
            if command.lower().startswith('use employees'):
                use_employees_count += 1
            if command.lower().startswith('use magazine'):
                use_magazine_count += 1
        if use_v_art_count > 1:
            answer.write(f"USE v_art; command used {use_v_art_count} times. Only use it once\n")
            answer.write("Skipping to the next file...\n")
            answer.write("***********************************\n\n")
            continue
        if use_employees_count > 1:
            answer.write(f"USE employees; command used {use_employees_count} times. Only use it once\n")
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
        join_counter = 0
        query1_clause_list = []
        query2_clause_list = []
        query3_clause_list = []
        query4_clause_list = []
        query5_clause_list = []
        query6_clause_list = []
        query7_clause_list = []
        query7_function_list = []
        
        for command in sqlCommands:
            a_number += 1
            
            # debug.write(f"Query {a_number}. {command}\n")            
            if a_number == 1 and not command.lower().__contains__('use'):
                answer.write(f"USE v_art; Statement NOT FOUND\n")


            if a_number == 2: # Query 1
                if command.lower().__contains__('select'):
                   
                    if not command.lower().__contains__('from'):
                        query1_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query1_clause_list.append(f"WHERE Clause NOT used")

            if a_number == 3: # Query 2
                if command.lower().__contains__('select'):
                    
                    if not command.lower().__contains__('from'):
                        query2_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query2_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query2_clause_list.append(f"WHERE Clause NOT used")
                    

            if a_number == 4: # Query 3
                if command.lower().__contains__('select'):
                    
                    if not command.lower().__contains__('from'):
                        query3_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('left join'):
                        query3_clause_list.append(f"LEFT JOIN Clause NOT used")
            
            if a_number == 5 and not command.lower().__contains__('use'):
                if not command.lower().__contains__('use'):
                    answer.write(f"USE magazine; Statement NOT FOUND\n")

            if a_number == 6: # Query 4
                if command.lower().__contains__('select'):
                    
                    if not command.lower().__contains__('from'):
                        query4_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query4_clause_list.append(f"JOIN Clause NOT used")
                    
            if a_number == 7: # Query 5
                if command.lower().__contains__('select'):
                    
                    if not command.lower().__contains__('from'):
                        query5_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query5_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query5_clause_list.append(f"WHERE Clause NOT used")

            if a_number == 8 and not command.lower().__contains__('use'): 
                if command.lower().__contains__('use'):
                    answer.write(f"USE employees; Statement NOT FOUND\n")

            if a_number == 9: # Query 6
                if command.lower().__contains__('select'):
                    
                    if not command.lower().__contains__('from'):
                        query6_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query6_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('join dept_emp'):
                        query6_clause_list.append(f"dept_emp table NOT used")
                    if not command.lower().__contains__('where'):
                        query6_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query6_clause_list.append(f"ORDER BY Clause NOT used")
                    
            if a_number == 10: # Query 7
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                    if not command.lower().__contains__(' as '):
                        query7_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query7_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query7_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('join dept_emp'):
                        query7_clause_list.append(f"dept_emp table NOT used")
                    if not command.lower().__contains__('where'):
                        query7_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query7_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('limit'):
                        query7_clause_list.append(f"LIMIT Clause NOT used")
                    if not command.lower().__contains__('concat(\'$\','):
                        query7_function_list.append(f"CONCAT Function NOT used")
                    if not command.lower().__contains__('format'):
                        query7_function_list.append(f"FORMAT Function NOT used")

            # pass each list to a function
            # the function will do all the replacing and formatting
            # then return the list
            
            new_query1c_list = format_list(query1_clause_list)
            new_query2c_list = format_list(query2_clause_list)
            new_query3c_list = format_list(query3_clause_list)
            new_query4c_list = format_list(query4_clause_list)
            new_query5c_list = format_list(query5_clause_list)
            new_query6c_list = format_list(query6_clause_list)
            new_query7c_list = format_list(query7_clause_list)
            new_query7f_list = format_list(query7_function_list)

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
            if a_number not in(1,5,8):
                output = mycursor.fetchall()
                # print(f"{a_number}. {number + 1} retrieved\n")
            # if the commans was a SELECT statement, and it didn't return
            # any results, print that no results were returned in the output list
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
            
            # filter out empty commands
            # only output the result if information is returned
            if len(output_list) > 0:
                student_answers = [list(row) for row in output_list if row is not None]
                

                # Compare the student answers to the correct answers
                if (student_answers in correct_answer_list or student_answers in correct_answer_list[number]):
                    number += 1
                    correct_answer_count += 1
                    
                
                else:
                    number += 1

                    answer.write("---------------------\n")
                    answer.write(f"{number}. Incorrect!\n")
                    # 1, 5, 8 are the USE statments
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
                    elif a_number == 9:
                        # debug.write(new_query6_list)
                        if len(new_query6c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query6c_list}\n")
                    elif a_number == 10:
                        # debug.write(new_query7_list)
                        if len(new_query7c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query7c_list}\n")

                    answer.write("----FUNCTIONS----\n")
                    if a_number == 2:
                        # debug.write(new_query1_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 3:
                        # debug.write(new_query2_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 4:
                        # debug.write(new_query3_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 6:
                        # debug.write(new_query4_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 7:
                        # debug.write(new_query5_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 9:
                        # debug.write(new_query6_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 10:
                        # debug.write(new_query7f_list)
                        if len(new_query7f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query7f_list}\n")
                    answer.write("-----ANSWERS-----\n")
                    
                    answer.write(f"Student Answer: {student_answers}\n")
                    answer.write(f"Correct Answer: {correct_answer_list[number-1]}\n")
                    answer.write("---------------------\n")
        # end timer
        end_time = time.time()
        answer.write("--------RESULTS-------\n") 
        answer.write(f"{alias_counter}/{total_aliases} Alias Used\n")
        answer.write(f"{number}/{total_queries} Queries Written\n")
        answer.write(f"{correct_answer_count}/{total_queries} Queries Correct\n")

        
        alias_counter = 0
        answer.write("***********************************\n\n")
    answer.write("***********************************\n")
    answer.write(f"Total Files Graded: {file_count}\n")
    answer.write(f"Total Time Elapsed: {end_time - start_time:.2f} seconds\n")
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
            os.remove(f"{directory}\\week09answers.txt")
        elif os_name == 'Linux' or os_name == 'Darwin':
            os.remove(f"{directory}/week09answers.txt")
        print("Files Deleted")
    else:
        f.close()
        print("Files Kept")

