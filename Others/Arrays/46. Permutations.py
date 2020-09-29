class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(n):
            if n == len(nums):
                ans.append(nums[:])
            for i in range(n, len(nums)):
                nums[n], nums[i] = nums[i], nums[n]
                helper(n + 1)
                nums[n], nums[i] = nums[i], nums[n]

        ans = []
        helper(0)
        return ans