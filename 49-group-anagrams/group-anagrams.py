class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {

        }

        """
        anagrams should look like:
        tuple(Counter(word)) -> (word1,word2,...,word_n)
        """

        for word in strs:

            if tuple(sorted(word)) not in anagrams:
                anagrams[tuple(sorted(word))] = [word]

            else:
                anagrams[tuple(sorted(word))].append(word)

        return anagrams.values()

        """
        Complexity
        Time: O(n)
        Space: O(n)
        """