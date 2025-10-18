class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)

        for char in word:
            count[char] -= 1
            if count[char]==0:
                del count[char]
            if len(set(count.values())) ==1:
                return True
            count[char] +=1

        return False