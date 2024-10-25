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
try:
    import regex as re
except ImportError or ModuleNotFoundError:
    print("REGEX module not found. Installing...")
    if os_name == 'Windows':
        os.system("pip install regex")
    elif os_name == 'Linux' or os_name == 'Darwin':
        os.system("pip3 install regex")
    import regex as re
    print("REGEX module installed") 


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
                       [['Venture', 'Lonzo', 'Coy', 1965, None, 'United States', 'y'], # 2
                        ['Leonardo', None, 'da Vinci', 1452, 1519, 'Italy', 'n'], 
                        ['Deborah', None, 'Gill', 1970, None, 'United States', 'y'], 
                        ['Gustav', None, 'Klimt', 1862, 1917, 'Italy', 'n'], 
                        ['Claude', None, 'Monet', 1840, 1926, 'France', 'n'], 
                        ['Pablo', None, 'Picasso', 1904, 1973, 'Spain', 'n'], 
                        ['Michelangelo', 'di Lodovico', 'Simoni', 1475, 1564, 'Italy', 'n'], 
                        ['Vincent', None, 'van Gogh', 1853, 1890, 'France', 'n'], 
                        ['Rembrandt', 'Harmenszoon', 'van Rijn', 1606, 1669, 'Netherlands', 'n']],
                       [[3]],
                       [[4]],
                       [['Latasha', 'Hays', '(716) 986-3359'], # 5
                        ['Sarai', 'Mckee', '(716) 912-8110'], 
                        ['Rubin', 'Decker', '(716) 950-9835'], 
                        ['Evelina', 'Byrd', '(716) 601-7704'], 
                        ['Agnes', 'Sims', '(716) 780-9901'], 
                        ['Lore', 'Sykes', '(716) 382-5169'], 
                        ['Anton', 'Barton', '(716) 472-3707'], 
                        ['Chantell', 'Bridges', '(716) 941-6072'], 
                        ['Lamar', 'Bush', '(716) 294-7174']],
                       [['Trek Domane SLR 9 Disc - 2018', '11999.99', '11399.99'], # 6
                        ['Trek Domane SLR 8 Disc - 2018', '7499.99', '6899.99'], 
                        ["Trek Silque SLR 8 Women's - 2017", '6499.99', '5899.99'], 
                        ['Trek Domane SL Frameset - 2018', '6499.99', '5899.99'], 
                        ["Trek Domane SL Frameset Women's - 2018", '6499.99', '5899.99'], 
                        ['Trek Emonda SLR 8 - 2018', '6499.99', '5899.99']],
                       [['Jannette', 'David', 'jannette.david@bikes.shop'], # 7
                        ['Marcelene', 'Boyer', 'marcelene.boyer@bikes.shop'], 
                        ['Venita', 'Daniel', 'venita.daniel@bikes.shop']],
                       [['Trek CrossRip 1 - 2018', 2018, '959.99'], # 8
                        ['Trek CrossRip 2 - 2018', 2018, '1299.99'], 
                        ['Trek CrossRip+ - 2018', 2018, '4499.99']],
                       [['Sun Bicycles Biscayne Tandem 7 - 2017', '619.99'], # 9
                        ['Electra Moto 3i - 2018', '639.99'], 
                        ['Electra Cruiser Lux Fat Tire 7D - 2018', '639.99'], 
                        ["Electra Townie Original 3i EQ Ladies' - 2018", '639.99'], 
                        ['Sun Bicycles Biscayne Tandem CB - 2017', '647.99'], 
                        ['Electra Amsterdam Original 3i - 2015/2017', '659.99'], 
                        ["Electra Amsterdam Original 3i Ladies' - 2017", '659.99'], 
                        ['Electra Townie Original 3i EQ - 2017/2018', '659.99'], 
                        ['Electra Townie Original 21D EQ - 2017/2018', '679.99'], 
                        ["Electra Townie Original 21D EQ Ladies' - 2018", '679.99'], 
                        ['Electra Townie Original 21D EQ - 2017/2018', '679.99'], 
                        ["Electra Townie Original 21D EQ Ladies' - 2018", '679.99'], 
                        ["Electra Townie Commute 8D Ladies' - 2018", '699.99'], 
                        ["Electra Townie Commute 8D Ladies' - 2018", '699.99'], 
                        ['Ritchey Timberwolf Frameset - 2016', '749.99'], 
                        ['Surly Ogre Frameset - 2017', '749.99'], 
                        ['Sun Bicycles Brickell Tandem 7 - 2017', '749.99'], 
                        ['Trek Marlin 7 - 2017/2018', '749.99'], 
                        ["Trek Domane AL 2 Women's - 2018", '749.99'], 
                        ['Surly ECR Frameset - 2018', '749.99'], 
                        ['Trek Domane AL 2 - 2018', '749.99'], 
                        ['Electra Queen of Hearts 3i - 2018', '749.99'], 
                        ["Electra Morningstar 3i Ladies' - 2018", '749.99'], 
                        ['Electra Townie Balloon 8D EQ - 2016/2017/2018', '749.99'], 
                        ["Electra Townie Balloon 8D EQ Ladies' - 2016/2017/2018", '749.99'],
                        ['Electra Townie Commute 8D - 2018', '749.99'], 
                        ['Electra White Water 3i - 2018', '749.99'], 
                        ['Electra Townie Balloon 3i EQ - 2017/2018', '749.99'], 
                        ['Electra Townie Balloon 3i EQ - 2017/2018', '749.99'], 
                        ['Electra Townie Balloon 8D EQ - 2016/2017/2018', '749.99'], 
                        ["Electra Townie Balloon 8D EQ Ladies' - 2016/2017/2018", '749.99'], 
                        ['Electra Townie Commute 8D - 2018', '749.99']],
                       [['Williemae', 'Holloway', '(510) 246-8375', '69 Cypress St. ', 'Oakland', 'CA', '94603'], # 10
                        ['Janetta', 'Aguirre', '(717) 670-2634', '214 Second Court ', 'Lancaster', 'NY', '14086'], 
                        ['Bennett', 'Armstrong', None, '688 Walnut Street ', 'Bethpage', 'NY', '11714'], 
                        ['Marni', 'Bolton', '(717) 670-6268', '7469 Plymouth Ave. ', 'Lancaster', 'NY', '14086'], 
                        ['Trisha', 'Johnson', '(717) 126-8787', '59 Wild Horse St. ', 'Lancaster', 'NY', '14086']]
                      ]

alias_counter = 0
total_aliases = 1
total_queries = 10

# open the test folder and read the files inside
if os_name == 'Windows':
    print("Windows OS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '\\tempgrades'
    answer = open(f"{directory}\\week07answers.txt", "w")

elif os_name == 'Linux':
    print("Linux Detected")
    directory = '/home/student/Desktop/itm111grading/v2'
    grading_directory = '/home/student/Desktop/itm111grading/v2/tempgrades'
    answer = open(f"{directory}/week07answers.txt", "w")

elif os_name == 'Darwin':
    print("MacOS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '/tempgrades'
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
                        query2_clause_list.append(f"Invalid SELECT Statement. 7 Column names should exist.")
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

