student_details  = [
    {"Student ID": 101, "Name": "Rahul", "Python Marks": 84, "SQL Marks": 75, "AI Marks": 90},
    {"Student ID": 102, "Name": "Anjali", "Python Marks": 72, "SQL Marks": 88, "AI Marks": 65},
    {"Student ID": 103, "Name": "Priya", "Python Marks": 70, "SQL Marks": 90, "AI Marks": 80}
]
print("===== Student Result =====")
subjects=["Python Marks","SQL Marks","AI Marks"]
for s in student_details:
    print("Student ID:", s["Student ID"])
    print("Name:", s["Name"])

    marks = [s[subject] for subject in subjects]
    total = sum(marks)
    print("Total:", total)
    average = total / len(marks)
    print("Average:", average)

    if average >= 80:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "D"

    print("Grade:", grade)
    result = "PASS" if average >= 40 else "FAIL"
    print("Result:", result)
    print()

highestScore = max(student_details, key = lambda s: s["Python Marks"]+ s["SQL Marks"] + s["AI Marks"]) ["Name"]
print("Highest Scoring Student:", highestScore)

students = []
for s in student_details:
        avg = sum(s[subject] for subject in ["Python Marks", "SQL Marks", "AI Marks"]) / 3
        if avg > 75:
            students.append(s["Name"])
print("Students above 75:", ", ".join(students))       