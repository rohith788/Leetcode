class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
          return []
        arr = []      
        l, r, u, d = 0, len(matrix[0]) - 1, 0, len(matrix) - 1 
        while( l <=r and u <= d):
          for i in range(l, r + 1):
            arr.append(matrix[u][i])
            
          for i in range(u + 1, d ):
            print(d)
            arr.append(matrix[i][r])
            
          for i in range(r, l - 1, -1 ):
            arr.append(matrix[d][i])
            
          for i in range(d - 1, u, -1):
            arr.append(matrix[i][l])
            
          l, r, u, d = l + 1, r - 1, u + 1, d - 1
          
        return arr[:len(matrix[0]) * len(matrix)]