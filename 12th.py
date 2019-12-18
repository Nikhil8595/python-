"""Given a string, we'll say that the front is the first 3 chars
of the string. If the string length is less than 3,
the front is whatever is there. Return a new string which
is 3 copies of the front."""

a=input('enter the string:')
if len(a) < 3:
    print("invalid string")
else:
    print(a[:3]*3)