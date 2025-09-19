class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        ans = []

        def dfs(num):
            if len(num) == n:
                ans.append(int(num))
                return
            
            last = int(num[-1])

            if last + k < 10:
                num_u = num + str(last + k)
                dfs(num_u)


            if k != 0 and last - k >= 0:
                num_l = num + str(last - k)
                dfs(num_l)
        

        for num in range(1, 10):
            dfs(str(num))

        return ans
