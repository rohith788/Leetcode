class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # left = [0] * n 
        # right = [0] * n
        ans = [0] * n
        # left[0] = 1
        ans[0] = 1
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i -1]
        #     left[i] = nums[i-1] * left[i-1]
        # right[n-1] = 1
        right = 1
        for i in reversed(range(n)):
            ans[i] = ans[i] * right
            right *= nums[i]
        #     right[i] = nums[i+1] * right[i+1]
        # for i in range(n):
        #     ans[i] = left[i] * right[i]
        return ans
            
        