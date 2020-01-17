class Solution:
    def isPalindrome(self, x: int) -> bool:
#         num = x
#         if(x < 0):
#           return False
#         temp = 0
#         for i in range(len(str(x))):
#           temp = temp * 10 + (x % 10)
#           x = (x - (x % 10)) / 10

#         if(int(temp) == num):
#           return True
        return str(x) == str(x)[::-1]