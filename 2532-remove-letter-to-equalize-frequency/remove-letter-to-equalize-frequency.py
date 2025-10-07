class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = defaultdict(int)

        for char in word:
            freq[char] += 1


        for char in list(freq):

            freq[char] -= 1
            if freq[char]==0:
                del freq[char]
            if len(set(freq.values())) == 1:
                return True

            freq[char] += 1

        return False