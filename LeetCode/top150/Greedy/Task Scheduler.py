import heapq
from typing import List, Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        sequence = []
        counter = Counter(tasks)

        while tasks:
            flag = True
            for key, _ in counter.most_common(n + 1):
                if key not in sequence[-n:] and counter[key] != 0:
                    sequence.append(key)
                    counter[key] -= 1
                    tasks.pop()
                    flag = False
            if flag:
                sequence.append('idle')
        return len(sequence)

    def leastInterval1(self, tasks: List[str], n: int) -> int:
        sequence = []
        counter = Counter(tasks)
        heap = [(-val, key) for key, val in counter.items()]
        heapq.heapify(heap)

        while tasks:
            tmp = []
            for _ in range(n + 1):
                if heap and tasks:
                    count, letter = heapq.heappop(heap)
                    count += 1
                    if count <= 0:
                        tmp.append((count, letter))
                        sequence.append(letter)
                        tasks.pop()
                else:
                    if tasks:
                        sequence.append('idle')

            while tmp:
                count, letter = tmp.pop()
                if count != 0:
                    heapq.heappush(heap, (count, letter))
        print(sequence)
        return len(sequence)

    def leastInterval3(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter -= Counter(task)
                counter += Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result


print(Solution().leastInterval3(tasks = ["A","A","A","B","B","B"], n = 2))
# print(Solution().leastInterval1(tasks=["B", "C", "D", "A", "A", "A", "A", "G"], n=1))
