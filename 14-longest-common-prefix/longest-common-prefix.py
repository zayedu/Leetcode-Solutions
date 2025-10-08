class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_pre = strs[0]

        for word in strs:
            index = 0
            running_longest = ''
            n = min(len(longest_pre),len(word))
            while index < n and longest_pre[index] == word[index]:
                running_longest += word[index]
                index+=1

            longest_pre = running_longest

        return longest_pre