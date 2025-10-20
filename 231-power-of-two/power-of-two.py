class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n = float(n)
        if n == 1:
            return True

        if n==0 or not n.is_integer():
            return False

        return self.isPowerOfTwo(n/2)
