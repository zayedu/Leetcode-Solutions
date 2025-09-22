class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sum_squares(n)
            if n == 1:
                return True

        return False


    def sum_squares(self,n):
        n_list = list(str(n))
        ans = 0
        for num in n_list:
            ans+= int(num)**2

        return ans