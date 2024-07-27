class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        available_chars = {
            'b' : 0,
            'a' : 0,
            'l' : 0,
            'o' : 0,
            'n' : 0
        }

        '''
        available_chars should look like:
        char -> frequency
        '''

        for char in text:
            if char in available_chars:
                available_chars[char] += 1

            
        '''
        {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        '''
        max_possible = len(text)
        for char, freq in available_chars.items():
            if char == 'l' or char == 'o':
                max_possible = min(max_possible,freq//2)
            else:
                max_possible = min(max_possible,freq)

            
        return max_possible