class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        kid,cookie = 0,0
        ans = 0
        while kid < len(g) and cookie < len(s):
            k_size = g[kid]
            c_size = s[cookie]

            if c_size >= k_size:
                ans += 1
                kid += 1
                cookie += 1
            else:
                cookie += 1

        return ans
