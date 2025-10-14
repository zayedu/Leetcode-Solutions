class NumMatrix:
    def row_prefix_sum(self,row):
        ans = []
        pref_sum = 0
        for num in row:
            pref_sum += num
            ans.append(pref_sum)

        return ans

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_matrix = []

        for row in self.matrix:
            self.prefix_matrix.append(self.row_prefix_sum(row))


    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val

        self.prefix_matrix[row] = self.row_prefix_sum(self.matrix[row])
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_region = 0

        for row in range(row1,row2+1):
            sum_region += self.prefix_matrix[row][col2] - (self.prefix_matrix[row][col1-1] if col1 > 0 else 0)
            
        return sum_region


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)