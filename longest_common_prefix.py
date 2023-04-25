x = ["app", "apple", "apply", "applications", "apolitical"]
def longestCommonPrefix(xlist) -> str:
    res=""
    sorted_list=sorted(xlist)
    first=sorted_list[0]
    last=sorted_list[-1]
    for i in range(min(len(first),len(last))):
        if(first[i]!=last[i]):
            return res
        res+=first[i]
    return res
c = longestCommonPrefix(xlist=x)
print(c)