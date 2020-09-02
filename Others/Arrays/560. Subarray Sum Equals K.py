class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1 if nums[0] == k else 0
        count = 0
        total = 0
        dict = {}
        dict[0] = 1
        for n in nums:
            total += n
            if total - k in dict:
                count += dict.get(total-k)
            dict[total] = dict.get(total, 0) + 1
        return count