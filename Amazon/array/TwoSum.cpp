//not very fast but it works
//
class Solution {
	public:
		    vector<int> twoSum(vector<int>& nums, int target) {
			            int l = nums.size();
				            vector<int> ans;
					            for( int i = 0; i < l; i++)
							            {
									              for(int j = i+1; j < l; j++ )
											                {
														            if((nums[i] + nums[j]) == target) 
																                {
																			                ans.push_back(i);
																					                ans.push_back(j);
																							            }
															              }
										              }
						            return ans;
							            
							        }
};
