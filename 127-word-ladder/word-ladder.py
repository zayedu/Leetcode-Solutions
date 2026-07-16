from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def _anon_words(word) -> list[str]:
            anon_words = []
            for index in range(len(word)):
                word_copy = list(word)
                word_copy[index] = '*'
                anon_words.append(''.join(word_copy))

            return anon_words

        adj_list = defaultdict(list)

        for word in wordList:
            for a_word in _anon_words(word):
                adj_list[a_word].append(word)


        queue = deque([(beginWord,1)])
        seen = set()

        while queue:
            word,count = queue.popleft()
            if word == endWord:
                return count
            a_words = _anon_words(word)

            for a_word in a_words:
                for w in adj_list[a_word]:
                    if w in seen:
                         continue
                    seen.add(w)
                    queue.append((w,count+1))
        return 0
