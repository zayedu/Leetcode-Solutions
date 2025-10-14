from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()

        l = 0
        ans = []
        for r in range(len(nums)):
            
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            while queue[0] < l:
                queue.popleft()

            if r < k-1:
                continue

            ans.append(nums[queue[0]])
            l+=1


        return ans