"""Given a string, return a new string where the first and last
chars have been exchanged."""

x=input('enter string: ')
mid=x[1:len(x)-1]
print(x[-1],end='')
for i in mid:
    print(i,end='')
print(x[0],end='')
