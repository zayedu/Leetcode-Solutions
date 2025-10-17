class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        sentences = []
        sentence = []

        def backtrack(index):

            if index == len(s):
                sentences.append(' '.join(sentence))
                return
            
            for j in range(index,len(s)):
                if s[index:j+1] in wordDict:
                    sentence.append(s[index:j+1])
                    backtrack(j+1)
                    sentence.pop()


        backtrack(0)
        return sentences

        