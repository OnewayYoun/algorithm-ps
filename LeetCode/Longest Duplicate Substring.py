class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def has_duplicate_of_length(length):
            nonlocal answer
            seen = set()
            for i in range(len(s) - length + 1):
                sub_string = s[i:i + length]
                if sub_string in seen:
                    answer = sub_string
                    return True
                seen.add(sub_string)
            return False

        left, right = 1, len(s)
        answer = ''
        while left <= right:
            mid = (left + right) // 2
            if has_duplicate_of_length(mid):
                left = mid + 1
            else:
                right = mid - 1
        return answer


print(Solution().longestDupSubstring("banana"))
