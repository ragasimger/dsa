import re
class RomanToInt:
    def __init__(self, s) -> None:
        self.s = s

    def is_roman_number(self):
        s = self.s
        pattern = re.compile(r"""   
                                    ^M{0,3}
                                    (CM|CD|D?C{0,3})?
                                    (XC|XL|L?X{0,3})?
                                    (IX|IV|V?I{0,3})?$
                """, re.VERBOSE)
        if re.match(pattern, s):
            return True
        return False

    def convert_roman_to_integer(self) -> int:
        if not self.is_roman_number():
            raise Exception("Not a valid roman")
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
    
y = RomanToInt("I")
z = y.convert_roman_to_integer()
print(z)

