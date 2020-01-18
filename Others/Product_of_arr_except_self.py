class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_arr = []
        L = [1 for i in range(len(nums))]
        R = [1 for i in range(len(nums))]
        for i in range(-1, len(nums)):
          if(i == -1 or i == 0):
            continue
          L[i] = (nums[i -1] * L[i -1])
        for j in range(len(nums) - 1, -1, -1):
          if(j == len(nums) - 1):
            continue
          R[j] = (nums[j + 1] * R[j + 1])
        print(R)
        print(L)
        for k in range(len(nums)):
          prod_arr.append(L[k] * R[k])
        return prod_arr