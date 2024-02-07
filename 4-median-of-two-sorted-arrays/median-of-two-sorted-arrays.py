class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Finds the median of two sorted arrays.
        :params:
            nums1 (List[int]): a sorted list of integer values
            nums2 (List[int]): a sorted list of integer values
        :returns:
            (int) median value of merged nums1 + nums2 array
        """

        # Binary Search
        # time:  O(log M + N)
        # space: O(1)
        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = b, a
        m, n = len(a), len(b)
        
        total = len(a) + len(b)
        half = total // 2

        left = 0
        right = len(a) - 1
        while True:
            i = left + (right - left) // 2
            j = half - i - 2

            a_left = a[i] if i >= 0 else -inf
            a_right = a[i+1] if i+1 < m else inf
            b_left = b[j] if j >= 0 else -inf
            b_right = b[j+1] if j+1 < n else inf

            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                return min(a_right, b_right)
            elif a_left > b_right:
                right = i - 1
            else:
                left = i + 1