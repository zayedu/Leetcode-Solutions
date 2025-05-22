class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman = {
            1 : 'I',
            4 : 'IV',
            5 : 'V',
            9 : 'IX',
            10 : 'X',
            40 : 'XL',
            50 : 'L',
            90 : 'XC',
            100 : 'C',
            400 : 'CD',
            500 : 'D',
            900 : 'CM',
            1000 : 'M',
        }

        result = ''
        for value,roman in reversed(int_to_roman.items()):
            div = int(num/value)
            result  += div*roman

            num = num%value
        return result