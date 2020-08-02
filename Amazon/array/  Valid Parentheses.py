class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return True
        arr = []
        left = {")" : "(", "]" : "[", "}" : "{"}
        # arr.append(s[0])
        for i in s:
            if i in left:
                temp = arr.pop() if arr else ''
                if temp != left[i]: return False
            else: arr.append(i)
        return not arr
                    