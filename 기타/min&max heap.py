import heapq

a = [3, 2, 1, 8, 7, 9, 5]
# Max Heap
heapq._heapify_max(a)
print(a)
for i in range(len(a)):
    print(heapq._heappop_max(a))

b = [3, 2, 1, 8, 7, 9, 5]
heapq.heapify(b)
print(b)
heapq.heappush(b, 7)
print(b)

# 항상 제일 앞은 제일 작은 숫자, Min heap에서

