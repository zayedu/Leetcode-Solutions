class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # T: O(log min(m, n)), S: O(1)
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Guarantees A is smaller of the two
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            A_i = (l + r) >> 1
            B_i = half - A_i - 2

            A_left = A[A_i] if A_i >= 0 else -inf
            A_right = A[A_i + 1] if A_i + 1 < len(A) else inf
            B_left = B[B_i] if B_i >= 0 else -inf
            B_right = B[B_i + 1] if B_i + 1 < len(B) else inf

            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                return min(A_right, B_right)
            elif A_left > B_right:
                r = A_i - 1
            else:
                l = A_i + 1