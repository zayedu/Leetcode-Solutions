class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {

        }

        '''
        anagrams should look like:
            tuple(chars_used) -> [anagrams,..]
        '''

        for word in strs:
            anagram = [0]*26

            for char in word:
                anagram[ord(char) - ord('a')] += 1

            tupled=tuple(anagram)

            if tupled not in anagrams:
                anagrams[tupled] = [word]
            else:
                anagrams[tupled].append(word)

        return list(anagrams.values())

            