# Employee File Management
A Python program that reads employee records from a text file and produces a short report: the full list, employees earning more than 50000, the highest salary, and the number of employees in each role.

# Files
>main.py :Contains the Employee class and the code that runs the report
>employees.txt :Stores one employee per line for all the employees [Employee ID,Name,Role,Salary]

# Method :                  	     What it does
__init__(self, file_path):	         Stores the path to the employee file
read_file(self):                     Prints every line in the file. 
salary_above_fiftyThousand(self):	 Prints each employee whose salary is greater than 50000
highest_Salary(self):                Finds the employee with the highest salary and prints name and amount
role_count(self):	                 Counts the employees in each role and prints the counts

# How the Program Works
>The program opens employees.txt with a with block, so the file closes automatically after reading.
>Each line is split at the commas with split(","). The salary is at index 3, the name is at index 1, and the role is at index 2.
>The salary is converted to a number with int() before it's compared.
>Blank lines are skipped with  if line.strip():.
>The program creates one Employee object and calls each method in turn.

# Sample input
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000

# Expected output

101,Rahul,Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
===== Employees with Salary > 50000 ===== John = 60000
highest salary goes to: John : 60000
Employee Count by Role:
Developer = 2
Tester = 2

# Requirements
>Python 3.x
>An employees.txt file in the same folder as the program, or file path

# How to Run
Open the Question2 folder in VS Code.
Make sure employees.txt is in the same folder as main.py.
Select a Python 3 interpreter.
Click the Run button, or run python main.py in the terminal.