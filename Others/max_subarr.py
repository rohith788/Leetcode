###################################Greedy Method(O(N))###############################
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         ans = nums[0]
#         curr = nums[0]
#         for i in range(1, len(nums)):
#           curr = max(curr + nums[i], nums[i])
#           ans = max(ans, curr)
#         return ans




#############################DnC Method(O(nlogn))##################################
class Solution:
    def other_summer(self, arr, left, right, mid):
      if(left == right):
        return arr[left]
      curr = 0
      left_sum = float('-inf')
      for i in range(mid, left - 1, -1):
        curr += arr[i]
        left_sum = max(left_sum, curr)
        
      right_sum = float('-inf')
      curr = 0
      for i in range(mid + 1, right + 1):
        curr += arr[i]
        right_sum = max(curr, right_sum)
        
      return right_sum + left_sum
    
    def summer(self, arr, left, right):
      if( left == right):
        return arr[left]
      mid = (left + right) // 2
      
      l_sum = self.summer(arr, left, mid)
      r_sum = self.summer(arr, mid + 1, right)
      other_sum = self.other_summer(arr, left, right, mid)
      
      return max(l_sum, other_sum, r_sum)
    
    def maxSubArray(self, nums: List[int]) -> int:
        return self.summer(nums, 0 , len(nums) - 1)
          