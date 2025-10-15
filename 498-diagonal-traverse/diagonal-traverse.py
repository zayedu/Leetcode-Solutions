class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        row,col=0,0
        ans = []
        
        going_up = True
        while len(ans) < rows*cols:

            if going_up:
                
                while row >=0 and col < len(mat[0]):

                    ans.append(mat[row][col])
                    row-= 1
                    col+= 1

                if col >= len(mat[0]) :
                    col -= 1
                    row+=1

                row+=1

                going_up = False
            
            else:
                while row < len(mat) and col>=0:
                    ans.append(mat[row][col])
                    row+=1
                    col-=1

                if row >=len(mat):
                    row -= 1
                    col+=1
                col +=1

                going_up = True

        return ans



