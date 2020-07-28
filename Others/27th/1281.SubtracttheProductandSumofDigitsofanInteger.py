class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        tot = 0
        prod = 1
        num = str(n)
        for i in range(len(num)):
            tot += int(num[i])
            prod *= int(num[i])
            
        return (prod - tot)