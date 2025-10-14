from collections import deque

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def anon_words(word):
            ans = []
            for index in range(len(word)):
                word_list = list(word)
                word_list[index] = '*'
                ans.append(''.join(word_list))

            return ans

        word_set = set(wordList)

        if endWord not in word_set:
            return 0 


        adj_list = defaultdict(list)

        for word in wordList:
            for anon_word in anon_words(word):
                adj_list[anon_word].append(word)


    #bfs
        seen = set()
        queue = deque([[beginWord,0]])

        while queue:
            
            word, steps = queue.popleft()

            if word == endWord:
                return steps +1


            a_words = anon_words(word)

            for anon_word in a_words:
                for edge in adj_list[anon_word]:
                    if edge not in seen:
                        seen.add(edge)
                        queue.append([edge,steps+1])

        return 0


