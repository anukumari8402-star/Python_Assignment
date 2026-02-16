#Write a program to demonstrate immutability of a tuple
my_tuple = (10, 20, 30, 40)
my_list = [10, 20, 30, 40]
print("Original tuple:", my_tuple)
print("Original list:", my_list)
my_list[1] = 99
print("Modified list:", my_list)

