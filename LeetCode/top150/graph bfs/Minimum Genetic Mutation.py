from typing import List
from collections import deque


class Solution:
    """
    Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
    Output: 1

    Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    Output: 2
    """

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        cnt = 0
        for i in range(len(startGene)):
            if startGene[i] != endGene[i]:
                cnt += 1
        return cnt

    def minMutation1(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        genes = ['A', 'C', 'G', 'T']
        dq = deque()
        dq.append([startGene, 0])
        visited = set()

        while dq:
            cur_gen, step = dq.popleft()
            for i in range(8):
                for gene in genes:
                    new_gen = cur_gen[:i] + gene + cur_gen[i + 1:]
                    if new_gen in bank and new_gen == endGene:
                        return step + 1
                    if new_gen not in visited and new_gen in bank:
                        dq.append([new_gen, step + 1])
                        visited.add(new_gen)
        return -1


# print(Solution().minMutation(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"]))
print(Solution().minMutation1(startGene="AACCTTGG", endGene="AATTCCGG",
                              bank=["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"]))
