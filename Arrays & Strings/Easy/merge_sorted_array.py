# Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_cleaned = nums1[:m]
        nums2_cleaned = nums2[:]

        nums1_cleaned.extend(nums2_cleaned)
        nums1_cleaned.sort()

        nums1[:] = nums1_cleaned

        return nums1