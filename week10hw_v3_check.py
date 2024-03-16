import mysql.connector
import decimal
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

answer = open(f"week10answers.txt", "w")

# print("***********************************")

# Create a cursor
mycursor = mydb.cursor()


correct_answer_list = [[[939]], #1
                   [['Santa Cruz Bikes', 10], #2
                    ['Baldwin Bikes', 10], 
                    ['Rowlett Bikes', 5]],
                    [[['Cyclocross Bicycles', '158', 'Santa Cruz Bikes'], #3 
                      ['Electric Bikes', '368', 'Santa Cruz Bikes'], 
                      ['Comfort Bicycles', '425', 'Santa Cruz Bikes'], 
                      ['Road Bikes', '687', 'Santa Cruz Bikes'], 
                      ['Mountain Bikes', '849', 'Santa Cruz Bikes'], 
                      ['Children Bicycles', '952', 'Santa Cruz Bikes'], 
                      ['Cruisers Bicycles', '1093', 'Santa Cruz Bikes']],
                     [['Santa Cruz Bikes', 'Cyclocross Bicycles', '158'], 
                      ['Santa Cruz Bikes', 'Electric Bikes', '368'], 
                      ['Santa Cruz Bikes', 'Comfort Bicycles', '425'], 
                      ['Santa Cruz Bikes', 'Road Bikes', '687'], 
                      ['Santa Cruz Bikes', 'Mountain Bikes', '849'], 
                      ['Santa Cruz Bikes', 'Children Bicycles', '952'], 
                      ['Santa Cruz Bikes', 'Cruisers Bicycles', '1093']], 
                     [['Cyclocross Bicycles', '158'], 
                      ['Electric Bikes', '368'], 
                      ['Comfort Bicycles', '425'], 
                      ['Road Bikes', '687'], 
                      ['Mountain Bikes', '849'], 
                      ['Children Bicycles', '952'], 
                      ['Cruisers Bicycles', '1093']]],
                   [[['Customer Service', 4], # 4
                     ['Development', 2], 
                     ['Finance', 2], 
                     ['Human Resources', 2], 
                     ['Marketing', 2], 
                     ['Production', 4], 
                     ['Quality Management', 4], 
                     ['Research', 2], 
                     ['Sales', 2], 
                     [None, 24]],
                    [['Customer Service', 4], # 4
                     ['Development', 2], 
                     ['Finance', 2], 
                     ['Human Resources', 2], 
                     ['Marketing', 2], 
                     ['Production', 4], 
                     ['Quality Management', 4], 
                     ['Research', 2], 
                     ['Sales', 2], 
                     ['Total', 24]]],
                    [[['Finance', '$70,815.89'], #5
                     ['Marketing', '$88,371.69'], 
                     ['Research', '$77,535.18'], 
                     ['Sales', '$85,738.76']],
                    [['Finance', '$ 70,815.89'], #5
                     ['Marketing', '$ 88,371.69'], 
                     ['Research', '$ 77,535.18'], 
                     ['Sales', '$ 85,738.76']],
                     [['Marketing', '$88,371.69'], 
                      ['Finance', '$70,815.89'], 
                      ['Sales', '$85,738.76'], 
                      ['Research', '$77,535.18']]],
                    [['Research', 'Arie', 'Staelin'], #6
                     ['Research', 'Hilary', 'Kambil']]]


alias_counter = 0
total_aliases = 5
total_queries = 6

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
        # print(sqlCommands)
        # filter out SELECT @ and SELECT @@ commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('select @') and not command.lower().startswith('select @@')]

        #filter out SET commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('set')]
    
        final_student_answers = []
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
            
            # print(f"{a_number}. {command}")
            if a_number == 1 and not command.lower().__contains__('use'):
                answer.write(f"USE bike; Statement NOT FOUND\n")


            if a_number == 2: # Query 1
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                    if not command.lower().__contains__(' as '):
                        query6_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query1_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('count'):
                        query1_function_list.append(f"COUNT Function NOT used")

            if a_number == 3: # Query 2
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                    if not command.lower().__contains__(' as '):
                        query6_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query2_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('count'):
                        query2_function_list.append(f"COUNT Function NOT used")
                    if not command.lower().__contains__('join'):
                        query2_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query2_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('group by'):
                        query2_clause_list.append(f"GROUP BY Clause NOT used")

            if a_number == 4: # Query 3
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                    if not command.lower().__contains__(' as '):
                        query6_clause_list.append(f"Alias NOT used")
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
                
            if a_number == 6: # Query 4
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                    if not command.lower().__contains__(' as '):
                        query6_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query4_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('count'):
                        query4_function_list.append(f"COUNT Function NOT used")
                    if not command.lower().__contains__('join'):
                        query4_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('with rollup'):
                        query4_clause_list.append(f"WITH ROLLUP Clause NOT used")
                    if not command.lower().__contains__('group by'):
                        query4_clause_list.append(f"GROUP BY Clause NOT used")
            if a_number == 7: # Query 5
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                    if not command.lower().__contains__(' as '):
                        query6_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query5_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('avg'):
                        query5_function_list.append(f"AVG Function NOT used")
                    if not command.lower().__contains__('format'):
                        query5_function_list.append(f"FORMAT Function NOT used")
                    if not command.lower().__contains__('concat'):
                        query5_function_list.append(f"CONCAT Function NOT used")
                    if not command.lower().__contains__('join'):
                        query5_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('group by'):
                        query5_clause_list.append(f"GROUP BY Clause NOT used")
                    if not command.lower().__contains__('having'):
                        query5_clause_list.append(f"HAVING Clause NOT used")
            if a_number == 8: # Query 6
                if command.lower().__contains__('select'):
                    
                    if not command.lower().__contains__('from'):
                        query6_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query6_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query6_clause_list.append(f"WHERE Clause NOT used")
                    
                    

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
            new_query5c_list = format_list(query5_clause_list)
            new_query5f_list = format_list(query5_function_list)
            new_query6c_list = format_list(query6_clause_list)

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
                        

            
            output_list = [list(row) for row in output if row is not None]
            # print(f"[{command}]")

            # change all decimal values to strings
            for row in output_list:
                for i in range(len(row)):
                    if type(row[i]) == decimal.Decimal:
                        row[i] = str(row[i])
            
            # filter out empty commands
            # only output the result if information is returned
            if len(output_list) > 0:
                student_answers = [list(row) for row in output_list if row is not None]
                final_student_answers.append(student_answers)

                # Compare the student answers to the correct answers
                if (student_answers in correct_answer_list or student_answers in correct_answer_list[number]) or not command.lower().__contains__(' as ') or not command.lower().__contains__(') as '):
                    number += 1
                    # answer.write(f"Command: {command}\n")
                    # answer.write(f"Student Answer: {student_answers}\n")
                
                else:
                    number += 1

                    answer.write("---------------------\n")
                    answer.write(f"{number}. Incorrect!\n")
                    
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
                    elif a_number == 6:
                        # print(new_query4_list)
                        if len(new_query4c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query4c_list}\n")
                    elif a_number == 7:
                        # print(new_query5_list)
                        if len(new_query5c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query5c_list}\n")
                    elif a_number == 8:
                        # print(new_query6_list)
                        if len(new_query6c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query6c_list}\n")

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
                    if a_number == 6:
                        # print(new_query4_list)
                        if len(new_query4f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query4f_list}\n")
                    if a_number == 7:
                        # print(new_query5_list)
                        if len(new_query5f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query5f_list}\n")
                    elif a_number == 8:
                        # print(new_query6_list)
                        answer.write(f"No functions Needed\n")
                    answer.write("-----ANSWERS-----\n")
                    
                    answer.write(f"Student Answer: {student_answers}\n")
                    answer.write(f"Correct Answer: {correct_answer_list[number-1]}\n")
                    answer.write("---------------------\n")

        answer.write(f"{alias_counter}/{total_aliases} Aliases Used\n")
        answer.write(f"{number}/{total_queries} Queries Written\n")

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
