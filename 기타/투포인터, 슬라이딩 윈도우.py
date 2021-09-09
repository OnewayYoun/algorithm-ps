####### 투포인터 #######

n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)


####### 슬라이딩 윈도우 #######
def solve_max_sum(arr, k):
    # 배열과 k값이 인자로 넘어온다.
    max_sum = float('-inf')
    # 최대값은 마이너스 무한대로 초기화
    start = 0
    # 시작 인덱스를 0으로 초기화
    curr_sum = 0
    # 현재까지의 합도 0으로 초기화

    for end, val in enumerate(arr):
        curr_sum += val
        # 현재까지의 합에 val값을 계속 더해줌
        if end - start + 1  == k:
            # 예를 들어 k가 3이라면 3개의 합이니까
            # 오른쪽(end)-왼쪽(start)+1  했을 때 그 합이 k가 되면 끝남
            max_sum = max(max_sum, curr_sum)
            # 최대값 계속해서 갱신해주기
            curr_sum -= arr[start]
            # 현재까지의 합 (3개의 합이겠지?) 에다가 시작점의 원소 하나 빼줘,
            # 그럼 첫번째 원소를 뺀 나머지 뒤에 2개 원소의 합이 curr_sum 이겠지.
            start += 1
            # 시작점 한칸 오른쪽으로 옮겨줘
    return max_sum

arr = [2,3,4,1,5]
k = 3

print(solve_max_sum(arr,k))