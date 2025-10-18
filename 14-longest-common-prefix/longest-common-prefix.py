class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        longest_prefix = strs[0]

        for word in strs:

            index = 0
            new_pref = ''
            while index< min(len(word),len(longest_prefix)) and word[index] == longest_prefix[index]:
                
                new_pref += longest_prefix[index]
                index += 1

            longest_prefix = new_pref

        return longest_prefix

            

