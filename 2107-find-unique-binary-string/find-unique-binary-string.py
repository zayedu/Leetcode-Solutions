class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        index_to_chars={

        }
        n = len(nums)
        '''
        index_to_chars should look like
            index -> set(chars_at_that_index)
        '''

        for num in nums:
            for index in range(len(str(num))):
                
                if index not in index_to_chars:
                    index_to_chars[index] = set()

                index_to_chars[index].add(num[index])


        def dfs(index,binary):
            if index == n:
                if binary not in nums:
                    return binary

                else:
                    return False

            return dfs(index+1, binary+'1') or dfs(index+1, binary+'0')
            
        return dfs(0,'')