class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        nums = self.nums
        l,r = 0,len(nums) - 1

        l_val = 0
        r_val = sum(nums)
        while l < left:
            l_val += nums[l]
            l += 1

        while r > right:
            r_val -= nums[r]
            r -= 1

        return r_val - l_val
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)