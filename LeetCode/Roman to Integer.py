class Solution:
    def romanToInt(self, s: str) -> int:
        d = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        answer = 0
        flag = False
        for i in range(1, len(s)):
            if flag:
                flag = False
                continue
            if d[s[i-1]] >= d[s[i]]:
                answer += d[s[i-1]]
            else:
                answer += d[s[i]] - d[s[i-1]]
                flag = True
        if not flag:
            answer += d[s[-1]]

        return answer


if __name__ == '__main__':
    s = "MCMXCIV"
    Output = 1994

    S = Solution()
    print(S.romanToInt(s))
