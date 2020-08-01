class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s ==" " or s =="": True
        i, j = 0, len(s) - 1
        while( i < j ):
            a, z = s[i].lower(), s[j].lower()
            if(a.isalnum() and z.isalnum()):
                if(a != z): return False
                else:
                    i += 1
                    j -= 1
                    continue
            print(i," ", i + (not a.isalnum()))
            i, j = i + (not a.isalnum()), j - (not z.isalnum())
                
        return True
        
        