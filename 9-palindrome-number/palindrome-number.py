class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False


        temp = x

        reversed_num = 0

        while temp:

            digit = temp%10

            reversed_num = reversed_num*10 + digit

            temp = temp //10

        return reversed_num == x