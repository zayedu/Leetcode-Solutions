class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        result = []
        for i in range(0,len(words)):
            l,r = 0,len(words[i])-1
            reversed_word = list(words[i])
            while l <= r:
                temp = reversed_word[l]
                reversed_word[l] = reversed_word[r]
                reversed_word[r]= temp
                l += 1
                r -= 1
            result.append(''.join(reversed_word))

        return ' '.join(result)