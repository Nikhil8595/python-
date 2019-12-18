"""Given an array of ints, return the number of 9's in the array."""

l=list(input("enter the list"))
#print(l)
#print(len(l))

count=0
for key in range(len(l)):
    if l[key] == '9':
        count=count+1
print(count)
