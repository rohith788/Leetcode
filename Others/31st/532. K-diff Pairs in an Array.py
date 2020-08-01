class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = []
        nums = sorted(nums)
        d = {}
        for i in nums:
            if (i in d):
                count.append((d[i], i))
            d[i + k] = i
        return len(set(count))
           
