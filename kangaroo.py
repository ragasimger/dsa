def kangaroo(x1, v1, x2, v2):
    if (
        (x1 > x2) and (v1 > v2) or 
        (x1 < x2) and (v1 < v2) or
        v1 == v2
    ):
        return "NO"
    elif (x2-x1) % (v1-v2) == 0:
        return "YES"
    else:
        "NO"
x1 = 0
v1 = 3
x2 = 4
v2 = 2
k = kangaroo(x1,v1,x2,v2)
print(k)