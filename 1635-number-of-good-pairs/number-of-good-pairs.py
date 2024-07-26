class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = { }
        '''
        seen map should look like val - > [idx's]
        '''
        ctr = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = [i]

            else:
                idxs = seen[nums[i]]
                for j in idxs:
                    if j < i:
                        ctr += 1
                seen[nums[i]].append(i)

        return ctr