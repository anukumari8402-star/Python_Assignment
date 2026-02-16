#Write a program to count occurrences of each element in a tuple.
n = (23,78,45,23,56,34,78,56,23,80,90,90,78)
print("Tuple:",n)
print("\nOccurrence of each element:")
for element in set(n):
    count = n.count(element)
    print(f"{element}: {count}")

