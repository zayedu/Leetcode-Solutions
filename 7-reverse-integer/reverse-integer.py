class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        ans = ''
        flip = False
        for idx in range(len(x_str)-1,-1,-1):
            char =x_str[idx]
            if char.isdigit():
                ans+=char

            if char == '-':
                flip = True

        ans = int(ans)
        if flip:
            ans *= -1
        if ans > 2**31 - 1 or ans < -1*2**31:
            return 0
        return ans