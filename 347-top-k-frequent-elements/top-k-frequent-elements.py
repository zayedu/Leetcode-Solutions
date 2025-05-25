class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq= {

        }
        '''
        freq should look like:
            num -> freq
        '''

        for num in nums:
            if num not in freq:
                freq[num] = 1

            else:
                freq[num] += 1

        
        items = list(freq.items())
        items.sort(reverse = True, key = lambda x:x[1])
        result = []
        for count in range(k):
            result.append(items[count][0])

        return result


