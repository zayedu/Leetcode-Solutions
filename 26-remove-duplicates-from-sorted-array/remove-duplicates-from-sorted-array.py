class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert = 0
        index = 0

        while index < len(nums):
            count = 1
            
            while index + count < len(nums) and nums[index+count]== nums[index]:
                count+=1

            nums[insert] = nums[index]

            insert+=1
            if index + count < len(nums):
                nums[insert] = nums[index+count]

            index += count


        return insert
            
