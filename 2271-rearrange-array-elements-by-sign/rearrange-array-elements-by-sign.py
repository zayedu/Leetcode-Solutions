class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]

        ans = []
        pos_idx = 0
        neg_idx = 0


        for i in range(len(nums)//2):
            ans.append(pos[pos_idx])
            ans.append(neg[neg_idx])
            pos_idx+=1
            neg_idx+=1

        return ans
