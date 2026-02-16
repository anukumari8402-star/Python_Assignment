#Write a program to find the sum of all elements in a list
#if list element is asking by user
n = int(input("Enter number of elements: "))
my_list = []    
for i in range(n):
    element = int(input("Enter element: "))
    my_list.append(element)
print("The elements in the list are:")
print(my_list)
total_sum = sum(my_list)
print("The sum of all elements in the list is:", total_sum)

#if list element is already given....
n=[2,3,4,5,6]
print("The sum of elements in the list are:",sum(n))