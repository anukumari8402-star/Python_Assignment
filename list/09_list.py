#Write a program to check whether a list is sorted or not
x=[3,5,2,6,1,0,9,8,4,7,10]
z=[1,2,3,4,5,6,7,8,9,10]
# x.sort() #unsorted list ko sort ko krne k liye.
print(x)
y=sorted( x)
if x==y:
    print("The list is sorted.")
else:
    print("The list is not sorted.")
        
'''
#for sorted list
print(z)
y=sorted( z)
if z==y:
    print("The list is sorted.")
else:
    print("The list is not sorted.")'''