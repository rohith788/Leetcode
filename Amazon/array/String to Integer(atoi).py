MAPPING = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}

MAX_INT = 2**31-1
MIN_INT = -(2**31)

class Solution:
    def myAtoi(self, string: str) -> int:
        s = string.lstrip(' ')
        if not s:
            return 0
        sign = -1 if s[0] == '-' else 1
        if sign == -1 or s[0] == '+': s = s[1:]
        ans = 0
        for i in s:
            print(i)
            if i not in MAPPING:
                return max(MIN_INT, min(MAX_INT, ans * sign))
            ans = (ans*10) + MAPPING[i]
        return max(MIN_INT, min(MAX_INT, ans * sign))