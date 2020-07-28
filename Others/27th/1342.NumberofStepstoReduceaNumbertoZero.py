class Solution:
    def numberOfSteps (self, num: int) -> int:
        if(num == 0):
          return 0
        if(num == 1):
          return 1
        count = 0
        while(num > 0):
          print(num)
          if(num % 2 == 0):
            count += 1
            num = num // 2
          else:
            count += 1
            num -= 1
        return count