from typing import List


def reverseString(l: List[str]):
    left, right = 0, len(l) - 1
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    print(l)


if __name__ == '__main__':
    reverseString(['a', 'b', 'c'])
    # 리스트인경우
    s = ['a', 'b', 'c']
    s[:] = s[::-1]
    print(s)
