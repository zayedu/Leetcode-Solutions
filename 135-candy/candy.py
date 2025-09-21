class Solution:
    def candy(self, ratings: List[int]) -> int:
        n= len(ratings)
        candies = [1]*n

        for index in range(n):
            if index > 0 and ratings[index] > ratings[index-1]:
                candies[index] = candies[index-1]+1

        for index in range(n-1,-1,-1):
            if index < n-1 and ratings[index] > ratings[index+1] :
                candies[index] = max(candies[index+1]+1,candies[index])

        return sum(candies)