class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        length = len(s)
        wordDict = set(wordDict)
        sentences = [ ]
        
        sentence = [ ]

        def backtrack(left_index):

            if left_index == len(s):
                sentences.append(" ".join(sentence))
                return

            for right_index in range(left_index,length):
                if s[left_index:right_index+1] in wordDict:
                    sentence.append(s[left_index:right_index+1])
                    backtrack(right_index+1)
                    sentence.pop()
            
        backtrack(0)

        return sentences

