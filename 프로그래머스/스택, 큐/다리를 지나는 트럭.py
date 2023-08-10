from collections import deque


def solution(bridge_length, weight, truck_weights):
    curr_time, curr_sum = 0, 0
    total_trucks = len(truck_weights)
    passed = []
    curr_bridge = deque([0] * bridge_length)
    while True:
        if len(passed) == total_trucks:
            break
        popped = curr_bridge.pop()
        if popped != 0:
            curr_sum -= popped
            passed.append(popped)
        if truck_weights and curr_sum + truck_weights[0] <= weight:
            curr_bridge.appendleft(truck_weights.pop(0))
            curr_sum += curr_bridge[0]
        else:
            curr_bridge.appendleft(0)
        curr_time += 1
    return curr_time


if __name__ == '__main__':
    bridge_length, weight, truck_weights = 2, 10, [7, 4, 5, 6]
    print(solution(bridge_length, weight, truck_weights))
