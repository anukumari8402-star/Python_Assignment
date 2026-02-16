#Write a program to find the second largest element in a list.
numbers = [11,34,23,56,98,45,34,76,84,34,67]
print("Original list:", numbers)
numbers.sort()
print(numbers)
print("The second largest element in the list is:", numbers[-2])