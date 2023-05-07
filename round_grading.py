'''
If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.


grade = 84 round to 85 (85 - 84 is less than 3)
grade = 29 do not round (result is less than 40)
grade = 57 do not round (60 - 57 is 3 or higher)

'''

import math

def gradingStudentsusingmath(grades):
    new_list = []
    for i in grades:
        if i < 38:
            new_list.append(i)
        else:
            c = math.ceil(i/5) * 5
            if c - i < 3:
                # return x
                new_list.append(c)
            elif c - i >= 3:
                # return i
                new_list.append(i)
    return new_list

def gradingStudentswithloop(grades):
    new_list = []
    for i in grades:
        if i < 38:
            new_list.append(i)
        else:
            for _ in range(5):
                x = _ + i
                if x % 5 == 0:
                    if x - i < 3:
                        new_list.append(x)
                    elif x - i == 3:
                        new_list.append(i)
    return new_list


grades = [
    73,
    67,
    38,
    33
]

x = gradingStudentsusingmath(grades=grades)
y = gradingStudentswithloop(grades=grades)
print(x)
print(y)