# Overview

This is for use for any graders of the ITM 111 (Intro to Databases) course at BYU-Idaho

# System Requirements

Access to the AWS instance that hosts MySQL Workbench

OR

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

The student user and database access can be created from the files in the `setup` folder

On line 9 in root.py, you may need to replace the password with your root password if you are on a local machine. If you are using AWS to grade, you can ignore this.


# How to Access the Application

If you are on the AWS instance, the mysql.connector library is already installed.

If you are on a local machine, you must install the mysql.connector library:

```
pip install mysql-connector-python
```

To run the application, choose the particular week you are grading and click the play button

If everything has been successfully installed, the application will run.
