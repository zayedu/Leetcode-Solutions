class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)

        for match in matches:
            losses[match[0]] += 0
            losses[match[1]] += 1

        no_losses = [ ]
        one_loss= [ ]

        for k,v in losses.items():
            if v == 0:
                no_losses.append(k)
            elif v == 1:
                one_loss.append(k)

        return[sorted(no_losses),sorted(one_loss)]