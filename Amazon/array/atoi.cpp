ass Solution {
	public:
		    int myAtoi(string str) {
			          int sign = 1, i = 0;
				        long num = 0;
					      
					      while(i < str.size() and str[i] == ' ')
						            {
								            i++;
									          }
					            if(str[i] == '-')
							          {
									          sign = -1;
										          i++;
											        }
						          else if(str[i] == '+')
								        {
										        sign = 1;
											        i++;
												      }
							        else if(not isdigit(str[i]))return 0;
								      else if(i == str.size())return 0;
								            while(isdigit(str[i]) and i < str.size())
										          {
												          num = num * 10 + (str[i] - '0');
													          if( sign == -1 and -num < INT_MIN)return INT_MIN;
														          else if( sign == 1 and num > INT_MAX)return INT_MAX;
															          i++;
																        }
									          
									          return sign * num;
										      }
};
