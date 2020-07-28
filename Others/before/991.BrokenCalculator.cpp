class Solution {
public:
    int brokenCalc(int X, int Y) {
      int count = 0;
      while(Y > X){
        count++;
        if(Y % 2 == 1) Y++;
        else Y = Y / 2;
      }
    return (count + X - Y);
  }
};