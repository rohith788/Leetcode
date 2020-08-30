class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        word = {}
        max_l = 0
        for r in range(len(s)):
            if s[r] not in word:
                max_l = max(max_l, r-l+1)
            else:
                if word[s[r]] < l:
                    max_l = max(max_l, r-l+1)
                else:
                    l = word[s[r]] + 1
            word[s[r]] = r
        return max_l