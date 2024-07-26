class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        seen = {}
        ctr = 0

        # Count occurrences of rows
        for row in grid:
            row_tuple = tuple(row)
            seen[row_tuple] = seen.get(row_tuple, 0) + 1

        # Check columns against rows
        for j in range(len(grid)):
            col = tuple(grid[i][j] for i in range(len(grid)))
            if col in seen:
                ctr += seen[col]

        return ctr