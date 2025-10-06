from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_list, digit_list = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit_list.append(log)
            else:
                letter_list.append(log)
        letter_list.sort(key=lambda x: (' '.join(x.split()[1:]), x.split()[0]))
        return letter_list + digit_list
