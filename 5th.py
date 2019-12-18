"""Given a string, return the count of the number of times that a
substring length 2 appears in the string and also as the last 2 chars
 of the string, so "hixxxhi" yields 1 (we won't count the end substring)."""

def string_last(str1):
    l=len(str1)
    s=str1[l-2:]
    #print(s)
    s1=str1[0:2]
    asa=str1[:-2]
    #print(asa)
    count=0
    for i in range(len(asa)):
        s1=str1[i:i+2]
        if s==s1:
            count=count+1

    return count
print(string_last('hihihihi'))