class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
      if(k <= 1) return 0;
      int count = 0;
      int prod = 1;
      int l = 0;
      for(int r = 0; r < nums.size(); r ++){
        prod *= nums[r];
        while( prod >= k) prod /= nums[l++];
        count += r - l + 1;
      }  
      return count;
    }
};