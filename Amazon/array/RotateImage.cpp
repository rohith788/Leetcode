class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
      int m = matrix.size();
      for(int i = 0; i < (m + 1) / 2; i++){
        for(int j = 0; j < m / 2; j++){
          int temp = matrix[m - 1 - j][i];
          matrix[m - 1 - j][i] = matrix[m - i - 1][m - j - 1];
          matrix[m - 1 - i][m - j - 1] = matrix[j][m - 1 - i];
          matrix[j][m - 1 - i] = matrix[i][j];
          matrix[i][j] = temp;
        }
      }
    }
};

