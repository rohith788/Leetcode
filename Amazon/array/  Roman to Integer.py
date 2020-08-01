MAPPING = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            if(i + 1 < len(s) and MAPPING[s[i]] < MAPPING[s[i+1]]):  
                count += MAPPING[s[i + 1]] - MAPPING[s[i]]
                i += 2
            else:
                count += MAPPING[s[i]]
                i += 1
        return count
            