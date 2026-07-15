class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0

        def _is_palindrome(l, r):
            nonlocal cnt
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                    cnt += 1
    
        for i in range(len(s)):
            _is_palindrome(i, i)
            _is_palindrome(i, i + 1)
        
        return cnt