"""Given a non-empty string like "Code" return a string like "CCoCodCode"""

def string_sp(str):
    result=""
    for i in range(len(str)):
        result=result+ str[:i+1]
    return result
print(string_sp('nikhil'))