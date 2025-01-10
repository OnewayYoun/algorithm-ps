from typing import List


class Solution:
    """
    Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3

    Input: gas = [2,3,4], cost = [3,4,3]
    Output: -1
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(total) < 0:
            return -1
        answer = 0
        cur_sum = 0

        for idx, val in enumerate(total):
            cur_sum += val
            if cur_sum < 0:
                answer = idx + 1
                cur_sum = 0
        return answer


print(Solution().canCompleteCircuit(gas=[3, 1, 1], cost=[1, 2, 2]))
print(Solution().canCompleteCircuit(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1]))
print(Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
print(Solution().canCompleteCircuit(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1]))
