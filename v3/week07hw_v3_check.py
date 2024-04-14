import mysql.connector
import decimal
import os
import platform
import regex as re


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


correct_answer_list = [[[1]],
                       [[['Venture', 'Lonzo', 'Coy', 1965, None, 'United States', 'y'], #2
                         ['Leonardo', None, 'da Vinci', 1452, 1519, 'Italy', 'n'], 
                         ['Deborah', None, 'Gill', 1970, None, 'United States', 'y'], 
                         ['Claude', None, 'Monet', 1840, 1926, 'France', 'n'], 
                         ['Pablo', None, 'Picasso', 1904, 1973, 'Spain', 'n'], 
                         ['Michelangelo', 'di Lodovico', 'Simoni', 1475, 1564, 'Italy', 'n'], 
                         ['Vincent', None, 'van Gogh', 1853, 1890, 'France', 'n'], 
                         ['Rembrandt', 'Harmenszoon', 'van Rijn', 1606, 1669, 'Netherlands', 'n'], 
                         ['George', None, 'Washington', 1732, 1798, 'United States', 'y']],
                        [['Venture', 'Lonzo', 'Coy', 1965, None, 'United States', 'y'], 
                         ['Leonardo', None, 'da Vinci', 1452, 1519, 'Italy', 'n'], 
                         ['Deborah', None, 'Gill', 1970, None, 'United States', 'y'], 
                         ['Claude', None, 'Monet', 1840, 1926, 'France', 'n'], 
                         ['Pablo', None, 'Picasso', 1904, 1973, 'Spain', 'n'], 
                         ['Michelangelo', 'di Lodovico', 'Simoni', 1475, 1564, 'Italy', 'n'], 
                         ['Vincent', None, 'van Gogh', 1853, 1890, 'France', 'n'], 
                         ['Rembrandt', 'Harmenszoon', 'van Rijn', 1606, 1669, 'Netherlands', 'n'], 
                         ['george', None, 'washington', 1732, 1798, 'united states', 'y']]],
                       [[3]],
                       [[4]],
                       [['Ollie', 'Zimmerman', '(657) 648-2863'], 
                        ['Jone', 'Bernard', '(657) 536-5165'], 
                        ['Joaquin', 'Hawkins', '(657) 557-1746'], 
                        ['Tony', 'Hicks', '(657) 260-6783'], 
                        ['Ana', 'Palmer', '(657) 323-8684'], 
                        ['Kiara', 'Deleon', '(657) 378-8011'], 
                        ['Twana', 'Arnold', '(657) 988-1904'], 
                        ['Stephen', 'Vega', '(657) 288-3778'], 
                        ['Raeann', 'Duncan', '(657) 256-2008'], 
                        ['Delma', 'Bailey', '(657) 454-8493'], 
                        ['Penni', 'Best', '(657) 611-2991']],
                        [['Trek Domane SLR 9 Disc - 2018', '11999.99', '11899.99'], 
                         ['Trek Domane SLR 8 Disc - 2018', '7499.99', '7399.99']],
                        [['Kali', 'Vargas', '(972) 530-5555'], 
                         ['Layla', 'Terrell', '(972) 530-5556'], 
                         ['Bernardine', 'Houston', '(972) 530-5557']],
                        [['Trek Crockett 5 Disc - 2018', 2018, '1799.99'], 
                         ['Trek Crockett 7 Disc - 2018', 2018, '2999.99']],
                        [["Sun Bicycles Lil Kitt'n - 2017", '109.99'], 
                         ["Trek Boy's Kickster - 2015/2017", '149.99'], 
                         ["Trek Girl's Kickster - 2017", '149.99'], 
                         ['Trek Kickster - 2018', '159.99'], 
                         ['Trek Precaliber 12 Boys - 2017', '189.99'], 
                         ['Trek Precaliber 12 Girls - 2017', '189.99'], 
                         ["Trek Precaliber 12 Girl's - 2018", '199.99'], 
                         ["Trek Precaliber 12 Boy's - 2018", '199.99'], 
                         ['Trek Precaliber 16 Boys - 2017', '209.99'], 
                         ['Trek Precaliber 16 Girls - 2017', '209.99'], 
                         ['Haro Shredder 20 - 2017', '209.99'], 
                         ['Haro Shredder 20 Girls - 2017', '209.99'], 
                         ["Trek Precaliber 16 Boy's - 2018", '209.99'], 
                         ["Trek Precaliber 16 Girl's - 2018", '209.99'], 
                         ["Trek Precaliber 20 Boy's - 2018", '229.99'], 
                         ["Trek Precaliber 20 Girl's - 2018", '229.99'], 
                         ['Haro Shredder Pro 20 - 2017', '249.99'], 
                         ['Trek MT 201 - 2018', '249.99'], 
                         ['Strider Sport 16 - 2018', '249.99']],
                        [['Mozelle', 'Carter', '(281) 489-9656', '895 Chestnut Ave. ', 'Houston', 'TX', '77016'], 
                         ['Lolita', 'Mosley', '(281) 363-3309', '376 S. High Ridge St. ', 'Houston', 'TX', '77016'], 
                         ['Neil', 'Mccall', None, '7476 Oakland Dr. ', 'San Carlos', 'CA', '94070'], 
                         ['Dorthey', 'Jackson', '(281) 926-8010', '9768 Brookside St. ', 'Houston', 'TX', '77016'], 
                         ['Minerva', 'Decker', '(281) 271-6390', '794 Greenrose Street ', 'Houston', 'TX', '77016']]
                        ]


alias_counter = 0
total_aliases = 1
total_queries = 10

# open the test folder and read the files inside
os_name = platform.system()
if os_name == 'Windows':
    print("Windows OS Detected")
    directory = os.getcwd() + '\\v3'
    print(directory)
    grading_directory = os.getcwd() + '\\v3\\tempgrades'
    print(grading_directory)
    answer = open(f"{directory}\\week07answers.txt", "w")

elif os_name == 'Linux' or os_name == 'Darwin':
    print("Linux/MacOS Detected")
    directory = os.getcwd() + '/v3'
    grading_directory = os.getcwd() + '/v3/tempgrades'
    answer = open(f"{directory}/week07answers.txt", "w")
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
            file_contents = file_contents.replace("INSERT", "-- ~\nINSERT")
            file_contents = file_contents.replace("UPDATE", "-- ~\nUPDATE")
            file_contents = file_contents.replace("DELETE", "-- ~\nDELETE")
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
        sqlCommands = [command for command in sqlCommands if (not command.lower().startswith('select *') and command.lower().startswith('select')) or command.lower().startswith('use') or command.lower().startswith('insert') or command.lower().startswith('update') or command.lower().startswith('delete')]
        use_bike_count = 0
        use_v_art_count = 0
        for command in sqlCommands:
            if command.lower().startswith('use v_art'):
                use_v_art_count += 1
            if command.lower().startswith('use bike'):
                use_bike_count += 1
        if use_bike_count > 1:
            answer.write(f"USE v_art; command used {use_bike_count} times. Only use it once\n")
            answer.write("Skipping to the next file...\n")
            answer.write("***********************************\n\n")
            continue
        if use_v_art_count > 1:
            answer.write(f"USE magazine; command used {use_v_art_count} times. Only use it once\n")
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
        query6_alias_counter = 0
        like_counter = 0
        
        query1_clause_list = []
        query2_clause_list = []
        query3_clause_list = []
        query4_clause_list = []
        query5_clause_list = []
        query6_clause_list = []
        query7_clause_list = []
        query8_clause_list = []
        query9_clause_list = []
        query10_clause_list = []
    
        
        for command in sqlCommands:
            a_number += 1
            
            # debug.write(f"Query {a_number}. {command}\n")            
            if a_number == 1 and not command.lower().__contains__('use'):
                answer.write(f"USE v_art; Statement NOT FOUND\n")


            if a_number == 2: # Query 1
                if command.lower().__contains__('insert'):
                    
                    if not command.lower().__contains__('artist_id'):
                        query1_clause_list.append(f"artist_id column NOT used")

            if a_number == 3: # Query 2
                if command.lower().__contains__('select'):
                    if not re.search(r'(select).*fname.*\,.*mname.*\,.*lname.*\,.*dob.*\,.*dod.*\,.*country.*\,.*local', command, re.I | re.S):
                        query2_clause_list.append(f"Invalid SELECT Statement.")
                    if not re.search(r'^.*from.*artist',command, re.I | re.S):
                        query2_clause_list.append(f"FROM Clause NOT used")
                    if command.lower().__contains__('*'):
                        query2_clause_list.append(f"SELECT * used. Use column names instead")
                    if not command.lower().__contains__('order by'):
                        query2_clause_list.append(f"ORDER BY Clause NOT used")
                    
                    

            if a_number == 4: # Query 3
                if command.lower().__contains__('update'):
                    if not command.lower().__contains__('set'):
                        query3_clause_list.append(f"SET Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query3_clause_list.append(f"WHERE Clause NOT used. All rows will be updated")
                    if not command.lower().__contains__('artist_id'):
                        query3_clause_list.append(f"artist_id column NOT used in WHERE Clause")
                    
            if a_number == 5: # Query 4
                if command.lower().__contains__('delete'):
                    if not command.lower().__contains__('where'):
                        query4_clause_list.append(f"WHERE Clause NOT used. All rows will be deleted")
                    if not command.lower().__contains__('artist_id'):
                        query4_clause_list.append(f"artist_id column NOT used in WHERE Clause")
            
            if a_number == 6 and not command.lower().__contains__('use'):
                if not command.lower().__contains__('use'):
                    answer.write(f"USE bike; Statement NOT FOUND\n")

            if a_number == 7: # Query 5
                if command.lower().__contains__('select'):
                    if not command.lower().__contains__('from'):
                        query5_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query5_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('city ='):
                        query5_clause_list.append(f"Wrong filter used. Use city = 'Anaheim'")

                    
            if a_number == 8: # Query 6
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        for word in command.split():
                            if word.lower() == 'as':
                                alias_counter += 1
                                query6_alias_counter += 1
                    if query6_alias_counter < 3:
                        query5_clause_list.append(f"1 Alias needed. {1 - query6_alias_counter} missing")
                    if not command.lower().__contains__(' as '):
                        query5_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query5_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query5_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query5_clause_list.append(f"ORDER BY Clause NOT used")

            if a_number == 9: # Query 7
                if command.lower().__contains__('select'):
                    if not command.lower().__contains__('from'):
                        query7_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query7_clause_list.append(f"WHERE Clause NOT used")

            if a_number == 10: # Query 8
                if command.lower().__contains__('select'):
                    if not command.lower().__contains__('from'):
                        query8_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query8_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('like'):
                        query8_clause_list.append(f"LIKE Operator NOT used")

            if a_number == 11: # Query 9
                if command.lower().__contains__('select'):
                    if not command.lower().__contains__('from'):
                        query9_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query9_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query9_clause_list.append(f"ORDER BY Clause NOT used")

            if a_number == 12: # Query 10
                if command.lower().__contains__('select'):
                    if not command.lower().__contains__('from'):
                        query10_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query10_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('limit'):
                        query10_clause_list.append(f"LIMIT Clause NOT used")
                    if not command.lower().__contains__('phone is not null'):
                        query10_clause_list.append(f"IS NOT NULL Operator NOT used")
                    if command.lower().__contains__('city like'):
                        for word in command.split():
                            if word.lower() == 'like':
                                like_counter += 1
                        if like_counter < 2:
                            query10_clause_list.append(f"2 LIKE Operators needed. {2 - like_counter} missing")
                        

            

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
            new_query8c_list = format_list(query8_clause_list)
            new_query9c_list = format_list(query9_clause_list)
            new_query10c_list = format_list(query10_clause_list)
            
            output = ''

            try:
                mycursor.execute(command)
                if a_number in(1,2,4,5,6):
                    mydb.commit()
            except mysql.connector.Error as e:
                # number the queries run and print the error
                answer.write("Error found. Skipping to the next file...\n")
                answer.write("-------ERROR DETAILS-------\n")
                answer.write(f"Query {number + 1}. Error: {e}\n")
                
                answer.write("------QUERY------\n")
                answer.write(f"{command}\n")
                answer.write("---------------------\n")
                
                break
            if a_number not in(1,2,4,5,6):
                output = mycursor.fetchall()
            

            # if the output is empty, no error was found and 
            # the command was an insert, update, or delete statement
            # print that the command was successful
            if len(output) == 0 and (command.lower().__contains__('insert')):
                answer.write(f"Query {number + 1}. INSERT Successful\n")
                number += 1
                correct_answer_count += 1
                continue
            if len(output) == 0 and (command.lower().__contains__('update')):
                answer.write(f"Query {number + 1}. UPDATE Successful\n")
                number += 1
                correct_answer_count += 1
                continue
            if len(output) == 0 and (command.lower().__contains__('delete')):
                answer.write(f"Query {number + 1}. DELETE Successful\n")
                number += 1
                correct_answer_count += 1
                continue
            
            # if the output is empty and the command is a select statement
            # print that no results were returned
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

                    elif a_number == 8:
                        # debug.write(new_query6_list)
                        if len(new_query6c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query6c_list}\n")

                    elif a_number == 9:
                        # debug.write(new_query7_list)
                        if len(new_query7c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query7c_list}\n")

                    elif a_number == 10:
                        # debug.write(new_query8_list)
                        if len(new_query8c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query8c_list}\n")

                    elif a_number == 11:
                        # debug.write(new_query9_list)
                        if len(new_query9c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query9c_list}\n")

                    elif a_number == 12:
                        # debug.write(new_query10_list)
                        if len(new_query10c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query10c_list}\n")
                   
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
            os.remove(f"{directory}\\week07answers.txt")
        elif os_name == 'Linux' or os_name == 'Darwin':
            os.remove(f"{directory}/week07answers.txt")
        print("Files Deleted")
    else:
        f.close()
        print("Files Kept")

