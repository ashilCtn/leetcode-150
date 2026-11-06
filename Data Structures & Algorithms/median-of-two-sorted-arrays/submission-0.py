class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        small = nums1 if len(nums1) <= len(nums2) else nums2
        large = nums1 if len(nums1) > len(nums2) else nums2

        length = len(nums1) + len(nums2)

        l, r = 0, len(small)

        while l <= r:
            partitionX = (l + r) // 2
            partitionY = (length + 1) // 2 - partitionX

            l1 = float('-inf') if partitionX == 0 else small[partitionX - 1]
            r1 = float('inf') if partitionX == len(small) else small[partitionX]

            l2 = float('-inf') if partitionY == 0 else large[partitionY - 1]
            r2 = float('inf') if partitionY == len(large) else large[partitionY]

            if l1 <= r2 and l2 <= r1:
                if length % 2 != 0:
                    return max(l1, l2)

                return (max(l1, l2) + min(r1, r2)) / 2

            elif l1 > r2:
                r = partitionX - 1

            else:
                l = partitionX + 1