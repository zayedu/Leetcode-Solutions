class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        
        result = [[0]*n for i in range(m)]
        for i in range(m): 
            for j in range(k): 
                if mat1[i][j] != 0:
                    for p in range(n): 
                        if mat2[j][p] != 0:
                            result[i][p] += mat1[i][j] * mat2[j][p]
    
        return result