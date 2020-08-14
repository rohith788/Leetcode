class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(mat, r, c):
            len_r = len(mat)
            len_c = len(mat[0])
            
            if r < 0 or c < 0 or r >= len_r or c >= len_c or mat[r][c] != "1" :
                # print(r,c,r < 0,c < 0 , r >= len_r , c >= len_c , mat[r][c] != 1 , mat[r][c], "rpw")
                return
            
            mat[r][c] = "0"
            dfs(mat, r - 1, c)
            dfs(mat, r + 1, c)
            dfs(mat, r, c - 1)
            dfs(mat, r, c + 1) 
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                #     dfs(grid, i , j)
                    count += 1
                    stack = [(i,j)]
                    for r,c in stack:
                        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                            grid[r][c] = 0
                            stack.extend([(r+1,c),(r-1,c),(r,c+1),(r,c-1)])

                    
        return count
                    