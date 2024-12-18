from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        nums1_idx = m - 1
        nums2_idx = n - 1

        while nums1_idx >= 0 and nums2_idx >= 0:
            if nums1[nums1_idx] >= nums2[nums2_idx]:
                nums1[idx] = nums1[nums1_idx]
                nums1_idx -= 1
            else:
                nums1[idx] = nums2[nums2_idx]
                nums2_idx -= 1
            idx -= 1

        while nums2_idx >= 0:
            nums1[idx] = nums2[nums2_idx]
            nums2_idx -= 1
            idx -= 1



if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    s = Solution().merge(nums1, m, nums2, n)
    print(nums1)
