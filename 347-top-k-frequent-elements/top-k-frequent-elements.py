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

        items = list(freq.items())

        items.sort(key = lambda x:x[1], reverse = True)

        ans = []
        
        for index in range(k):
            ans.append(items[index][0])


        return ans
