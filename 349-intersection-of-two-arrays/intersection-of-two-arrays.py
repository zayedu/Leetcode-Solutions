class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2= set(nums2)


        
        set_to_use = set()

        if len(nums1) < len(nums2):
            set_to_use = nums1
        else:
            set_to_use = nums2
        ans = set()
        
        for num in set_to_use:
            if num in nums2 and num in nums1:
                ans.add(num)

        return list(ans)