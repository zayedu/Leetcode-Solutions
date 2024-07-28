class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        seen = [ ]

        for i in range(len(paths)):
            seen.append(paths[i][0])

        for i in range(len(paths)):
            if paths[i][1] not in seen:
                return paths[i][1]


        