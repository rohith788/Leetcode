class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        k = i - 1
        if i == 0:
            nums.reverse()
            return
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l = k + 1
        r = len(nums) - 1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -= 1
