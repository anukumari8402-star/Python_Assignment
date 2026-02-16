#Write a program to create a new tuple containing only positive numbers

ori_tup = (5, -3, 8, -1, 0, 12, -7, 4, -2, 9)
pos_tup = tuple(x for x in ori_tup if x > 0)
print(f"Original tuple: {ori_tup}")
print(f"Positive numbers tuple: {pos_tup}")
