from collections import defaultdict
from datetime import datetime
from math import ceil


def solution(fees, records):
    answer = []
    d = defaultdict(list)
    for record in records:
        time, car_num, type_ = record.split()
        d[car_num].append(time)

    for key, val in d.items():
        if len(val) % 2 != 0:
            d[key].append('23:59')

    for key, val in sorted(d.items()):
        total = 0
        for i in range(0, len(val), 2):
            time_diff = datetime.strptime(d[key][i+1], "%H:%M") - datetime.strptime(d[key][i], "%H:%M")
            time_diff = time_diff.total_seconds() / 60
            total += time_diff
        total_price = fees[1] + ceil((total - fees[0]) / fees[2]) * fees[3]
        answer.append(total_price) if total_price > fees[1] else answer.append(fees[1])
    return answer


if __name__ == '__main__':
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    result = [14600, 34400, 5000]

    print(solution(fees, records))