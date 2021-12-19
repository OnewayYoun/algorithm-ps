class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        strs = sorted(strs, key=len)
        answer = ''
        for i in range(len(strs[0])):
            flag = False
            for j in range(1, len(strs)):
                if strs[j - 1][i] != strs[j][i]:
                    flag = True
            if flag:
                return answer
            else:
                answer += strs[0][i]

        return answer

    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0:
            return ''
        answer = ''
        min_pre = min(strs)
        max_pre = max(strs)
        for i, v in enumerate(min_pre):
            if v != max_pre[i]:
                return min_pre[:i]
        return min_pre




if __name__ == '__main__':
    strs = ["dog","racecar","car"]
    S = Solution()
    print(S.longestCommonPrefix(strs))
    print(S.lcp(strs))
