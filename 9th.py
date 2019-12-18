"""Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings."""

def string_match(str1,str2):
    count=-1
    sub1=str1[0:2]
    for i in range(0,len(str1)):
        sub1=str1[i:i+2]
        for j in range(0,len(str2)):
            if sub1==str2[j:j+2]:
                count=count+1
    print(count)
string_match('abc', 'abc')


