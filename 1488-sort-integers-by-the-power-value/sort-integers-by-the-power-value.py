class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
        12 -> 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1: power = 9
        13 -> 40 -> 20 -> 10: power = 9
        14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13: 8 + 9 = 17
        15 -> 46 -> 23 -> 70 -> 35 -> 106 -> 53 -> 160 -> 80 -> 40 -> 20 -> 10: 17

        cache = {
            
        }

        power(x):
            if x == 1:
                return 0
            if x in cache:
                return cache[x]
            if x % 2 == 0:
                return 1 + fun(x // 2)
            return 1 + fun(x * 3 + 1)
        """

        # 1 + power(6) = 2 + power(3)
        cache = {}

        def power(x: int):
            if x == 1:
                return 0
            if x in cache:
                return cache[x]
            if x % 2 == 0:
                tmp = 1 + power(x // 2)
                cache[x] = tmp
                return tmp
            tmp = 1 + power(x * 3 + 1)
            cache[x] = tmp
            return tmp

        arr = [i for i in range(lo, hi + 1)]
        # [12, 13, 14, 15]
        arr.sort(key=lambda x: (power(x), x))
        print(arr)

        return arr[k - 1]