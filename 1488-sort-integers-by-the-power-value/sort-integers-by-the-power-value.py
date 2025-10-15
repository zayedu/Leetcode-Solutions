class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {}
        def getPower(num,power):

            if num == 1:
                return power

            if num %2==0:
                return getPower(num//2,power+1)
            
            return getPower(3*num+1,power+1)

        num_power = defaultdict(int)

        '''
        num_power should look like int -> power
        '''

        for num in range(lo,hi+1):
            num_power[num] = getPower(num,0)

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

        
            
