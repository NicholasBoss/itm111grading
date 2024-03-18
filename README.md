# Overview

This is for use for any graders of the ITM 111 (Intro to Databases) course at BYU-Idaho

# System Requirements

VS Code

Python (Make sure you add it to the path/environment variables when installing)

MySQL Workbench 

MySQL Server

(Use the 8.0.34 versions on Windows, MAC users: Workbench does not work normally but you can try using the 8.0.36 versions)

A student user with access to the following databases:

bike

employees

magazine

v_art

world

film

university
The student user is created in the Local Instance tab (Root User):

```
CREATE USER 'student'@'localhost';
GRANT ALL ON bike.* TO 'student'@'localhost';
GRANT ALL ON employees.* TO 'student'@'localhost';
GRANT ALL ON magazine.* TO 'student'@'localhost';
GRANT ALL ON v_art.* TO 'student'@'localhost';
GRANT ALL ON world.* TO 'student'@'localhost';
GRANT ALL ON film.* TO 'student'@'localhost';
GRANT ALL ON university.* TO 'student'@'localhost';
```

# How to Access the Application

You must use the mysql.connector library. You can install it using:

```
pip install mysql-connector-python
```

To run the application, choose the particular week you are grading and click the play button:

If everything has been successfully installed, the application will run.
