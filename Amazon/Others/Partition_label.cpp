class Solution {
public:
    vector<int> partitionLabels(string S) {
      vector <int> ans;
      if(S.size() == 0) return ans;
      unordered_map <int,int> lmp;
      int s = 0, l = 0;
      //initializing the map with the characters of the string
      for(int i = 0; i < S.size(); i++){
        lmp[S[i]] = i;
      }
      ans.emplace_back(1);
      for(int i = 0; i < S.size(); i++){
        int indx = lmp[S[i]];
        if(i <= l){
          l = max(l, indx);
          ans.back() = max(ans.back(), l - s + 1);
        }
        else{
          l = indx;
          s = i;
          ans.emplace_back(l - s + 1);
        }
      }
      return ans;
    }
};