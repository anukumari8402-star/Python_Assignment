#  Write a program to compare two tuples element-wise

tuple1 = (10, 20, 30, 40)
tuple2 = (10, 25, 30, 35)
i = 0
for element in tuple1:
    if element == tuple2[i]:
        print("Elements at position", i, "are equal:", element)
    else:
        print("Elements at position", i, "are not equal:", element, "and", tuple2[i])
    i = i + 1
