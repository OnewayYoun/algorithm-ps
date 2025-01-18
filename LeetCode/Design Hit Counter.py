from collections import deque
from bisect import bisect_right


class HitCounter:
    def __init__(self):
        self.q = deque()

    def hit(self, timestamp: int):
        self.q.append(timestamp)

    def get_hits(self, timestamp: int):
        while len(self.q) > 0 and (timestamp - self.q[0]) >= 300:
            self.q.popleft()
        return len(self.q)


class HitCounter1:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int):
        self.hits.append(timestamp)

    def get_hits(self, timestamp: int):
        target = timestamp - 300
        return len(self.hits) - bisect_right(self.hits, target)


# obj = HitCounter1()
# obj.hit(1)
# obj.hit(2)
# obj.hit(3)
# print(obj.get_hits(4))
# obj.hit(300)
# print(obj.get_hits(300))
# print(obj.get_hits(301))


def br(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def bl(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


# Example usage
arr = [1, 3, 3, 5, 7]
target = 3

print(br(arr, target))
print(bl(arr, target))
