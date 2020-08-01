class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0): return 0
        if(len(s) == 1): return 1
        count_max = 0
        arr = []
        arr = set(arr)
        i, j = 0, 0
        while(i < len(s) and j < len(s)):
            if(s[j] not in arr):
                arr.add(s[j])
                j += 1
                count_max = max(count_max, (j - i))
            else: 
                arr.remove(s[i])
                i += 1
            
        return count_max