class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        l = 0

        r = 0
        while word[r] != ch:
            r += 1
            if r == len(word):
                return word
        word_list = list(word)
        while l <= r :
            word_list[l],word_list[r] = word_list[r],word_list[l]
            l += 1
            r -=1

        return ''.join(word_list)
