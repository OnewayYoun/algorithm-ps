from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        answer = -1
        lst = [gas[i] - cost[i] for i in range(len(gas))]
        for i in range(len(gas)):
            length = len(gas)
            cur = 0
            cnt = 0
            while cnt != length:
                if cur < 0:
                    break
                cur += lst[(i + cnt) % length]
                cnt += 1
                if cnt == length and cur >= 0:
                    return i

        return answer

    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        lst = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(lst) < 0:
            return -1

        cur_sum = 0
        answer = 0

        for i in range(len(gas)):
            cur_sum += lst[i]
            if cur_sum < 0:
                cur_sum = 0
                answer = i + 1

        return answer


# print(Solution().canCompleteCircuit1(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
print(Solution().canCompleteCircuit1(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
# print(Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
