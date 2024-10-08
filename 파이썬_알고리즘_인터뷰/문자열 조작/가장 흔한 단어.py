import re
from collections import Counter, defaultdict

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

counts = defaultdict(int)
for word in words:
    counts[word] += 1

print(max(counts, key=counts.get))
print(Counter(words).most_common()[0][0])
