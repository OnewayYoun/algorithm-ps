def divide_and_conquer_sum(start, end):
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        left_sum = divide_and_conquer_sum(start, mid)
        right_sum = divide_and_conquer_sum(mid + 1, end)
        return left_sum + right_sum


start = 1
end = 6
result = divide_and_conquer_sum(start, end)
print(f"The sum of numbers from {start} to {end} is: {result}")