from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # Set pointers to the last elements of both arrays
    p1 = m - 1  # Last element in nums1
    p2 = n - 1  # Last element in nums2
    p = m + n - 1  # Last position in merged array

    # While there are elements in both arrays
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2
    # (no need to handle nums1 since they're already in place)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


# Test case
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(f"Before merge: nums1 = {nums1}, nums2 = {nums2}")
merge(nums1, m, nums2, n)
print(f"After merge: nums1 = {nums1}")
