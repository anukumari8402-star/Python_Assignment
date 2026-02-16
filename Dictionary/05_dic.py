#Write a program to delete a key from a dictionary after checking its existence
stu = {"Anu": 85, "Ravi": 78, "Neha": 92}
print("DIctionary:",stu)
key = input("Enter Key:")
if key in stu:
    del stu[key]
    print("Key deleted successfully")
else:
    print("Key does not exist")
print("Updated dictionary:", stu)
