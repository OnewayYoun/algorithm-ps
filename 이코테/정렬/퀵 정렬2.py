def quick_sort(A):
    if len(A) <= 1: return A
    p = A[0]
    S, M, L = [], [], []
    for num in A:
        if num > p:
            L.append(num)
        elif num < p:
            S.append(num)
        else:
            M.append(num)

    return quick_sort(S) + M + quick_sort(L)


tmp = [5, 1, 3, 6, 32, 7, 9]
print(quick_sort(tmp))
