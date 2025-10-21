class Solution:

    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            mp = {}
            for j in range(i, n):
                mp[s[j]] = mp.get(s[j], 0) + 1
                if min(mp.values())==max(mp.values()):
                    l = j - i + 1
                    ans = max(ans, l)
        return ans