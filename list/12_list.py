#Write a program to find common elements between two lists
x = [2,4,6,7,5,9,3]
y=[2,4,6,12,7,11,0,10]
common=[]
for i in x:    
    if i in y:
        common.append(i)
print(common)