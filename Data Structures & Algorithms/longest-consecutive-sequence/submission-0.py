class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxLen = 0

        for n in hashSet:
            #check if this num is start of a seq
            if n - 1 not in hashSet:
                length = 1
                while n + length in hashSet:
                    length += 1
                maxLen = max(maxLen, length)
        
        return maxLen
        

        