class Solution:
    def countSubstrings(self, s: str) -> int:
        max_cnt = 0

        def _is_palindrome(l, r):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1
            return cnt
    
        for i in range(len(s)):
            max_cnt += _is_palindrome(i, i) + _is_palindrome(i, i + 1)
        
        return max_cnt