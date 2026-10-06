class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        visited = set()
        answer = 0

        def dfs(start, cnt):
            nonlocal answer

            if start in visited:
                answer = max(answer, cnt)
                return

            visited.add(start)
            dfs(nums[start], cnt + 1)


        for i in range(len(nums)):
            if i not in visited:
                dfs(i, 0)

        return answer

    def arrayNesting_optimized(self, nums: list[int]) -> int:
        visited = [False] * len(nums)
        answer = 0

        def dfs(start):
            if visited[start]:
                return 0

            visited[start] = True
            return 1 + dfs(nums[start])

        for i in range(len(nums)):
            if not visited[i]:
                answer = max(answer, dfs(i))

        return answer


print(Solution().arrayNesting(nums=[5, 4, 0, 3, 1, 6, 2]))
