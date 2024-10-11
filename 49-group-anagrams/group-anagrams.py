class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {

        }

        """
        anagrams should look like:
        tuple(Counter(word)) -> (word1,word2,...,word_n)
        """

        for word in strs:
            chars = [0]*26
            for char in word:
                chars[(ord(char)-ord('a'))] += 1
            chars = tuple(chars)
            if chars not in anagrams:
                anagrams[chars] = [word]

            else:
                anagrams[chars].append(word)

        return anagrams.values()

        """
        Complexity
        Time: O(n)
        Space: O(n)
        """