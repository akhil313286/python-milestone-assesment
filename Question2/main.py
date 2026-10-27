import os
file_path = r"C:\Users\313286\Desktop\python-milestone-assesment\Question2\employees.txt"

class Employee:

 def __init__(self, file_path):
    self.file_path = file_path

 def read_file(self):
    try:
     with open (file_path, "r") as file:
      for line in file:
        print(line,end="")
    except FileNotFoundError:
           print("employee file not found")
            

 def salary_above_fiftyThousand(self):
   with open (self.file_path, "r") as file:
        for line in file:
          if line.strip():
             data = line.strip().split(",")
             if int(data[3]) > 50000:
                print("===== Employees with Salary > 50000 =====", data[1], "=" ,data[3])

 def highest_Salary(self):
   name = ""
   HighestSalary = 0
   with open (file_path, "r") as file:
        for line in file:
           if line.strip():
              data = line.strip().split(",")
              if int(data[3]) > HighestSalary:
                 HighestSalary = int(data[3])
                 name = data[1]

   print("highest salary goes to:" ,name, ":",HighestSalary)  

 def role_count(self):
    print("Employee Count by Role:")
    roles = {}
    with open (file_path, "r") as file:
            for line in file:
               if line.strip():
                  role = line.strip().split(",")[2]
                  roles[role] = roles.get(role,0) +1
    for role,count in roles.items():
      print(role, "=", count)


emp = Employee(file_path)  
emp.read_file() 
emp.salary_above_fiftyThousand()
emp.highest_Salary()
emp.role_count()