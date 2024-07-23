class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i,j = 0,0
        while nums1[i] != nums2[j]:
            if nums2[j] > nums1[i]:
                i += 1
            else:
                j += 1

            if i >= len(nums1) or j >= len(nums2):
                return -1
        return nums1[i]