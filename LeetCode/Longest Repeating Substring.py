class Solution:
    """
    Input: S = "abcd"
    Output: 0

    Input: S = "abbaba"
    Output: 2

    Input: S = "aabcaabdaab"
    Output: 3

    Input: "aaaaa"
    Output: 4
    """

    def longestRepeatingSubstring(self, S: str) -> int:
        sub_string_set = set()
        n = len(S)
        answer = 0

        for i in range(n):
            for j in range(i + 1):
                sub_string = S[j:i + 1]
                if sub_string not in sub_string_set:
                    sub_string_set.add(sub_string)
                else:
                    answer = max(answer, len(sub_string))

        return answer

    def longestRepeatingSubstring1(self, S: str) -> int:
        sub_string_set = set()
        n = len(S)
        answer = 0

        for left in range(n):
            for right in range(left + 1, n + 1):
                sub_string = S[left:right]
                if sub_string not in sub_string_set:
                    sub_string_set.add(sub_string)
                else:
                    answer = max(answer, len(sub_string))

        return answer

    def longestRepeatingSubstring2(self, S: str) -> int:
        n = len(S)

        for length in range(n - 1, 0, -1):
            sub_string_set = set()

            for left in range(n - length + 1):
                sub_string = S[left:left + length]
                if sub_string in sub_string_set:
                    return length
                sub_string_set.add(sub_string)

        return 0

    def longestRepeatingSubstring3(self, S: str) -> int:
        def has_duplicate_of_length(length):
            seen = set()
            for i in range(len(S) - length + 1):
                sub_string = S[i:i + length]
                if sub_string in seen:
                    return True
                seen.add(sub_string)
            return False

        left, right = 1, len(S)
        while left <= right:
            mid = (left + right) // 2
            if has_duplicate_of_length(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1


print(Solution().longestRepeatingSubstring3(S="abcd"))
