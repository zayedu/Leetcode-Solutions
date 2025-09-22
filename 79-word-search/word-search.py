class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        seen = set()

        def dfs(row,col,k):
            if row < 0 or row > len(board)-1 or col < 0 or col >len(board[0])-1 or (row,col) in seen or word[k] != board[row][col]:
                return False

            
            if k == len(word)-1:
                return True

            seen.add((row,col))

            possible = dfs(row+1,col,k+1) or dfs(row-1,col,k+1) or dfs(row,col+1,k+1) or dfs(row,col-1,k+1)

            seen.remove((row,col))
            return possible
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row,col,0):
                        return True

        return False


                

        

