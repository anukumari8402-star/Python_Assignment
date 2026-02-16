
#  Write a program to find the largest and smallest element in a list
n = int(input("Enter number of elements: "))
my_list = []    
for i in range(n):
    element = int(input("Enter element: "))
    my_list.append(element)
print("The elements in the list are:")
print(my_list)

print("The largest element in the list is:", max(my_list))
print("The smallest element in the list is:", min(my_list))