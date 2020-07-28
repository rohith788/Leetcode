class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for i in range(len(nums)):
          if nums[i] == target:
            return i
          elif nums[i] < target:
            index += 1
        return index