def solution_dfs(cost, hint):
    n = len(cost)
    answer = float('inf')
    cur_hint = [0] * n

    def dfs(stage, total):
        nonlocal answer

        if total >= answer:
            return

        if stage == n - 1:
            for i in range(n):
                total += cost[i][min(cur_hint[i], n - 1)]
            answer = min(answer, total)
            return

        # 1. 현재 번들을 구매하지 않는 경우
        dfs(stage + 1, total)

        # 2. 현재 번들을 구매하는 경우
        bundle_cost = hint[stage][0]

        for target in hint[stage][1:]:
            cur_hint[target - 1] += 1

        dfs(stage + 1, total + bundle_cost)

        # 상태 복구 (백트래킹)
        for target in hint[stage][1:]:
            cur_hint[target - 1] -= 1

    dfs(0, 0)
    return answer

def solution_masking(cost, hint):
    n = len(cost)
    answer = float('inf')

    # 각 비트는 해당 스테이지의 번들 구매 여부
    for mask in range(1 << (n - 1)):
        hint_count = [0] * n
        total = 0

        for stage in range(n - 1):
            if mask & (1 << stage):
                total += hint[stage][0]

                for target in hint[stage][1:]:
                    hint_count[target - 1] += 1

        for stage in range(n):
            cnt = min(hint_count[stage], n - 1)
            total += cost[stage][cnt]

        answer = min(answer, total)

    return answer


if __name__ == '__main__':
    print(solution_dfs(
        cost=[[160, 140, 120, 110, 60], [290, 270, 260, 120, 10], [160, 130, 120, 60, 20], [160, 120, 80, 70, 20],
              [110, 70, 60, 30, 20]],
        hint=[[40, 2, 3], [40, 5, 3], [20, 5, 4], [50, 5, 5]]
    ))

'''
cost = [[160, 140, 120, 110, 60], [290, 270, 260, 120, 10], [160, 130, 120, 60, 20], [160, 120, 80, 70, 20], [110, 70, 60, 30, 20]],
hint = [[40, 2, 3], [40, 5, 3], [20, 5, 4], [50, 5, 5]]
result = 810
'''
