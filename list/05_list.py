# Write a program to count how many times a given element appears in a list.
n = int(input("Enter number of elements: "))
my_list = []
for i in range(n):
    element = input("Enter element: ")
    my_list.append(element)
print("The elements in the list are:")
print(my_list)
print("Enter the element to count:")
count = input()
print("The element", count, "appears", my_list.count(count), "times in the list.")

#if list element is given....
my_list = ['apple', 'banana', 'orange', 'banana', 'grape','banana']
print(my_list.count('banana'))