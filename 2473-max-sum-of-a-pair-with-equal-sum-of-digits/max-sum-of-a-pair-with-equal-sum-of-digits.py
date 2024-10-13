class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        seen = {

        }

        def getDigSum(num):
            str_num = str(num)
            ans = 0
            for c in str_num:
                ans += int(c)

            return ans


        """
        seen should look like:
        num_sum -> [nums]
        """        

        for i in nums:
            if getDigSum(i) not in seen:
                seen[getDigSum(i)] = [i]
            else:
                if len(seen[getDigSum(i)]) > 1:
                    #remove min value
                    if (min(seen[getDigSum(i)])) < i:
                        seen[getDigSum(i)].pop(seen[getDigSum(i)].index(min(seen[getDigSum(i)])))
                        seen[getDigSum(i)].append(i)

                else:
                    seen[getDigSum(i)].append(i)
        
        max_val = -1
        print(seen)
        for k,v in seen.items():
            if len(v) > 1:
                max_val = max(max_val,sum(v))


        return max_val