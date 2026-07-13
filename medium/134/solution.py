class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1

        tmp = 0
        idx = 0

        for i in range(len(gas)):
            if tmp < 0:
                tmp = 0
                idx = i
            tmp += gas[i] - cost[i]

        return idx