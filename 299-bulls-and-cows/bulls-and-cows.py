class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        chars = Counter(list(secret))

        bulls = 0
        cows = 0

        for index in range(len(guess)):
            
            if secret[index] == guess[index]:
                bulls += 1
                chars[guess[index]] -= 1
            
        for index in range(len(guess)):
            if secret[index] != guess[index] and guess[index] in chars and chars[guess[index]]>0:
                cows += 1
                chars[guess[index]] -= 1
            

        return f'{bulls}A{cows}B'

        """
        cows = 1
        bulls = 1
        counter = {
            1: 1,
            2: 1
        }
        "1122"
         
        "1222"
           ^
        """