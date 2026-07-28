class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(row,col):
            if row <0 or row >=len(grid) or col<0 or col>=len(grid[row]) or grid[row][col]==0:
                return 0
            grid[row][col] = 0
            return dfs(row+1,col) + dfs(row-1,col) + dfs(row,col+1) + dfs(row,col-1) + 1

        max_count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    continue
                count = dfs(row,col)
                max_count = max(max_count,count)

        return max_count