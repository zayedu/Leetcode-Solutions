class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        seen = { }
        
        '''
        seen should look like:
        val -> occorunces
        '''
        counter = 0
        for i in nums:
            if i not in seen:
                seen[i] = 1

            else:
                seen[i] += 1

        
        for k,v in seen.items():
            if v == 1:
                counter += k

        return counter
                

