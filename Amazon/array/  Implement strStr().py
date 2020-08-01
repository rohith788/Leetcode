class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0 #if needle is blank
        if len(haystack) != 0: 
            if len(needle) > len(haystack):  #if haystack is smaller than needle
                return -1
        n_len = len(needle) 
        h_len = len(haystack)
        for i in range(h_len):#iterate through haystack
            j = 0 
            if(i + n_len <= h_len): #check if needle is bigger than the rest of haystack
                if(haystack[i:(i+n_len)] == needle): return i #check match and return index
        return -1