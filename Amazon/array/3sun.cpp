class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
      vector <vector<int>> sol;
	    sort (nums.begin (), nums.end ());
      for(int i = 0; i < nums.size(); i++){
        if(i > 0 and nums[i-1] == nums[i]) continue;
        int j = i + 1;
        int k = nums.size() - 1;
        while(k > j){
          if((nums[i] + nums[j] + nums[k]) == 0){
            sol.push_back( {nums[i], nums[j], nums[k]} );
            ++j;
            while (j < k && nums[j] == nums[j-1]) ++j;
          }
          if((nums[i] + nums[j] + nums[k]) > 0) {
            k--;
            if(nums[k] == nums[k+1]) k--;
          }
          if((nums[i] + nums[j] + nums[k]) < 0) j++;
        }
      }
      return sol;
    }
};