def compareTriplets(a, b):
    a1 = 0
    b1 = 0
    for x, y in zip(a,b):
        if x > y:
            a1 += 1
        elif x < y:
            b1 += 1
    return a1, b1


x = [17, 28, 30]
y = [99, 16, 8]
result = compareTriplets(x,y)
print(result)