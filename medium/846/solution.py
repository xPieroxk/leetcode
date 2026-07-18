from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize != 0): return False
        if groupSize == 1: return True

        target_groups = len(hand) / groupSize
        current_groups = 0
        freq = defaultdict(list)

        for card in sorted(hand):
            if card - 1 not in freq:
                freq[card].append(1)
                current_groups += 1
                if current_groups > target_groups:
                    return False
            else:
                s = freq[card - 1].pop()
                if not len(freq[card - 1]):
                    del freq[card - 1]
                if s + 1 == groupSize:
                    continue
                freq[card].append(s + 1)

        return current_groups == target_groups

# using counter
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand)%groupSize != 0 ): return False
        count = Counter(hand)

        for card in sorted(count):
            if count[card]>0:
                need = count[card]
                for i in range(groupSize):
                    if count[card+i]< need:
                        return False
                    count[card+i]-=need
        return True