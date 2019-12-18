class Solution {
	public:
	    int lengthOfLongestSubstring(string s) {
	            vector<int> sub(128, -1);
	        int l = 0, c = 0, i = 0, window = 0;
            
        while (i < s.length())
        {
            if(sub[s[i]] == -1)
                {
                    sub[s[i]] = i;
                l++;
                c = max(c, l);
                i++;
                continue;
            }
            fill(sub.begin(), sub.end(), -1);
            i = window + 1;
            window = i;
            l = 0;
        }
        return max(c,l);	
