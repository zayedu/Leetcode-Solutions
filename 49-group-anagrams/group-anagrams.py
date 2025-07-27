class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {
            
        }

        '''
        anagrams should look like:
            (representing count of each alpha char) - > [anagrams,...]
        '''

        for word in strs:
            word_list = [0]*26
            for char in word:
                word_list[ord(char)-ord('a')] += 1
            
            word_list = tuple(word_list)

            if word_list not in anagrams:
                anagrams[word_list] = [word]
            else:
                anagrams[word_list].append(word)

        return list(anagrams.values())
