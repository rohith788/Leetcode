class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
      vector <int> sol;
      vector <int> dist;
	    sort (nums.begin (), nums.end ());
      if(nums.size() == 0) return (nums[0] + nums[1] + nums[2]);
      for(int i = 0; i < nums.size(); i++){
        int j = i + 1;
        int k = nums.size() - 1;
        while(k > j){
          sol.push_back(nums[i] + nums[j] + nums[k]);
          if(nums[j] + nums[k] < target - nums[i]) j++;
          else if(nums[j] + nums[k] > target - nums[i]) k--;
          else return (nums[i] + nums[j] + nums[k]);
        }
      }
      
      for(int i = 0; i < sol.size(); i++){
        dist.push_back(abs(sol[i] - target));
      }
      int min = dist[0], index = 0;
      
      for(int i = 0; i < dist.size(); i++){
        if(min > dist[i]){
          min = dist[i];
          index = i;
        }
      }
			return (sol[index]);

    }
};