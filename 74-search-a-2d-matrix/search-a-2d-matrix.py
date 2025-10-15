class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Convert 1D index to 2D coordinates
            mid_val = matrix[mid // n][mid % n]
            
            if mid_val == target:
                return True
            elif target > mid_val:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
        