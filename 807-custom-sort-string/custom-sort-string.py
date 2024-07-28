class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Count occurrences of each character in s
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Build the result string
        result = []
        
        # Add characters from order
        for char in order:
            if char in char_count:
                result.append(char * char_count[char])
                del char_count[char]
        
        # Add remaining characters not in order
        for char, count in char_count.items():
            result.append(char * count)
        
        return ''.join(result)