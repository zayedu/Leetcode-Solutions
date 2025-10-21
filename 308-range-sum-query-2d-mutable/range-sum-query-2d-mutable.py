class NumMatrix:
    def compute_prefix(self,nums):
        prefix = 0
        pref = []
        for num in nums:
            prefix+=num
            pref.append(prefix)
        return pref


    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_matrix = [self.compute_prefix(row) for row in self.matrix]

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        self.prefix_matrix[row] = self.compute_prefix(self.matrix[row])
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_sum = 0
        
        for row in range(row1,row2+1):
            region_sum += self.prefix_matrix[row][col2] - (self.prefix_matrix[row][col1-1] if col1 > 0 else 0)

        return region_sum

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)