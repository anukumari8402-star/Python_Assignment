#Write a program to find the key with the maximum value.
stu = {"Anu": 85, "Ravi": 78, "Neha": 92}
print("Key with maximum value:", max(stu, key=stu.get))
print("Maximum value:", stu[max(stu, key=stu.get)])
