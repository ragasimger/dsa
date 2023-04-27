if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x = student_marks.get(query_name)
    y = 0
    for _ in x:
        y = _ + y
    res = float(y/len(x))
    print(format(res, '.2f'))