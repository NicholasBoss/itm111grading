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
import datetime


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


correct_answer_list = [[[['Lillie', 'Summers', 'November 05, 1999'], # 1
                         ['Josh', 'Rollins', 'November 28, 1998']],
                        [['Lillie', 'Summers', 'November 05 1999'], 
                         ['Josh', 'Rollins', 'November 28 1998']],
                        [['Lillie', 'Summers', 'November 5, 1999'], 
                         ['Josh', 'Rollins', 'November 28, 1998']],
                        [['Summers', 'Lillie', 'November 5, 1999'], 
                         ['Rollins', 'Josh', 'November 28, 1998']],
                        [['Summers', 'Lillie', 'November 05, 1999'], 
                         ['Rollins', 'Josh', 'November 28, 1998']]],
                       [[['Woodward', 'Erick', '1998-08-05', 25, 43, '25 - Yrs, 43 - Days'], # 2
                         ['Rollins', 'Josh', '1998-11-28', 24, 293, '24 - Yrs, 293 - Days'], 
                         ['Summers', 'Lillie', '1999-11-05', 23, 316, '23 - Yrs, 316 - Days'], 
                         ['Spence', 'Marshall', '2000-06-23', 23, 85, '23 - Yrs, 85 - Days'], 
                         ['Marquez', 'Nellie', '2001-06-25', 22, 83, '22 - Yrs, 83 - Days'], 
                         ['Clark', 'Maria', '2002-01-25', 21, 234, '21 - Yrs, 234 - Days'], 
                         ['Woodward', 'Tracy', '2002-10-04', 20, 347, '20 - Yrs, 347 - Days'], 
                         ['Shah', 'Kerri', '2003-04-05', 20, 164, '20 - Yrs, 164 - Days'], 
                         ['Meyers', 'Isabel', '2004-06-23', 19, 84, '19 - Yrs, 84 - Days'], 
                         ['Stokes', 'Allen', '2004-09-16', 18, 364, '18 - Yrs, 364 - Days']],
                        [['Woodward', 'Erick', '1998-08-05', 25, 43, '25-yrs 43-days '], 
                         ['Rollins', 'Josh', '1998-11-28', 24, 293, '24-yrs 293-days '], 
                         ['Spence', 'Marshall', '2000-06-23', 23, 85, '23-yrs 85-days '], 
                         ['Summers', 'Lillie', '1999-11-05', 23, 316, '23-yrs 316-days '],
                         ['Marquez', 'Nellie', '2001-06-25', 22, 83, '22-yrs 83-days '], 
                         ['Clark', 'Maria', '2002-01-25', 21, 234, '21-yrs 234-days '], 
                         ['Woodward', 'Tracy', '2002-10-04', 20, 347, '20-yrs 347-days '], 
                         ['Meyers', 'Isabel', '2003-05-15', 20, 124, '20-yrs 124-days '], 
                         ['Shah', 'Kerri', '2003-04-05', 20, 164, '20-yrs 164-days '], 
                         ['Stokes', 'Allen', '2004-09-16', 18, 364, '18-yrs 364-days ']],
                        [['Woodward', 'Erick', '1998-08-05', 25, 43, '25 - Yrs, 43 - Days'], 
                         ['Rollins', 'Josh', '1998-11-28', 24, 293, '24 - Yrs, 293 - Days'], 
                         ['Summers', 'Lillie', '1999-11-05', 23, 316, '23 - Yrs, 316 - Days'], 
                         ['Spence', 'Marshall', '2000-06-23', 23, 85, '23 - Yrs, 85 - Days'], 
                         ['Marquez', 'Nellie', '2001-06-25', 22, 83, '22 - Yrs, 83 - Days'], 
                         ['Clark', 'Maria', '2002-01-25', 21, 234, '21 - Yrs, 234 - Days'], 
                         ['Woodward', 'Tracy', '2002-10-04', 20, 347, '20 - Yrs, 347 - Days'], 
                         ['Shaw', 'Kerri', '2003-04-05', 20, 164, '20 - Yrs, 164 - Days'], 
                         ['Meyers', 'Isabel', '2003-05-15', 20, 124, '20 - Yrs, 124 - Days'], 
                         ['Stokes', 'Allen', '2004-09-16', 18, 364, '18 - Yrs, 364 - Days']],
                        [['Woodward', 'Erick', '1998-08-05', 25, 43, '25 -Yrs 43 -Days'], 
                         ['Rollins', 'Josh', '1998-11-28', 24, 293, '24 -Yrs 293 -Days'], 
                         ['Summers', 'Lillie', '1999-11-05', 23, 316, '23 -Yrs 316 -Days'], 
                         ['Spence', 'Marshall', '2000-06-23', 23, 85, '23 -Yrs 85 -Days'], 
                         ['Marquez', 'Nellie', '2001-06-25', 22, 83, '22 -Yrs 83 -Days'], 
                         ['Clark', 'Maria', '2002-01-25', 21, 234, '21 -Yrs 234 -Days'], 
                         ['Woodward', 'Tracy', '2002-10-04', 20, 347, '20 -Yrs 347 -Days'], 
                         ['Shah', 'Kerri', '2003-04-05', 20, 164, '20 -Yrs 164 -Days'], 
                         ['Meyers', 'Isabel', '2003-05-15', 20, 124, '20 -Yrs 124 -Days'], 
                         ['Stokes', 'Allen', '2004-09-16', 18, 364, '18 -Yrs 364 -Days']],
                        [['Erick', 'Woodward', '1998-08-05', '25', 43, '25 - Yrs, 43 - Days'], 
                         ['Josh', 'Rollins', '1998-11-28', '25', 293, '25 - Yrs, 293 - Days'], 
                         ['Lillie', 'Summers', '1999-11-05', '24', 316, '24 - Yrs, 316 - Days'], 
                         ['Marshall', 'Spence', '2000-06-23', '23', 85, '23 - Yrs, 85 - Days'], 
                         ['Nellie', 'Marquez', '2001-06-25', '22', 83, '22 - Yrs, 83 - Days'], 
                         ['Maria', 'Clark', '2002-01-25', '22', 234, '22 - Yrs, 234 - Days'], 
                         ['Tracy', 'Woodward', '2002-10-04', '21', 347, '21 - Yrs, 347 - Days'], 
                         ['Kerri', 'Shah', '2003-04-05', '20', 164, '20 - Yrs, 164 - Days'], 
                         ['Isabel', 'Meyers', '2003-05-15', '20', 124, '20 - Yrs, 124 - Days'], 
                         ['Allen', 'Stokes', '2004-09-16', '19', 364, '19 - Yrs, 364 - Days']],
                        [['Woodward', 'Erick', '1998-08-05', 25, 43, '25 - yrs, 43 - days'], 
                         ['Rollins', 'Josh', '1998-11-28', 24, 293, '24 - yrs, 293 - days'], 
                         ['Summers', 'Lillie', '1999-11-05', 23, 316, '23 - yrs, 316 - days'], 
                         ['Spence', 'Marshall', '2000-06-23', 23, 85, '23 - yrs, 85 - days'], 
                         ['Marquez', 'Nellie', '2001-06-25', 22, 83, '22 - yrs, 83 - days'], 
                         ['Clark', 'Maria', '2002-01-25', 21, 234, '21 - yrs, 234 - days'], 
                         ['Woodward', 'Tracy', '2002-10-04', 20, 347, '20 - yrs, 347 - days'], 
                         ['Shah', 'Kerri', '2003-04-05', 20, 164, '20 - yrs, 164 - days'], 
                         ['Meyers', 'Isabel', '2003-05-15', 20, 124, '20 - yrs, 124 - days'], 
                         ['Stokes', 'Allen', '2004-09-16', 18, 364, '18 - yrs, 364 - days']],
                        [['Woodward', 'Erick', '1998-08-05', 25, 43, '25-Yrs, 43-Days'], 
                         ['Rollins', 'Josh', '1998-11-28', 24, 293, '24-Yrs, 293-Days'], 
                         ['Summers', 'Lillie', '1999-11-05', 23, 316, '23-Yrs, 316-Days'], 
                         ['Spence', 'Marshall', '2000-06-23', 23, 85, '23-Yrs, 85-Days'], 
                         ['Marquez', 'Nellie', '2001-06-25', 22, 83, '22-Yrs, 83-Days'], 
                         ['Clark', 'Maria', '2002-01-25', 21, 234, '21-Yrs, 234-Days'], 
                         ['Woodward', 'Tracy', '2002-10-04', 20, 347, '20-Yrs, 347-Days'], 
                         ['Shah', 'Kerri', '2003-04-05', 20, 164, '20-Yrs, 164-Days'], 
                         ['Meyers', 'Isabel', '2003-05-15', 20, 124, '20-Yrs, 124-Days'], 
                         ['Stokes', 'Allen', '2004-09-16', 18, 364, '18-Yrs, 364-Days']],
                        [['Woodward', 'Erick', '1998-08-05', 25, 43, '25 - Yrs, 43 - Days'], 
                         ['Rollins', 'Josh', '1998-11-28', 24, 293, '24 - Yrs, 293 - Days'], 
                         ['Summers', 'Lillie', '1999-11-05', 23, 316, '23 - Yrs, 316 - Days'], 
                         ['Spence', 'Marshall', '2000-06-23', 23, 85, '23 - Yrs, 85 - Days'], 
                         ['Marquez', 'Nellie', '2001-06-25', 22, 83, '22 - Yrs, 83 - Days'], 
                         ['Clark', 'Maria', '2002-01-25', 21, 234, '21 - Yrs, 234 - Days'], 
                         ['Woodward', 'Tracy', '2002-10-04', 20, 347, '20 - Yrs, 347 - Days'], 
                         ['Shah', 'Kerri', '2003-04-05', 20, 164, '20 - Yrs, 164 - Days'], 
                         ['Meyers', 'Isabel', '2003-05-15', 20, 124, '20 - Yrs, 124 - Days'], 
                         ['Stokes', 'Allen', '2004-09-16', 18, 364, '18 - Yrs, 364 - Days']],
                        [['Erick', 'Woodward', '1998-08-05', 25, 43, '25 - Yrs, 43 - Days'], 
                         ['Josh', 'Rollins', '1998-11-28', 24, 293, '24 - Yrs, 293 - Days'], 
                         ['Marshall', 'Spence', '2000-06-23', 23, 85, '23 - Yrs, 85 - Days'], 
                         ['Lillie', 'Summers', '1999-11-05', 23, 316, '23 - Yrs, 316 - Days'], 
                         ['Nellie', 'Marquez', '2001-06-25', 22, 83, '22 - Yrs, 83 - Days'], 
                         ['Maria', 'Clark', '2002-01-25', 21, 234, '21 - Yrs, 234 - Days'], 
                         ['Tracy', 'Woodward', '2002-10-04', 20, 347, '20 - Yrs, 347 - Days'], 
                         ['Isabel', 'Meyers', '2003-05-15', 20, 124, '20 - Yrs, 124 - Days'], 
                         ['Kerri', 'Shah', '2003-04-05', 20, 164, '20 - Yrs, 164 - Days'], 
                         ['Allen', 'Stokes', '2004-09-16', 18, 364, '18 - Yrs, 364 - Days']]],
                       [[['Marshall', 'Spence', 'Student'], # 3
                         ['Nellie', 'Marquez', 'Student'], 
                         ['Allen', 'Stokes', 'Student'], 
                         ['Kerri', 'Shah', 'Student'], 
                         ['Brady', 'Meyer', 'Teacher'], 
                         ['Bryan', 'Drew', 'Teacher']],
                        [['Marshall', 'Spence', 'Student'], 
                         ['Allen', 'Stokes', 'Student'], 
                         ['Kerri', 'Shah', 'Student'], 
                         ['Nellie', 'Marquez', 'Student'], 
                         ['Brady', 'Meyer', 'Teacher'], 
                         ['Bryan', 'Drew', 'Teacher']],
                        [['Marshall', 'Spence', 'Student'], 
                         ['Allen', 'Stokes', 'Student'], 
                         ['Kerri', 'Shaw', 'Student'], 
                         ['Nellie', 'Marquez', 'Student'], 
                         ['Brady', 'Meyer', 'Teacher'], 
                         ['Bryan', 'Drew', 'Teacher']],
                        [['Marshall', 'Spence', 'student'], 
                         ['Allen', 'Stokes', 'student'], 
                         ['Kerri', 'Shah', 'student'], 
                         ['Nellie', 'Marquez', 'student'], 
                         ['Brady', 'Meyer', 'teacher'], 
                         ['Bryan', 'Drew', 'teacher']]],
                       [[['Lillie', 'Summers', 'TA', 'Musicianship 4'], # 4
                         ['Allen', 'Stokes', 'TA', 'Web Frontend Development I']],
                        [['Allen', 'Stokes', 'TA', 'Web Frontend Development I'], 
                         ['Lillie', 'Summers', 'TA', 'Musicianship 4']],
                        [['Lillie', 'Summers', 'TA', 'Musicianship 4'], 
                         ['Allen', 'Stokes', 'TA', 'Web Frontend Development 1']]],
                       [[['Allen', 'Stokes', 'Winter'], # 5
                         ['Erick', 'Woodward', 'Fall']],
                        [['Stokes', 'Allen', 'Winter'], 
                         ['Woodward', 'Erick', 'Fall']],
                        [['Allen', 'Stokes', 'Musicianship 4', 'Winter'], 
                         ['Erick', 'Woodward', 'Musicianship 4', 'Fall']],
                        [['Erick', 'Woodward', 'Musicianship 4'], 
                         ['Allen', 'Stokes', 'Musicianship 4']],
                        [['Erick', 'Woodward', 'Fall'], 
                         ['Allen', 'Stokes', 'Winter']],
                        [['Allen', 'Stokes', 'Student', 'Winter'], 
                         ['Erick', 'Woodward', 'Student', 'Fall']]],
                       [[['CSE', 251, 'Parallelism and Concurrency', 1, 'Fall'], # 6
                         ['CSE', 251, 'Parallelism and Concurrency', 2, 'Winter']],
                        [['CSE', 251, 'Parallelism and Concurrency', '1', 'Fall'], 
                         ['CSE', 251, 'Parallelism and Concurrency', '2', 'Winter']],
                        [['Brady', 'Meyer', 'Parallelism and Concurrency', 1, 'Fall'], 
                         ['Brady', 'Meyer', 'Parallelism and Concurrency', 2, 'Winter']],
                        [['CSE', '251', 'Parallelism and Concurrency', 1, 'Fall'], 
                         ['CSE', '251', 'Parallelism and Concurrency', 2, 'Winter']]],
                       [[['Fall', 2024, 5]], # 7
                        [['Fall', 2024, 7]],
                        [[5, 'Fall', 2024]]],
                       [['Computer Science and Engineering', 2], # 8
                        ['Mathematics', 1], 
                        ['Music', 1]],
                       [[['Adam', 'Woods', '25'], # 9
                        ['Brady', 'Meyer', '35'], 
                        ['Lucy', 'Fuller', '45'], 
                        ['Andy', 'Kipner', '60']],
                        [['Adam', 'Woods', 25.0], 
                         ['Brady', 'Meyer', 35.0], 
                         ['Lucy', 'Fuller', 45.0], 
                         ['Andy', 'Kipner', 60.0]],
                        [['Adam', 'Woods', '25', 'Teacher', 'Fall'], 
                         ['Brady', 'Meyer', '35', 'Teacher', 'Fall'], 
                         ['Lucy', 'Fuller', '45', 'Teacher', 'Fall'], 
                         ['Andy', 'Kipner', '60', 'Teacher', 'Fall']]],
                       [[['Marquez', 'Nellie', '3'], # 10
                         ['Shah', 'Kerri', '3'], 
                         ['Rollins', 'Josh', '2'], 
                         ['Meyers', 'Isabel', '2']],
                        [['Shah', 'Kerri', '3'], 
                         ['Marquez', 'Nellie', '3'], 
                         ['Rollins', 'Josh', '2'], 
                         ['Meyers', 'Isabel', '2']],
                        [['Shaw', 'Kerri', '3'], 
                         ['Marquez', 'Nellie', '3'], 
                         ['Rollins', 'Josh', '2'], 
                         ['Meyers', 'Isabel', '2']],
                        [['Kerri', 'Shah', '3'], 
                         ['Nellie', 'Marquez', '3'], 
                         ['Josh', 'Rollins', '2'], 
                         ['Isabel', 'Meyers', '2']],
                        [['Shah', 'Kerri', 3], 
                         ['Marquez', 'Nellie', 3], 
                         ['Rollins', 'Josh', 2], 
                         ['Meyers', 'Isabel', 2]],
                        [['Shah', 'Kerri', '3.0'], 
                         ['Marquez', 'Nellie', '3.0'], 
                         ['Rollins', 'Josh', '2.0'], 
                         ['Meyers', 'Isabel', '2.0']],
                        [['Nellie', 'Marquez', '3'], 
                         ['Kerri', 'Shah', '3'],
                         ['Josh', 'Rollins', '2'], 
                         ['Isabel', 'Meyers', '2']],
                        [['Marquez', 'Nellie', '3'], 
                         ['Shah', 'Kerri', '3'], 
                         ['Meyers', 'Isabel', '2'], 
                         ['Rollins', 'Josh', '2']]]
                      ]


alias_counter = 0
total_aliases = 8
total_erd_queries = 29
total_queries = 10

# open the test folder and read the files inside
if os_name == 'Windows':
    print("Windows OS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '\\tempgrades'
    answer = open(f"{directory}\\week12answers.txt", "w")

elif os_name == 'Linux':
    print("Linux Detected")
    directory = '/home/student/Desktop/itm111grading/v3'
    grading_directory = '/home/student/Desktop/itm111grading/v3/tempgrades'
    answer = open(f"{directory}/week12answers.txt", "w")

elif os_name == 'Darwin':
    print("MacOS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '/tempgrades'
    answer = open(f"{directory}/week12answers.txt", "w")
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
            file_contents = file_contents.replace("USE", "-- ~\nUSE")
            file_contents = file_contents.replace("SET", "-- ~\nSET")
            file_contents = file_contents.replace("DEFAULT CHARACTER -- ~\nSET", "DEFAULT CHARACTER SET")
            file_contents = file_contents.replace("DROP", "-- ~\nDROP")
            file_contents = file_contents.replace("CREATE", "-- ~\nCREATE")
            file_contents = file_contents.replace("SELECT", "-- ~\nSELECT")
            file_contents = file_contents.replace("(-- ~\nSELECT", "(SELECT")
            file_contents = file_contents.replace("INSERT", "-- ~\nINSERT")
            file_contents = file_contents.replace("-- --~\nSELECT", "-- SELECT")
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
        
        
        sqlCommands = [command for command in sqlCommands if command.lower().startswith('use') or command.lower().startswith('drop') or command.lower().startswith('create') or command.lower().startswith('insert') or command.lower().startswith('update') or command.lower().startswith('delete') or command.lower().startswith('select')]
        # check to make sure there are only 2 USE commands

       
        university_count = 0

        erd_count = 0
        total_erd_count = 20
        drop_count = 0
        total_drop_count = 10
        create_count = 0
        total_create_count = 10
        insert_count = 0
        total_insert_count = 10
        mydb_count = 0
        select_count = 0
        total_select_count = 10

        command_num = 0
        drop_schema_count = 0
        create_schema_count = 0

        for command in sqlCommands:
            command_num += 1
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
            if command.lower().startswith('use `university`'):
                university_count += 1
            if command.lower().startswith('drop table'):
                drop_count += 1
                erd_count += 1
            if command.lower().startswith('create table'):
                create_count += 1
                erd_count += 1
            if command.lower().__contains__('insert'):
                insert_count += 1
            if command.lower().startswith('select'):
                select_count += 1
            if mydb_count > 0:
                break
            if command.lower().__contains__('mydb'):
                answer.write("`mydb` database name found. Please switch this to be named university\n")
                answer.write("Skipping ERD check...\n")
                mydb_count += 1
                continue
        if university_count > 2:
            answer.write(f"USE university; command used {university_count} times. There should only be two.\n One in the Forward Engineering code, One before the INSERT statements\n")
            answer.write("Skipping to the next file...\n")
            answer.write("***********************************\n\n")
            continue
            

        # debug.write(f"COMMAND LIST: {sqlCommands}")
        
        #filter out SET commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('set @OLD_UNIQUE_CHECKS') or not command.lower().startswith('set @OLD_FOREIGN_KEY_CHECKS') or not command.lower().startswith('set @OLD_SQL_MODE') or not command.lower().startswith('set OLD_UNIQUE_CHECKS') or not command.lower().startswith('set OLD_FOREIGN_KEY_CHECKS') or not command.lower().startswith('set OLD_SQL_MODE')]

        # filter out SELECT commands
        sqlQueryCommands = [command for command in sqlCommands if (not command.lower().startswith('select *') and command.lower().startswith('select')) or command.lower().startswith('use')]
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('select')]


        sqlQueryCommands = [command for command in sqlQueryCommands if not command.lower().startswith('drop') and not command.lower().startswith('create') and not command.lower().startswith('use `university`;') and not command.lower().startswith('use `university` ;')]
        # print(f"QUERY COMMANDS: {sqlQueryCommands}\n")
        # filter out SELECT @ and SELECT @@ commands
        sqlQueryCommands = [command for command in sqlQueryCommands if not command.lower().startswith('select @') and not command.lower().startswith('select @@')]
        
        sqlQueryCommands = [command for command in sqlQueryCommands if not command.lower().startswith('select*')]
        #filter out SET commands
        sqlQueryCommands = [command for command in sqlQueryCommands if not command.lower().startswith('set')]

        correct_answer_count = 0
        number = 0
        erd_number = 0
        
        for command in sqlCommands:
            erd_number += 1
            
            # answer.write(f"ERD QUERY: {erd_number}. {command}\n")
        

            try:
                mycursor.execute(command)
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
        answer.write("---FINAL ERD TOTALS---\n")
        answer.write(f"{erd_count}/{total_erd_count} of 20 total possible ERD Statements Written\n")
        answer.write(f"{number}/{total_erd_queries} of 29 total possible Statements Written\n")
        answer.write(f"{correct_answer_count}/{total_erd_queries} of 29 total possible Statements Correct\n")


        
    
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
        query7_clause_list = []
        query7_function_list = []
        query8_clause_list = []
        query8_function_list = []
        query9_clause_list = []
        query9_function_list = []
        query10_clause_list = []
        query10_function_list = []

        alias2_counter = 0
        floor_counter = 0
        datediff_counter = 0

        for command in sqlQueryCommands:
            a_number += 1
            
            # answer.write(f"QUERY COMMAND: {a_number}. {command}\n")
            if a_number == 1 and not command.lower().__contains__('use'):
                answer.write(f"USE university; Statement NOT FOUND\n")


            if a_number == 2: # Query 1
                if command.lower().__contains__('select'):
        
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                        
                    if not command.lower().__contains__(' as '):
                        query1_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query1_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query1_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('date_format'):
                        query1_function_list.append(f"DATE_FORMAT Function NOT used")
                    if not command.lower().__contains__('\'%M %d, %Y\'') :
                        query1_function_list.append(f"'%M %d, %Y' NOT used")
                    

            if a_number == 3: # Query 2
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        for word in command.split():
                            if word.lower() == 'as':
                                alias_counter += 1
                                alias2_counter += 1
                    if alias2_counter < 3:
                        query2_clause_list.append(f"3 Aliases required. {3 - alias2_counter} missing")
                        
                    if not command.lower().__contains__(' as '):
                        query2_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('distinct'):
                        query2_clause_list.append(f"DISTINCT Clause NOT used")
                    if not command.lower().__contains__('from'):
                        query2_clause_list.append(f"FROM Clause NOT used")                        
                    if not command.lower().__contains__('join'):
                        query2_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query2_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query2_clause_list.append(f"ORDER BY Clause NOT used")
                    if command.lower().__contains__('floor('):
                        for word in command.split():
                            if word.lower().__contains__('floor'):
                                floor_counter += 1
                        if floor_counter < 2:
                            query2_function_list.append(f" 2 FLOOR Functions required. {2 - floor_counter} missing")
                    if not command.lower().__contains__('floor'):
                        query2_function_list.append(f"FLOOR Function NOT used")
                    if command.lower().__contains__('datediff'):
                        for word in command.split():
                            if word.lower().__contains__('datediff'):
                                datediff_counter += 1
                        if datediff_counter < 4:
                            query2_function_list.append(f" 4 DATEDIFF Functions required. {4 - datediff_counter} missing")
                    if not command.lower().__contains__('datediff'):
                        query2_function_list.append(f"DATEDIFF Function NOT used")
                    if not command.lower().__contains__('concat'):
                        query2_function_list.append(f"CONCAT Function NOT used")

            if a_number == 4: # Query 3
                if command.lower().__contains__('select'):
                    
                    if not command.lower().__contains__('distinct'):
                        query3_clause_list.append(f"DISTINCT Clause NOT used")
                    if not command.lower().__contains__('from'):
                        query3_clause_list.append(f"FROM Clause NOT used")                        
                    if not command.lower().__contains__('join'):
                        query3_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query3_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query3_clause_list.append(f"ORDER BY Clause NOT used")
                
            if a_number == 5: # Query 4
                if command.lower().__contains__('select'):
                    
                    if not command.lower().__contains__('from'):
                        query4_clause_list.append(f"FROM Clause NOT used")                        
                    if not command.lower().__contains__('join'):
                        query4_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query4_clause_list.append(f"WHERE Clause NOT used")

            if a_number == 6: # Query 5
                if command.lower().__contains__('select'):
                    if not command.lower().__contains__('from'):
                        query5_clause_list.append(f"FROM Clause NOT used")                        
                    if not command.lower().__contains__('join'):
                        query5_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query5_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query5_clause_list.append(f"ORDER BY Clause NOT used")
                    
            if a_number == 7: # Query 6
                if command.lower().__contains__('select'):
                    
                    if not command.lower().__contains__('from'):
                        query6_clause_list.append(f"FROM Clause NOT used")                        
                    if not command.lower().__contains__('join'):
                        query6_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query6_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query6_clause_list.append(f"ORDER BY Clause NOT used")

            if a_number == 8: # Query 7
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                        
                    if not command.lower().__contains__(' as '):
                        query7_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('distinct'):
                        query7_clause_list.append(f"DISTINCT Clause NOT used")
                    if not command.lower().__contains__('from'):
                        query7_clause_list.append(f"FROM Clause NOT used")                        
                    if not command.lower().__contains__('join'):
                        query7_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query7_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('count'):
                        query7_function_list.append(f"COUNT Function NOT used")

            if a_number == 9: # Query 8
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                        
                    if not command.lower().__contains__(' as '):
                        query8_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query8_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query8_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('group by'):
                        query8_clause_list.append(f"GROUP BY Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query8_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('count'):
                        query8_function_list.append(f"COUNT Function NOT used")

            if a_number == 10: # Query 9
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                        
                    if not command.lower().__contains__(' as '):
                        query9_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query9_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query9_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query9_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('group by'):
                        query9_clause_list.append(f"GROUP BY Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query9_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('sum'):
                        query9_function_list.append(f"SUM Function NOT used")

            if a_number == 11: # Query 10
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                        alias_counter += 1
                        
                    if not command.lower().__contains__(' as '):
                        query10_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query10_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('join'):
                        query10_clause_list.append(f"JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query10_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('group by'):
                        query10_clause_list.append(f"GROUP BY Clause NOT used")
                    if not command.lower().__contains__('having'):
                        query10_clause_list.append(f"HAVING Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query10_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('sum'):
                        query10_function_list.append(f"SUM Function NOT used")
                    
                    

            # pass each list to a function
            # the function will do all the replacing and formatting
            # then return the list
            
            # print(filename)
            # print(f"{a_number}. {query2_function_list}")
            new_query1c_list = format_list(query1_clause_list)
            new_query1f_list = format_list(query1_function_list)
            new_query2c_list = format_list(query2_clause_list)
            new_query2f_list = format_list(query2_function_list)
            new_query3c_list = format_list(query3_clause_list)
            new_query3f_list = format_list(query3_function_list)
            new_query4c_list = format_list(query4_clause_list)
            newquery4f_list = format_list(query4_function_list)
            new_query5c_list = format_list(query5_clause_list)
            new_query5f_list = format_list(query5_function_list)
            new_query6c_list = format_list(query6_clause_list)
            new_query6f_list = format_list(query6_function_list)
            new_query7c_list = format_list(query7_clause_list)
            new_query7f_list = format_list(query7_function_list)
            new_query8c_list = format_list(query8_clause_list)
            new_query8f_list = format_list(query8_function_list)
            new_query9c_list = format_list(query9_clause_list)
            new_query9f_list = format_list(query9_function_list)
            new_query10c_list = format_list(query10_clause_list)
            new_query10f_list = format_list(query10_function_list)

            
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
            if a_number != 1:
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

            # change all datetime values to strings
            for row in output_list:
                for i in range(len(row)):
                    if type(row[i]) == datetime.date:
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
                    elif a_number == 5:
                        # debug.write(new_query4_list)
                        if len(new_query4c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query4c_list}\n")
                    elif a_number == 6:
                        # debug.write(new_query5_list)
                        if len(new_query5c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query5c_list}\n")
                    elif a_number == 7:
                        # debug.write(new_query6_list)
                        if len(new_query6c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query6c_list}\n")

                    elif a_number == 8:
                        # debug.write(new_query7_list)
                        if len(new_query7c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query7c_list}\n")
                    elif a_number == 9:
                        # debug.write(new_query8_list)
                        if len(new_query8c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query8c_list}\n")

                    elif a_number == 10:
                        # debug.write(new_query9_list)
                        if len(new_query9c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query9c_list}\n")

                    elif a_number == 11:
                        # debug.write(new_query10_list)
                        if len(new_query10c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query10c_list}\n")

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
                    elif a_number == 4:
                        # debug.write(new_query3f_list)
                        if len(new_query3f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query3f_list}\n")
                    elif a_number == 5:
                        # debug.write(new_query4f_list)
                        if len(newquery4f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{newquery4f_list}\n")
                    elif a_number == 6:
                        # debug.write(new_query5f_list)
                        if len(new_query5f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query5f_list}\n")
                    elif a_number == 7:
                        # debug.write(new_query6f_list)
                        if len(new_query7f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query7f_list}\n")
                    elif a_number == 8:
                        # debug.write(new_query7f_list)
                        if len(new_query8f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query8f_list}\n")
                    elif a_number == 9:
                        # debug.write(new_query8f_list)
                        if len(new_query9f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query9f_list}\n")
                    elif a_number == 10:
                        # debug.write(new_query9f_list)
                        if len(new_query10f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query10f_list}\n")
                    elif a_number == 11:
                        # debug.write(new_query10f_list)
                        if len(new_query10f_list) == 0:
                            answer.write(f"All Functions accounted for\n")
                        else:
                            answer.write(f"{new_query10f_list}\n")
                    answer.write("-----ANSWERS-----\n")
                    
                    answer.write(f"Student Answer: {student_answers}\n")
                    answer.write(f"Correct Answer: {correct_answer_list[number-1]}\n")
                    answer.write("---------------------\n")

        answer.write("--------SELECTS-------\n")
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
            os.remove(f"{directory}\\week12answers.txt")
        elif os_name == 'Linux' or os_name == 'Darwin':
            os.remove(f"{directory}/week12answers.txt")
        print("Files Deleted")
    else:
        f.close()
        print("Files Kept")

