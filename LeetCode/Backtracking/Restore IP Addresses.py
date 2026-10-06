class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        answer = []

        def dfs(start, path):
            if len(path) == 4:
                if start == len(s):
                    answer.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                if len(part) > 1 and part[0] == "0":
                    break

                if int(part) > 255:
                    break

                path.append(part)
                dfs(start + length, path)
                path.pop()

        dfs(0, [])

        return answer


print(Solution().restoreIpAddresses(s="101023"))
