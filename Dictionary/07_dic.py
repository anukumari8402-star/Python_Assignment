# Write a program to create a dictionary of numbers and their squares
stu = {"Anu": 85, "Ravi": 78, "Neha": 92}
print("Original dictionary:", stu)
squares = {}
for key in stu:
    squares[key] = stu[key] ** 2
print("Dictionary with squares:", squares)
