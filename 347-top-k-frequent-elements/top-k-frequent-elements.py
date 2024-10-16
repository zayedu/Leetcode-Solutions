class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = {

        }

        """
        freq should look like:
        num -> freq
        """

        for i in nums:
            if i not in freq:
                freq[i] = 1

            else:
                freq[i] += 1


        freq_pairs = freq.items()

        """
        [(2,2),(1,3),(3,1)]
        """
        freq_pairs.sort(reverse = True, key = lambda x:x[1])
        result = []
        for idx in range(k):
            result.append(freq_pairs[idx][0])

        return result
        