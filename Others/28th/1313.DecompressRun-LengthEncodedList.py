class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer_arr = []
        i = 0
        while(i < len(nums)):
            arr = [nums[i+1]] * nums[i]
            answer_arr += arr
            i += 2
        return answer_arr