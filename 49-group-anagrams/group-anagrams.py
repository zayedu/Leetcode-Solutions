class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {

        }
        '''
        tuple_id -> anagrams
        '''
        for word in strs:
            word_list = [0]*26

            for s in word:

                word_list[ord(s)-ord('a')] += 1

            tuple_id = tuple(word_list)

            if tuple_id not in anagrams:
                anagrams[tuple_id] = [word]
            else:
                anagrams[tuple_id].append(word)

        return list(anagrams.values())