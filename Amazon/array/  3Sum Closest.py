class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i, v in enumerate(nums):
            j, k = i+1, len(nums)-1
            while(j < k):
                sum = nums[i] + nums[j] + nums[k]
                if(target > sum): j += 1
                else: k -= 1
                if(abs(target-sum) < abs(target - ans)): ans = sum
                # ans = min(ans, target - sum)
                # print(sum, abs(target-sum), abs(target - ans))
        return ans