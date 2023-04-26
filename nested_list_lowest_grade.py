# number_of_records = int(input())
# l1 = []
# l2 = []
# for _ in range(number_of_records):
#     name = input()
#     score = float(input())
#     stu = [name, score]
#     l1.append(stu)
# for x in l1:
#     l2.append(x[1])
# sorted(l2)
# l3 = []
# l4 = []
# l4.append(l2[0])
# for _ in l2:
#     if l4[0] == _:
#         l3.append(_)
# l5 = []
# for x,y in enumerate(l1):
#     for _ in l3:
#         if _ == y[1]:
#             l5.append(y[0])
# l5.sort()
# final_list = list(set(l5))
# for _ in final_list:
#     print(_)

number_of_records = int(input())
stu = []
for _ in range(number_of_records):
    name = input()
    score = float(input())
    stu = [name, score]
    # l1.append(stu)
    stu.append(
        [name,score]
    )

sorted_scores = sorted(
    list(
        set(x[1] for x in stu)
    )
)
# print(sorted_scores)
second_lowest = sorted_scores[1]
low_final_list = []
for student in stu:
    if second_lowest == student[1]:
        low_final_list.append(student[0])
for student in sorted(low_final_list):
    print(student)