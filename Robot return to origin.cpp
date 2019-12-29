class Solution {
public:
    bool judgeCircle(string moves) {
      vector<int> start = {0,0};
      for(int i = 0; i < moves.size(); i++){
        if(moves[i] == 'U') start[0] = start[0] + 1;
        else if(moves[i] == 'D') start[0] = start[0] - 1;
        else if(moves[i] == 'L') start[1] = start[1] - 1;
        else if(moves[i] == 'R') start[1] = start[1] + 1;
      }
      if(start[0] == 0 and start[1] == 0) return true;
      return false;
    }
};