class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                print(row, col)
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    count += 1
        return count
        
        
    def dfs(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
            return False
        grid[r][c] = "0"
        self.dfs(grid,r+1,c)
        self.dfs(grid,r-1,c)
        self.dfs(grid,r,c+1)
        self.dfs(grid,r,c-1)
        return True