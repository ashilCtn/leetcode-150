class Solution:
    def swap(self, a, first, second):
        temp = a[first]
        a[first] = a[second]
        a[second] = temp

    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correctIdx = nums[i] - 1
            if nums[correctIdx] != nums[i]:
                self.swap(nums, correctIdx, i)
            else:
                i += 1

        return nums[-1] 