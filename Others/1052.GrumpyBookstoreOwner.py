class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        no_cust, ones, max_ones = 0, 0 ,0
        for i in range(len(customers)):
          if grumpy[i] == 1:
            ones += customers[i]
          else:
            no_cust += customers[i]
          if i >= X:
            if grumpy[i - X] == 1:
              ones -= customers[i - X]
          max_ones = max(max_ones, ones)
          
        return (max_ones + no_cust)
