#Write a program to separate positive and negative numbers from a list.  
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_numbers = []
negative_numbers = []

for num in numbers:
    if num > 0:
        positive_numbers.append(num)
    else:
        negative_numbers.append(num)
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)