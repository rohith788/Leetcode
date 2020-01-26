class Solution:
    def isValid(self, s: str) -> bool:
      brack = {")":"(",  "}" :"{", "]":"["}
      stack = []
      for i in s:
        
        if i in brack:
          top = stack.pop() if stack else '?'
          if brack[i] != top:
            return False
        else:
          stack.append(i)  
      return not stack     
