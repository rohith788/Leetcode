class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int exp_sum = (nums.size() * (nums.size() + 1)) / 2;
        int act_sum = 0;
        for(int i = 0; i < (nums.size()); i++){
          act_sum += nums[i];
        }
        return(exp_sum- act_sum);
    }
};