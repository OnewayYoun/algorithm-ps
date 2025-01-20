from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        for i in range(n):
            nums1[-1 - i] = nums2[i]
        nums1.sort()

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        nums1 = [1], m = 1, nums2 = [], n = 0
        nums1 = [0], m = 0, nums2 = [1], n = 1
        """
        cur = n + m - 1
        r1, r2 = m - 1, n - 1

        while r2 >= 0:
            if r1 >= 0 and nums1[r1] > nums2[r2]:
                nums1[cur] = nums1[r1]
                r1 -= 1
            else:
                nums1[cur] = nums2[r2]
                r2 -= 1
            cur -= 1
        print(nums1)

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1, p2 = m - 1, n - 1
        cur_idx = len(nums1) - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[cur_idx] = nums1[p1]
                p1 -= 1
            else:
                nums1[cur_idx] = nums2[p2]
                p2 -= 1
            cur_idx -= 1
        if p1 < 0:
            nums1[:cur_idx + 1] = nums2[:p2 + 1]
        print(nums1)


s2 = Solution()
s2.merge2([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
