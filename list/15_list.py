#Write a program to split a list into even-index and odd-index lists
lst = [2,4,5,3,5,7,3,23,56,75,34,76,32,8,9,10]
even_index = lst[::2]
odd_index = lst[1::2]
print("Even index list:", even_index)
print("Odd index list:", odd_index)
