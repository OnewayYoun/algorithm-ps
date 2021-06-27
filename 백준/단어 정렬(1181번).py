'''
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
'''

n = int(input())
words = set([input() for _ in range(n)])
a = sorted(words, key = lambda x : (len(x), x))
print('\n'.join(a))