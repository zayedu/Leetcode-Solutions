from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh = 0
        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row,col))
        
        minutes = 0
        if fresh == 0:
            return minutes
        while queue:
            
            if fresh == 0:
                return minutes

            breadth_size = len(queue)

            for _ in range(breadth_size):
                row, col = queue.popleft()

                if not(row - 1 < 0 or grid[row-1][col] != 1):
                    grid[row-1][col] = 2
                    fresh -= 1
                    queue.append((row-1,col))
                
                if not(row + 1 >= len(grid) or grid[row+1][col] != 1):
                    grid[row+1][col] = 2
                    fresh -= 1
                    queue.append((row+1,col))
                
                if not(col - 1 < 0 or grid[row][col-1] != 1):
                    grid[row][col-1] = 2
                    fresh -= 1
                    queue.append((row,col-1))

                if not(col + 1 >= len(grid[0]) or grid[row][col+1] != 1):
                    grid[row][col+1] = 2
                    fresh -= 1
                    queue.append((row,col+1))

            minutes += 1
                      
        return -1