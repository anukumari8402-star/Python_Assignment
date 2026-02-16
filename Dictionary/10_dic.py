#Write a program to sort a dictionary based on values using loops.

stu = {"Anu": 85, "Ravi": 78, "Neha": 92, "Amit": 88}

# Convert dictionary to list of items
items = list(stu.items())

# Sorting using loops (Bubble sort)
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            # Swap
            items[i], items[j] = items[j], items[i]

# Convert back to dictionary
sorted_dic = dict(items)
print("Sorted dictionary based on values:",sorted_dic)




