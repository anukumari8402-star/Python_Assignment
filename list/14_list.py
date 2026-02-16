# Write a program to find the frequency of each element in a list
my_list = [1, 2, 2, 3, 4, 4, 4]
frequency = {}
for element in my_list:
    frequency[element] = frequency.get(element, 0) + 1
print(frequency)