class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


        rows = { 

        }

        """
        row should look like:
        tuple(row) -> freq
        """

        for row in grid:
            if tuple(row) not in rows:
                rows[tuple(row)] = 1
            else:
                rows[tuple(row)] += 1
        ctr = 0

        for x in range (0,len(grid)):
            column = []
            for y in range (0,len(grid)):
                value = grid[y][x]
                column.append(value)

            if column in grid:
                ctr += rows[tuple(column)]



        return ctr
                

        