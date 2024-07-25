class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)

        for match in matches:
            losses[match[0]] += 0
            losses[match[1]] += 1


        no_losses = [key for key, value in losses.items() if value == 0]
        one_loss = [key for key, value in losses.items() if value == 1]
        return[sorted(no_losses),sorted(one_loss)]