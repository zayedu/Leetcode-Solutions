class Solution:
    def frequencySort(self, s: str) -> str:
        seen = {

        }
        for c in s:
            if c not in seen:
                seen[c] = 1

            else:
                seen[c] += 1

        result = ""
        lis = list(seen.items())
        lis.sort(reverse = True, key = lambda x:x[1])
        for k,v in lis:
            result+=(k*v)


        return result