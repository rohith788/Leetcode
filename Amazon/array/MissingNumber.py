class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        m = len(nums)
        tot = (m * (m + 1)) // 2
        tot2 = sum(nums)
          
        return(tot - tot2)
        