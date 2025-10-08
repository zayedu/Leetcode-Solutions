class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        def backtrack(level=1):
            if level == numRows+1:
                return
            row = []


            for i in range(level):
                if i == 0 or i == level-1:
                    row.append(1)

                else:
                    row.append(triangle[-1][i]+triangle[-1][i-1])

            triangle.append(row)
            backtrack(level+1)

            

        backtrack()
        return triangle