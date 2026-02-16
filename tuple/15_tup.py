#Write a program to find common elements between two tuples.

tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 60, 70, 10)
for i in tuple1:
    for j in tuple2:
        if i == j:
            print("Common element are:",i)
