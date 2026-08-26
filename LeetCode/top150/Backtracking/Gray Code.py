from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        n = 2**n
        visited = [False] * n
        cur_lst = []
        flag = False

        def check(lst: List[int]):
            for i in range(1, len(lst)):
                if (lst[i]^lst[i-1]).bit_count() != 1:
                    return False
            if (lst[-1] ^ lst[0]).bit_count() != 1:
                return False
            return True

        def dfs():
            nonlocal flag
            if len(cur_lst) == n:
                if check(cur_lst):
                    flag = True
                return

            for i in range(n):
                if not visited[i]:
                    cur_lst.append(i)
                    visited[i] = True
                    dfs()
                    if flag:
                        return cur_lst
                    visited[i] = False
                    cur_lst.pop()
        dfs()
        return cur_lst


class Solution1:
    def grayCode(self, n: int) -> List[int]:
        n = 2**n
        visited = [False] * n
        cur_lst = []

        def dfs():
            if len(cur_lst) == n:
                return (cur_lst[-1] ^ cur_lst[0]).bit_count() == 1

            for i in range(n):
                if not visited[i]:
                    if cur_lst and (cur_lst[-1]^i).bit_count() != 1:
                        continue
                    cur_lst.append(i)
                    visited[i] = True
                    if dfs():
                        return cur_lst
                    visited[i] = False
                    cur_lst.pop()
        dfs()
        return cur_lst

    def grayCode1(self, n: int) -> List[int]:
        original_n = n
        n = 2**n
        visited = [False] * n
        cur_lst = [0]
        visited[0] = True

        def dfs():
            if len(cur_lst) == n:
                return (cur_lst[-1] ^ cur_lst[0]).bit_count() == 1

            for bit in range(original_n):
                i = cur_lst[-1] ^ (1 << bit)
                if not visited[i]:
                    cur_lst.append(i)
                    visited[i] = True
                    if dfs():
                        return cur_lst
                    visited[i] = False
                    cur_lst.pop()
        dfs()
        return cur_lst

# print(Solution().grayCode(n=2))
print(Solution1().grayCode1(n=2))