#Write a program to input n elements into a list and display them using a loop
n = int(input("Enter number of elements: "))
list = []
for i in range(n):
    num = input("Enter element for my list: ")
    list.append(num)
print("The elements in the list are:")
print(list)