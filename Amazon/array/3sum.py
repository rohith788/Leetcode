class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) #sort the array
        arr = set() #hashset to avoid repetation of pairs
        for i, v in enumerate(nums): # first loop to keep one element locked
            d = {} #map refreshed after every Two sum loop
            for index, val in enumerate(nums[i+1:]): #Two sum problem from here
                if((-v - val) in d): arr.add((val, -v-val, v)) 
                d[val] = index
        return arr
    
