class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        flip = -1

        ans = 1

        t =0

        while t < time:

            if ans >=n or ans == 1:
                flip = flip*-1
            
            ans += flip
            t += 1

        return ans

            # ans = 3
            # [1,2,3,4]
            #           t