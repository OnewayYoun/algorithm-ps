from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(cur_str, num_open, num_close):
            if num_open < num_close or num_open > n:
                return

            if num_open == num_close == n:
                answer.append(cur_str)

            dfs(cur_str + '(', num_open + 1, num_close)
            dfs(cur_str + ')', num_open, num_close + 1)

        dfs('', 0, 0)

        return answer


if __name__ == "__main__":
    # Output: ["((()))","(()())","(())()","()(())","()()()"]
    print(Solution().generateParenthesis(n=3))



def dfs():
    if ~~~:
        pass

    if ~~~:
        pass

    append
    pop()_