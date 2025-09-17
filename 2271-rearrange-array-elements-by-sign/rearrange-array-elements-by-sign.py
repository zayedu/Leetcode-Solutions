class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = [v for v in nums if v > 0]
        neg = [v for v in nums if v < 0]
        ans = []
        i=0
        while i < len(pos):
            ans.append(pos[i])
            ans.append(neg[i])
            i+=1

        return ans
