class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0 or len(s) < len(t): return ""
        d = Counter(t) #map of all the elements with the count
        min_win = len(s) + 1 #setting a default value for the minim window size
        l, r = 0, 0 
        tot_char = len(t) #number of charactes the window should contain
        ans = "" #output variable
        while(r < len(s)):
            if s[r] in d: #if the char is one of the desired chars
                if d[s[r]] > 0: #if there are more than one of those chars in the window
                    tot_char -= 1 #decrease the number needed
                d[s[r]] -= 1 #decrese even if -v, this will be balaced if there are more than necessary chars
            while tot_char == 0: #star making the window small
                if (r - l + 1) < min_win: #if the window is smaller then the previously small window
                    min_win = (r - l + 1) 
                    ans = s[l:r+1] #save the output
                if s[l] in d: #if the char is one of the desired chars
                    d[s[l]] += 1 #balancing the chars
                    if d[s[l]] > 0:
                        tot_char += 1 #counting for necessary chars
                l += 1
            r += 1
        return  ans
            
        
        
