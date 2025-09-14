class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        ans = [ ]
        words = [ ]
        def dfs(i):
            if i >= len(s):                
                ans.append(" ".join(words))
                return

            
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict:
                    
                    words.append(s[i:j+1])
                    dfs(j+1)
                    words.pop()


        dfs(0)

        return ans

                    

