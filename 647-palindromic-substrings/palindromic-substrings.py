class Solution:
    def countSubstrings(self, s: str) -> int:
        max_count = 0

        def _is_palindrome(l,r):
            count = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        for index in range(len(s)):
            max_count += _is_palindrome(index,index) + _is_palindrome(index,index+1)

        return max_count
                