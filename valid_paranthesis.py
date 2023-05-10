def isValid(s):
    if len(s) % 2 != 0:
        return False
    dict_data = {
        '(' : ')', 
        '[' : ']', 
        '{' : '}'
    }
    params_list = []
    for i in s:
        if i in dict_data.keys():
            params_list.append(i)
        else:
            if len(params_list) == 0:
                return False
            x = params_list.pop()
            if i!= dict_data[x]:
                return False
    return len(params_list) == 0
# s = "()[]{}"
# s = "(]"
# s = "()"
s = "()[()]{({})}"
ob = isValid(s=s)
print(ob)

