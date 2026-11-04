class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = ( l  + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        minIdx = r

        if minIdx == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[minIdx - 1]:
            l, r = 0, minIdx - 1
        else:
            l, r = minIdx, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        
        return -1
            
        