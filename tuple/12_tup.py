# Write a program to check whether a tuple is a palindrome
n = (1, 2, 3, 2, 1)

if n == n[::-1]:
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")