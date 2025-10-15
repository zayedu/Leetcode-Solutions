class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def getPower(num,power):
            if num == 1:
                return power

            if num %2==0:
                return getPower(num/2,power+1)
            
            return getPower(3*num+1,power+1)
        num_power = defaultdict(int)

        '''
        num_power should look like int -> power
        '''

        for num in range(lo,hi+1):
            num_power[num] = getPower(num,0)

        items = list(num_power.items())
        items.sort(key= lambda x:x[1])

        return items[k-1][0]
            
