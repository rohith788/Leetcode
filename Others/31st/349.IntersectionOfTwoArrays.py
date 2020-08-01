class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if(len(set(nums1)) < len(set(nums2))): return [i for i in set(nums1) if i in set(nums2)]
        else: return [i for i in set(nums2) if i in set(nums1)]