class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0:
            return 0

        if n == 0:
            return 1

        def shrink(val,exp):
            if exp == 1:
                return val

            if exp == 0:
                return 1

            res = shrink(val,exp//2)

            if exp%2 ==0:
                return res*res

            return res*res*val

        val = shrink(x,abs(n))

        if n < 0:
            return 1/val

        return val

            