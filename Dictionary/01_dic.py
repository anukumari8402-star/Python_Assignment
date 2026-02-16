#Write a Python program to create a dictionary of n students and their marks and to count the number of students for whose marks ≥ 40.
n = int(input("Enter number of students: "))
students = {}
count = 0
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
for key in students:
    if students[key] >= 40:
        count += 1
print("Student dictionary:", students)
print("Number of students with marks greater than or equal to 40:", count)
