# Student Marks Management System

# Description
This program stores marks for three students, calculates each student's total, average, grade, and result, and then prints a summary.

# DATA
Each student is stored as a dictionary inside the student_details list:

>Student ID
>Name
>Python Marks
>SQL Marks
>AI Marks

# What the program does:
 Print the header. It shows ===== Student Result =====.
Loop through each student. For every student, the program:
 >Prints the student ID and name
 >Adds the three subject marks to get the total
 >Divides the total by 3 to get the average
 >Assigns a grade and a PASS/FAIL result

max() compares the total marks of all students and returns the top student's name.
List comprehension: marks = [s[subject] for subject in subjects], which builds student’s list of marks.
The program checks each student's average and collects the names of students with an average above 75.
It shows the highest scorer and the list of students above 75.

# Technologies Used :
 >Dictionaries
 >Lists
 >Conditional statements
 >Loops
A student passes if the average is 40 or more. Otherwise, the result is FAIL.

# Sample output
===== Student Result =====
Student ID: 101
Name: Rahul
Total: 249
Average: 83.0
Grade: A
Result: PASS

Student ID: 102
Name: Anjali
Total: 225
Average: 75.0
Grade: B
Result: PASS

Student ID: 103
Name: Priya
Total: 240
Average: 80.0
Grade: A
Result: PASS

Highest Scoring Student: Rahul
Students above 75: Rahul, Priya

# How to run:
 Open main.py in VS Code.
 Select a Python 3 interpreter.
 Click the Run button, or run python main.py in the terminal.