ass Solution {
	public:
		    int maxArea(vector<int>& height) {
			          int m = 0;
				        int i = 0, j = height.size() - 1;
					      while(i < j){
						              int area = (j - i) * min(height[i], height[j]);
							              m = max(m, area);
								              if(height[i] < height[j]) i++;
									              else j--;
										            }
					            return m;
						          // return dnc(height, 0, height.size()-1);
							  //     }
							  //       
							  //       public:
							  //         int dnc(vector<int>& height, int i, int j){
							  //             int area = (j - i) * min(height[j], height[i]);
							  //                 if(i == j)return 0;
							  //                     int m = max(area, dnc(height, i+1, j));
							  //                         return max(m, dnc(height, i, j-1)); 
							  //                           }
							  //                           };
