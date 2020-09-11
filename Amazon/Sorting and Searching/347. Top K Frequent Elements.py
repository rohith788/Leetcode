class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return nums
        count_dict = Counter(nums)
        ans = heapq.nlargest(k, count_dict.keys(), key=count_dict.get)
        return ans