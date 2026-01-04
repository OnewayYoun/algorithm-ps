from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        return sorted(letter_logs, key=lambda x: (x.split(" ", 1)[1], x)) + digit_logs


if __name__ == "__main__":
    print(Solution().reorderLogFiles(["dig1 8 1 5 1", "let2 art can", "dig2 3 6", "let1 art can", "let3 art zero"]))
