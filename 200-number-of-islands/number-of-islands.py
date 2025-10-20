class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set() #(row,col)

        def dfs(row,col):

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0' or (row,col) in seen:
                return
            
            seen.add((row,col))
            grid[row][col]='0'

            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col-1)
            dfs(row,col+1)

            seen.remove((row,col))

        islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row,col)

        return islands