from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def anon_words(word):
            words = []

            for index in range(len(word)):
                word_list = list(word)

                word_list[index] = '*'

                words.append(''.join(word_list))

            return words

        adj_list = defaultdict(list)

        for word in wordList:
            a_words = anon_words(word)

            for anon_word in a_words:
                adj_list[anon_word].append(word)

        queue = deque([[beginWord,1]])
        seen = set()
        while queue:

            word, steps = queue.popleft()

            if word == endWord:
                return steps

            a_words = anon_words(word)

            seen.add(word)

            for anon_word in a_words:
                for edge in adj_list[anon_word]:
                    if edge not in seen:
                        queue.append([edge,steps+1])
        return 0
