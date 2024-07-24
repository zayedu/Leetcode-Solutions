class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        max_len = 0

        cnt = 0
        my_len = 0
        for r in range (len(s)):
            if cnt > maxCost:
                if s[l] != t[l]:
                    cnt -= abs((ord(s[l])-ord(t[l])))
                l += 1
            if s[r] != t[r]:
                cnt += abs((ord(s[r]) - ord(t[r])))
            my_len = r - l +1
            if cnt <= maxCost:
                max_len = max(my_len,max_len)
            
        return max_len
        