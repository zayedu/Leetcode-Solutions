import math
class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        
        def _check(guess) -> bool:
            count = 0
            for num in nums:
                res = num -y*guess 
                if res < 0:
                    continue
                
                count += math.ceil(res/(x-y))
            return count <= guess

        # binary search
        l,r = 0, 10**9
        result = 0

        while l <= r:
            mid = (l+r)//2

            if _check(mid):
                r = mid - 1
                result = mid
            else:
                l = mid+1

        return result