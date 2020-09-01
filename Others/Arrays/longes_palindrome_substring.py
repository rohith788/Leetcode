class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 1 or n is None: return ""
        if n == 1: return s
        ans = ''
        for i in range(n):
            word = self.check_pal(s, i, i)
            if len(word) > len(ans):
                ans = word
            word = self.check_pal(s, i, i+1)
            if len(word) > len(ans):
                ans = word
        return ans
    def check_pal(self, word, l, r):
        while l >= 0 and r < len(word) and word[l] == word[r]:
            l -= 1
            r += 1
        
        return word[l+1:r]