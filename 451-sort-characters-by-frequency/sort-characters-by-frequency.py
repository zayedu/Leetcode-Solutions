class Solution:
    def frequencySort(self, s: str) -> str:
        seen = {

        }
        
        for char in s:
            if char not in seen:
                seen[char] = 1

            else:
                seen[char] += 1

        items = list(seen.items())

        items.sort(reverse = True, key = lambda x:x[1])


        print(items)
        result = ""
        for char in items:
            result += (char[0]*char[1])

        return result
