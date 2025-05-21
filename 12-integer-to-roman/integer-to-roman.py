class Solution:
    def intToRoman(self, num: int) -> str:

        roman_to_int = {
             1 : 'I',
             5 : 'V',
             10 : 'X',
             50 : 'L',
             100 : 'C',
             500 : 'D',
             1000 : 'M'
             }
        def num_to_roman(num:int)->str:
            num = str(num)
            if num[0] == '5':
                order = 10**(len(num)-1)
                return roman_to_int[5*order]
            if num[0] == '4':
                order = 10**(len(num)-1)
                higher = 5*order
                return roman_to_int[order] + roman_to_int[higher]

            
            if num[0] == '9':
                order = 10**(len(num)-1)
                higher = 10*order
                return roman_to_int[order] + roman_to_int[higher]
            
            order = 10**(len(num)-1)
            return roman_to_int[order] * int(num[0])


        num_str = str(num)
        nums_to_add = []
        exp = len(num_str)-1
        
        result = ''
    
        for char in num_str:
            num_to_add=(int(char) * 10**exp)

            if int(str(num_to_add)[0]) in range(5,9) :
                difference = 5*10**exp
                num_to_add -= difference
                nums_to_add.append(difference)

            nums_to_add.append(num_to_add)
            exp -= 1
        print(nums_to_add)    
        for i in nums_to_add:
            result += num_to_roman(i)

        return result

    