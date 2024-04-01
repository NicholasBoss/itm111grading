import mysql.connector
import decimal
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


correct_answer_list = [[[[14]],[['14']]], #1
                       [['Electra Amsterdam Royal 8i Ladies - 2018'], # 2
                        ["Electra Cruiser 1 Ladies' - 2018"], 
                        ["Electra Girl's Hawaii 1 (16-inch) - 2015/2016"], 
                        ['Electra Townie Commute Go! - 2018'], 
                        ['Electra Townie Go! 8i - 2017/2018'], 
                        ['Electra Townie Original 1 - 2018'], 
                        ["Electra Townie Original 1 Ladies' - 2018"], 
                        ['Electra Townie Original 21D - 2018'], 
                        ["Electra Townie Original 3i EQ Ladies' - 2018"], 
                        ['Haro Shredder 20 - 2017'], 
                        ['Surly Ice Cream Truck Frameset - 2016'], 
                        ['Surly Pack Rat - 2018'], 
                        ['Surly Straggler - 2018'], 
                        ['Surly Wednesday Frameset - 2016'], 
                        ['Trek CrossRip 1 - 2018'], 
                        ['Trek Domane S 5 Disc - 2017'], 
                        ['Trek Domane SL 6 Disc - 2018'], 
                        ['Trek Domane SLR Frameset - 2018'], 
                        ['Trek Emonda SLR 6 - 2018'], 
                        ['Trek Farley Alloy Frameset - 2017'], 
                        ['Trek Fuel EX 5 27.5 Plus - 2017'], 
                        ['Trek Precaliber 24 (21-Speed) - Girls - 2017'], 
                        ['Trek Remedy 29 Carbon Frameset - 2016'], 
                        ['Trek Remedy 9.8 - 2017']],
                       [[['Cyclocross Bicycles', '97'], # 3
                         ['Electric Bikes', '328'], 
                         ['Comfort Bicycles', '393'], 
                         ['Road Bikes', '758'], 
                         ['Children Bicycles', '769'], 
                         ['Mountain Bikes', '877'], 
                         ['Cruisers Bicycles', '1137']]],
                       [[300024]], # 4
                       [[['Customer Service', '$58,755.44'], # 5
                         ['Development', '$59,503.57'], 
                         ['Human Resources', '$55,353.52'], 
                         ['Production', '$59,539.79'], 
                         ['Quality Management', '$57,294.66'], 
                         ['Research', '$59,866.24']],
                         [['Customer Service', '58,755.44'], 
                         ['Development', '59,503.57'], 
                         ['Human Resources', '55,353.52'], 
                         ['Production', '59,539.79'], 
                         ['Quality Management', '57,294.66'], 
                         ['Research', '59,866.24']]
                        ],
                       [['Customer Service', 9448], # 6
                        ['Development', 34258], 
                        ['Finance', 7015], 
                        ['Human Resources', 7075], 
                        ['Marketing', 8037], 
                        ['Production', 29549], 
                        ['Quality Management', 8078], 
                        ['Research', 8439], 
                        ['Sales', 20854]]
                        ]


alias_counter = 0
total_aliases = 5
total_queries = 6

# open the test folder and read the files inside
os_name = platform.system()
if os_name == 'Windows':
    print("Windows OS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '\\tempgrades'
    answer = open(f"{directory}\\week10answers.txt", "w")

elif os_name == 'Linux' or os_name == 'Darwin':
    print("Linux/MacOS Detected")
    directory = os.getcwd() + '/original'
    grading_directory = os.getcwd() + '/original/tempgrades'
    answer = open(f"{directory}/week10answers.txt", "w")
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
        # check to see if delimiter exists
        if not file_contents.__contains__('-- ~'):
            print("Formatting File...")
            file_contents = file_contents.replace("SET", "-- ~\nSET")
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
        

        sqlFile = f.read()
        sqlCommands = sqlFile.split('-- ~')
        # strip the \n from the commands
        sqlCommands = [command.strip() for command in sqlCommands]
                # Filter out SELECT and USE commands
        
        
        sqlCommands = [command for command in sqlCommands if (not command.lower().startswith('select *') and command.lower().startswith('select')) or command.lower().startswith('use')]
        # check to make sure there are only 2 USE commands
        use_bike_count = 0
        use_employees_count = 0
        for command in sqlCommands:
            if command.lower().startswith('use bike'):
                use_bike_count += 1
            if command.lower().startswith('use employees'):
                use_employees_count += 1
        if use_bike_count > 1:
            answer.write(f"USE bike; command used {use_bike_count} times. Only use it once\n")
            answer.write("Skipping to the next file...\n")
            answer.write("***********************************\n\n")
            continue
        if use_employees_count > 1:
            answer.write(f"USE employees; command used {use_employees_count} times. Only use it once\n")
            answer.write("Skipping to the next file...\n")
            answer.write("***********************************\n\n")
            continue
        


        # debug.write(f"COMMAND LIST: {sqlCommands}")
        # filter out SELECT @ and SELECT @@ commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('select @') and not command.lower().startswith('select @@')]
        
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('select*')]
        #filter out SET commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('set')]
    
        correct_answer_count = 0
        number = 0
        a_number = 0
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
        query6_clause_list = []
        query6_function_list = []
        
        for command in sqlCommands:
            a_number += 1
            
            # debug.write(f"Query {a_number}. {command}\n")            
            if a_number == 1 and not command.lower().__contains__('use'):
                answer.write(f"USE bike; Statement NOT FOUND\n")


            if a_number == 2: # Query 1
                if command.lower().__contains__('select'):
                    
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                        
                    if not command.lower().__contains__(' as '):
                        query1_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query1_clause_list.append(f"FROM Clause NOT used")
                    if command.lower().__contains__('where'):
                        query1_clause_list.append(f"WHERE Clause used")
                    if not command.lower().__contains__('avg'):
                        query1_function_list.append(f"AVG Function NOT used")
                    if not command.lower().__contains__('round'):
                        query1_function_list.append(f"ROUND Function NOT used")

            if a_number == 3: # Query 2
                if command.lower().__contains__('select'):
                    if not command.lower().__contains__('distinct'):
                        query2_clause_list.append(f"DISTINCT NOT used")
                    if not command.lower().__contains__('from'):
                        query2_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query2_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query2_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query2_clause_list.append(f"ORDER BY Clause NOT used")


            if a_number == 4: # Query 3
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                        
                    if not command.lower().__contains__(' as '):
                        query3_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query3_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('sum'):
                        query3_function_list.append(f"SUM Function NOT used")
                    if not command.lower().__contains__('join'):
                        query3_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query3_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('group by'):
                        query3_clause_list.append(f"GROUP BY Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query3_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('order by sum(quantity)') and not command.lower().__contains__('order by sum(quantity) asc'):
                        query3_clause_list.append(f"SUM(quantity) NOT used in ORDER BY Clause")
                
            if a_number == 6: # Query 4
                if command.lower().__contains__('select'):
                    
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                        
                    if not command.lower().__contains__(' as '):
                        query4_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query4_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('count'):
                        query4_function_list.append(f"COUNT Function NOT used")
                    
            if a_number == 7: # Query 5
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                        
                    if not command.lower().__contains__(' as '):
                        query5_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query5_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query5_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('group by'):
                        query5_clause_list.append(f"GROUP BY Clause NOT used")
                    if not command.lower().__contains__('having'):
                        query5_clause_list.append(f"HAVING Clause NOT used")
                    if not command.lower().__contains__('format'):
                        query5_function_list.append(f"FORMAT Function NOT used")
                    
            if a_number == 8: # Query 6
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                        
                    if not command.lower().__contains__(' as '):
                        query5_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query6_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query6_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query6_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('group by'):
                        query6_clause_list.append(f"GROUP BY Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query6_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('count'):
                        query6_function_list.append(f"COUNT Function NOT used")
                    
                    

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
            new_query6c_list = format_list(query6_clause_list)
            new_query6f_list = format_list(query6_function_list)

            
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
            
            # filter out empty commands
            # only output the result if information is returned
            if len(output_list) > 0:
                student_answers = [list(row) for row in output_list if row is not None]
                

                # Compare the student answers to the correct answers
                if (student_answers in correct_answer_list or student_answers in correct_answer_list[number]) :
                    number += 1
                    correct_answer_count += 1
                    
                
                else:
                    number += 1

                    answer.write("---------------------\n")
                    answer.write(f"{number}. Incorrect!\n")
                    
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
                    elif a_number == 8:
                        # debug.write(new_query6_list)
                        if len(new_query6c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query6c_list}\n")

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
                    elif a_number == 8:
                        # debug.write(new_query6f_list)
                        if len(new_query6f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query6f_list}\n")
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
    mydb.close()
    delete_files = input("Would you like to delete the files in the tempgrades folder? (yes/no): ")
    if delete_files.lower() == "yes":
        f.close()
        for filename in os.listdir(grading_directory):
            os.remove(f"{grading_directory}/{filename}")
        if os_name == 'Windows':
            os.remove(f"{directory}\\week10answers.txt")
        elif os_name == 'Linux' or os_name == 'Darwin':
            os.remove(f"{directory}/week10answers.txt")
        print("Files Deleted")
    else:
        f.close()
        print("Files Kept")

