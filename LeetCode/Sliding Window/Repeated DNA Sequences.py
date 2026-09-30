class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        check = set()
        answer = set()

        left = 0
        for right in range(9, len(s)):
            substring = s[left:right + 1]
            if substring not in check:
                check.add(substring)
            else:
                answer.add(substring)
            left += 1

        return list(answer)
