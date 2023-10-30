class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        dror1 = list(arr)
        dror1.sort(key=lambda x: (bin(x).count('1'), x))
        return dror1