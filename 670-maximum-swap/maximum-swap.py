class Solution:
    def maximumSwap(self, num: int) -> int:
        
        arr_num = [int(val) for val in str(num)]

        max_val = arr_num[-1]
        max_idx = len(arr_num) - 1
        post_fixes = [0] * len(arr_num)
        for index in range(len(arr_num)-1,-1,-1):

            val = arr_num[index]
            if val > max_val:
                max_idx = index
                max_val = val

            post_fixes[index] = max_idx

        for index in range(len(arr_num)):
            if arr_num[index] < arr_num[post_fixes[index]]:
                temp = arr_num[index]

                arr_num[index] = arr_num[post_fixes[index]]
                arr_num[post_fixes[index]] = temp

                arr_str = [str(char) for char in arr_num]

                return int(''.join(arr_str))

        return num


