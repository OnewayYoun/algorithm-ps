import heapq
from collections import defaultdict
from typing import List


class Solution:
    """
    Input: nums = [100,4,200,1,3,2]
    Output: 4

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
    """

    # O(nlog(n))
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dd = defaultdict(int)
        nums.sort()

        for num in nums:
            dd[num] = 1 + dd[num - 1] + dd[num + 1]

        return max(dd.values())

    # O(nlog(n))
    def longestConsecutive2(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        answer = 1
        nums = list(set(nums))
        nums.sort()
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1

        return answer

    # O(n)
    def longestConsecutive3(self, nums: List[int]) -> int:
        nums_set = set(nums)
        answer = 0
        visited = set()
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            cnt = 0
            while (num + cnt) in nums_set:
                cnt += 1
                visited.add(num)
            answer = max(answer, cnt)
        return answer

    def longestConsecutive4(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        uf, nums_set = UF(nums), set(nums),
        for num in nums_set:
            if num + 1 in nums_set:
                uf.union(num, num + 1)
        dd = defaultdict(int)
        for num in nums_set:
            dd[uf.find(num)] += 1
        return max(dd.values())


class UF:
    def __init__(self, nums):
        self.parent = {n: n for n in nums}
        self.rank = {n: 0 for n in nums}

    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                self.parent[p2] = p1
                self.rank[p1] += 1


print(Solution().longestConsecutive4([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
