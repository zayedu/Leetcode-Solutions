class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        freq = defaultdict(int)

        for char in nums:
            freq[char] += 1

        buckets= [[]for _ in range(len(nums)+1)]

        for num,count in freq.items():
            buckets[count].append(num)


       
        ans = []

        for i in range(len(nums),-1,-1):
            
            for num in buckets[i]:
                ans.append(num)

            if len(ans) ==k:
                return ans

        return ans