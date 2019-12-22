class Solution {
public:
    int romanToInt(string s) {
      if( s == "") return 0;

      int l = s.size()-1;
      return number(s, l);
    }
public:
  int number(string s, int l) {
    if(l < 0) return 00;
    if(s[l-1] == 'I' && s[l] == 'V'){
                return 4 + number(s, l-2);
            }
    else if(s[l-1] == 'I' && s[l] == 'X'){
                return 9 + number(s, l-2);
            }
    else if(s[l-1] == 'X' && s[l] == 'L'){
                return 40 + number(s, l-2);
            }
    else if(s[l-1] == 'X' && s[l] == 'C'){
                return 90 + number(s, l-2);
            }
    else if(s[l - 1] == 'C' && s[l] == 'D'){
                return 400 + number(s, l-2);
            }
    else if(s[l - 1] == 'C' && s[l] == 'M'){
                return 900 + number(s, l - 2);
    }
    else if(s[l] == 'I') return 1 + number(s, l-1);
    else if(s[l] == 'V') return 5 + number(s, l-1);   
    else if(s[l] == 'X') return 10 + number(s, l-1);
    else if(s[l] == 'L') return 50 + number(s, l-1);
    else if(s[l] == 'C') return 100 + number(s, l-1);
    else if(s[l] == 'D') return 500 + number(s, l-1);
    else if(s[l] == 'M') return 1000 + number(s, l-1);
    return 0;
  }
};