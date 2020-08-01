class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if((k - nums [i]) in d):
                return [d[k - nums[i]], i]
            else:
                d[nums[i]] = i 
        return []
                