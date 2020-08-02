class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]] = [i]
                
        for i in enumerate(d):
            if len(d[i[1]]) == 1:
                return d[i[1]][0]
        return -1
            