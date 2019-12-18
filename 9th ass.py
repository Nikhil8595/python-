def string_match(a,b):
    count=0
    shorter=min(len(a),len(b))
    for i in range(shorter -1):
        sub_a= a[i:i+2]
        sub_b= b[i:i+2]
        if sub_a==sub_b:
            count=count+1
    print(count)
string_match('xxcaazz','xxbaazz')