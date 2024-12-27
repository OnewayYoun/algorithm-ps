from collections import deque
from typing import List


class Solution:
    """
    Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
    Output: 1

    Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    Output: 2
    """

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        dq = deque([[startGene, 0]])
        visited = {startGene}

        while dq:
            cur_gen, cnt = dq.popleft()
            if cur_gen == endGene:
                return cnt
            for gen_str in 'ACGT':
                for i in range(len(cur_gen)):
                    if cur_gen[i] == gen_str:
                        continue
                    new_gen = cur_gen[:i] + gen_str + cur_gen[i + 1:]
                    if new_gen in bank and new_gen not in visited:
                        visited.add(new_gen)
                        dq.append([new_gen, cnt + 1])
        return -1


print(Solution().minMutation(startGene="AAAAAAAA", endGene="CCCCCCCC",
                             bank=["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC", "ACCACCCC",
                                   "ACCCCCCC", "CCCCCCCA"]))
