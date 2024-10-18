class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {

        }

        """
        seen should look like:
        tuple([ordinals of each char]) -> [a1,a2,...,an]
        """

        for word in strs:
            identifier = [0]*26
            for char in word:
                identifier[ord(char)-ord('a')] += 1

            tupled_id = tuple(identifier)

            if tupled_id not in seen:
                seen[tupled_id] = [word]

            else:
                seen[tupled_id].append(word)

        
        return list(seen.values())

        """ 
        Complexity:
        Time: O(w) where w is the sum of the length of all words
        Space: O(s) where s is the length of strings

        """