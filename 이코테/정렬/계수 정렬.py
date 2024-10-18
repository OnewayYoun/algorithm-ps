l = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
cnt = [0] * (max(l) + 1)

for i in range(len(l)):
    cnt[l[i]] += 1

l = []
for idx, val in enumerate(cnt):
    l = l + ([idx] * val)

print(l)
