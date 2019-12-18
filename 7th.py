"""Given an array of ints, return True if one of the first 4 elements
 in the array is a 9. The array length may be less than 4."""

l=list(input("enter the list:"))
#key = 9
count=0
for key in (range(0,4)):
    if l[key] == '9':
        count=count+1
print(count)


