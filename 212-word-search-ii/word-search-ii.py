class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self,word):
        curr  = self

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for word in words:
            root.addWord(word)

        words = set()
        seen = set() # (row,col)
        word = []

        def dfs(row,col,node):

            if node.isWord:

                words.add(''.join(word.copy()))
                node.isWord = False
                
            
            out_of_bounds = row < 0 or row == len(board) or col < 0 or col == len(board[0])

            if out_of_bounds or (row,col) in seen or board[row][col] not in node.children:
                return


            node = node.children[board[row][col]]

            word.append(board[row][col])
            seen.add((row,col))

            dfs(row+1,col,node)
            dfs(row-1,col,node)
            dfs(row,col+1,node)
            dfs(row,col-1,node)

            seen.remove((row,col))
            word.pop()

            return

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in root.children:
                    dfs(row,col,root)

        return list(words)