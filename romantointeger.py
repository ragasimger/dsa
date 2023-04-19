class RomanToInt:
    def __init__(self, s) -> None:
        self.s = s
    # def check_occurence(self):
    #     s = self.s
    #     k = dict()
    #     str_list = s.strip()
    #     list_len = len(str_list)
    #     # for i in range(0,list_len)
    def convert_roman_to_integer(self) -> int:
        # self.check_occurence()
        roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        result = 0
        s = self.s
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[(i+1)]]:
                result-=roman[s[i]]
            else:
                result+=roman[s[i]]
        return result+roman[s[-1]]
    
y = RomanToInt("IX")
z = y.convert_roman_to_integer()
print(z)

