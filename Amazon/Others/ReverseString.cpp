class Solution {
public:
    int reverse(int x) {
      if(x == 0) return x;
      if(x < pow(-2, 31) or x >= pow(2,31)) return 0;
      int ans = 0;
      while(x != 0){
        int temp = x % 10;
        if (ans > INT_MAX/10 || (ans == INT_MAX / 10 && temp > 7)) return 0;
        if (ans < INT_MIN/10 || (ans == INT_MIN / 10 && temp < -8)) return 0;        
        ans = (ans * 10) + temp;
        x /= 10;
      }
      return ans;
    }
};