class UF:
    def __init__(self, nums):
        self.parent = {n: n for n in nums}
        self.rank = {n: 0 for n in nums}

    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                self.parent[p2] = p1
                self.rank[p1] += 1


def detect_cycle(edges, nums):
    uf = UF(nums)
    for u, v in edges:
        if uf.find(u) == uf.find(v):  # 두 노드가 이미 같은 집합에 있다면 싸이클 발생
            return True
        uf.union(u, v)
    return False


nums = [1, 2, 3]
edges = [(1, 2), (2, 3), (3, 1)]

if detect_cycle(edges, nums):
    print("싸이클이 존재합니다.")
else:
    print("싸이클이 존재하지 않습니다.")

"""
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')


# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
"""
