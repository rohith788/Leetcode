class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []        
        for i,v in enumerate(nums):
            arr.insert(index[i], v)
        return arr