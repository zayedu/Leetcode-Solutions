class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """

        position = {

        }

        minimum_distance = len(cards) + 1
        """
        position would look like:
        value -> position
        """

        for i in range(0,len(cards)):
            
            if cards[i] not in position:
                position[cards[i]] = i

            else:
                minimum_distance = min(minimum_distance, i - position[cards[i]] + 1)
                position[cards[i]] = i

        if minimum_distance == len(cards)+1:
            return -1

        return minimum_distance

        