class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = [ ]
        for char in s:
            nums.append(str(ord(char)-ord('a') + 1))

        nums = list("".join(nums))
        count = 0

        while count < k:
            print(nums)
            num = sum(int(d) for d in nums)
            print(num)
            nums = list(str(num))

            count += 1

        return num