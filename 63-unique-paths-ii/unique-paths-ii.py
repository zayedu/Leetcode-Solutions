class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        seen = set() #(row,col)
        @lru_cache(maxsize=None)
        def dfs(row,col):

            if row < 0 or row == len(obstacleGrid) or col < 0 or col == len(obstacleGrid[0]) or obstacleGrid[row][col] or (row,col) in seen :
                return 0

            if row == len(obstacleGrid)-1 and col == len(obstacleGrid[0])-1:
                return 1
            seen.add((row,col))
            paths = dfs(row+1,col) + dfs(row,col+1)
            seen.remove((row,col))
            return paths
            
        return dfs(0,0)