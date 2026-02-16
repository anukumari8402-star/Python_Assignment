#Write a program to rotate a list by k positions
l = [10, 20, 30, 40, 50]
k = 2
rotated = l[k:] + l[:k]
print("Rotated list:", rotated)
