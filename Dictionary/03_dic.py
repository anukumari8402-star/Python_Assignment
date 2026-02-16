#Write a program to check whether a given key exists in a dictionary.
stu = {"Anu": 85,"Ravi": 78,"Neha": 92}
key = input("Enter key to search: ")
if key in stu:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")
