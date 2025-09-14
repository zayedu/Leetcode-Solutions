class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q = [[]]   
        for i in nums:
            temp = []
            for t in q:   
                temp.append(t)         
                temp.append(t + [i])   
            q = temp   
        return q