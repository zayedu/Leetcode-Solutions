class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {

        }

        '''
        anagrams should look like:
            anagram_tuple:() -> [words]

        '''


        for word in strs:
            char_count = [0] * 26

            for char in word:
                char_count[ord(char)-ord('a')] += 1

            tupled = tuple(char_count)

            if tupled not in anagrams:
                anagrams[tupled] = [word]
            else:
                anagrams[tupled].append(word)

        return list(anagrams.values()) 
        
        '''
        Complexity:
            Time: O(n*k)
            Memory: O(n*k)
        '''