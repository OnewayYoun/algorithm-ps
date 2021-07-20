n, m, k = map(int, input().split())
a = list(map(int, input().split()))
result = 0
a.sort(reverse = True)

big_1st = a[0]
big_2nd = a[1]

first = big_1st * ( k * ( m // (k+1) ) + ( m % (k+1) ) )
second = big_2nd * ( m // (k+1) )

print(first + second)