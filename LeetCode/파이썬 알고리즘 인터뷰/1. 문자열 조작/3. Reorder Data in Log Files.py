from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def helper(s):
            identifier, rest = s.split()[0], " ".join(s.split()[1:])
            if rest[0].isalpha():
                return (0, rest, identifier)
            else:
                return (1,)

        return sorted(logs, key=helper)


class Solution2:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split(' ', 1)[1][0].isalpha():
                letters.append(log)
            else:
                digits.append(log)

        letters.sort(key=lambda x: (x.split(' ', 1)[1], x.split(' ', 1)[0]))
        return letters + digits


print(Solution().reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
print(Solution2().reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
