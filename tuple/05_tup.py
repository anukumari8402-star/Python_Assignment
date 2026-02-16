#Write a program to count even and odd numbers in a tuple.
n = (23,4,5,6,45,67,32,78)
print("Tuple:",n)
even_count=0
odd_count=0
for i in n:
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Even Number:",even_count)
print("Odd Number:",odd_count)