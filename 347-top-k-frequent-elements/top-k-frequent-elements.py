class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        seen = defaultdict(int)

        '''
        Seen should look like vals -> occurences
        '''
        for i in nums:
            seen[i] += 1
        result = [ ]
        keys = sorted(seen.items(),reverse=True, key = lambda x:x[1])
        print(keys)
        for i in range(k):
            result.append(keys[i][0])
        return result