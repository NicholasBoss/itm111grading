# Overview

This is for use for any graders of the ITM 111 (Intro to Databases) course at BYU-Idaho

## System Requirements

Access to the AWS instance that hosts MySQL Workbench

OR

VS Code

Python (Make sure you add it to the path/environment variables when installing)

MySQL Workbench 

MySQL Server

(Use the 8.0.34 versions on Windows, MAC users: Workbench does not work normally but you can try using the 8.0.36 versions)

A student user and database access:

This can be created from the files in the `setup` folder

On line 9 in `root.py`, you may need to replace the password with your root password if you are on a local machine. If you are using AWS to grade, you can ignore this.


## How to Access the Application

If you are on the AWS instance, the mysql.connector library is already installed.

If you are on a local machine, you must install the mysql.connector library:

```
pip install mysql-connector-python
```

To run the application, choose the particular week you are grading and click the play button

If everything has been successfully installed, the application will run.

## How to Use the Application

***Video Coming Soon***
<!-- [How to Use the Application](https://youtu.be/1Q6J9Q1Z9Zo) -->

Depending on the week, you will need to use the correct file.  
The versions are separated into folders by their version.  
Each file is a different week. 

When you first run a file, it will create a folder called `tempgrades` in the same directory as the file. This is where the files you are grading will be placed.

To use the hw check files, you must have a file in the `tempgrades` folder.

Without a file, the program will state that there are `No Files to Grade`.

