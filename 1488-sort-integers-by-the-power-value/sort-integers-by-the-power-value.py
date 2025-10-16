class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}

        def getPower(num: int) -> int:
            if num in memo:
                return memo[num]

            if num % 2 == 0:
                memo[num] = 1 + getPower(num // 2)
            else:
                memo[num] = 1 + getPower(3 * num + 1)

            return memo[num]

        num_power = defaultdict(int)

        '''
        num_power should look like int -> power
        '''

        for num in range(lo,hi+1):
            num_power[num] = getPower(num)

        ans = [[] for _ in range(max(num_power.values())+1)]

        for num, power in num_power.items():
            ans[power].append(num)

        count = 0

        for index in range(len(ans)):
            if not ans[index]:
                continue

            if count + len(ans[index]) >= k:
                vals = sorted(ans[index])

                return vals[k-count-1]

            count += len(ans[index])

        
            
