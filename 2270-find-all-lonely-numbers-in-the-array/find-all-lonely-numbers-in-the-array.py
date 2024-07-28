class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        seen = { }

        '''
        seen set should look like:
        value -> it and its neigbours occurences
        '''

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1

            else:
                seen[nums[i]] += 1

            if (nums[i] + 1) in seen:
                seen[nums[i]] += 1
                seen[nums[i] + 1] += 1

            if (nums[i] - 1) in seen:
                seen[nums[i]] += 1 
                seen[nums[i] - 1] += 1
                

        result = []
        for key,value in seen.items():
            if value == 1:
                result.append(key)

        return result

        