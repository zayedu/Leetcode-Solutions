from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        def anon_word(word):
            anon_words = []

            for index in range(len(word)):
                anon_word = list(word)
                anon_word[index] = '*'
                anon_words.append(''.join(anon_word))
            
            return anon_words
        
        word_matches = defaultdict(list)

        for word in wordList:
            for index in range(len(word)):
                word_anon = list(word)
                word_anon[index] = '*'
                word_matches["".join(word_anon)].append(word)


            
        queue = deque([[beginWord,0]])
        visited = set()
        while queue:

            word, moves = queue.popleft()
            if word == endWord:
                return moves+1

            anon_words = anon_word(word)

            for a_word in anon_words:
                for edge in word_matches[a_word]:
                    if edge in visited:
                        continue
                    visited.add(edge)
                    queue.append([edge,moves+1])
                    
                    
        return 0