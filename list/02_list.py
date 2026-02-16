# Write a program to count even and odd numbers in a given list
n= int(input("Enter number of elements: "))
my_list = []
for i in range(n):
    element = int(input("Enter element: "))
    my_list.append(element)
print("The elements in the list are:")
print(my_list)
even_count = 0
odd_count = 0
for num in my_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)