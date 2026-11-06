class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        maxLen = 0

        l, r = 0, 0
        while r < len(s):
            if s[r] not in hashSet:
                maxLen = max(maxLen, r - l + 1)
                hashSet.add(s[r])
                r += 1
            else:
                while s[r] in hashSet:
                    hashSet.remove(s[l])
                    l += 1
                
        
        return maxLen
        