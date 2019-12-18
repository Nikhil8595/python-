"""Given a string and a non-negative int n, return a larger string that
is n copies of the original string."""

def string_times(str,n):
    result=""
    for i in range(n):
        result=result+str
        print(result)
string_times('nik',4)
